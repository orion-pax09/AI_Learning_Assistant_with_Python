# 🎓 AI Learning Assistant with Python

A command-line AI tutor powered by Google's Gemini API — ask questions, get patient, step-by-step explanations, and learn at your own pace right from your terminal.

<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Gemini%20API-Google-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini API">
  <img src="https://img.shields.io/badge/Status-Active%20Development-orange?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge" alt="PRs Welcome">
</p>

---

## 📖 Overview

**AI Learning Assistant** is a lightweight, extensible command-line application that turns Google's Gemini API into a personal tutor. Instead of just returning raw model output, the assistant is guided by a custom **system instruction** that shapes its behavior — encouraging it to break down complex topics step by step, while still answering direct factual questions concisely and accurately.

The project is intentionally built with clean, modular Python so it can grow from a simple CLI tool into a full-stack learning platform (see [Future Improvements](#-future-improvements)).

**Why this project?**
- Demonstrates practical integration with a modern LLM API (Gemini)
- Shows secure configuration/secrets management with `.env`
- Emphasizes clean code structure and error handling
- Serves as a foundation for a larger AI-powered application

---

## ✨ Features

1.💬 Interactive CLI Chatbot :- Ask questions directly in your terminal and get real-time responses 
2.🤖 Gemini API Integration  :- Uses Google's `google-genai` SDK to communicate with Gemini models 
3.🔐 Secure API Key Management :- API keys are stored in a `.env` file, never hardcoded or committed 
4.🧑‍🏫 System Prompt Customization :- A tutor-style system instruction guides the AI's tone and teaching approach 
5.🛡️ Robust Error Handling :- Graceful `try/except` handling for API and runtime errors 
6.🧩 Modular Code Structure :- Organized into clear, reusable components for easy extension 

---
Example interaction:

```
$ python main.py

🎓 AI Learning Assistant — type 'exit' to quit

You: What is a binary search tree?
Tutor: Great question! Let's break it down step by step...
1. A binary search tree (BST) is a data structure...
2. Each node has at most two children...
3. The left child is always smaller, the right child is always larger...
```

---

## ⚙️ Installation

### Prerequisites
- Python **3.9+**
- A **Google Gemini API key** ([Get one here](https://ai.google.dev/))
- `pip` package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ai-learning-assistant.git
   cd ai-learning-assistant
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Environment Variables

This project uses a `.env` file to securely store your Gemini API key.

1. Copy the example file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` and add your API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

**`.env.example`**
```env
# Google Gemini API Key
# Get your key from: https://ai.google.dev/
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file. It is already included in `.gitignore`.

---

## 🚀 Usage

Run the assistant from your terminal:

```bash
python main.py
```

Then simply type your question and press **Enter**:

```
You: Explain how recursion works
Tutor: Sure! Let's go step by step...
```

Type `exit` or `quit` to end the session.

---

## 📂 Project Structure

```
ai-learning-assistant/
│
├── main.py                # Entry point — runs the CLI chat loop
├── tutor.py               # Core logic for Gemini API calls & response handling
├── config.py               # Loads environment variables and app configuration
├── requirements.txt        # Python dependencies
├── .env.example             # Example environment variable file
├── .gitignore
└── README.md
```

> Structure may vary slightly depending on your implementation — update this section to match your actual file layout.

---

## 🧠 How the Gemini API Is Used

The application uses Google's **`google-genai`** SDK to communicate with the Gemini model. At a high level:

1. **Configuration** — The API key is loaded securely from the `.env` file using `python-dotenv`.
2. **Client Initialization** — A Gemini client is created using the loaded API key.
3. **System Instruction** — A custom system prompt is passed to the model, instructing it to act as a **patient, step-by-step tutor** while still answering direct factual questions concisely.
4. **User Input Loop** — The app continuously reads user input from the terminal.
5. **Response Generation** — Each user message is sent to the Gemini model along with the system instruction, and the generated response is printed back to the terminal.
6. **Error Handling** — API calls are wrapped in `try/except` blocks to catch and gracefully handle network issues, invalid keys, or unexpected API errors.

Example (simplified) flow:

```python
from google import genai

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=user_input,
    config={"system_instruction": TUTOR_SYSTEM_PROMPT}
)

print(response.text)
```

---

## 🛣️ Future Improvements

Planned enhancements to expand this project's capabilities:

- 🧵 **Conversation Memory** — Maintain context across multiple turns
- ⚡ **Streaming Responses** — Display AI output token-by-token in real time
- 💾 **Save Chat History** — Persist conversations to a local file or database
- 🎭 **Multiple Tutor Modes** — e.g., beginner, exam-prep, socratic-style tutoring
- 🌐 **Streamlit Web Interface** — A browser-based UI for non-technical users
- 🔌 **FastAPI Backend** — Expose the tutor as a REST API for other apps to consume
-📝 **Markdown Response Rendering** — Render formatted code blocks, lists, and tables in output

---

## 💡 What I Learned

Building this project helped me strengthen several practical skills:

- Integrating a third-party AI API (Gemini) into a real Python application
- Managing secrets and configuration securely using environment variables
- Designing effective system prompts to control AI behavior and tone
- Structuring a small Python project in a modular, maintainable way
- Implementing defensive programming with proper error handling
- Thinking about a project's roadmap and designing code that can scale (CLI → web app → API)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure to update tests and documentation as appropriate.

---

👤Author

Muhammad Hamza Khan

---

<p align="center"> Made with ❤️ and Python </p>
