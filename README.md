# Personalized Learning Assistant

An LLM based learning assistant that will help students understand and retain materials better.

## Motivation
The primary objective of this project is to create an assisted learning system powered by large language models (LLMs) that simplifies the process of generating study materials. The platform allows users to up- load text or PDF files, which are then processed to generate contextually relevant questions and summaries. This tool aims to enhance the learning experience by providing tailored educational content, fostering better comprehension and engagement.

## Significance
* Reduces the time and effort required to create study materials.
* Enhances accessibility to tailored educational content.


## Project Flow

The chosen methodology is designed to address the challenges of creating personalized study materials efficiently. By employing GEMMA for summarization and LLAMA 3.2 for question generation, the system ensures high-quality outputs tailored to the user’s needs.
1. Data Preprocessing
   
* Load and preprocess the given input using NLP techniques.
* Extract text from uploaded PDFs using pypdf if necessary.
* Tokenize the dataset to prepare inputs for LLMs.

2. Context and QA Pipeline

* Model 1 GEMMA: Summarisation
  
  Input: Pre-processed Text or a PDF file.

  Output: Summary of the input

* Model 2 LLaMA 3.2: Question-Answering Generation
  
  Input: Pre-processed Text or a PDF file.

  Output: Precise answers and questions generated based on context.

3. Evaluation
* Metrics: Use ROGUE score to determine how the model is performing for generating summaries.
* Using human as a judge to see the quality of questions generated.

4. Deployment
* Build a user-friendly interface using Streamlit for interactive input, knowledge retrieval, questionand summary generation.
