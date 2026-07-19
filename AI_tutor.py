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


def getDate_time():
    now = datetime.now()
    return now.strftime("%I:%M:%S %P")


def calculator(expression):
    try:
        return eval(expression)
    except Exception as e:
        return "Invalid expression"
    

def Motivational_quotes():
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

def generate_password():
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
            

def get_weather():
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
                                
def main():
    history = []
    Max_history =20
    print("="*50)
    print("AI tutor")
    print("="*50)
    while True:
        try:
            prompt = input("Ask AI tutor: ")
            if prompt.lower().strip() in ["bye","goodbye","exit","quit","q","stop","end","close","leave","terminate","finish","done",
                          "see you","see ya","farewell","exit()","quit()"]:
                 print("Goodbye")
                 break
            else:
                history.append(f"Users: {prompt}")
                conversation_context = "\n".join(history)
                start_time = time.time()
                AI_response = get_query(prompt , conversation_context)
                print(f"AI tutor: {AI_response}")
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