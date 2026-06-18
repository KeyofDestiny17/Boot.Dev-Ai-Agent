import os
from dotenv import load_dotenv
from google import genai

def get_api_key():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError(
            "Gemini API key not found. Please set the GEMINI_API_KEY environment variable."
            )
    return api_key

def get_gemini_response(api_key, prompt):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
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
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    print("Waiting for Gemini response...")
    text = get_gemini_response(api_key, prompt)
    print(text)




if __name__ == "__main__":
    main()