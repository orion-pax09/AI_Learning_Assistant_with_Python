from google import genai
from dotenv import load_dotenv
from google.genai import types
import requests
import os
import time
from datetime import datetime
import random
from tavily import TavilyClient
load_dotenv()


class AI_Agent_Roadmap:
    def __init__(self , goal):
        self.goal = goal
    
    #step 01: Reasoning
    def reason(self):
        print("AI tutor understanding the goal....")
        prompt = f"""
        Goal: {self.goal}
        Identifying all skill required
        Return only to the skill"""

        response = client.models.generate_content(
            model= "gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    
    #step 02: Planning
    def planning(self,skill):
        print("AI planning the goal.....")
        prompt = f"""Goal: {self.goal}
        skill: {skill}
        Arrange these skill in best learning order"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    
    #step 03: Executing

    def executing(self,plan):
        print("AI executing the goal.....")
        prompt = f"""Goal: {self.goal}
        Learning the plan: {plan}
        Create the 90-days roadmap"""
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    
    #step 04: Run AI agent
    def run(self):
        skill = self.reason()
        time.sleep(1)

        plan = self.planning(skill=skill)
        time.sleep(1)

        execute = self.executing(plan=plan)
        print(execute)



system_instruction = "You are an expert and patient AI tutor. If the user asks for factual information, definitions, lists, or recommendations, answer directly and clearly." \
"If the user asks for homework, coding problems, math problems, or wants to learn a concept, guide them step-by-step instead of immediately giving the full solution." \
"Be concise unless the user asks for more detail."


Token = os.getenv("Gemini_API_KEY")
client = genai.Client(api_key=Token)
if Token is None:
    print("API key not found")

Token_Weather = os.getenv("Weather_API_key")
if Token_Weather is None:
    print("Weather API key not found")

Token_Tavily = os.getenv("tavily_search_api")
if Token_Tavily is None:
    print("Search API key not found")

def ask_AI_Tutor(prompt:str) -> str:
    print("Generating response......")
    full_stream_response = ""
    try:
        streams = client.models.generate_content_stream(
            model = "gemini-2.5-flash" ,
            contents = prompt , 
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=  0.1,
                max_output_tokens= 3000,
            )
        )
        for chunks in streams:
            if chunks.text:
                print(chunks.text , end="" , flush=True)
                full_stream_response +=chunks.text
            
        return full_stream_response
    except Exception as e:
        print("An error occured: ", e)


def getDate_time(query=None):
    now = datetime.now()
    return now.strftime("%I:%M:%S %P")


def calculator(expression):
    try:
        return eval(expression)
    except Exception as e:
        return "Invalid expression"
    

def Motivational_quotes(query=None):
    quotes = [
    "Discipline beats motivation.",
    "No pain, no gain.",
    "Success is earned, not given.",
    "Pain is temporary. Quitting lasts forever.",
    "Every expert was once a beginner.",
    "Talk is cheap. Show me the code.",
    "First, solve the problem. Then, write the code.",
    "Comfort is the enemy of progress.",
    "Consistency beats intensity.",
    "One bug at a time.",
    "Pressure creates diamonds.",
    "Stay hungry. Stay foolish.",
    "Dream big. Start small. Act now.",
    "Small improvements every day lead to big results.",
    "You become what you repeatedly do.",
    "The grind never lies.",
    "Build. Break. Learn. Repeat.",
    "Your only competition is who you were yesterday.",
    "Hard times create strong people.",
    "The best developers were once confused beginners.",
    "Your GitHub tells the story your résumé can't",
    "Discipline gets you to the gym. Consistency builds your body. Persistence writes the code. Time rewards them all",
    "Pain is temporary. Quitting lasts forever.",
    "Don't wish for it. Work for it.",
    "Train like a beast.",
    "Every workout counts.",
    "One more rep.",
    "One more problem.",
    "Success is earned, not given.",
    "One more day.",
    "Win the day.",
    "Stay disciplined.",
    "Trust the process.",
    "Never stop learning."
]
    return random.choice(quotes)

def generate_password(query=None):
    symbol = "AB`CD~EFGHI!JK@LM#NO$PQ%RS^TU&VW*XY(Za)bc+d9-e8=f7g6h5i4j321klmnopqrstuvwxyz"
    try:
        length = int(input("Enter the length of input: "))
        if length <=0:
            return "❌ length should not be less than or equal to zero"
        if length >=len(symbol):
            return f"❌ length shouldn't exceed the {len(symbol)}"
        password = "".join(random.sample(symbol,length))
        return password
    
    except Exception as e:
        return "Invalid. Enter the length in digit"
            

def get_weather(query=None):
    city = input("Enter the city: ")
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={Token_Weather}")
    try:
        if weather_data.status_code==200:
            data = weather_data.json()
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            description = data["weather"][0]["description"]
            City = data["name"]
            return (
                f"📍Location: {City}\n"
                f"🌡️Temperature: {temperature:.1f}°C\n"
                f"🥵Feel like Temperature: {feels_like:.1f}°C\n"
                f"☁️Weather: {description}\n"
                )
        else:
            return f"❌{city} does not exist. Please check the spelling"
    except Exception as e:
        return "❌ Unable to connect to the weather service. Please try again later."

def get_web_searching(query):
    client = TavilyClient(Token_Tavily)
    response = client.search(query)
    result = ""
    for items in response['results']:
        result +=f"{items['title']}\n"
        result +=f"{items['content']}\n\n"
    return result

def get_query(query , Conservational_context):
    WEB_KEYWORDS = [
    "latest",
    "today",
    "current",
    "news",
    "recent",
    "live",
    "score",
    "winner",
    "price",
    "release",
    "version",
    "documentation",
    "docs",
    "research",
    "paper",
    "api",
    "sport",
    "fifa",
    "game",
    "GTA"
    ]
    if "time" in query.lower():
        return getDate_time()
    elif "motivational" in query.lower() or "quotes".lower().strip() in query.lower():
        return Motivational_quotes()
    elif "generate password" in query.lower():
        return generate_password()
    elif "weather" in query.lower() or "city".lower().strip() in query.lower():
        return get_weather()
    elif any(keywords in query.lower() for keywords in WEB_KEYWORDS):
        return get_web_searching(query)
    else:
        return ask_AI_Tutor(Conservational_context)

def Generate_ROADMAP(topic):
    return f""""
    Roadmap for {topic}
    1. Learn Fundamental
    2. Practice Projects
    3. Build portfolio
    4. Apply for jobs
    """""

TOOlS = {
    "time_tools" : getDate_time,
    "Calculator_tools": calculator,
    "Weather_Tools":get_weather,
    "web_Search_tools":get_web_searching,
    "Motivational tools":Motivational_quotes,
    "Generate password tools":generate_password,
    "Road map tools":Generate_ROADMAP
}

def select_tools(conversation_context):
    prompt = f"""
You are an intelligent tool-selection system.

Your job is to decide whether the user's request requires
a tool or can be answered directly by the AI.

Available tools:
- time_tools
- Calculator_tools
- Weather_Tools
- web_Search_tools
- Motivational tools
- Generate password tools
- Road map tools
- no_tool

Tool descriptions:
- time_tools: Get the current time.
- Calculator_tools: Perform numerical calculations.
- Weather_Tools: Get weather information.
- web_Search_tools: Search the internet for current or external information.
- Motivational tools: Provide motivational quotes or motivation.
- Generate password tools: Generate passwords.
- Road map tools: Create learning roadmaps.
- no_tool: Use this when the AI can answer the user's request directly
  without using any external tool.

Rules:
1. Understand the user's intent.
2. Use conversation context for follow-up requests.
3. Select a tool only when that tool is actually required.
4. Do NOT force a tool selection.
5. If the user asks for explanations, concepts, derivations,
   programming help, general knowledge, or tutoring,
   use no_tool unless another tool is clearly required.
6. If the request is a calculation, use Calculator_tools.
7. If the request requires current or external information,
   use web_Search_tools.
8. Always return exactly one option.
9. Return ONLY the exact tool name.
10. Never return None.

Conversation context:
{conversation_context}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()


def Execute_tools(tool_name,query):
    if tool_name not in TOOlS:
        return f"Tools not found: {tool_name}"
    tools = TOOlS[tool_name]
    return tools(query)    

def main():
    history = []
    Max_history =20
    print("="*50)
    print("AI tutor")
    print("="*50)
    while True:
        try:
            prompt = input("Ask AI tutor: ")
            # Roadmap agent 
            if prompt.lower().strip() in ["bye","goodbye","exit","quit","q","stop","end","close","leave","terminate","finish","done",
                          "see you","see ya","farewell","exit()","quit()"]:
                 print("Goodbye")
                 break
            else:
                if prompt.lower().startswith("roadmap"):
                    goal = prompt[8:].strip()
                    agent = AI_Agent_Roadmap(goal=goal)
                    agent.run()
                    print("\n" + "="*50)
                    print("Final roadmap")
                    print("="*50 , end="")
                    
                    # after running roadmap agent, skip normal query handling
                    
                    continue

                #Save user Query

                history.append(f"Users: {prompt}")
                conversation_context = "\n".join(history)
                start_time = time.time()

                # Ask LLM which tools to use
                tools_name = select_tools(conversation_context)

                #if no such tools found then shift AI tutor to assisstant
                if tools_name == "no_tool":
                    AI_response = ask_AI_Tutor(conversation_context)
                else:
                    #otherwise shift AI tutor to become AI agent
                    print(f"Tool selected: {tools_name}")
                    AI_response = Execute_tools(tool_name=tools_name ,query=prompt)

                print(AI_response)

                print()

                history.append(f"AI tutor: {AI_response}")
                
                if len(history)>Max_history:
                    history = history[-Max_history:]
                
                end_time = time.time() 
                total_time=round(end_time - start_time, 2)
                print(f"\nResponse time taken: {total_time} seconds")
            
        except Exception as e:
            print("AI tutor is unavailable temporary")
            print(e)




if __name__ == "__main__":
    main()