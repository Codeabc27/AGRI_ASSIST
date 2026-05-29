import os

from dotenv import load_dotenv

from groq import Groq

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma

# ==========================================
# LOAD ENV VARIABLES
# ==========================================

load_dotenv()

# ==========================================
# GROQ CLIENT
# ==========================================

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ==========================================
# EMBEDDING MODEL
# ==========================================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ==========================================
# LOAD VECTOR DATABASE
# ==========================================

vectordb = Chroma(persist_directory="RAG/vectordb", embedding_function=embedding_model)

# ==========================================
# RAG FUNCTION
# ==========================================


def retrieve_answer(query):

    try:
        # ======================================
        # RETRIEVE RELEVANT DOCUMENTS
        # ======================================

        results = vectordb.similarity_search(query, k=3)

        # ======================================
        # HANDLE EMPTY RESULTS
        # ======================================

        if not results:
            return "I could not find relevant agriculture information."

        # ======================================
        # CREATE CONTEXT
        # ======================================

        context = "\n".join([doc.page_content for doc in results])

        # ======================================
        # PROMPT ENGINEERING
        # ======================================

        prompt = f"""

You are AgriAssist AI,
an expert agriculture assistant.

Use ONLY the agriculture context provided.

If the answer is not found in the context,
reply:

"I do not have enough agriculture data to answer this accurately."

Guidelines:
- Be accurate
- Be practical
- Use simple farmer-friendly language
- Keep answers concise
- Do not invent facts

Agriculture Context:
{context}

Farmer Question:
{query}

Answer:
"""

        # ======================================
        # GROQ LLM REQUEST
        # ======================================

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )

        # ======================================
        # EXTRACT ANSWER
        # ======================================

        answer = response.choices[0].message.content

        return answer

    # ==========================================
    # ERROR HANDLING
    # ==========================================

    except Exception as e:
        return f"Error: {str(e)}"
