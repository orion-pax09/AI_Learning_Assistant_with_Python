# Python AI Learning Assistant

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Gemini API](https://img.shields.io/badge/Gemini-API-orange?logo=google&logoColor=white)
![Tavily](https://img.shields.io/badge/Tavily-Web%20Search-green)
![OpenWeather](https://img.shields.io/badge/OpenWeather-API-yellow)
![Status](https://img.shields.io/badge/Status-In%20Development-brightgreen)

A command-line AI tutor built with Google's Gemini API. It started out as a simple chatbot that answers questions, but it's slowly turning into something smarter — an assistant that can pick the right tool for the job, not just chat.

![Architecture](assets/architecture.svg)

## What this project actually does

At its core, you type a question or request into the terminal, and one of two things happens:

- If it's a normal question (like "explain recursion"), Gemini just answers it directly, like a tutor would.
- If it sounds like something that needs a tool (like "what's the weather in Tokyo"), Gemini figures out *which* tool fits best, and then Python actually runs that tool and gives you the result.

So Gemini isn't running the tools itself — it's more like the decision-maker. It looks at your message and says "this needs the weather tool" or "this needs the calculator." Then plain Python code takes over and does the actual work. If Gemini decides no tool is needed, it just answers you directly as a tutor.

There's also a separate part of the project — the **roadmap agent** — that builds you a 90-day learning plan for any topic. You trigger it by typing `roadmap` followed by your goal (e.g. `roadmap learn web development`), and it runs through three steps: it figures out the skills you need (reasoning), puts them in the right learning order (planning), and then writes out the full 90-day roadmap (execution).

## How a request flows through the app

**Normal question:**
```
You ask something → Gemini answers directly → You get a response
```

**Something that needs a tool:**
```
You ask something → Gemini decides which tool fits → Python runs that tool → You get the result
```

**Roadmap request:**
```
You type "roadmap <your goal>" → Reasoning → Planning → Execution → Full 90-day roadmap
```

## What it can do right now

- Chat with you like a tutor, and remember what you talked about earlier in the conversation
- Tell you the current time
- Do calculations
- Check the weather for a city
- Search the web (using Tavily)
- Give you a motivational quote when you need one
- Generate a secure random password
- Build you a 90-day learning roadmap for any goal

## The roadmap agent, a bit more detail

Typing `roadmap <goal>` skips the normal tool-selection step and goes straight into its own three-step process:

1. **Reasoning** – Gemini looks at your goal and figures out what skills are actually needed
2. **Planning** – it arranges those skills into the best order to learn them
3. **Execution** – it writes out the full 90-day roadmap based on that plan

## A couple of quick examples

**Asking about the weather:**
```
You: What's the weather in Tokyo?
Gemini decides: Weather_Tools
Python runs: get_weather()
You get: current weather for Tokyo
```

**Asking for motivation:**
```
You: Give me motivation.
Gemini decides: Motivational tools
Python runs: Motivational_quotes()
You get: a random motivational quote
```

**Just asking a normal question:**
```
You: What is a binary search tree?
Gemini decides: no_tool
Gemini answers directly, step by step
```

## Setting it up

1. Clone the repo:
```bash
git clone https://github.com/your-username/Python_AI_learning_Assistant.git
cd Python_AI_learning_Assistant
```

2. (Optional but recommended) make a virtual environment:
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

3. Install what it needs:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project folder and add your API keys:
```env
Gemini_API_KEY=your_gemini_api_key
Weather_API_key=your_weather_api_key
tavily_search_api=your_tavily_api_key
```

**Important:** don't ever commit your `.env` file to GitHub. Keep your keys private — make sure `.env` is in your `.gitignore`.

## Running it

```bash
python AI_tutor.py
```

Then just type whatever you want:
- Ask a question and get tutored
- Ask for the weather, a calculation, a password, or a motivational quote
- Type `roadmap <your goal>` to get a full 90-day learning plan

Type `exit`, `quit`, `bye`, or similar to end the session.

## Where this is headed

This is still very much a work in progress. Things I'm planning to add or improve:

- Using Gemini's actual function-calling feature instead of just asking it to name a tool in plain text
- Having the AI pull out the details it needs for a tool automatically (like the city name for weather), instead of asking for input separately
- Letting it chain multiple steps together instead of just picking one tool at a time
- Saving conversations and roadmaps somewhere permanent (a database) instead of losing them when the app closes
- A proper web interface, so it's not just a terminal app
- A FastAPI backend so other apps could talk to it too
- Actually deploying it somewhere so other people could use it

## A note on how the "tool selection" works

Right now, when I say Gemini "picks a tool," I mean I'm prompting it with the user's message and a list of tool names, and it just replies with the name of the one it thinks fits (or `no_tool` if none apply). Python then matches that name to a function and runs it. It's not using Gemini's official built-in function-calling system yet — that's one of the upgrades I want to make later.

## About me

Built by Muhammad Hamza Khan, as a way to learn how to actually build with LLMs instead of just using them.
