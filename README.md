# AI Personalized Learning Assistant

An LLM-based learning assistant that helps students understand and retain materials better by generating contextually relevant questions and summaries.

## Overview

This project combines various AI technologies to create an assisted learning system powered by large language models (LLMs) that simplifies the process of generating study materials. The platform allows users to upload text or PDF files, which are then processed to generate contextually relevant questions and summaries to enhance the learning experience.

## Motivation

The primary objective of this project is to create an assisted learning system powered by large language models (LLMs) that simplifies the process of generating study materials. The platform allows users to upload text or PDF files, which are then processed to generate contextually relevant questions and summaries. This tool aims to enhance the learning experience by providing tailored educational content, fostering better comprehension and engagement.

## Significance

* Reduces the time and effort required to create study materials
* Enhances accessibility to tailored educational content
* Provides personalized learning experiences
* Increases student engagement and comprehension

## Project Flow

The chosen methodology is designed to address the challenges of creating personalized study materials efficiently. By employing GEMMA for summarization and LLAMA 3.2 for question generation, the system ensures high-quality outputs tailored to the user's needs.

1. **Data Preprocessing**
   * Load and preprocess the given input using NLP techniques
   * Extract text from uploaded PDFs using pypdf if necessary
   * Tokenize the dataset to prepare inputs for LLMs

2. **Context and QA Pipeline**
   * **Model 1 (GEMMA)**: Summarization
     * Input: Pre-processed Text or a PDF file
     * Output: Summary of the input
   * **Model 2 (LLaMA 3.2)**: Question-Answering Generation
     * Input: Pre-processed Text or a PDF file
     * Output: Precise answers and questions generated based on context

3. **Evaluation**
   * Metrics: Use ROUGE score to determine how the model is performing for generating summaries
   * Using human as a judge to see the quality of questions generated

4. **Deployment**
   * Build a user-friendly interface using Streamlit for interactive input, knowledge retrieval, question and summary generation

## Prerequisites

Before you begin, ensure you have:
- Python 3.8 or higher installed
- Git installed
- Accounts with the following services:
  - [Exa](https://exa.ai/) for advanced web search capabilities
  - [ConvertAPI](https://www.convertapi.com/) for document conversion
  - [Eleven Labs](https://elevenlabs.io/) for text-to-speech
  - [Ollama](https://ollama.ai/) for running local AI models

## Installation

### 1. Fork or Clone the Repository

```bash
git clone https://github.com/yourusername/personalized-learning-assistant.git
cd personalized-learning-assistant
```

Alternatively, fork the repository and clone your fork.

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Up Local Models with Ollama

Ensure you have the following models downloaded:
- LLaMA 3.2
- Gemma

To download these models with Ollama:

```bash
ollama pull llama3.2
ollama pull gemma
```

### 4. Configure API Keys

Create a `.env` file in the project root directory with the following content:

```
EXA_API_KEY=your_exa_api_key
CONVERTAPI_SECRET=your_convertapi_secret
ELEVEN_LABS_API_KEY=your_eleven_labs_api_key
```

Replace the placeholder values with your actual API keys.

## Usage

Start the application with:

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501` by default.

## Features

- **Document Processing**: Upload and analyze educational materials in PDF or text format
- **Intelligent Summarization**: Generate concise summaries using GEMMA model
- **Question Generation**: Create relevant practice questions using LLaMA 3.2
- **Voice Interaction**: Engage with content through natural speech using Eleven Labs
- **Knowledge Retrieval**: Access up-to-date information from the web via Exa
- **Local AI Processing**: Utilize powerful LLMs on your machine for privacy and performance

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Insert your license information here]

## Acknowledgements

- LLaMA 3.2 and Gemma model developers
- Eleven Labs for voice synthesis technology
- Exa for knowledge retrieval capabilities
- ConvertAPI for document processing
- Streamlit for the web application framework
