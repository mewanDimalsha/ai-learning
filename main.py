import utils.clients
import utils.http_session
import utils.transport
import utils.session
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents="Who is mewan dimalsha?"
# )

chat_session = client.chats.create(model="gemini-3-flash-preview")


def chat(user_input):
    response = chat_session.send_message(user_input)
    return response.text


# print(response.text[:100])
while True:
    user_input = input("What is the questions you want to ask from ai? ")
    if user_input.lower() == "quit":
        break
    result = chat(user_input)
    print(result)
