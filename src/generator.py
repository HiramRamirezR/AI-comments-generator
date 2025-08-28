import torch
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2-medium')

def generate_comment(text, tone):
    """
    Generates a comment for a given text and tone.

    Args:
        text (str): The text of the social media post.
        tone (str): The desired tone of the comment.

    Returns:
        list: A list of generated comments.
    """
    prompt = f"Here is a social media post: \"{text}\"\n\nA great {tone} comment about it is:"
    response = generator(
        prompt,
        max_length=50,
        num_return_sequences=3
    )
    # Clean the generated text by removing the prompt from the beginning
    return [res['generated_text'][len(prompt):].strip() for res in response]
