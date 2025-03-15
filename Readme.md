# Groq API Integration for RAG Framework

This project is a FastAPI-based implementation that integrates Groq LLMs for Retrieval-Augmented Generation (RAG). The API allows users to send queries and receive responses from the Groq model while securely managing API keys via AWS Secrets Manager.

## Features

- FastAPI-based REST API for Groq LLM integration.
- Secure API key management using AWS Secrets Manager.
- Logging for monitoring errors and requests.
- Asynchronous API for efficient handling of requests.

## Requirements

Ensure you have the following dependencies installed:

```sh
pip install fastapi boto3 groq pydantic uvicorn
```

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/groq_rag_api.git
   cd groq_rag_api
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up AWS Secrets Manager with the Groq API key:
   - Store your API key in AWS Secrets Manager under the secret name `groq_key` with the key `GROQ_API`.

## Usage

### Running the API

Start the FastAPI server using Uvicorn:

```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### API Endpoints

#### Chat Completion

- **Endpoint:** `POST /chat`
- **Request Body:**
  ```json
  {
    "user_input": "Hello, how are you?"
  }
  ```
- **Response:**
  ```json
  {
    "response": "I am an AI model. How can I assist you?"
  }
  ```

## Environment Variables

Ensure you have AWS credentials set up for accessing Secrets Manager.

## Logging

The application logs errors and important events using Python’s built-in logging module.

## Deployment

For deployment, consider using AWS Lambda, ECS, or any containerized solution like Docker.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

