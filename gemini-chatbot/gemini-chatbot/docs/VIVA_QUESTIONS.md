# Viva Questions and Answers
### Project: AI Chatbot Using Gemini API (chatbot name: Sara)

Learn the answers in your own words. Short, honest answers are better than memorised long ones. If you do not know something, say: *"I did not study that part in depth, but I understand it as…"*

---

## 🎬 Your 2-minute demo script

1. *"My project is an AI chatbot named Sara, built with Python, Streamlit and the Google Gemini API."*
2. Open the live link. Say: *"It is deployed on Streamlit Community Cloud."*
3. Type **"My name is Rahul"**, then **"What is my name?"** → *"It remembers the conversation. This is called context."*
4. Switch to **Hinglish**, ask **"Python kya hai?"** → *"It can answer in Hinglish too."*
5. Click **Clear chat** → *"This deletes the history."*
6. Say: *"The API key is not in my code. It is stored in Streamlit secrets, and `.gitignore` stops it going to GitHub."*
7. Say: *"If the key is wrong or the quota is finished, the app shows a friendly message instead of crashing."*

---

## A. Basic questions

**1. What is your project about?**
It is a web chatbot named Sara. The user types a question, and Sara, powered by the Gemini AI model, answers. It remembers the earlier conversation and can reply in English or Hinglish.

**2. What is a chatbot?**
A chatbot is a program that talks with people using text or voice.

**3. What is AI?**
AI (Artificial Intelligence) means making computers do tasks that normally need human intelligence, like understanding language.

**4. What is an LLM?**
A Large Language Model is an AI model trained on a huge amount of text. It can understand questions and write answers. Gemini is an LLM from Google.

**5. What is Gemini?**
Gemini is Google's family of AI models. We use it through the Gemini API.

**6. What is an API?**
An Application Programming Interface lets one program talk to another. My app sends the question to Google's server using the API and gets the answer back.

**7. What is an SDK?**
A Software Development Kit is a ready-made library. The `google-genai` SDK gives me simple Python functions so I do not have to write raw web requests.

**8. What is Streamlit?**
It is a Python library to create web apps using only Python, without HTML, CSS or JavaScript knowledge.

**9. Why did you choose Streamlit?**
It is easy, fast, has built-in chat components, and has free hosting (Streamlit Community Cloud).

**10. Which language and libraries did you use?**
Python, with `streamlit` and `google-genai` (plus `httpx`, which comes automatically with the SDK and which I use to detect network errors).

---

## B. Questions about how the project works

**11. How does your chatbot remember the conversation?**
I save every message in `st.session_state.messages`. Before each new question, I send the old messages to Gemini as `history`. So Gemini knows what was said before.

**12. What is `st.session_state`?**
Streamlit re-runs the whole script after every click, which would erase normal variables. `st.session_state` is a special storage that survives these re-runs, so the chat history stays.

**13. Why does Streamlit re-run the script every time?**
That is how Streamlit works: whenever the user does something, it runs the Python file again from top to bottom and refreshes the screen.

**14. What is a system instruction?**
It is a hidden instruction given to the model before the conversation, such as "always reply in Hinglish." It controls the bot's behaviour and language.

**14b. How did you give the bot the name Sara and a female personality?**
In the system instruction I wrote "Your name is Sara" and that she is a friendly female assistant. For Hinglish I also told her to use feminine Hindi grammar, like "main kar sakti hoon". The name is stored in `BOT_NAME` in `app.py`, so it is easy to change.

**15. How did you implement Hinglish?**
Through the system instruction. For Hinglish, it tells Gemini to reply in Hindi written with English letters, mixed with English words. There is a radio button in the sidebar to switch.

**16. What is Hinglish?**
A mix of Hindi and English written in the English alphabet, for example: "Kal exam hai, preparation kaise karu?"

**17. What are the roles `user` and `model`?**
Gemini marks each message as coming from the `user` or the `model` (the AI). In my app I store `assistant`, and convert it to `model` in `build_history()`.

**18. What is streaming?**
The answer arrives in small pieces and is shown while being generated, so the user does not wait for the whole answer. I used `send_message_stream`.

**19. What is the difference between `generate_content` and `chats`?**
`generate_content` sends one request with no memory. The chat object is made for multi-turn conversations and works with history. I used `client.chats.create(...)`.

**20. Why do you send only the last 20 messages?**
Longer history means more tokens, more cost and slower answers, and it can hit limits. The latest 20 messages are enough for good context.

**21. What is a token?**
A token is a small piece of text (a word or part of a word). Models read and charge usage in tokens.

**22. What does `@st.cache_resource` do?**
It creates the Gemini client once and reuses it, instead of creating a new one after every click.

**23. Which Gemini model did you use and why?**
`gemini-3.5-flash-lite` by default, because it is fast and works on the free tier. The user can also choose `gemini-3.6-flash` or `gemini-3.8-flash`. I checked Google's official model list for currently supported models. Older ones like `gemini-2.0-flash` are shut down.

**24. Why don't you use temperature settings?**
Google's release notes mark `temperature`, `top_p` and `top_k` as deprecated for newer models, so I kept the default behaviour.

---

## C. Security questions

**25. Where is your API key stored?**
In Streamlit secrets: in `.streamlit/secrets.toml` on my computer (not uploaded) and in the Secrets box on Streamlit Cloud. It is not in my code.

**26. Why should the API key not be in the code?**
If it is in the code and I upload it to GitHub, anyone can steal it and use my quota or run up bills. Bots scan GitHub for keys.

**27. How do you stop the key going to GitHub?**
The `.gitignore` file lists `.streamlit/secrets.toml`, so Git ignores it. I upload only `secrets.toml.example`, which has a fake value.

**28. What will you do if the key is leaked?**
Delete it immediately in Google AI Studio, create a new key, update it in secrets, and make sure the file is not in the repository. Deleting only from GitHub is not enough because old versions stay in history.

**29. What is a `.gitignore` file?**
A file that tells Git which files or folders it must not track or upload.

**30. How do you read the secret in the code?**
`st.secrets["GEMINI_API_KEY"]`.

**31. What data privacy issue exists?**
On the free tier, Google may use prompts to improve its products, so users should not enter personal information. My app also does not store chats in any database.

---

## D. Error handling questions

**32. What errors does your app handle?**
Invalid API key, quota or rate limit (error 429), model not found (404), Google server errors (5xx), timeout, no internet, empty or blocked answer, and any unknown error.

**33. What is error 429?**
"Too Many Requests" with status `RESOURCE_EXHAUSTED`. It means the free quota or rate limit is finished. Waiting, switching to a lighter model, or trying the next day fixes it.

**34. How did you catch the errors?**
With `try/except`. The SDK gives `ClientError` (4xx) and `ServerError` (5xx) in `google.genai.errors`. Network problems come as `httpx` errors. My `explain_error()` function converts them into simple messages.

**35. What happens to the chat history if an error occurs?**
The failed question is not saved, so the history stays correct. A Retry button can resend it.

**36. Why don't you show the full technical error?**
It confuses users, and it could expose sensitive details. I show a simple explanation and replace the key with `***` if it ever appears in text.

---

## E. Deployment and Git questions

**37. What is GitHub?**
A website to store code online using Git, a version-control system.

**38. What is Git?**
A tool that tracks changes in code and helps share it.

**39. What is `requirements.txt`?**
A file listing the libraries the project needs. Streamlit Cloud installs them automatically.

**40. How did you deploy the project?**
I pushed the code to GitHub, signed in to share.streamlit.io with GitHub, clicked Create app, chose my repository, branch `main` and file `app.py`, pasted my key into Advanced settings → Secrets, and saved. Streamlit built the app and gave me a public link.

**41. Why is the app sometimes "sleeping"?**
Free Streamlit apps sleep when nobody visits for some time. One click wakes them up.

**42. Do all visitors share the same API key?**
Yes. All users use my key and my quota, which is a limitation. A bigger system would need login and usage limits per user.

---

## F. Understanding and improvement questions

**43. What are the limitations of your project?**
No permanent storage, free quota limits, answers can be wrong, text only, and all users share one key.

**44. What is hallucination?**
When an AI gives a confident answer that is wrong or made up. So important facts must be verified.

**45. How can you improve this project?**
Add voice, file upload, user login, database for chat history, Google Search grounding for current information, and more languages.

**46. How is this different from ChatGPT or the Gemini app?**
Those are complete products. My project is a small application that I built myself using the Gemini API. It shows how to integrate an AI model into my own app, add memory, language control, security and deployment.

**47. What did you learn from this project?**
Using an AI API and SDK, Streamlit, session state, secret management, error handling, Git/GitHub, and cloud deployment.

**48. Can the bot work without internet?**
No. The AI model runs on Google's servers, so internet is required.

**49. Which part did you find most difficult?**
*(Give your honest answer. For example: "Understanding how Streamlit re-runs the script and why I needed `st.session_state`," or "Handling the different error types.")*

**50. Show me where in the code the memory is created.**
In `build_history()` (turns saved messages into Gemini format) and `stream_reply()` (passes it as `history` to `client.chats.create`).

---

## ✅ Last-day checklist

- [ ] Open the live app today and test it once (wakes it up).
- [ ] Keep a backup: the project folder on a pen drive and the code on GitHub.
- [ ] Have your Gemini key ready in case you must re-enter it in Secrets.
- [ ] Take screenshots in case the internet fails in the lab.
- [ ] Print the report and fill in your name, roll number and college details.
- [ ] Be able to run it locally too: `streamlit run app.py`.
