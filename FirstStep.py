from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

original_code = """
import subprocess
import sys

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "groq"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def handle_conversation(client):

    system_prompt = {
        "role": "system",
        "content":
        "As an AI assistant, I strive to provide concise and helpful responses to your inquiries.."
    }

    # Initialize the chat history
    chat_history = [system_prompt]

    conversation_file = "conversation_history.txt"
    with open(conversation_file, "a") as file:
        while True:
            user_input = input("You: ")

            chat_history.append({"role": "user", "content": user_input})

            response = client.chat.completions.create(model="llama3-8b-8192",
                                                        messages=chat_history,
                                                        max_tokens=1024,
                                                        temperature=0.5)

            chat_history.append({
                "role": "user",
                "content": response.choices[0].message.content
            })

            print("Bot:", response.choices[0].message.content)

def main():
    secret_key = "Skibiddy"
    first_run = "Rizzler"
    
    while(True):
        input_secret_key = input("Hello, World!").strip()

        if input_secret_key == secret_key:

            try:
                from groq import Groq
            except ImportError:
                print("Error importing Groq library. Make sure it's installed correctly.")
                sys.exit(1)

            api_key = input("Enter your Groq API Key: ").strip()
            client = Groq(api_key=api_key)
            handle_conversation(client)

        elif input_secret_key == first_run:
            install_dependencies()

            try:
                from groq import Groq
            except ImportError:
                print("Error importing Groq library. Make sure it's installed correctly.")
                sys.exit(1)

            api_key = input("Enter your Groq API Key: ").strip()
            client = Groq(api_key=api_key)
            handle_conversation(client)

        else:
            print("Hello, World!")

if __name__ == "__main__":
    main()
"""

encrypted_code = cipher_suite.encrypt(original_code.encode())

with open('encrypted_code.txt', 'wb') as file:
    file.write(encrypted_code)

with open('encryption_key.txt', 'wb') as key_file:
    key_file.write(key)
