from exa_py import Exa
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables from .env file


def perform_web_search(prompt: str):
    load_dotenv()

    # Get the API key from environment variables
    api_key = os.getenv("EXA_API_KEY")

    # Initialize Exa with the loaded API key
    exa = Exa(api_key=api_key)
    result = exa.search(
        prompt,
        type="neural",
        use_autoprompt=True
    )
    
    # Inspect the structure of the result object
    st.write(result)  # This will output the raw result so you can inspect it
    
    try:
        # Access the 'results' list directly from the 'result' object
        results = result.results
        
        # Parse the required details from each result
        parsed_results = [{
            'title': r.title,           # Access the 'title' from Result object
            'url': r.url,               # Access the 'url' from Result object
            'score': r.score if hasattr(r, 'score') else 'No Score',  # Check if 'score' exists
            'published_date': r.published_date if hasattr(r, 'published_date') else 'No Date'  # Check for 'published_date'
        } for r in results]
        
        return parsed_results
    
    except Exception as e:
        st.error(f"Error parsing search results: {str(e)}")
        return []