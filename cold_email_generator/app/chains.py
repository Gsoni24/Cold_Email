import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        # if not os.environ.get("GROQ_API_KEY"):
        #     os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

        # self.llm = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise EnvironmentError("GROQ_API_KEY is not set.")

        self.llm = init_chat_model(
            model="llama-3.3-70b-versatile",
            model_provider="groq",
            api_key=api_key
        )

    def extract_jobs(self, cleared_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCITON:
            The scraped text is from the careers's page of a website.
            Your job  is to extract the job posting and return them in JSON format containing \
            following keys: 'role', 'experience', 'skills' and 'description'.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )

        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleared_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Content is loo big . Unable to extract job posting")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Gaurav Soni a recent graduate with a strong passion for Artificial Intelligence, Machine Learning, and Data Science. /
            You have hands-on experience through internships at Unified Mentor and Byte Uprise, where you worked on projects such as /
            COVID-19 data analysis, customer satisfaction prediction, Netflix data analysis, and movie prediction systems using Python, Pandas, NumPy, Scikit-learn, and visualization tools. /
            You have also developed a movie recommendation system website with Streamlit. /
            Your technical skills include Python, SQL, ML/DL, Computer Vision, and web technologies, supported by certifications in Generative AI (AWS), LLM Applications with Prompt Engineering (NVIDIA), and Emerging Technologies (SAP & Edunet Foundation). \
            With leadership experience in team projects and presentations, you aim to start your career as a Data Scientist or AI Engineer, /
            focusing on building impactful AI solutions, particularly in the field of Generative AI.
            Your job is to write a cold email to the hiring manager/team/person regarding the job mentioned above describing your capability to /
            in fulfiling their needs.
            Remember you are Gaurav Soni
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE)
            """
        )

        chain_email = prompt_email | self.llm
        res_email = chain_email.invoke({'job_description': str(job)})
        return res_email.content

