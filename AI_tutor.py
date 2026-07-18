from google import genai
from dotenv import load_dotenv
from google.genai import types
import os
import time
load_dotenv()

system_instruction = "You are an expert and patient AI tutor. If the user asks for factual information, definitions, lists, or recommendations, answer directly and clearly." \
"If the user asks for homework, coding problems, math problems, or wants to learn a concept, guide them step-by-step instead of immediately giving the full solution." \
"Be concise unless the user asks for more detail."
Token = os.getenv("Gemini_API_KEY")
client = genai.Client(api_key=Token)
if Token is None:
    print("API key not found")


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
                AI_response = ask_AI_Tutor(conversation_context)
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