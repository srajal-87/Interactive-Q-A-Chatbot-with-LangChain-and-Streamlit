# 🤖 Interactive Q&A Chatbot with LangChain and Streamlit

This project is an **Interactive Question & Answer Chatbot** built using **LangChain**, **Ollama models**, and **Streamlit**. The chatbot can handle queries intelligently and offers features like contextual memory and a feedback mechanism to improve the user experience.

---

## 📋 Features
- Uses open-source **Ollama models** for generating intelligent responses.
- Contextual memory to retain the conversation history.
- Adjustable parameters for fine-tuning responses (Temperature, Max Tokens).
- Feedback mechanism to rate the responses.
- Interactive Streamlit UI for a smooth user experience.

---

## 🚀 Getting Started

Follow these steps to clone and set up the repository on your local machine.

### 1️⃣ Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone https://github.com/your-username/interactive-qa-chatbot.git
cd interactive-qa-chatbot
```

### 2️⃣ Set Up a Python Environment
It is recommended to create a Python virtual environment to manage dependencies:
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
Install the required Python dependencies using:
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the project root directory and add the following variables:
```
LANGCHAIN_API_KEY=<Your_LangChain_API_Key>
```
Make sure to replace `<Your_LangChain_API_Key>` with your actual LangChain API key.

### 5️⃣ Run the Streamlit App
Start the Streamlit server by running:
```bash
streamlit run app.py
```

---

## ⚙️ Usage Instructions

1. **Open the App**: Once the Streamlit server is running, open the provided URL (typically [http://localhost:8501](http://localhost:8501)) in your browser.
2. **Select the Model**: Use the sidebar to choose between available Ollama models (e.g., llama3.1, llama3.2).
3. **Adjust Parameters**: Fine-tune the response behavior using the sliders for Temperature and Max Tokens.
4. **Ask Questions**: Type your question in the input box and receive intelligent responses.
5. **Provide Feedback**: Use the feedback mechanism to rate the chatbot's response.

---

## 📦 Project Structure
```
interactive-qa-chatbot/
├── app.py             # Main Streamlit app
├── requirements.txt   # Python dependencies
├── .env               # Environment variables (not included in the repo)
└── README.md          # Documentation
```

---

## 🛠️ Customization
- Modify the chatbot's behavior by editing the prompt in `app.py`.
- Add new features or models by updating the relevant sections of the app.

---

## 🤝 Acknowledgments
- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)
- [Ollama Models](https://ollama.ai/)

