# 👩 AI Chatbot Using Gemini API – "Sara"

**BSc Computer Science – Semester 5 Mini Project**

Meet **Sara**, a friendly female AI chatbot built with **Python**, **Streamlit** and the **Google Gemini API** (official `google-genai` SDK). It remembers the conversation, replies in **English or Hinglish**, shows the answer live as it is being written, and handles errors (wrong API key, quota finished, no internet) with simple messages instead of crashing.

---

## ✨ Features

| Feature | How it works |
|---|---|
| Chat history | Every message is stored in `st.session_state` and shown on screen |
| Conversational context | Past messages are sent to Gemini with each new question, so it remembers what you said earlier |
| English + Hinglish | A "system instruction" tells Gemini which language to use (choose in the sidebar) |
| Live (streaming) replies | The answer appears word-by-word using `send_message_stream` |
| Clear chat button | One click deletes the whole conversation |
| Download chat | Saves the conversation as a `.txt` file |
| Model selector | Choose between Gemini 3.5 Flash-Lite, 3.6 Flash and 3.8 Flash |
| Secure API key | Read from Streamlit **secrets**, never written in the code, never uploaded to GitHub |
| Error handling | Invalid key, quota/rate limit, wrong model, server busy, timeout, no internet |
| Retry button | After an error, retry your last message with one click |

---

## 📁 Project structure

```
gemini-chatbot/
├── app.py                         ← the whole application
├── requirements.txt               ← libraries to install
├── README.md                      ← this guide
├── .gitignore                     ← tells Git to NEVER upload secrets
├── .streamlit/
│   ├── config.toml                ← theme (safe to upload)
│   ├── secrets.toml.example       ← SAMPLE secrets file (safe, no real key)
│   └── secrets.toml               ← YOUR real key (you create it; NEVER upload)
└── docs/
    ├── PROJECT_REPORT.md          ← project report
    └── VIVA_QUESTIONS.md          ← viva questions and answers
```

> ⚠️ `.streamlit/secrets.toml` does **not** exist when you download this project. You create it yourself in Step 3 (only for running on your own computer).

---

## 🧰 Model used

The app uses **`gemini-3.5-flash-lite`** by default and lets you switch to **`gemini-3.8-flash`** or **`gemini-3.6-flash`**.

These names were checked against Google's official documentation on **28 October 2026**. Older models such as `gemini-2.0-flash` have been shut down, and `gemini-2.5-flash` is now limited to people who used it before, so they are **not** used here.

Google changes model names regularly. If you ever see a **"Model not found"** error, open `app.py`, find `MODEL_OPTIONS` near the top and replace the model name with a current one from <https://ai.google.dev/gemini-api/docs/models>.

---

# 🚀 STEP-BY-STEP GUIDE (for beginners)

You need: a computer with internet, a Google account, and a GitHub account (free).

## STEP 1 – Install the tools (one time only)

1. **Python 3.10 or newer** – download from <https://www.python.org/downloads/>.
   - On Windows, tick **"Add Python to PATH"** on the first installer screen. This is important.
2. **A code editor** – VS Code from <https://code.visualstudio.com/> is recommended.
3. **A GitHub account** – sign up at <https://github.com/signup>.

Check Python is installed. Open **Command Prompt** (Windows) or **Terminal** (Mac) and type:

```
python --version
```

You should see something like `Python 3.12.x`. (On Mac, if this fails, use `python3 --version`.)

## STEP 2 – Get your free Gemini API key

1. Open <https://aistudio.google.com/apikey> and sign in with your Google account.
2. Click **Create API key** (create it in a new or existing project when asked).
3. **Copy** the key. It is a long text, usually starting with `AIza`.
4. Keep it private. Treat it like a password. **Never** put it in `app.py`, in WhatsApp groups, in screenshots or on GitHub.

Notes about the free tier:
- It is free but has **limits** (messages per minute and per day). If you see a "Quota" error, wait or switch to Flash-Lite in the sidebar.
- Google may use free-tier prompts to improve its products, so **do not type personal or private information** into the chatbot.

## STEP 3 – Run the chatbot on your own computer (test first!)

1. Put the project folder somewhere easy, for example `Desktop/gemini-chatbot`.
2. Open the folder in **VS Code** (File → Open Folder), then open the terminal: **Terminal → New Terminal**.
3. Create a virtual environment (a private box for this project's libraries):

   **Windows:**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   **Mac / Linux:**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
   You will now see `(venv)` at the start of the line.

4. Install the libraries:
   ```
   pip install -r requirements.txt
   ```
5. Create your **secrets file**:
   - Inside the `.streamlit` folder, make a **copy** of `secrets.toml.example` and rename the copy to exactly **`secrets.toml`**.
   - Open `secrets.toml` and replace the placeholder with your real key, keeping the quotes:
     ```toml
     GEMINI_API_KEY = "AIzaSy...your-real-key..."
     ```
   - Save the file.
6. Start the app:
   ```
   streamlit run app.py
   ```
   Your browser opens at `http://localhost:8501`. 🎉
7. Test it (see the checklist at the end of this guide). Press `Ctrl + C` in the terminal to stop the app.

## STEP 4 – Upload the project to GitHub

> 🔴 **Most important rule:** upload everything **except** `.streamlit/secrets.toml` and the `venv` folder.

### Option A – Using the GitHub website (easiest, no commands)

1. Log in to <https://github.com>.
2. Click the **+** icon (top-right) → **New repository**.
3. Repository name: `gemini-chatbot`. Choose **Public**. Do **not** tick "Add a README" (you already have one). Click **Create repository**.
4. On the next page click the link **"uploading an existing file"**.
5. Open your project folder on your computer. **Select and drag these into the GitHub page:**
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - the `.streamlit` folder – **but first open it and make sure `secrets.toml` is NOT inside the files you drag.** Only `config.toml` and `secrets.toml.example` should go.
   - the `docs` folder
6. **Do NOT drag:** `venv`, `__pycache__`, or `.streamlit/secrets.toml`.
7. Scroll down, type a message such as `Initial commit`, and click **Commit changes**.
8. **Double-check:** click into the `.streamlit` folder on GitHub. You must see `config.toml` and `secrets.toml.example` only. If you see `secrets.toml`, **delete it on GitHub immediately** and read "If your key leaks" below.

> 💡 The GitHub website upload does **not** read `.gitignore`. That is why you must choose the files yourself. If your computer hides files starting with a dot (`.gitignore`, `.streamlit`), turn on **View → Show hidden items** (Windows) or press `Cmd + Shift + .` (Mac).

### Option B – Using Git commands (professional way)

Install Git from <https://git-scm.com/downloads>. Create the empty repository on GitHub (steps 1–3 above). Then, in the VS Code terminal inside your project folder:

```
git init
git add .
git status
```

Read the list printed by `git status`. **`secrets.toml` and `venv` must NOT appear** (the `.gitignore` file blocks them). Then:

```
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/gemini-chatbot.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. GitHub may open a browser window asking you to log in the first time.

## STEP 5 – Deploy on Streamlit Community Cloud (free hosting)

1. Go to <https://share.streamlit.io> and sign in using **Continue with GitHub**. Allow the permissions it asks for.
2. Click **Create app** (top-right corner).
3. When asked *"Do you already have an app?"*, click **Yup, I have an app**.
4. Fill in the form:
   - **Repository:** `YOUR-USERNAME/gemini-chatbot`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL (optional):** choose a short name, e.g. `my-gemini-chatbot`
5. Click **Advanced settings**.
   - **Python version:** pick **3.12** (the default is fine).
   - In the **Secrets** box, paste exactly this line with **your real key**:
     ```toml
     GEMINI_API_KEY = "AIzaSy...your-real-key..."
     ```
   - Click **Save**.
6. Streamlit now builds and launches your app. Wait 2–3 minutes while it installs the libraries from `requirements.txt`.
7. When the chatbot appears, copy the address from your browser (like `https://my-gemini-chatbot.streamlit.app`). **This is your live project link** – put it in your report and show it in the viva.

**To change the key later:** open your app on Streamlit Cloud → **Manage app** (bottom-right) → **Settings → Secrets**, edit, save. If the app still uses the old key, reboot it from the same menu.

**To update the app later:** change the file on GitHub (or `git push` again). Streamlit redeploys automatically.

> Free apps go to "sleep" if nobody opens them for a while. If you see *"This app has gone to sleep"*, just click **Yes, get this app back up**. **Open your app once the evening before the viva** so it is awake.

## ✅ Testing checklist (do this before submitting)

- [ ] The app opens without errors.
- [ ] Ask: *"My name is Rahul"*, then ask: *"What is my name?"* → it should say Rahul (this proves memory works).
- [ ] Switch to **Hinglish** and ask *"Python kya hai?"* → the answer is in Roman Hindi.
- [ ] Switch back to **English** and ask a question → the answer is in English.
- [ ] Click **Clear chat** → the conversation disappears.
- [ ] Try the other model in the sidebar.
- [ ] (Optional) Put a wrong key in Secrets → you should see "Invalid or unauthorised API key". Then put the correct key back.
- [ ] Your GitHub repository does **not** contain `secrets.toml`.

---

## 🛠️ Troubleshooting

| What you see | What it means | What to do |
|---|---|---|
| 🔑 "Gemini API key not found" | Secret missing or has the wrong name | The name must be exactly `GEMINI_API_KEY`. Check `.streamlit/secrets.toml` (local) or Settings → Secrets (cloud) |
| "Invalid or unauthorised API key" | Key is wrong, deleted or has a space/quote problem | Create a new key in AI Studio and paste it again |
| "Quota / rate limit reached" | Free limit used up | Wait a minute, switch to **Flash-Lite**, or try tomorrow (daily limits reset every day) |
| "Model not found" | Google renamed or retired a model | Pick another model in the sidebar or update `MODEL_OPTIONS` in `app.py` |
| "Gemini is busy right now" | Google's server is overloaded | Wait a few seconds and click **Retry** |
| "Network problem" / "timed out" | Internet issue | Check your connection and retry |
| `ModuleNotFoundError: No module named 'google'` | Libraries not installed | Run `pip install -r requirements.txt` (with `(venv)` active) |
| `'streamlit' is not recognized` | venv not active or Streamlit not installed | Activate the venv, then `pip install -r requirements.txt` |
| Cloud build fails | Typo in `requirements.txt` or the file is missing from GitHub | Confirm `requirements.txt` is in the repo's main folder |
| Cloud app says "secrets not found" | Secrets box left empty | Manage app → Settings → Secrets → paste the key line |

---

## 🔒 Security rules (remember these)

1. The API key lives **only** in `.streamlit/secrets.toml` (on your PC) and in the Streamlit **Secrets** box (on the cloud).
2. `.gitignore` blocks `secrets.toml`, `.env` and `venv` from Git.
3. The code reads the key with `st.secrets["GEMINI_API_KEY"]` – the key itself never appears in `app.py`.
4. Error messages hide the key even if an error text contains it.

### 🚨 If your key leaks (uploaded to GitHub by mistake)

Deleting the file from GitHub is **not enough** – bots scan GitHub within minutes and old versions stay in history.

1. Go to <https://aistudio.google.com/apikey> and **delete** the leaked key.
2. **Create a new key.**
3. Put the new key in `secrets.toml` and in Streamlit Secrets.
4. Make sure `secrets.toml` is no longer in the repository.

---

## 🧠 How the code works (short)

1. `load_api_key()` reads the key from Streamlit secrets.
2. `get_client()` creates one `genai.Client` and reuses it.
3. When you send a message, `stream_reply()` calls `client.chats.create(...)` with your earlier messages as `history` and the language rule as `system_instruction`, then `chat.send_message_stream(prompt)` to get the answer in pieces.
4. The pieces are shown live. When the answer is complete, both your message and the reply are saved in `st.session_state.messages`.
5. If anything fails, `explain_error()` turns the technical error into a simple message, and your message is **not** saved, so the history never breaks.

## 📚 Documents

- Project report → [`docs/PROJECT_REPORT.md`](docs/PROJECT_REPORT.md)
- Viva questions → [`docs/VIVA_QUESTIONS.md`](docs/VIVA_QUESTIONS.md)

## 📜 Sources used to verify this project

- Google Gen AI Python SDK: <https://github.com/googleapis/python-genai>
- Gemini API models: <https://ai.google.dev/gemini-api/docs/models>
- Gemini API release notes: <https://ai.google.dev/gemini-api/docs/changelog>
- Streamlit Community Cloud – deploy: <https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy>
- Streamlit Community Cloud – secrets: <https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management>

---
*Made for educational purposes. AI answers can be wrong – always double-check important facts.*
