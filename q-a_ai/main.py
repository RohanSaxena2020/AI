from dotenv import load_dotenv
import os
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
import langchain.llms as llms
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_community.llms import GooglePalm

# Load the .env file
load_dotenv()

# Get the API key
api_key = os.getenv('GOOGLE_API_KEY')

# Use the internal function to import GooglePalm
GooglePalm = llms._import_google_palm()

# Initialize the GooglePalm instance with the API key
llm = GooglePalm(google_api_key=api_key, temperature=0.7)

# Initialize instructor embeddings using the Hugging Face model
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
e = instructor_embeddings.embed_query("What is your refund policy?")

vectordb_file_path = 'faiss_index'

def create_vector_db():
    # Load data from FAQ sheet
    file_path = './codebasics_faqs.csv'
    loader = CSVLoader(file_path=file_path, source_column="prompt", encoding="latin1")
    data = loader.load()

    # Create a FAISS instance for vector database from 'data'
    vectordb = FAISS.from_documents(documents=data,
                                    embedding=instructor_embeddings)

    # Save vector database locally
    vectordb.save_local(vectordb_file_path)

if __name__ == '__main__':
    create_vector_db()

# # Create a retriever for querying the vector database
# retriever = vectordb.as_retriever(score_threshold = 0.7)