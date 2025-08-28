# Project Action Plan: Automatic Social Media Comment Generator

## Project Status

We have a working proof-of-concept with a Streamlit interface. The core comment generation logic is functional and has been improved by upgrading the model to `gpt2-medium` and refining the prompt engineering. The project is ready to be restructured into a more robust architecture featuring a separate backend API and frontend application.

## Current Position

We are at the **architectural refactoring** stage. The goal is to separate the application into a backend API (for portfolio purposes) and a frontend UI that consumes it.

## Next Steps

1.  **Architectural Refactoring: API and Frontend Separation**
    *   **Goal:** Create a dedicated FastAPI backend to serve the comment generation model, and have the Streamlit UI consume this new API.
    *   **Update Dependencies:** Add `fastapi`, `uvicorn`, and `requests` to `requirements.txt`.
    *   **Create API Backend:** Build a new `src/api.py` file using FastAPI to expose a `/generate-comment` endpoint.
    *   **Modify Frontend:** Update `src/main.py` to make HTTP requests to the new local API instead of calling the Python function directly.
    *   **Testing:** Run both the API server and the Streamlit app simultaneously to test the end-to-end functionality.

2.  **Refinement:**
    *   Refine the UI/UX based on the testing feedback.
    *   Continue to improve the prompt engineering in `src/generator.py` for better results.

3.  **Deployment to Hugging Face Spaces:**
    *   Create a new Space on Hugging Face.
    *   Configure the Space to run both the FastAPI backend and the Streamlit frontend.
    *   Deploy the application to make it publicly accessible.

4.  **Final Documentation:**
    *   Update the `README.md` with a link to the live application and instructions on how to use the API.
    *   Add any additional documentation or notes.
