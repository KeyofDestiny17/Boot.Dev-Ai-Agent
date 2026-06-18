import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def get_api_key():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError(
            "Gemini API key not found. Please set the GEMINI_API_KEY environment variable."
            )
    return api_key

def parser():
    parser = argparse.ArgumentParser(description="Gemini Flash 2.5 Free")
    parser.add_argument("user_prompt", type=str, help="Your prompt for Gemini")
    return parser.parse_args()
    
def get_gemini_response(api_key, parser):
    args = parser()
    client = genai.Client(api_key=api_key)
    messages: list[types.chat.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
        )
     
    metadata = response.usage_metadata
    if not metadata:
        raise RuntimeError(
            "Failed to get a response. Check if connected to internet"
            )
    print(f"Prompt tokens: {metadata.prompt_token_count}")
    print(f"Response tokens: {metadata.candidates_token_count}")

    return response.text

def main():
    api_key = get_api_key()
    print("Waiting for Gemini response...")
    text = get_gemini_response(api_key, parser)
    print(text)




if __name__ == "__main__":
    main()