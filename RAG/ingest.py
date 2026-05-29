from langchain_community.document_loaders import DirectoryLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma

# ==========================================
# LOAD DOCUMENTS
# ==========================================

loader = DirectoryLoader("RAG/data/agriculture_docs", glob="*.txt")

documents = loader.load()

# ==========================================
# SPLIT DOCUMENTS
# ==========================================

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

docs = text_splitter.split_documents(documents)

# ==========================================
# EMBEDDINGS
# ==========================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ==========================================
# VECTOR DATABASE
# ==========================================

vectordb = Chroma.from_documents(
    documents=docs, embedding=embedding_model, persist_directory="RAG/vectordb"
)

vectordb.persist()

print("Vector Database Created")
