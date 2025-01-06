from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")

# Step 1: Load Documents (PDF and Web)
def scrap_web(source):
    """
    This function loads documents from a given URL.
    If the URL is invalid, an error is raised.
    """
    try:
        if not source:
            raise ValueError("The URL seems invalid. Please check and try again.")
        loader = WebBaseLoader(source)
        return loader.load()
    except Exception as e:
        raise Exception(f"Error while loading documents: {str(e)}")

# Step 2: Process Documents with RecursiveCharacterTextSplitter
def process_documents(documents):
    """
    Split large documents into smaller chunks for easier processing.
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  # Maximum size of each chunk
            chunk_overlap=200,  # Overlap between chunks for continuity
            separators=["\n\n", "\n", ".", " "]  # Different separators to handle content
        )
        return text_splitter.split_documents(documents)
    except Exception as e:
        raise Exception(f"Error while processing documents: {str(e)}")

# Step 3: Create FAISS Retriever with Hugging Face Embeddings
def create_faiss_retriever(docs):
    """
    Create a FAISS retriever using Hugging Face embeddings.
    """
    try:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        return FAISS.from_documents(docs, embeddings)
    except Exception as e:
        raise Exception(f"Error while creating FAISS retriever: {str(e)}")

# Step 4: Setup LLM with Hugging Face Hub
def setup_llm(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", temperature=0.6, top_k=30):
    """
    Setup the Hugging Face LLM with appropriate configurations.
    """
    try:
        return HuggingFaceHub(
            repo_id=repo_id,
            huggingfacehub_api_token=api_key,
            model_kwargs={"temperature": temperature, "top_k": top_k}
        )
    except Exception as e:
        raise Exception(f"Error while setting up the LLM: {str(e)}")

# Step 5: Create RetrievalQA Chain
def create_retrieval_qa_chain(faiss_index, llm):
    """
    Combine the retriever and LLM into a RetrievalQA chain.
    """
    try:
        retriever = faiss_index.as_retriever()

        # Prompt template for the question
        template = """
        Answer the following question based on the provided context. If the answer is not in the context, say "I don't know."

        Context: {context}
        Question: {question}
        Answer:
        """
        prompt = PromptTemplate(template=template, input_variables=["context", "question"])

        # Define the RAG pipeline
        rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        return rag_chain
    except Exception as e:
        raise Exception(f"Error while creating the RetrievalQA chain: {str(e)}")

def ask_chat(base_url: str, query: str):
    """
    This function handles the end-to-end process:
    1. Load the documents from the web.
    2. Process the documents into smaller chunks.
    3. Create a FAISS retriever.
    4. Setup the LLM.
    5. Create the RetrievalQA chain and provide the answer to the query.
    """
    try:
        # Load documents from the web
        raw_data = scrap_web(base_url)

        # Process documents
        processed_docs = process_documents(raw_data)

        # Create FAISS retriever
        faiss_retriever = create_faiss_retriever(processed_docs)

        # Setup LLM
        mistral_llm = setup_llm()

        # Create RetrievalQA chain
        qa_chain = create_retrieval_qa_chain(faiss_retriever, mistral_llm)

        # Query the system
        answer = qa_chain.invoke(query)
        return answer
    except Exception as e:
        return f"An error occurred during the process: {str(e)}"


def main():
    """
    Main function to handle user inputs and provide answers.
    """
    try:
        base_url = input("Please enter the website URL: ").strip()
        if not base_url:
            print("Invalid URL, exiting...")
            return

        print("Type 'exit' to quit the application.")

        while True:
            query = input("Ask your question: ").strip()
            
            if query.lower() == 'exit':
                print("Goodbye! Have a great day!")
                break
            
            # Ask the model and get the answer
            answer = ask_chat(base_url, query)
            print(f"Answer: {answer}")

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == '__main__':
    main()
