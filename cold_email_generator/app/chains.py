import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("GROQ_API_KEY is missing.")
        
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

    # Change the INSTRUCTION prompt according to your personal details.
    def write_mail(self, job):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            IMPORTANT : Enter prompt describing your information about yourself what is your job role and the industry you are targeting.
            
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE)
            """
        )

        chain_email = prompt_email | self.llm
        res_email = chain_email.invoke({'job_description': str(job)})
        return res_email.content




