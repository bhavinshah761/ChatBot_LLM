Full-Stack Local RAG Chatbot

An enterprise-grade, privacy-first Retrieval-Augmented Generation (RAG) chatbot designed to perform semantic search and question answering over local documents with **100% data privacy**, **zero cloud API costs**, and **zero external data leakage**.

---

### 🚀 Key Features

* **100% Local & Private Execution:** Operates entirely offline using open-source models via Ollama (Mistral-7B/Llama 3) and local HuggingFace embeddings—no data ever leaves your machine.
* **Decoupled Microservice Architecture:** Asynchronous **FastAPI** backend handling RAG orchestration and vector storage querying, paired with an interactive **Streamlit** chat interface.
* **Grounded Responses with Source Citation:** Retrieves top relevant document chunks from **ChromaDB** to eliminate model hallucinations and provide verifiable source links.
* **Persistent Vector Storage:** Automatically parses, chunks, and indexes documents (PDFs, Markdown, Text) into high-dimensional vector embeddings stored on disk.

---

### 🏗️ Architecture & Technical Workflow

Full-Stack Local RAG Chatbot

An enterprise-grade, privacy-first Retrieval-Augmented Generation (RAG) chatbot designed to perform semantic search and question answering over local documents with **100% data privacy**, **zero cloud API costs**, and **zero external data leakage**.

---

### 🚀 Key Features

* **100% Local & Private Execution:** Operates entirely offline using open-source models via Ollama (Mistral-7B/Llama 3) and local HuggingFace embeddings—no data ever leaves your machine.
* **Decoupled Microservice Architecture:** Asynchronous **FastAPI** backend handling RAG orchestration and vector storage querying, paired with an interactive **Streamlit** chat interface.
* **Grounded Responses with Source Citation:** Retrieves top relevant document chunks from **ChromaDB** to eliminate model hallucinations and provide verifiable source links.
* **Persistent Vector Storage:** Automatically parses, chunks, and indexes documents (PDFs, Markdown, Text) into high-dimensional vector embeddings stored on disk.

---

### 🏗️ Architecture & Technical Workflow

The architecture of the Full-Stack Local RAG Chatbot is built as a decoupled, privacy-first microservice system divided into four primary layers: document processing, vector storage, backend orchestration, and user presentation.Ingestion & Embedding PipelineThe pipeline begins when unstructured local documents (such as PDFs, Markdown files, or text documents) are ingested and split into manageable, overlapping passages using a recursive text splitter. These text chunks are passed to a local HuggingFace embedding model (sentence-transformers/all-MiniLM-L6-v2), which translates each chunk into a high-dimensional vector representation representing its semantic meaning.Persistent Vector StorageThese generated embeddings, along with their raw text and source metadata, are indexed and saved directly to disk within a persistent ChromaDB vector database. Storing the vectors locally ensures that document indexing happens once, allowing instantaneous similarity retrieval for subsequent user queries without needing re-embedding or external network connectivity.Asynchronous Backend & LangChain OrchestrationA FastAPI application serves as the core backend engine, exposing asynchronous RESTful endpoints (/ask, /ingest) for communication. When a query is received from the client, FastAPI uses LangChain to embed the question, execute a top-$k$ nearest-neighbor vector search in ChromaDB, and pull the most contextually relevant document chunks. LangChain then constructs an augmented prompt containing both the user's question and the retrieved context.Local Inference & Frontend InterfaceThe augmented prompt is passed to Ollama, which runs an open-source Large Language Model (such as Mistral-7B or Llama 3) entirely on the host machine's hardware. The LLM generates a grounded response restricted strictly to the provided context, which FastAPI returns back to the interactive Streamlit user interface. This complete separation of the frontend UI, backend orchestration API, and local inference engine guarantees zero cloud API costs, zero data leakage, and a modular design where models or database components can be upgraded independently.

---

### 🛠️ Tech Stack

* **Backend Framework:** FastAPI, Python, Uvicorn
* **AI & Orchestration:** LangChain, Ollama (Mistral / Llama 3)
* **Vector Store & Embeddings:** ChromaDB, HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)
* **Frontend UI:** Streamlit
* **Document Processing:** Unstructured, PyPDF, RecursiveCharacterTextSplitter




