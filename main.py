from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from groq import Groq
import logging
import boto3


app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Base model for request and response
class ChatRequest(BaseModel):
    user_input: str

class ChatResponse(BaseModel):
    response: str

# Load your API key from AWS Secrets Manager
def get_secret(secret_name):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name='your-region')  # Replace 'your-region' with the AWS region
    secret_value = client.get_secret_value(SecretId=secret_name)
    return secret_value['SecretString']

GROQ_API_KEY = get_secret('your-secret-name')  # Replace 'your-secret-name' with the actual name of your secret

@app.post("/chat", response_model=ChatResponse)
async def chat_completion(request: ChatRequest):
    try:
        user_input = request.user_input
        client = Groq(api_key=GROQ_API_KEY)

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="llama3-8b-8192",  # Ensure this model is supported
        )

        # Make the request to Groq API
        response = chat_completion.choices[0].message.content

        return ChatResponse(response=response)  # Return an instance of ChatResponse
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")  # Log the error
        raise HTTPException(status_code=500, detail="Internal Server Error")
