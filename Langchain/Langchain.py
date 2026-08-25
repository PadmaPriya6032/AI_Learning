from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import FewShotChatMessagePromptTemplate

import os

from openai import OpenAI
from API_Token.API_Token import method1
import base64


api_token = method1()  # Call method1 to set the API key and retrieve it
client = OpenAI(api_key=api_token)  # Use the retrieved API key to create

openai = ChatOpenAI(
    model="gpt-3.5-turbo"
)

response = openai.invoke(

    "What is a savings account?"
)

print(response.content)