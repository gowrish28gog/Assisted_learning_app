import requests

def generate_grok_api_response(prompt: str, context: str, model: str = "grok-2-vision-1212", grok_api_url: str = "https://api.grok.ai/v1/generate") -> str:
    """
    Sends the prompt and context to the Grok API and retrieves the response.

    :param prompt: The input prompt/question.
    :param context: The context/document that provides information for the model.
    :param model: The model name (default: "grok-2-vision-1212").
    :param grok_api_url: The API endpoint URL for the Grok model.
    :return: The generated response from the model.
    """
    # Construct the request payload
    payload = {
        "model": model,
        "input": {
            "context": context,
            "prompt": prompt
        }
    }

    headers = {
        "Authorization": "Bearer YOUR_API_KEY",  
        "Content-Type": "application/json"
    }

    try:
        # Send the request to the Grok API
        response = requests.post(grok_api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response and extract the output
        response_data = response.json()

        # Return the model's generated response
        return response_data.get('output', 'No output returned from the model.')
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"
