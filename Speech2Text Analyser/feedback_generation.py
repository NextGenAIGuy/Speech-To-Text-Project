import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

class ConversationReviewer:
    def __init__(self):
        load_dotenv()
        groq_api_key = os.getenv("groq_api_key")
        self.llm = ChatGroq(temperature=0.5, groq_api_key=groq_api_key, model_name="llama3-8b-8192")
        self.prompt_template = """
        You are Conversation reviewer. Your Job is to review the conversation based on the review. Generate the Feedback of all unique speakers.
        The conversation data consists of sentiment as well. So you need to detect the topic of discussion and feedback for each speaker.
        conversation: {conversation}
        """
        self.prompt = PromptTemplate(
            template=self.prompt_template,
            input_variables=["conversation"]
        )
        self.output_chain = self.prompt | self.llm | StrOutputParser()

    def review_conversation(self, conversation):
        search_output = self.output_chain.invoke({"conversation": conversation})
        return search_output
