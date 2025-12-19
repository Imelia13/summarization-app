# AI Text Summarization App

A web-based application for automatic text summarization using a pretrained T5 model and FastAPI backend.

## Project Structure

summarization-app/
├── backend/
│ ├── app/
│ ├── model/
│ ├── requirements.txt
│ └── start.sh
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js

## Backend

- Framework: FastAPI
- Model: T5 (pretrained)
- Endpoint: `POST /summarize`

Request:

```json
{ "text": "input text" }

Response:
{ "summary": "generated summary" }

## Frontend
- HTML, CSS, JavaScript
- Fetch API to communicate with backend

## Run Locally
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

```
