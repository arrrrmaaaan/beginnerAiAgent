import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types

def main():
    print("Hello from beginneraiagent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY environment variable is not set.")
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    query = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        config=types.GenerateContentConfig(system_instruction="Respond with only 1 line. Be concise."),
        contents=messages
    )

    ## Printing
    if response.usage_metadata is not None:
        if args.verbose == True:
            print(f"User prompt: {query}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Response:")
        print(f"{response.text}")   
    else:
        raise RuntimeError("Error when calling the API.")



if __name__ == "__main__":
    main()
