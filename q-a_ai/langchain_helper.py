from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv('GOOGLE_API_KEY')

from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key, temperature=0.7)

# Print the instance to verify
print(llm)

# Initialize instructor embeddings using the Hugging Face model
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
vectordb_file_path = "faiss_index"

def create_vector_db():
    # Load data from FAQ sheet
    file_path = './codebasics_faqs.csv'
    loader = CSVLoader(file_path=file_path, source_column="prompt", encoding="latin1")
    data = loader.load()

    # Create a FAISS instance for vector database from 'data'
    vectordb = FAISS.from_documents(documents=data, embedding=instructor_embeddings)

    # Save vector database locally
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain

if __name__ == '__main__':
    chain = get_qa_chain()

    print(chain({"query": "Do you guys provide internship and also do you offer EMI payments?"}))