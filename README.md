# AI Personalized Learning Assistant

An intelligent learning companion powered by large language models (LLMs) that helps students absorb and retain material by generating summaries and context-aware questions.

## 📘 Overview

This project brings together cutting-edge AI technologies to build a personalized learning system. Users can upload PDFs or text documents, and the platform will automatically generate concise summaries and context-relevant questions—turning study materials into interactive learning experiences.

## 🎯 Motivation

Creating high-quality study materials takes time and effort. This assistant aims to automate that process using LLMs, helping students understand content more deeply while saving time. By tailoring educational outputs to each user, the platform encourages better comprehension, retention, and engagement.

## 🌟 Key Benefits

- Automatically generates learning content from existing documents  
- Enhances access to personalized study material  
- Boosts engagement through voice and interactive features  
- Promotes better understanding with tailored summaries and questions  

## 🔄 Project Workflow

The system uses a structured pipeline to deliver accurate summaries and questions, utilizing:

- **GEMMA** for summarization  
- **LLaMA 3.2** for generating context-based questions  

### Step-by-Step Process

1. **Data Preprocessing**
   - Extract text from PDFs using `pypdf`
   - Apply NLP techniques to clean and tokenize text

2. **Model Pipeline**
   - **Summarization (GEMMA)**: Produces concise summaries
   - **Question Generation (LLaMA 3.2)**: Creates relevant questions and answers based on context

3. **Evaluation**
   - **Summaries**: Evaluated using ROUGE score
   - **Questions**: Assessed through human judgment

4. **Deployment**
   - Streamlit-based user interface for uploading documents and viewing output

## 🛠️ Prerequisites

Make sure the following are set up before you begin:

- Python 3.8+
- Git
- API access for:
  - [Exa](https://exa.ai/) – for web-based knowledge retrieval
  - [ConvertAPI](https://www.convertapi.com/) – for document conversion
  - [Eleven Labs](https://elevenlabs.io/) – for text-to-speech
  - [Ollama](https://ollama.ai/) – for running local models

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/gowrish28gog/Assisted_learning_app.git
cd personalized-learning-assistant
```

### 2. Activate the Virtual Environment

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Or manually install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Load LLMs with Ollama

Download the required models:

```bash
ollama pull llama3.2
ollama pull gemma2:2b
```

### 4. Set API Keys

Edit the `.env` file with your credentials:

```
EXA_API_KEY=your_exa_api_key
CONVERTAPI_SECRET=your_convertapi_secret
ELEVEN_LABS_API_KEY=your_eleven_labs_api_key
```

## 🚀 Running the App

Start the Streamlit application:

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

## ✨ Features

- 📄 **PDF/Text Upload**: Process all of your documents (.docx, .pptx, .pdf) with ease
- 🌍 **Web Data Extraction**: Extract and process data directly from any web URL  
- ✍️ **Smart Summarization**: Use GEMMA to condense content  
- ❓ **Question Generation**: Get context-based Q&A from LLaMA 3.2  
- 🗣️ **Voice Interaction**: Learn via natural speech (Eleven Labs)  
- 🌐 **Web Knowledge Integration**: Enrich learning with Exa  
- 🔐 **Local AI Execution**: Keeps data private and fast  

## 🤝 Contributing

We welcome contributions of all kinds! Feel free to open issues or submit pull requests.

## 🙏 Acknowledgements

- Meta (LLaMA 3.2) and Google (Gemma) for the models  
- Eleven Labs for voice synthesis  
- Exa for real-time search capabilities  
- ConvertAPI for PDF handling  
- Streamlit for building the interactive interface
