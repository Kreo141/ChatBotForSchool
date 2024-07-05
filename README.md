

---

# Sneaky Groq Chatbot

Welcome to the Sneaky Groq Chatbot! This isn't just any chatbot—it's your secret weapon for navigating school bans on AI tools. When your professor runs it, it simply says "Hello, World!" But for you, it’s a full-fledged chatbot ready to assist.

## What Does It Do?

- **For Professors:** A polite "Hello, World!" greeting.
- **For You:** A helpful chatbot that maintains conversation history and assists with your programming questions.

## How to Use

1. **Download and Install:**
    - Clone this repository:

    ```sh
    git clone https://github.com/Kreo141/ChatBotForSchool.git
    cd sneaky-groq-chatbot
    ```

2. **Set Up Your Environment:**
    - Install dependencies (only when you enter the secret key):

    ```sh
    pip install cryptography
    ```

3. **Encrypt the Code:**

    ```python
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

    with open('CODES/encrypted_code.txt', 'wb') as file:
        file.write(encrypted_code)

    with open('CODES/encryption_key.txt', 'wb') as key_file:
        key_file.write(key)
    ```

4. **Run the Program:**

    ```python
    from cryptography.fernet import Fernet

    with open('CODES/encryption_key.txt', 'rb') as key_file:
        key = key_file.read()

    cipher_suite = Fernet(key)

    with open('CODES/encrypted_code.txt', 'rb') as file:
        encrypted_code = file.read()

    decrypted_code = cipher_suite.decrypt(encrypted_code).decode()

    exec(decrypted_code)
    ```

5. **Secret Key:**
    - When prompted, enter the secret key: `Skibiddy Ohio Gyatt`

    If you enter the secret key correctly, the chatbot functionality will be activated. Otherwise, it just prints "Hello, World!" and remains inconspicuous.

## Code Example

Here's a sneak peek of the magic:

```python
import os
from groq import Groq

# Create the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Initialize the chat history
chat_history = []

while True:
    # Get user input from the console
    user_input = input("You: ").strip()

    # Append the user input to the chat history
    chat_history.append({"role": "user", "content": user_input})

    # Create a completion with the current chat history
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=100,
        temperature=1.2
    )

    # Append the assistant's response to the chat history
    chat_history.append({
        "role": "assistant",
        "content": response.choices[0].message.content
    })

    # Print the assistant's response
    print("Assistant:", response.choices[0].message.content)
```

## Disclaimer

This project is for educational purposes only. Use it responsibly and be mindful of your school's policies. If your professor asks, just say it’s a "Hello, World!" program with some extra flair. 😉

Happy coding!

---
