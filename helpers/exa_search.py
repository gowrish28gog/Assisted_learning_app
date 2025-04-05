from exa_py import Exa
from dotenv import load_dotenv
import os
import streamlit as st


def perform_web_search(prompt: str):
    """
    
    Performs a web search using the Exa API based on the provided prompt.
    This function initializes the Exa API client with the API key
    and performs a search using the specified prompt.
    It returns a list of parsed results containing the title, URL, score, and published date.

    Parameters:
        prompt (str): The search query or prompt to search for.
    Returns:
        List[dict]: A list of dictionaries containing parsed search results.

    """

    # Load environment variables from .env file
    load_dotenv()

    # Get the API key from environment variables
    api_key = os.getenv("EXA_API_KEY")

    # Initialize Exa with the loaded API key
    exa = Exa(api_key=api_key)

    # Perform the search using Exa API
    # Use the prompt to search for relevant articles
    # and set the type to 'neural' for neural search
    # Set use_autoprompt to True to enable autoprompting
    # Set the max_results to 5 to limit the number of results
    result = exa.search(
        prompt,
        type="neural",
        use_autoprompt=True
    )
    
    # Inspect the structure of the result object
    st.write(result)  
    # This will output the raw result so you can inspect it
    
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
        
        return parsed_results  # List of dictionaries with parsed results
    
    # Handle the case where 'results' is not present or is empty
    except Exception as e:
        st.error(f"Error parsing search results: {str(e)}")
        return []
    

## Function to extract text from a list of URLs using the Exa API
# This function uses the Exa API to extract text content from the provided URLs.
# It returns the extracted text content as a string.
# The function requires the Exa API key to be set in the environment variables.
def extract_text_from_exa(urls):
    """
    Extracts full page text content from a list of URLs using the Exa API.

    Parameters:
        api_key (str): Your Exa API key.
        urls (list): List of URLs to extract text from.

    Returns:
        List[str]: A list of extracted text content from each URL and its subpages.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get the API key from environment variables
    api_key = os.getenv("EXA_API_KEY")

    # Initialize Exa with the loaded API key
    exa = Exa(api_key=api_key)
    
    # Extract text content from the provided URLs
    response = exa.get_contents(urls,
    text = {
        "max_characters": 20000,
        "include_html_tags": False
        }
    )
    
    # Inspect the structure of the response objec
    if response.status_code == 200:
        st.write("Response received successfully.")
    else:
        st.error(f"Failed to fetch content. Status code: {response.status_code}")
   
    # Check if the response contains 'text' and 'subpages' keys
    return str(response) 



