import streamlit as st
from helpers.ollama_helper import generate_response, generate_summary
from helpers.pdf_reader import extract_text_from_pdf
from helpers.exa_search import perform_web_search



# Streamlit UI setup
st.set_page_config(page_title="PDF Q&A with Ollama", layout="centered")

st.title("📄 PDF Q&A with Ollama")
st.write("Upload a PDF, select the question severity, and generate AI-generated questions and answers!")

# File uploader
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

# Get the available Ollama models 


# Dropdown to select question severity
severity = st.selectbox("Select the severity of the questions:", ["Easy", "Medium", "Tough"])

num_questions = st.number_input("Number of questions to generate:", min_value=1, max_value=20, value=5)

# Prompt input for generating questions
if severity == "Easy":
    prompt_file = "prompts/easy_questions.txt"
elif severity == "Medium":
    prompt_file = "prompts/medium_questions.txt"
else:
    prompt_file = "prompts/tough_questions.txt"

# Read the selected prompt from the file
with open(prompt_file, 'r') as file:
    question_prompt = file.read()

# Submit button to generate questions
if st.button("Generate Questions"):
    if uploaded_file is None:
        st.error("Please upload a PDF file.")
    else:
        with st.spinner("Extracting text from PDF..."):
            extracted_text = extract_text_from_pdf(uploaded_file)
        
        if not extracted_text:
            st.error("No text could be extracted from the PDF.")
        else:
            # Generate the questions based on the prompt
            with st.spinner("Generating questions..."):
                # Modify the prompt to include the number of questions to generate
                num_questions = 5  # Adjust this as needed
                formatted_prompt = question_prompt.format(num_questions=num_questions)

                # Store the generated questions in session state
                response = generate_response(formatted_prompt, extracted_text)
                st.session_state['questions'] = response
                
                st.subheader("Generated Questions:")
                st.write(response)


summary_prompt_file = "prompts/summary.txt"
with open(summary_prompt_file, 'r') as file:
    summary_prompt = file.read()

if st.button("Generate Summary"):
    if uploaded_file is None:
        st.error("Please upload a PDF file.")
    else:
        with st.spinner("Generating summary..."):
            extracted_text = extract_text_from_pdf(uploaded_file)
            if not extracted_text:
                st.error("No text could be extracted from the PDF.")
            else:
                summary = generate_summary(summary_prompt, extracted_text)
                st.subheader("Document Summary:")
                st.write(summary)





answers_file = "prompts/answers.txt"
with open(answers_file, 'r') as file:
    answer_prompt = file.read()

# Section to generate answers for the generated questions
if st.button("Generate Answers"):
    if 'questions' in st.session_state and st.session_state['questions']:
        st.subheader("Generated Answers:")
        extracted_text = extract_text_from_pdf(uploaded_file)
        # Loop through the generated questions and get answers for each one
        questions_list = st.session_state['questions'].split("\n")
        
        for idx, question in enumerate(questions_list):
            if question.strip():  # Ensure the question is not empty
                with st.spinner(f"Generating answer for question {idx + 1}..."):
                    # Generate an answer for the question
                    prompt_for_question = f"{answer_prompt}\n{question}"
                    try:
                        # Generate an answer for the question
                        answer = generate_response(prompt_for_question, extracted_text)
                    except Exception as e:
                        answer = f"Error generating answer: {str(e)}"
                
                # Display the answer
                st.write(f"**Q{idx + 1}:** {question}")
                st.write(f"**A{idx + 1}:** {answer}")
                st.write("\n")



# Streamlit interface
st.subheader("Need assistance with a topic?")
user_topic = st.text_input("Enter a topic or question you'd like help with:")

# Perform web search for articles or YouTube links
if user_topic:
    search_option = st.selectbox("Where would you like to search?", ["Articles", "YouTube"])

    # Button to perform web search
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