
# 📧 Cold Email Generator

This project is a Streamlit web app that helps generate personalized cold emails to hiring managers by scraping job postings from company career pages.
It extracts job details (role, experience, skills, description) using LLMs (Groq LLaMA 3.3-70B) and automatically crafts tailored cold emails highlighting your skills, experience, and fit for the role



## 🚀 Features



- 🌐 Enter any career/job page URL.

- 🧹 Cleans raw text (removes HTML, URLs, special characters).

- 🤖 Extracts job postings using Groq LLM.

- ✉️ Generates cold emails tailored to each job.

- 🎨 Simple Streamlit interface for ease of use.


## 📂 Project Structure
```bash
.
├── chains.py   # LLM chains: job extraction & email generation
├── main.py     # Streamlit app entry point
├── utils.py    # Helper functions (text cleaning)
└── README.md   # Project documentation
```
## Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/your-username/cold-email-generator.git
cd cold-email-generator
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
_(Make sure to include a requirements.txt file with streamlit, langchain, langchain-community, python-dotenv, and other dependencies.)_

4. Set up environment variables
Create a .env file in the root directory and add your Groq API key:
```bash
GROQ_API_KEY=your_api_key_here
```

## ▶️ Running App
Run the Streamlit app with:
```bash
streamlit run main.py
```
Then open the provided localhost link in your browser.
## 🧩 Example Workflow
**1.** Enter a company’s careers page URL.

**2.** The app scrapes job postings.

**3.** LLM extracts structured job info.

**4.** A tailored cold email is generated for each posting.
## Tech Stack

- Python 3.9+

- Streamlit (UI)

- LangChain (LLM framework)

- Groq API (LLaMA 3.3-70B model)

- Regex (text cleaning)

## Authors

Gaurav Soni
- 💻 Aspiring Data Scientist | AI Engineer
- 📧 [Gmail](gauravsoni242001@gmail.com)
- 🔗 [LinkedIn](www.linkedin.com/in/gaurav-soni-75488a311)


