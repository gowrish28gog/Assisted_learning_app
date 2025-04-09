# Personalized Learning Assistant

An LLM based learning assistant that will help students understand and retain materials better.

## Motivation

This project aims to address the common challenges students face in processing study materials and evaluating their understanding. By integrating multiple large language models (LLMs), it automates the extraction of key information, generates concise summaries, and offers personalized quizzes for self-assessment. This tool is designed to help students learn more efficiently by simplifying complex content and providing targeted practice for better retention and comprehension.

## Project Flow

1. Knowledge Retrieval (Model 1)

* Input: Text notes or PDF files
* Process: The system processes the provided study materials (notes or PDFs) and extracts key information using advanced language models.
* Output: A detailed summary of the study material, highlighting the most relevant points for better understanding and quick review.

2. Quiz Generation (Model 2)

* Input: Text notes or PDF files

* Process: Based on the content of the study materials, the system generates context-specific questions based on the desired level (easy, medium or tough). This helps students self-assess their comprehension and reinforce their learning. 
* Output: A set of personalized questions designed to test the student's understanding of the material. The students can then get the answers for those questions as well if they desire. We will add more features in the coming week.

## Dataset Information: SQuAD v1.1

* Dataset Name: SQuAD v1.1 (Stanford Question Answering Dataset)
* Source: SQuAD GitHub Repository
* Format: JSON
* Structure:
  * Context: A passage or paragraph of text from which the questions are derived. Typically sourced from Wikipedia articles.
  * Questions: A set of questions designed to test the reader's understanding of the context. These questions are paired with answers directly extracted from the context.
  * Answers: The answer(s) to each corresponding question, typically a span of text extracted directly from the context.

### Dataset Overview

SQuAD v1.1 is a widely used benchmark dataset for evaluating machine learning models in the task of machine reading comprehension. It consists of over 100,000 question-answer pairs based on a diverse set of articles from the English Wikipedia. The dataset is designed to help train models in the task of extractive question answering, where the goal is to extract a precise span of text from a given context in response to a question.

## Work in This Branch

### Summarization Task

* Model: Google Gemma 2.0 2B params

* Prompt: Prompt for generating concise summary from the given text

### Evaluation

* Questions: **BERTScore** that matches words in candidate and reference sentences by cosine similarity. It leverages the pre-trained contextual embeddings from BERT models and computes precision, recall, and F1 measure

* Summary: **ROUGE_score** is used for evaluating automatic summarization and machine translation software in natural language processing. Here we have utilized unigram, bigram, and lsongest common subsequence based scoring.

### Text to speech

Integrated the Elevenlabs API to convert the generated summary to audio. The audio is generated in a short time (few seconds) and gives quality output.