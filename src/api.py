from fastapi import FastAPI
from pydantic import BaseModel
from .generator import generate_comment

# Data model
class CommentRequest(BaseModel):
    text: str
    tone: str

# Create an instance of the FastAPI application
app = FastAPI()

# Define the API endpoint
@app.post("/generate-comment")
async def generate_comment_endpoint(request: CommentRequest):
    """
    Generates a list of comments for a given text and tone.
    """
    comments = generate_comment(text=request.text, tone=request.tone)
    # Return comments in a JSON
    return {"comments": comments}