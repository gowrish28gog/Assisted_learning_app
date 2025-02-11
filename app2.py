import streamlit as st
from helpers.ollama_helper import generate_response
from helpers.pdf_reader import extract_text_from_pdf
from helpers.exa_search import perform_web_search

# Streamlit UI setup
st.set_page_config(page_title="PDF Q&A with Ollama", layout="centered")

# Sidebar navigation
page = st.radio("Select a page:", ["Questions", "Answers", "Web Search"])

# File uploader and severity dropdown
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
severity = st.selectbox("Select the severity of the questions:", ["Easy", "Medium", "Tough"])

if severity == "Easy":
    prompt_file = "prompts/easy_questions.txt"
elif severity == "Medium":
    prompt_file = "prompts/medium_questions.txt"
else:
    prompt_file = "prompts/tough_questions.txt"

# Read the selected prompt from the file
with open(prompt_file, 'r') as file:
    question_prompt = file.read()

if page == "Questions":
    # Question generation page
    st.title("📄 PDF Q&A with Ollama - Questions")
    st.write("Upload a PDF, select the question severity, and generate AI-generated questions!")

    if uploaded_file:
        with st.spinner("Extracting text from PDF..."):
            extracted_text = extract_text_from_pdf(uploaded_file)
        
        if extracted_text:
            num_questions = 5
            formatted_prompt = question_prompt.format(num_questions=num_questions)

            if st.button("Generate Questions"):
                with st.spinner("Generating questions..."):
                    response = generate_response(formatted_prompt, extracted_text)
                    st.session_state['questions'] = response
                    st.subheader("Generated Questions:")
                    st.write(response)
        else:
            st.error("No text could be extracted from the PDF.")
    else:
        st.error("Please upload a PDF file.")

elif page == "Answers":
    # Answer generation page
    st.title("📄 PDF Q&A with Ollama - Answers")

    if 'questions' in st.session_state and st.session_state['questions']:
        # Display generated questions and answer them
        answers_file = "prompts/answers.txt"
        with open(answers_file, 'r') as file:
            answer_prompt = file.read()

        if uploaded_file:
            extracted_text = extract_text_from_pdf(uploaded_file)

            st.subheader("Generated Answers:")
            questions_list = st.session_state['questions'].split("\n")
            
            for idx, question in enumerate(questions_list):
                if question.strip():
                    with st.spinner(f"Generating answer for question {idx + 1}..."):
                        prompt_for_question = f"{answer_prompt}\n{question}"
                        try:
                            answer = generate_response(prompt_for_question, extracted_text)
                            st.write(f"**Q{idx + 1}:** {question}")
                            st.write(f"**A{idx + 1}:** {answer}")
                            st.write("\n")
                        except Exception as e:
                            st.write(f"Error generating answer: {str(e)}")
        else:
            st.error("Please upload a PDF file.")
    else:
        st.write("No questions have been generated yet. Please go to the 'Questions' page and generate questions first.")

elif page == "Web Search":
    # Web search page
    st.title("📄 PDF Q&A with Ollama - Web Search")
    st.subheader("Need assistance with a topic?")
    user_topic = st.text_input("Enter a topic or question you'd like help with:")

    if user_topic:
        search_option = st.selectbox("Where would you like to search?", ["Articles", "YouTube"])

        if st.button("Generate Web Search"):
            try:
                if search_option == "Articles":
                    prompt = f"Articles about {user_topic}"
                elif search_option == "YouTube":
                    prompt = f"YouTube links about {user_topic}"

                parsed_results = perform_web_search(prompt)
                
                if parsed_results:
                    st.subheader(f"Results for {search_option} on '{user_topic}':")
                    for result in parsed_results:
                        st.write(f"**Title**: {result['title']}")
                        st.write(f"**URL**: [{result['url']}]({result['url']})")
                        st.write(f"**Score**: {result['score']:.2f}")
                        st.write(f"**Published Date**: {result['published_date']}")
                        st.write("---")
                else:
                    st.write(f"No results found for {user_topic} on {search_option}.")
            except Exception as e:
                st.error(f"An error occurred while performing the web search: {str(e)}")
