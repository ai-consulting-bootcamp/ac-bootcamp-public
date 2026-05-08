# %% [markdown]
# # RAG Pipeline Optimization
# 
# This notebook demonstrates techniques to improve RAG pipeline performance: query improvement, reranking, and metadata filtering.

# %% [markdown]
# ## Setup

# %% [markdown]
# !pip install langchain langchain-openai langchain-pinecone pinecone-client python-dotenv -q

# %%
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document

# Load environment variables from .env file
load_dotenv()

# Verify API keys are loaded
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please create a .env file with your API key.")
if not os.getenv("PINECONE_API_KEY"):
    raise ValueError("PINECONE_API_KEY not found in environment variables. Please create a .env file with your API key.")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# %% [markdown]
# ## Section 1: Query Improvement

# %%
# Query rewriting example
def rewrite_query(original_query):
    prompt = f"Rewrite this query to be more specific and better suited for document retrieval: {original_query}"
    response = llm.invoke(prompt)
    return response.content

original = "Tell me about AI"
rewritten = rewrite_query(original)
print(f"Original: {original}")
print(f"Rewritten: {rewritten}")

# %%
# Sub-query decomposition
def decompose_query(complex_query):
    prompt = f"Break this complex query into 2-3 simpler sub-queries: {complex_query}"
    response = llm.invoke(prompt)
    return response.content

complex = "How does machine learning compare to deep learning and what are their applications?"
sub_queries = decompose_query(complex)
print(f"Complex query: {complex}")
print(f"Sub-queries: {sub_queries}")

# %% [markdown]
# **Scoping Insight**: Test when query improvement helps vs when it's unnecessary complexity. Simple queries often work fine - only add query rewriting when you see consistent retrieval failures.

# %% [markdown]
# ## Section 2: Parent Document Retrieval

# %%
# Parent document retrieval pattern
# 1. Store small chunks with parent IDs
# 2. Retrieve small chunks (better semantic match)
# 3. Fetch parent documents for full context

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Create parent documents
parent_docs = [
    Document(page_content="Machine learning is a subset of AI. Deep learning uses neural networks. NLP processes human language.")
]

# Split into small chunks with parent metadata
small_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)
small_chunks = small_splitter.split_documents(parent_docs)

# Add parent ID to each chunk
for i, chunk in enumerate(small_chunks):
    chunk.metadata["parent_id"] = 0  # Reference to parent document

print(f"Created {len(small_chunks)} small chunks from 1 parent document")
print(f"First chunk: {small_chunks[0].page_content}")

# %% [markdown]
# **Scoping Insight**: Recognize when parent document retrieval is needed vs when simple chunks work. Use this pattern when you need both precise semantic matching (small chunks) and full context (parent documents).

# %% [markdown]
# ## Section 3: Relevance Scoring & Reranking

# %%
# LLM-based reranking
def rerank_documents(query, documents, top_k=2):
    # Score each document
    scores = []
    for doc in documents:
        prompt = f"Rate the relevance of this document to the query '{query}' on a scale of 0-1: {doc.page_content}"
        response = llm.invoke(prompt)
        # Extract score (simplified - in practice, use structured output)
        try:
            score = float(response.content.split()[0])
            scores.append((score, doc))
        except:
            scores.append((0.5, doc))
    
    # Sort by score and return top_k
    scores.sort(reverse=True, key=lambda x: x[0])
    return [doc for score, doc in scores[:top_k]]

# Example usage
sample_docs = [
    Document(page_content="Machine learning is a subset of artificial intelligence."),
    Document(page_content="The weather today is sunny and warm."),
    Document(page_content="Deep learning uses neural networks for pattern recognition.")
]

query = "What is machine learning?"
reranked = rerank_documents(query, sample_docs)
print(f"Query: {query}")
print(f"Top result: {reranked[0].page_content}")

# %% [markdown]
# **Scoping Insight**: Measure improvement vs cost - when reranking is justified. Reranking adds latency and cost. Use it when retrieval quality is critical, not for every query.

# %% [markdown]
# ## Section 4: Metadata Filtering

# %%
# Add metadata to documents
from datetime import datetime

documents_with_metadata = [
    Document(
        page_content="New regulation on data privacy",
        metadata={"date": "2024-01-15", "category": "regulations", "source": "legal"}
    ),
    Document(
        page_content="Old regulation from 2020",
        metadata={"date": "2020-03-10", "category": "regulations", "source": "legal"}
    ),
    Document(
        page_content="Technical documentation",
        metadata={"date": "2024-02-20", "category": "technical", "source": "docs"}
    )
]

# Filter by metadata before retrieval
def filter_by_metadata(docs, date_cutoff=None, category=None):
    filtered = docs
    if date_cutoff:
        filtered = [d for d in filtered if d.metadata.get("date", "") >= date_cutoff]
    if category:
        filtered = [d for d in filtered if d.metadata.get("category") == category]
    return filtered

# Example: Get recent regulations only
recent_regs = filter_by_metadata(documents_with_metadata, date_cutoff="2024-01-01", category="regulations")
print(f"Found {len(recent_regs)} recent regulations")
for doc in recent_regs:
    print(f"- {doc.page_content} ({doc.metadata['date']})")

# %% [markdown]
# **Scoping Insight**: When metadata setup is worth the upfront cost vs when to skip it. Metadata filtering requires upfront work to tag documents. Use it when you have clear filtering needs (dates, categories, sources), not as a default.


