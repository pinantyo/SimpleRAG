import os
from decouple import config
from groq import Groq


class ChatBot:
    def __init__(self, ):
        self.client = Groq(
            # This is the default and can be omitted
            api_key=config("GROQ_API"),
        )

    def text_similarity(self, query, context):
        pass
    
    def interact(self, query):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a helpful assistant."
                },{
                    "role": "user",
                    "content": query,
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        return chat_completion.choices[0].message.content
