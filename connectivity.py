import os
from dotenv import load_dotenv
from groq import Groq


def main():
    try:
        # Load environment variables
        load_dotenv()

        # Get API key
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found in environment variables."
            )

        print("Environment ready. Sending prompt...")

        # Create Groq client
        client = Groq(api_key=api_key)

        # Define prompt
        prompt = "What is prompt engineering? Answer in one sentence."

        print(f"\nPrompt: {prompt}")

        # Send prompt to LLM
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # Extract response
        answer = response.choices[0].message.content

        print("\nResponse:")
        print(answer)

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"API/Network Error: {e}")


if __name__ == "__main__":
    main()
