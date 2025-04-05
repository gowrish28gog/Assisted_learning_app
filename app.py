import streamlit as st
from helpers.ollama_helper import generate_response
from helpers.pdf_reader import extract_text_from_pdf
from helpers.exa_search import perform_web_search

# Streamlit UI setup
st.set_page_config(page_title="PDF & Text Q&A with Ollama", layout="centered")

st.title("📄 PDF & Text Q&A with Ollama")
st.write("Upload a PDF **or** enter text manually to generate AI-generated questions and answers!")

# File uploader and text box input
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

# Disable text input if a file is uploaded
text_disabled = uploaded_file is not None

# Text input box (Disabled if file is uploaded)
user_text_input = st.text_area("Or enter text manually:", "",height=200, disabled=text_disabled)

#uploaded_file_disabled = user_text_input is not None

if uploaded_file or user_text_input.strip():
    # Extract text from PDF or use manual input
    extracted_text = "Extracted text from PDF" if uploaded_file else user_text_input


# Dropdown to select education level
level = st.selectbox("Select your education level:", ['High School', 'Bachelors', 'Masters', 'PhD'])

# Dropdown to select question severity
severity = st.selectbox("Select the severity of the questions:", ["Easy", "Medium", "Tough"])

# Number of questions to generate
num_questions = st.number_input("Number of questions to generate:", min_value=1, max_value=20, value=5)

# Determine which prompt file to use
prompt_file = f"prompts/{severity.lower()}_questions.txt"
with open(prompt_file, 'r') as file:
    question_prompt = file.read()

# Function to get text from either PDF or text box
def get_input_text():
    if uploaded_file is not None:
        with st.spinner("Extracting text from PDF..."):
            return extract_text_from_pdf(uploaded_file)
    elif user_text_input.strip():
        return user_text_input.strip()
    else:
        return None

# Generate Questions
if st.button("Generate Questions"):
    extracted_text = get_input_text()
    
    if extracted_text is None:
        st.error("Please upload a PDF or enter text manually.")
    else:
        with st.spinner("Generating questions..."):
            formatted_prompt = question_prompt.format(num_questions=num_questions, level=level)
            response = generate_response(formatted_prompt, extracted_text)
            st.session_state['questions'] = response

            st.subheader("Generated Questions:")
            st.write(response)

# Answer Generation Section
answers_file = "prompts/answers.txt"
with open(answers_file, 'r') as file:
    answer_prompt = file.read()

if 'questions' in st.session_state and st.session_state['questions']:
    if st.button("Generate Answers"):
        extracted_text = get_input_text()
        st.subheader("Generated Answers:")

        questions_list = [q.strip() for q in st.session_state['questions'].split("\n") if q.strip()]

        for idx, question in enumerate(questions_list):
            with st.spinner(f"Generating answer for question {idx + 1}..."):
                prompt_for_question = f"{answer_prompt}\n{question}"
                try:
                    answer = generate_response(prompt_for_question, extracted_text)
                except Exception as e:
                    answer = f"Error generating answer: {str(e)}"

            st.write(f"**Q: {question}**")
            st.write(f"**Answer: {answer}**")
            st.write("")  # Spacing for readability

# Summary Generation Section
summary_prompt_file = "prompts/summary.txt"
with open(summary_prompt_file, 'r') as file:
    summary_prompt = file.read()

if st.button("Generate Summary"):
    extracted_text = get_input_text()
    
    if extracted_text is None:
        st.error("Please upload a PDF or enter text manually.")
    else:
        with st.spinner("Generating summary..."):
            summary = generate_response(summary_prompt, extracted_text)
            st.subheader("Document Summary:")
            st.write(summary)

# Web Search Section
st.subheader("Need assistance with a topic?")
user_topic = st.text_input("Enter a topic or question you'd like help with:")

if user_topic:
    search_option = st.selectbox("Where would you like to search?", ["Articles", "YouTube"])

    if st.button("Generate Web Search"):
        try:
            prompt = f"{search_option} about {user_topic}"
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
