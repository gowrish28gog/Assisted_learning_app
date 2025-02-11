import ollama

def generate_response(prompt: str, document: str, model: str = "llama3.2") -> str:
    """
    Generates a response from an Ollama model given a prompt and document.

    :param prompt: The input prompt/question.
    :param document: The document text to provide context.
    :param model: The name of the Ollama model to use (default: "mistral").
    :return: The generated response from the model.
    """
    full_prompt = f"Document: {document}\n\nPrompt: {prompt}"
    
    response = ollama.chat(model=model, messages=[{"role": "user", "content": full_prompt}])
    
    return response['message']['content']

# Example Usage
if __name__ == "__main__":
    doc_text = "Ollama is a local LLM runner that enables offline AI processing."
    user_prompt = "What is Ollama?"
    
    result = generate_response(user_prompt, doc_text)
    print(result)
