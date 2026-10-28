"""
AI Chatbot Using Gemini API  -  chatbot name: Sara (female persona)
BSc Computer Science - Semester 5 Mini Project

Tech stack : Python, Streamlit, Google Gemini API (official google-genai SDK)
Features   : chat history, conversational context, English + Hinglish,
             streaming replies, clear-chat button, friendly error messages,
             secure API key handling through Streamlit secrets.

IMPORTANT: The API key is NEVER written in this file. It is read from
Streamlit secrets (.streamlit/secrets.toml locally, or the "Secrets" box on
Streamlit Community Cloud).
"""

import os

import httpx
import streamlit as st
from google import genai
from google.genai import errors, types

# ----------------------------------------------------------------------------
# 1. SETTINGS
# ----------------------------------------------------------------------------
APP_TITLE = "Sara - Your AI Friend"
BOT_NAME = "Sara"
BOT_AVATAR = "👩"

# Label shown to the user -> exact model ID used by the API.
# (Checked against Google's official model list on 28 Oct 2026.)
MODEL_OPTIONS = {
    "Gemini 3.5 Flash-Lite  (fast, free-tier friendly)": "gemini-3.5-flash-lite",
    "Gemini 3.8 Flash  (smarter, newest Flash)": "gemini-3.8-flash",
    "Gemini 3.6 Flash  (balanced)": "gemini-3.6-flash",
}
DEFAULT_MODEL_LABEL = "Gemini 3.5 Flash-Lite  (fast, free-tier friendly)"

# Only the most recent messages are sent to the model. This keeps the
# conversation memory useful but stops requests from becoming too large.
MAX_HISTORY_MESSAGES = 20

# The "system instruction" tells Gemini how to behave and which language to use.
SYSTEM_PROMPTS = {
    "English": (
        "Your name is Sara. You are a friendly, warm and helpful female AI "
        "assistant inside a student project chatbot. If asked, introduce "
        "yourself as Sara. Reply in simple, clear English. Keep answers short and "
        "well-organised unless the user asks for detail. Use bullet points "
        "or short code blocks when they make the answer easier to read. "
        "If you are not sure about something, say so honestly."
    ),
    "Hinglish": (
        "Your name is Sara. You are a friendly, warm and helpful female AI "
        "assistant inside a student project chatbot. If asked, introduce "
        "yourself as Sara. Always use feminine Hindi grammar for yourself "
        "(for example 'main kar sakti hoon', 'main samajh gayi'). "
        "ALWAYS reply in Hinglish: Hindi written in the English "
        "(Roman) alphabet, mixed naturally with common English words, the "
        "way young people in India chat. Example style: 'Bilkul! Python ek "
        "easy programming language hai.' Do not use Devanagari script. "
        "Keep answers short, simple and friendly. Technical terms and code "
        "can stay in English. If you are not sure about something, say so "
        "honestly."
    ),
}

LANGUAGE_LABELS = {
    "English": "English",
    "Hinglish": "Hinglish (Hindi in English letters)",
}

STARTER_PROMPTS = {
    "English": [
        "Explain Python lists in simple words",
        "Give me 3 tips to prepare for my exams",
        "What is an API? Explain with an example",
    ],
    "Hinglish": [
        "Python mein list kya hoti hai? Simple bata do",
        "Exam ki preparation ke liye 3 tips do",
        "API kya hoti hai? Example ke saath samjhao",
    ],
}

PLACEHOLDERS = {
    "English": "Type your message here...",
    "Hinglish": "Apna message yahan likho...",
}

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=BOT_AVATAR,
    layout="centered",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# 2. LOOK AND FEEL (a little custom CSS)
# ----------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
.hero {
    padding: 1.1rem 1.4rem;
    border-radius: 16px;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 55%, #db2777 100%);
    color: #ffffff;
    margin-bottom: 1rem;
}
.hero h1 { margin: 0; font-size: 1.7rem; color: #ffffff; padding: 0; }
.hero p  { margin: 0.25rem 0 0 0; opacity: 0.92; font-size: 0.95rem; }
[data-testid="stChatMessage"] { border-radius: 14px; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ----------------------------------------------------------------------------
# 3. API KEY AND CLIENT
# ----------------------------------------------------------------------------
def load_api_key():
    """Read the API key from Streamlit secrets (or an environment variable).

    Returns the key as a string, or None if it is missing / still a placeholder.
    The key is never printed or stored anywhere else.
    """
    key = ""
    try:
        key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        # No secrets file, or no GEMINI_API_KEY inside it -> try env variable.
        key = os.environ.get("GEMINI_API_KEY", "")
    key = str(key).strip()
    if not key or key.upper().startswith("PASTE_"):
        return None
    return key


@st.cache_resource(show_spinner=False)
def get_client(api_key):
    """Create the Gemini client once and reuse it (official google-genai SDK)."""
    return genai.Client(api_key=api_key)


# ----------------------------------------------------------------------------
# 4. FRIENDLY ERROR MESSAGES
# ----------------------------------------------------------------------------
def explain_error(exc, api_key=None):
    """Convert any exception into (title, simple explanation) for the user."""
    text = str(exc)
    if api_key:
        text = text.replace(api_key, "***")  # safety: never show the key
    lower = text.lower()

    if isinstance(exc, errors.ClientError):
        code = getattr(exc, "code", None)
        if code in (401, 403) or "api key not valid" in lower or "api_key_invalid" in lower:
            return (
                "Invalid or unauthorised API key",
                "Google rejected the API key. Create a fresh key in Google AI "
                "Studio, paste it into your Streamlit secrets as GEMINI_API_KEY, "
                "then reboot the app.",
            )
        if code == 429 or "resource_exhausted" in lower or "quota" in lower:
            return (
                "Quota / rate limit reached",
                "You have used up the free quota (or are sending messages too "
                "fast). Wait a minute and try again. If it keeps happening, "
                "choose 'Gemini 3.5 Flash-Lite' in the sidebar, or try again "
                "tomorrow because daily limits reset every day.",
            )
        if code == 404:
            return (
                "Model not found",
                "The selected Gemini model is not available for your key. "
                "Pick a different model in the sidebar.",
            )
        return (
            "The request was not accepted",
            "Gemini could not process this message. Try rephrasing it. "
            "(Technical detail: " + text[:200] + ")",
        )

    if isinstance(exc, errors.ServerError):
        return (
            "Gemini is busy right now",
            "Google's servers are temporarily overloaded or down. This is not "
            "your fault - please try again in a few seconds.",
        )

    if isinstance(exc, httpx.TimeoutException) or isinstance(exc, TimeoutError):
        return (
            "The request timed out",
            "Gemini took too long to answer. Check your internet connection "
            "and try again.",
        )

    if isinstance(exc, (httpx.TransportError, ConnectionError, OSError)):
        return (
            "Network problem",
            "Could not reach Google's servers. Check your internet "
            "connection and try again.",
        )

    return (
        "Something went wrong",
        "An unexpected error happened. Please try again. (Technical detail: "
        + text[:200]
        + ")",
    )


# ----------------------------------------------------------------------------
# 5. TALKING TO GEMINI
# ----------------------------------------------------------------------------
def build_history(messages):
    """Turn our saved messages into the format the Gemini chat API expects.

    Gemini uses the role names "user" and "model" (not "assistant").
    This is what gives the bot its memory / conversational context.
    """
    recent = messages[-MAX_HISTORY_MESSAGES:]
    # A conversation sent to Gemini must start with a user message.
    while recent and recent[0]["role"] != "user":
        recent = recent[1:]

    history = []
    for m in recent:
        role = "user" if m["role"] == "user" else "model"
        history.append(
            types.Content(role=role, parts=[types.Part.from_text(text=m["content"])])
        )
    return history


def stream_reply(client, model_id, language, past_messages, prompt):
    """Send the new prompt (plus past messages) and yield the answer in pieces."""
    chat = client.chats.create(
        model=model_id,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPTS[language],
        ),
        history=build_history(past_messages),
    )
    for chunk in chat.send_message_stream(prompt):
        if chunk.text:
            yield chunk.text


# ----------------------------------------------------------------------------
# 6. SESSION STATE (the app's memory between clicks)
# ----------------------------------------------------------------------------
def init_state():
    st.session_state.setdefault("messages", [])      # chat history
    st.session_state.setdefault("last_error", None)  # (title, message, prompt)
    st.session_state.setdefault("queued_prompt", None)


def clear_chat():
    """Callback for the 'Clear chat' button."""
    st.session_state.messages = []
    st.session_state.last_error = None
    st.session_state.queued_prompt = None


def queue_prompt(text):
    """Callback for starter / retry buttons."""
    st.session_state.queued_prompt = text


def transcript_text():
    """Plain-text copy of the chat for the download button."""
    lines = []
    for m in st.session_state.messages:
        who = "You" if m["role"] == "user" else BOT_NAME
        lines.append(f"{who}: {m['content']}\n")
    return "\n".join(lines)


# ----------------------------------------------------------------------------
# 7. MAIN APP
# ----------------------------------------------------------------------------
def main():
    init_state()

    # ---- Header ----
    st.markdown(
        f"""
        <div class="hero">
            <h1>{BOT_AVATAR} {APP_TITLE}</h1>
            <p>Hi, I'm {BOT_NAME}! Ask me anything in English or Hinglish. I remember our conversation!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---- Sidebar ----
    with st.sidebar:
        st.header("⚙️ Settings")
        language = st.radio(
            "Reply language",
            options=list(LANGUAGE_LABELS.keys()),
            format_func=lambda k: LANGUAGE_LABELS[k],
            help="Choose the language the bot will answer in.",
        )
        model_label = st.selectbox(
            "Gemini model",
            options=list(MODEL_OPTIONS.keys()),
            index=list(MODEL_OPTIONS.keys()).index(DEFAULT_MODEL_LABEL),
            help="If you see a quota error, switch to Flash-Lite.",
        )
        model_id = MODEL_OPTIONS[model_label]

        st.button("🗑️ Clear chat", on_click=clear_chat, help="Delete the whole conversation")

        if st.session_state.messages:
            st.download_button(
                "⬇️ Download chat (.txt)",
                data=transcript_text(),
                file_name="chat_history.txt",
                mime="text/plain",
            )

        st.divider()
        st.caption(
            "Built with Python, Streamlit and the Google Gemini API "
            "(google-genai SDK). BSc CS Semester 5 mini project."
        )
        st.caption(f"Messages in this chat: {len(st.session_state.messages)}")

    # ---- API key check ----
    api_key = load_api_key()
    if api_key is None:
        st.error("🔑 **Gemini API key not found.**")
        st.markdown(
            "Add your key to Streamlit secrets with this exact name:\n\n"
            "```toml\nGEMINI_API_KEY = \"your-key-here\"\n```\n"
            "- **On your computer:** put it in `.streamlit/secrets.toml`\n"
            "- **On Streamlit Community Cloud:** App → Settings → Secrets\n\n"
            "Get a free key from Google AI Studio: https://aistudio.google.com/apikey"
        )
        st.stop()

    client = get_client(api_key)

    # ---- Get the user's new message (typed, or from a button) ----
    # We read it BEFORE drawing the page so an old error message disappears
    # as soon as the user sends something new. (The input box always appears
    # at the bottom of the page, whatever order we call it in.)
    typed = st.chat_input(PLACEHOLDERS[language], max_chars=2000)
    prompt = typed or st.session_state.queued_prompt
    st.session_state.queued_prompt = None
    if prompt:
        st.session_state.last_error = None

    # ---- Show the saved conversation ----
    for message in st.session_state.messages:
        avatar = "🧑‍🎓" if message["role"] == "user" else BOT_AVATAR
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # ---- Starter suggestions (only when the chat is empty) ----
    if not st.session_state.messages and not st.session_state.last_error and not prompt:
        st.markdown("**Try one of these:**")
        for i, suggestion in enumerate(STARTER_PROMPTS[language]):
            st.button(
                suggestion,
                key=f"starter_{i}",
                on_click=queue_prompt,
                args=(suggestion,),
            )

    # ---- Show the last error (if any) with a Retry button ----
    if st.session_state.last_error:
        title, detail, failed_prompt = st.session_state.last_error
        st.error(f"**{title}**\n\n{detail}")
        st.button(
            "🔄 Retry my last message",
            on_click=queue_prompt,
            args=(failed_prompt,),
        )

    # ---- Nothing new to answer? Then we are done for this run ----
    if not prompt:
        return

    with st.chat_message("user", avatar="🧑‍🎓"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        placeholder = st.empty()
        reply = ""
        try:
            placeholder.markdown("_Thinking..._")
            for piece in stream_reply(
                client,
                model_id,
                language,
                st.session_state.messages,  # history BEFORE the new prompt
                prompt,
            ):
                reply += piece
                placeholder.markdown(reply + "▌")

            if not reply.strip():
                reply = (
                    "I could not generate an answer for that message. It may "
                    "have been blocked by Gemini's safety filters. Please try "
                    "asking in a different way."
                )
            placeholder.markdown(reply)

            # Save both messages only when everything worked.
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": reply})

        except Exception as exc:  # noqa: BLE001 - we show a friendly message
            placeholder.empty()
            title, detail = explain_error(exc, api_key)
            st.session_state.last_error = (title, detail, prompt)
            st.rerun()


main()
