# AI CHATBOT USING GEMINI API
### (Chatbot name: "Sara")

### A Mini Project Report

**Submitted in partial fulfilment of the requirements for the degree of**
**Bachelor of Science (Computer Science) – Semester V**

| | |
|---|---|
| **Submitted by** | [Your Full Name] |
| **Roll / Seat Number** | [Your Roll Number] |
| **Class** | T.Y.B.Sc. (Computer Science), Semester V |
| **College** | [Your College Name] |
| **University** | [Your University Name] |
| **Guide / Teacher** | [Guide's Name] |
| **Academic Year** | 2026 – 2027 |
| **Live Project Link** | [your-app-name].streamlit.app |
| **Source Code** | https://github.com/[your-username]/gemini-chatbot |

---

## CERTIFICATE

This is to certify that **[Your Full Name]**, Roll No. **[Roll No.]**, of T.Y.B.Sc. (Computer Science), Semester V, has successfully completed the mini project titled **"AI Chatbot Using Gemini API"** during the academic year 2026–2027, under my guidance.

Guide: ____________________  Head of Department: ____________________  External Examiner: ____________________

Date: ____________  Place: ____________

---

## DECLARATION

I declare that this project report is my own work. The project "AI Chatbot Using Gemini API" was developed by me, using the official documentation of Python, Streamlit and the Google Gemini API. All sources I used are listed in the References section.

Signature: ____________________  Name: [Your Full Name]  Date: ____________

---

## ACKNOWLEDGEMENT

I would like to thank my guide **[Guide's Name]** for helpful advice during this project. I also thank our Head of Department, all teachers of the Computer Science department, my family and my friends for their support. I am also thankful to the open-source community and the official documentation of Python, Streamlit and Google Gemini, which helped me learn while building this project.

---

## TABLE OF CONTENTS

1. Abstract
2. Introduction
3. Problem Statement
4. Objectives
5. Scope of the Project
6. Existing System and Proposed System
7. Technologies Used
8. System Requirements
9. System Design
10. Module Description
11. Implementation Details
12. Security Design
13. Error Handling
14. Testing
15. Screens (Output Description)
16. Limitations
17. Future Scope
18. Conclusion
19. References

---

## 1. ABSTRACT

A chatbot is a computer program that talks with a person in natural language. This project, **"AI Chatbot Using Gemini API"**, is a web-based chatbot named **Sara** (a friendly female AI assistant), made with **Python** and **Streamlit**. It uses Google's **Gemini** artificial-intelligence model through the official **google-genai** Python library.

The chatbot remembers earlier messages, so the conversation feels natural. It can reply in **English** or in **Hinglish** (Hindi written using English letters), which is how many Indian students chat every day. The user can clear the chat, download the chat, and choose between Gemini models. The API key is kept safe using **Streamlit secrets**, so it is never written in the code or uploaded to GitHub. The project also shows simple, friendly messages when something goes wrong, such as a wrong API key, finished quota, or no internet. The finished project is deployed free on **Streamlit Community Cloud**, so anyone can use it with a web link.

---

## 2. INTRODUCTION

Artificial Intelligence (AI) is now used in many daily tools such as voice assistants, translation apps and customer-support chat windows. A big reason is the arrival of **Large Language Models (LLMs)**. An LLM is an AI model trained on a huge amount of text, so it can understand questions and write answers in human-like language.

**Gemini** is a family of LLMs made by Google. Developers can use Gemini in their own programs through the **Gemini API**. Google gives an official Python library, called **google-genai**, that makes this easy.

**Streamlit** is a Python library for building web applications using only Python. A student does not need to learn HTML, CSS or JavaScript to create a good-looking app. Streamlit also has ready-made chat components, which makes it ideal for chatbot projects.

In this project, these tools are combined to build a complete chatbot that is also published on the internet.

---

## 3. PROBLEM STATEMENT

Many beginner chatbots have these problems:

1. They forget what the user said earlier, so they cannot continue a conversation.
2. They only support English, but many users are more comfortable in Hinglish.
3. The API key is often written inside the code and accidentally uploaded to GitHub, where it can be stolen.
4. When an error happens, the app crashes or shows confusing technical messages.
5. They run only on the developer's computer and are not available online.

This project solves these problems.

---

## 4. OBJECTIVES

1. To build a chatbot using Python, Streamlit and the Gemini API.
2. To keep chat history and use it as context, so the bot remembers the conversation.
3. To support both English and Hinglish replies.
4. To keep the API key secure using Streamlit secrets.
5. To handle errors (invalid key, quota limit, network problems) in a user-friendly way.
6. To design a clean and modern user interface.
7. To deploy the project online for free.

---

## 5. SCOPE OF THE PROJECT

**Inside the scope:**
- Text-based question-and-answer conversation.
- English and Hinglish replies.
- Multi-turn memory during one browser session.
- Choosing between three Gemini models.
- Clearing and downloading the chat.
- Free deployment on Streamlit Community Cloud.

**Outside the scope:**
- Voice input or output.
- Image or file upload.
- User login and permanent database storage.
- Training our own AI model (we use Google's ready-made model).

---

## 6. EXISTING SYSTEM AND PROPOSED SYSTEM

### 6.1 Existing system
Older rule-based chatbots use fixed "if the user says X, reply Y" rules. They cannot answer new questions, and they need a lot of manual work to write the rules. Many simple student chatbots built with AI APIs also have no memory, no error handling and an unsafe key.

### 6.2 Proposed system
The proposed system uses a powerful LLM (Gemini). It answers almost any question, remembers the conversation, supports Hinglish, protects the API key, handles errors politely and is available online.

| Point | Rule-based chatbot | Proposed Gemini chatbot |
|---|---|---|
| Answers | Only fixed, pre-written | Almost any topic |
| Memory | Usually none | Remembers the conversation |
| Language | Fixed | English and Hinglish |
| Effort | Many rules to write | Very little code |
| Key safety | Not applicable | Stored in secrets |

---

## 7. TECHNOLOGIES USED

| Technology | Purpose |
|---|---|
| **Python 3** | Main programming language |
| **Streamlit** | Builds the web user interface and chat screen |
| **Google Gemini API** | The AI "brain" that creates the answers |
| **google-genai SDK** | Official Python library to talk to Gemini |
| **Streamlit secrets** | Safe storage for the API key |
| **Git and GitHub** | Version control and code hosting |
| **Streamlit Community Cloud** | Free online hosting |
| **VS Code** | Code editor |

**What is an API?** An API (Application Programming Interface) lets one program talk to another. Our app sends the user's question to Google's server through the Gemini API and receives the answer.

**What is an SDK?** An SDK (Software Development Kit) is a ready-made library. The google-genai SDK hides difficult details (like building web requests) behind simple Python functions.

---

## 8. SYSTEM REQUIREMENTS

### 8.1 Hardware
- Any computer or laptop with 4 GB RAM or more
- Internet connection

### 8.2 Software
- Operating system: Windows, macOS or Linux
- Python 3.10 or newer
- Libraries: `streamlit`, `google-genai`
- A modern web browser (Chrome, Edge, Firefox)
- A Google account (to create a Gemini API key)
- A GitHub account (for hosting the code)

---

## 9. SYSTEM DESIGN

### 9.1 Architecture

```
 ┌──────────────┐     1. types message      ┌───────────────────────┐
 │     USER     │ ────────────────────────► │  Streamlit Web App    │
 │  (Browser)   │                           │  (app.py)             │
 │              │ ◄──────────────────────── │  - chat screen        │
 └──────────────┘   6. shows live answer    │  - session history    │
                                            │  - error handling     │
                                            └──────────┬────────────┘
                                   2. reads key        │  3. sends history
                                      ┌────────────┐   │     + new message
                                      │ Streamlit  │   │     + language rule
                                      │  Secrets   │◄──┤
                                      └────────────┘   ▼
                                            ┌───────────────────────┐
                                            │ google-genai SDK      │
                                            └──────────┬────────────┘
                                                       │ 4. HTTPS request
                                                       ▼
                                            ┌───────────────────────┐
                                            │  Google Gemini API    │
                                            │  (Gemini model)       │
                                            └───────────────────────┘
                                              5. answer comes back in pieces
```

### 9.2 Flow of one message

1. The user types a message and presses Enter.
2. The app checks that the API key exists in the secrets.
3. The app collects the earlier messages (the history).
4. It creates a chat with the history and the language instruction.
5. It sends the new message to Gemini.
6. Gemini sends the answer in small pieces; the app shows them live.
7. When finished, the question and the answer are saved in the history.
8. If there is any error, a friendly message is shown and the question is **not** saved.

### 9.3 Flowchart (text form)

```
START
  │
  ▼
API key found in secrets? ──No──► Show "key not found" help ──► STOP
  │Yes
  ▼
Show old messages
  │
  ▼
User sends new message?  ──No──► Wait
  │Yes
  ▼
Send history + message to Gemini
  │
  ▼
Success? ──No──► Show friendly error + Retry button
  │Yes
  ▼
Show answer live ──► Save question + answer in history ──► Wait for next message
```

### 9.4 Data design
There is no database. The chat is kept in memory in `st.session_state.messages`, which is a Python list. Each item is a dictionary:

```python
{"role": "user" or "assistant", "content": "message text"}
```

When the browser tab is closed, the chat is gone. This protects privacy and keeps the project simple.

---

## 10. MODULE DESCRIPTION

| # | Module (function) | Purpose |
|---|---|---|
| 1 | `load_api_key()` | Reads the API key from Streamlit secrets (or an environment variable). Returns nothing if it is missing |
| 2 | `get_client()` | Creates the Gemini client one time and reuses it (`st.cache_resource`) |
| 3 | `build_history()` | Converts saved messages into the format Gemini needs (roles `user` and `model`) and keeps only the latest 20 messages |
| 4 | `stream_reply()` | Creates a chat with history and language instruction, sends the message and yields the answer in pieces |
| 5 | `explain_error()` | Converts technical errors into simple, friendly messages |
| 6 | `init_state()` / `clear_chat()` | Prepare and reset the chat memory |
| 7 | `main()` | Draws the screen: header, sidebar, chat messages, input box, errors |

---

## 11. IMPLEMENTATION DETAILS

### 11.1 Creating the client
```python
client = genai.Client(api_key=api_key)
```
The `api_key` is read from secrets, not typed in the code.

### 11.2 Creating a chat with memory
```python
chat = client.chats.create(
    model=model_id,
    config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPTS[language]),
    history=build_history(past_messages),
)
```
- `model` – which Gemini model to use (for example `gemini-3.5-flash-lite`).
- `system_instruction` – a hidden instruction that sets the bot's behaviour and language.
- `history` – earlier messages, which give the bot its memory.

### 11.3 Streaming the answer
```python
for chunk in chat.send_message_stream(prompt):
    if chunk.text:
        yield chunk.text
```
The answer arrives in small parts, so the user sees it appear live instead of waiting.

### 11.4 English and Hinglish
The language is controlled by the system instruction. For Hinglish, the instruction tells Gemini to reply in Hindi written in English letters, mixed with common English words (for example: *"Bilkul! Python ek easy programming language hai."*).

### 11.5 Remembering the conversation (context)
Streamlit re-runs the whole script after every click. So the history is stored in `st.session_state`, which survives these re-runs. Before every new message, the saved history is sent to Gemini, so Gemini knows what was said before.

### 11.6 Model choice
Models checked in the official Google documentation on 28 October 2026:
- `gemini-3.5-flash-lite` (default; fast and free-tier friendly)
- `gemini-3.6-flash`
- `gemini-3.8-flash` (newest Flash model)

Old models like `gemini-2.0-flash` are shut down and are not used. The older sampling settings (`temperature`, `top_p`, `top_k`) are marked as deprecated by Google for newer models, so the project does not use them.

### 11.7 Clear chat
A button with a callback function sets `st.session_state.messages` to an empty list.

---

## 12. SECURITY DESIGN

| Risk | Protection used |
|---|---|
| API key written in code | Key is read by `st.secrets["GEMINI_API_KEY"]`; it is never in `app.py` |
| Key uploaded to GitHub | `.gitignore` blocks `.streamlit/secrets.toml`; only a sample file `secrets.toml.example` (with a fake value) is uploaded |
| Key shown in error text | `explain_error()` replaces the key with `***` before showing any text |
| Key stolen from the cloud | Key is pasted into the Streamlit Cloud "Secrets" box, not into files |
| Very long input | The input box allows at most 2000 characters |
| Privacy | No database; chat is kept only in the browser session |

**Note:** On the Gemini API free tier, Google says that prompts may be used to improve its products. So users should not type private information.

---

## 13. ERROR HANDLING

| Problem | Technical cause | Message shown to user |
|---|---|---|
| Wrong API key | Error 400/401/403 "API key not valid" | "Invalid or unauthorised API key" with steps to fix |
| Quota finished | Error 429 `RESOURCE_EXHAUSTED` | "Quota / rate limit reached" – wait or switch model |
| Wrong model name | Error 404 | "Model not found" – choose another model |
| Google server problem | Error 5xx (`ServerError`) | "Gemini is busy right now" |
| Slow network | Timeout | "The request timed out" |
| No internet | Connection error | "Network problem" |
| Blocked or empty answer | No text in reply | "I could not generate an answer…" |
| Any other error | Unknown | "Something went wrong" |

If an error happens, the failed message is **not** saved in the history, so the next request is not damaged. A **Retry** button sends the same message again.

---

## 14. TESTING

### 14.1 Test cases
Run these on your deployed app and write the result in the last column.

| # | Test | Input / Action | Expected result | Status (Pass/Fail) |
|---|---|---|---|---|
| 1 | App opens | Open the link | Chat page with header and sidebar | |
| 2 | Simple question (English) | "What is Python?" | Short English answer | |
| 3 | Memory | "My name is Rahul" then "What is my name?" | Bot answers "Rahul" | |
| 4 | Hinglish | Choose Hinglish, ask "Python kya hai?" | Answer in Roman Hindi | |
| 5 | Switch back to English | Choose English, ask any question | English answer | |
| 6 | Clear chat | Click "Clear chat" | All messages removed | |
| 7 | Starter buttons | Click a suggested question | It is sent and answered | |
| 8 | Download chat | Click "Download chat" | `.txt` file downloads | |
| 9 | Model change | Select Gemini 3.8 Flash and ask | Answer received | |
| 10 | Missing key | Remove the secret and reboot | "API key not found" help screen | |
| 11 | Wrong key | Put a wrong key in Secrets | "Invalid or unauthorised API key" message | |
| 12 | No internet | Disconnect internet (local run) and send message | "Network problem" message | |
| 13 | Retry | After an error click "Retry" | Message is sent again | |
| 14 | Secret safety | Check GitHub repository | No `secrets.toml` file present | |

### 14.2 Developer testing note
During development, the application was also tested with an automated script using Streamlit's built-in testing tool (`AppTest`). It checked the chat flow, memory, language switch, model switch, clear-chat button, retry button and all error messages. The script used a simulated Gemini client, because a real API key is not shared during testing. A call with a fake key through the real SDK was also made, to confirm that network failures are handled without crashing.

---

## 15. SCREENS (OUTPUT DESCRIPTION)

*(Add your own screenshots here after running the app.)*

1. **Home screen** – Gradient header "Sara - Your AI Friend" (the chatbot's name is Sara, a female persona), suggested questions, chat box at the bottom, settings in the sidebar.
2. **English chat** – User question and a streaming English answer.
3. **Hinglish chat** – User question and an answer in Roman Hindi.
4. **Sidebar** – Language selection, model selection, Clear chat button, Download chat button.
5. **Error screen** – A red box with a simple explanation and a Retry button.
6. **Streamlit Cloud** – The deployed app link and the Secrets settings page (hide the key in the screenshot!).

---

## 16. LIMITATIONS

1. The chat is lost when the browser tab is closed (no database).
2. The free API tier has daily and per-minute limits.
3. AI answers can sometimes be wrong or made-up ("hallucination"), so facts must be checked.
4. Only text is supported (no voice or images).
5. Only the latest 20 messages are remembered in one conversation.
6. All users of the deployed app share one API key and one quota.
7. Free-tier prompts may be used by Google to improve its products.
8. Hinglish has no fixed spelling, so the style of the answer may vary.

---

## 17. FUTURE SCOPE

1. Add voice input and text-to-speech output.
2. Upload PDF or image files and ask questions about them.
3. Add user login and save chat history in a database.
4. Add Google Search grounding for up-to-date answers.
5. Add more languages (Marathi, Tamil, Bengali, and so on).
6. Show usage statistics and limits.
7. Convert the project into a college helpdesk chatbot with its own knowledge base.

---

## 18. CONCLUSION

The project "AI Chatbot Using Gemini API" shows how a modern, useful AI application can be built with very little code using Python, Streamlit and the official Google Gemini SDK. The chatbot remembers conversation context, supports English and Hinglish, protects the API key with Streamlit secrets, and handles errors in a friendly way. It was deployed online for free. While building it, I learned about APIs, SDKs, LLMs, session state, secure secret handling, error handling, Git and GitHub, and cloud deployment. The project can be extended in many ways, so it is a good base for future learning.

---

## 19. REFERENCES

1. Google Gen AI Python SDK – https://github.com/googleapis/python-genai
2. Gemini API Documentation – https://ai.google.dev/gemini-api/docs
3. Gemini API Models – https://ai.google.dev/gemini-api/docs/models
4. Gemini API Release Notes – https://ai.google.dev/gemini-api/docs/changelog
5. Google AI Studio (API keys) – https://aistudio.google.com/apikey
6. Streamlit Documentation – https://docs.streamlit.io
7. Streamlit Community Cloud – Deploy your app – https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
8. Streamlit Community Cloud – Secrets management – https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management
9. Python Documentation – https://docs.python.org/3/
10. GitHub Docs – https://docs.github.com

---

## APPENDIX A – SOURCE CODE

The complete source code is in the file `app.py` of the project and on GitHub: https://github.com/[your-username]/gemini-chatbot
*(Print `app.py` and attach it here if your college asks for source code in the report.)*

## APPENDIX B – SAMPLE secrets.toml (NO REAL KEY)

```toml
GEMINI_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"
```
