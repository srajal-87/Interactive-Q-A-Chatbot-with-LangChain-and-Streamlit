import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Interactive Q&A Chatbot"

# Define prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("user", "Question: {question}")
    ]
)

def get_response(question, llm, temperature, max_tokens):
    """Fetch response from the selected LLM model."""
    llm_model = Ollama(model=llm)
    output_parser = StrOutputParser()
    chain = prompt | llm_model | output_parser
    response = chain.invoke({"question": question})
    return response

# Streamlit App Title
st.set_page_config(
    page_title="Interactive Q&A Chatbot",
    layout="centered"
)
st.title("Interactive Question & Answer Chatbot")

# Sidebar Configuration
st.sidebar.header("Model & Parameters")
llm = st.sidebar.selectbox(
    "Select an Open Source Model", ["llama3.1", "llama3.2"], index=0
)
temperature = st.sidebar.slider(
    "Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1,
    help="Controls the randomness of the model's responses."
)
max_tokens = st.sidebar.slider(
    "Max Tokens", min_value=50, max_value=300, value=150, step=10,
    help="Defines the maximum number of tokens for the response."
)

# Main Interface
st.write("Type your question below and receive intelligent responses instantly!")

# Maintain conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# User Input
user_input = st.text_area(
    "You:", placeholder="Type your question here...",
    height=100,  # Adjusted to dynamically display longer input text
    max_chars=1000  # Optional: Limit the maximum length of input text
)

if user_input:
    try:
        with st.spinner("Generating response..."):
            response = get_response(user_input, llm, temperature, max_tokens)
        st.session_state.history.append({"user": user_input, "bot": response})

        # Display conversation history
        st.markdown("### 🌐 Chat History")
        for entry in st.session_state.history:
            st.write(f"**You:** {entry['user']}")
            st.write(f"**Bot:** {entry['bot']}")

        # Feedback Mechanism
        feedback = st.radio("Was this response helpful?", ["👍 Yes", "👎 No"], key=f"feedback_{len(st.session_state.history)}")
        if feedback:
            st.write("Thank you for your feedback!")

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Awaiting your question! Please type in the input box above.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown(
    "Developed with ❤️ using [LangChain](https://www.langchain.com/) and [Streamlit](https://streamlit.io/)"
)
