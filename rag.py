from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

DB_PATH = "backend/vectorstore"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

llm = ChatOllama(model="llama3.1")

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Answer the question using only the context below.

If the answer is not available in the context, say:
"I don't know based on the provided document."

Context:
{context}

Question:
{question}
""")

def ask_question(question: str):
    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    chain = prompt | llm | StrOutputParser()

    answer = chain.invoke({
        "context": context,
        "question": question
    })

    sources = [doc.metadata for doc in docs]

    return {
        "answer": answer,
        "sources": sources
    }