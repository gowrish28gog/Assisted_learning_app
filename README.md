# Personalized Learning Assistant

An LLM based learning assistant that will help students understand and retain material better.

## Motivation

This project aims to address the common challenges students face in processing study materials and evaluating their understanding. By integrating multiple large language models (LLMs), it automates the extraction of key information, generates concise summaries, and offers personalized quizzes for self-assessment. This tool is designed to help students learn more efficiently by simplifying complex content and providing targeted practice for better retention and comprehension.

## Project Flow

Model 1 GEMMA: Summarisation

– Input: Pre-processed Text or a PDF file.

– Output: Summary of the input


Model 2 LLaMA 3.2: Question-Answering Generation

– Input: Pre-processed Text or a PDF file.

– Output: Precise answers and questions generated based on context.


## What this branch contains?

As of now, my branch contains:
1. Pre processed file for SQuAD dataset and some EDA
2. Helper functions to run the main application:
   
   a. Hugging Face transformer and,
   
   b. Exa search for web search asked by the user


March 10 2025, Iteration 3 submission:

3. Updated prompts for better question generation.

4. Added level of education and questions are being generated according to it.
   
5. Answer button will only appear once the questions are generated.
   
6. Number of questions to generate was hard coded to 5. Changed it.
   
7. Added a text box for input along with PDF file. Text box will disable if a file is uploaded.
