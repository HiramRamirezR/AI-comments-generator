import torch
from transformers import pipeline

generator = pipeline('text-generation', model='distilgpt2')

def generate_comment(text, tone):
    """
    Generates a comment for a given text and tone.

    Args:
        text (str): The text of the social media post.
        tone (str): The desired tone of the comment.

    Returns:
        list: A list of generated comments.
    """
    prompt = f"Generate a {tone} comment for the following post: {text}"
    response = generator(
        prompt,
        max_length=50,
        num_return_sequences=3
    )
    return [res['generated_text'] for res in response]
