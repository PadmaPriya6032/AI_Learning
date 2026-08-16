# Set your OpenAI API key as an environment variable
# IMPORTANT: Replace "YOUR_ACTUAL_API_KEY_HERE" with your actual key.
# For Colab, you can also use the 'Secrets' panel for better security.
import os


def method1():
    os.environ["OPENAI_API_KEY"] = "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"
    print("OPENAI_API_KEY environment variable set.")


    # Retrieve and print the OPENAI_API_KEY environment variable
    api_key_value = os.getenv("OPENAI_API_KEY")
    print("Retrieved OPENAI_API_KEY:", api_key_value)
    return api_key_value


# def method2():
#     import getpass

#     # Prompt for the API key securely
#     openai_api_key = getpass.getpass("Enter your OpenAI API Key: ")

#     # Set the environment variable
#     os.environ["OPENAI_API_KEY"] = openai_api_key

#     print("OPENAI_API_KEY environment variable set securely.")


