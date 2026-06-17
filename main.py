import os
from dotenv import load_dotenv
from google import genai

def main():
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Gemini API key not found. Please set the GEMINI_API_KEY environment variable.")

    client = genai.Client(api_key=api_key)
    print("Waiting for Gemini response...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
        ) 
    print(response.text)
    


if __name__ == "__main__":
    main()