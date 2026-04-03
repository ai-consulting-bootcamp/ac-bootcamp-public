# Vocabulary processed 

Format:
```text
CONCEPT HEADING
Subject — predicate — object (Unit Name as shown in the course)
```


## Canonical predicate reference

| Predicate          | Meaning |
|--------------------|---------|
| `specializes`      | A is a subtype or specific instance of B |
| `implements`       | A is a concrete realisation of B |
| `composed-of`      | A contains B as a component |
| `integrates-with`  | A connects to or works alongside B |
| `enables`          | A makes B possible |
| `produces`         | A outputs or generates B |
| `consumes`         | A takes B as input |
| `orchestrates`     | A coordinates or sequences B |
| `replaces`         | A supersedes B in common usage |
| `reduces`          | A decreases B |
| `increases`        | A increases B |
| `fails-when`       | A breaks or degrades under condition B |
| `preferred-when`   | A is the better choice when condition B holds |
| `avoid-when`       | A should not be used when condition B holds |
| `trades-off`       | A sacrifices B for another gain |
| `contrasts-with`   | A and B differ in a decision-relevant way |
| `see-also`         | B is a related concept (navigation only) |
| `used-by`          | A is consumed or depended on by B (reverse lookup) |
| `defined-as`       | A's formal definition is stated as B |
| `applied-to`       | A is used or deployed in context B |
| `measured-by`      | A is quantified using metric or tool B |
| `accumulates-when` | A grows or worsens under condition B |
| `subject-to`       | A is bound by regulation or constraint B |
| `produced-when`    | A arises or appears under condition B |
| `documented-via`   | A is recorded or formalized through artifact B |
| `implemented-via`  | A is realized through mechanism or tool B |

Domain-specific precise verbs (`runs-on`, `trains-on`, `isolates`, `traces`, `caps`, `billed-by`, etc.) remain valid where they are more precise than the canonical set.

---

## Week 1 — AI basics, Python, ML/NN, GenAI & APIs, speech

### AI literacy & consulting

AGENTIC AI  
Agentic AI — denotes — AI systems that autonomously plan, select tools, and execute multi-step tasks (Week 1, AI Literacy)  
LangChain — orchestrates — agentic AI workflows via composable chains and tool bindings (Week 3, LangChain Integration)  
LangGraph — implements — stateful agentic AI with graph-based control flow (Week 4, LangGraph Integration)  
n8n AI Agent node — runs — agentic AI logic within no-code workflows (Week 4, Advanced n8n Workflows)  
Autonomous agent — specializes — agentic AI (Week 4–5, Autonomous AI Systems + Project 3 Brief)  
ReAct pattern — drives — agentic AI reasoning–acting loop (Week 4, Agent Fundamentals)

NARROW AI  
Narrow AI — specializes — AI capability confined to a single domain or task (Week 1, AI Literacy)

WEAK AI  
Weak AI — specializes — AI that simulates intelligence without self-awareness or general reasoning (Week 1, AI Literacy)

ARTIFICIAL GENERAL INTELLIGENCE (AGI)  
AGI — specializes — hypothetical AI capable of human-level reasoning across any domain (Week 1, AI Literacy)

ARTIFICIAL SUPER INTELLIGENCE (ASI)  
ASI — specializes — hypothetical AI exceeding the full cognitive capacity of humanity (Week 1, AI Literacy)

AI TAXONOMY  
AI taxonomy — classifies — AI systems by scope, capability, and generality (Week 1, AI Literacy)

AI CONSULTING FRAMEWORK  
AI consulting framework — structures — how consultants scope, design, and deliver AI engagements (Week 1, AI Literacy)

AI-COMPLETE PROBLEMS  
AI-complete problems — define — tasks whose full solution requires general AI capability (Week 1, AI Literacy)

LARGE LANGUAGE MODELS (LLMs)  
LLM — specializes — transformer-scale language model pre-trained on large text corpora (Week 1, AI Literacy + Generative AI)  
Generative AI — relies-on — LLMs as the core generation model class (Week 1, Generative AI)

MORAVEC'S PARADOX  
Moravec's paradox — illustrates — that tasks trivial for humans are computationally hard for AI, and vice versa (Week 1, AI Literacy)

MULTIMODAL AI  
Multimodal AI — specializes — AI that processes and generates across vision, audio, and text simultaneously (Week 1, AI Literacy + Generative AI)  
Multimodal AI — enables — joint reasoning over images, speech, and text in a single model pass (Week 1, same)  
Vision API — implements — multimodal AI for image-plus-text LLM inputs (Week 1, LAB | API Calling to ChatGPT)

---

### Environment & tooling

CONDA  
Conda — isolates — Python runtime environments per project to prevent dependency conflicts (Week 1, Python Environment Setup)

GIT  
Git — tracks — version history of code and content through commits and branches (Week 1, Python Environment Setup)

GITHUB  
GitHub — hosts — remote repositories and pull-request-based collaboration workflows (Week 1, Python Environment Setup)

JUPYTER NOTEBOOKS (IN VSCODE)  
Jupyter in VSCode — executes — notebook cells inside the editor, mixing code and narrative (Week 1, Python Environment Setup)

PYTHON 3.8+  
Python — powers — all labs, API integrations, and automation scripts across the bootcamp (Week 1–9)

VSCODE (VISUAL STUDIO CODE)  
VSCode — integrates — code editing, Git source control, and Jupyter notebooks within a single IDE (Week 1, Python Environment Setup)

ENVIRONMENT VARIABLES (.env)  
Environment variables — store — API keys and secrets outside version-controlled source code (Week 2, API and Integration Patterns Fundamentals)  
Environment variables — loaded-by — `python-dotenv` or system environment at runtime (Week 2, same)

---

### Python programming

VARIABLES  
Variables — bind — names to values stored in program memory (Week 1, Python Review)

LISTS  
Lists — hold — ordered, mutable sequences of arbitrary values (Week 1, Python Review)

DICTIONARIES  
Dictionaries — map — string keys to values for structured data access (Week 1, Python Review)

SETS  
Sets — enforce — collections of unique, unordered elements (Week 1, Python Review)

CONTROL FLOW (IF/ELSE, FOR, WHILE)  
Control flow — governs — branching and iteration within a Python program (Week 1, Python Review)

FUNCTIONS  
Functions — encapsulate — named, reusable blocks of logic (Week 1, Python Review)  
Functions — accept — parameters and return values to their callers (Week 1, same)

CLASSES  
Classes — model — objects that bundle state (attributes) and behavior (methods) (Week 1, Python Review)

IMPORTING LIBRARIES  
Importing libraries — exposes — third-party modules such as `pandas` and `json` within a script (Week 1, Python Review)

---

### Data & files

DATA MANIPULATION (PANDAS)  
Pandas — loads-and-transforms — tabular data for filtering, grouping, aggregation, and export (Week 1, LAB | Data Manipulation + JSON Handling)

DESCRIPTIVE STATISTICS  
Descriptive statistics — summarizes — column distributions, central tendency, and spread of a dataset (Week 1, LAB | Data Manipulation + JSON Handling)

FEATURE ENGINEERING  
Feature engineering — derives — new columns from raw fields to improve model input quality (Week 1, LAB | Data Manipulation + JSON Handling)

JSON  
JSON — serializes — structured Python records as portable, human-readable text (Week 1, LAB | Data Manipulation + JSON Handling)  
LLM APIs — transmit — requests and responses formatted as JSON (Week 1, Generative AI)

MISSING VALUES  
Missing values — require — cleaning or imputation before model training or export (Week 1, LAB | Data Manipulation + JSON Handling)

STRUCTURED DATA EXPORT CLASSES  
Structured export classes — enforce — typed field schemas for validated JSON output (Week 1, LAB | Data Manipulation + JSON Handling)

---

### Machine learning & classical models

NON-GENERATIVE AI  
Non-generative AI — specializes — AI that predicts or classifies without sampling new content (Week 1, Neural Networks Fundamentals)

SUPERVISED LEARNING  
Supervised learning — trains — models on labeled input–output pairs (Week 1, Neural Networks Fundamentals)  
Supervised learning — produces — classifiers and regressors for prediction tasks (Week 1, same)

UNSUPERVISED LEARNING  
Unsupervised learning — discovers — structure in data without labeled targets (Week 1, Neural Networks Fundamentals)  
Unsupervised learning — produces — clusters and dimensionality reductions (Week 1, same)

DISTANCE-BASED MODELS  
Distance-based models — classify — new points by proximity to labeled training examples (Week 1, Neural Networks Fundamentals)

K-NEAREST NEIGHBORS (KNN)  
KNN — specializes — distance-based supervised classification (Week 1, Neural Networks Fundamentals)  
Scikit-learn — implements — KNN and other classical ML estimators (Week 1, LAB | sklearn Model Training + Evaluation)

LINEAR MODELS  
Linear models — specializes — supervised learning via linear decision surfaces (Week 1, Neural Networks Fundamentals)  
Linear models — optimize — coefficients by minimizing a convex loss function (Week 1, same)

TREE-BASED MODELS  
Tree-based models — specializes — supervised learning via recursive feature splits (Week 1, Neural Networks Fundamentals)  
Tree-based models — partition — feature space by minimizing node impurity (e.g. Gini) (Week 1, same)

SPECIALTY MODELS  
Specialty models — specializes — supervised learning for non-linear geometries and distributions (Week 1, Neural Networks Fundamentals)  
Specialty models — covers — SVMs, Naive Bayes, and kernel-based approaches (Week 1, same)

FINE-TUNING  
Fine-tuning — specializes — supervised training that updates a pre-trained model's weights on domain-specific data (Week 1, Neural Networks Fundamentals)  
Fine-tuning — contrasts-with — RAG: fine-tuning bakes knowledge into weights at training time; RAG retrieves it at inference time (Week 1–3, Neural Networks Fundamentals + RAG Introduction)  
Fine-tuning — preferred-when — domain knowledge is stable, high-volume, and latency-sensitive (Week 1, same)  
Fine-tuning — avoid-when — knowledge changes frequently or proprietary data cannot leave the organization's perimeter (Week 1, same)  
Fine-tuning — increases-cost — relative to prompting due to compute and data-preparation overhead (Week 1, same)

TRAIN/TEST SPLIT  
Train/test split — separates — training and hold-out data for unbiased evaluation (Week 1, LAB | sklearn Model Training + Evaluation)

STRATIFICATION  
Stratification — preserves — class proportions across train and test splits (Week 1, LAB | sklearn Model Training + Evaluation)

RANDOM SEED  
Random seed — ensures — reproducibility of stochastic splits and model initialization (Week 1, LAB | sklearn Model Training + Evaluation)

CLASSIFICATION METRICS  
Classification metrics — quantify — model performance on discrete class predictions (Week 1, Neural Networks Fundamentals)  
Classification metrics — covers — accuracy, precision, recall, F1, and ROC-AUC (Week 1, same)

REGRESSION METRICS  
Regression metrics — quantify — model error on continuous target predictions (Week 1, Neural Networks Fundamentals)  
Regression metrics — covers — MAE, MSE, RMSE, and R² (Week 1, same)

CLUSTERING METRICS  
Clustering metrics — quantify — cohesion and separation of unsupervised groupings (Week 1, Neural Networks Fundamentals)

DATA PROCESSING REQUIREMENTS  
Data processing requirements — constrain — which preprocessing steps a given model family needs (Week 1, Neural Networks Fundamentals)

MODEL SELECTION FACTORS  
Model selection factors — guide — choosing a model based on data type, interpretability need, and task (Week 1, Neural Networks Fundamentals)

---

### Deep learning & neural networks

DEEP LEARNING  
Deep learning — specializes — machine learning using multi-layer neural networks (Week 1, Neural Networks Fundamentals)

NEURAL NETWORK  
Neural network — specializes — machine learning model composed of interconnected layers of neurons (Week 1, Neural Networks Fundamentals)

FEEDFORWARD NEURAL NETWORK  
Feedforward neural network — implements — neural network with strictly forward signal propagation (Week 1, ML & Neural Networks (Notebooks))  
Feedforward neural network — trained-via — backpropagation and gradient descent (Week 1, same)

ACTIVATION FUNCTION  
Activation function — introduces — nonlinearity into neural network layer outputs (Week 1, ML & Neural Networks (Notebooks))  
Activation function — controls — which neurons fire and at what magnitude per forward pass (Week 1, same)

EPOCHS  
Epochs — count — full passes through the training dataset during optimization (Week 1, ML & Neural Networks (Notebooks))

OVERFITTING  
Overfitting — occurs-when — a model memorizes training data and fails to generalize to new examples (Week 1, ML & Neural Networks (Notebooks))  
Training curves — detect — overfitting via divergence between train and validation loss (Week 1, same)

UNDERFITTING  
Underfitting — occurs-when — a model lacks sufficient capacity to capture training patterns (Week 1, ML & Neural Networks (Notebooks))

TENSORFLOW  
TensorFlow — backs — Keras computation graph construction and distributed execution (Week 1, ML & Neural Networks (Notebooks))

KERAS  
Keras — provides — high-level API for defining, compiling, and training neural network layers (Week 1, ML & Neural Networks (Notebooks))  
Keras — runs-on — TensorFlow as its default execution backend (Week 1, same)

SAVEDMODEL  
SavedModel — serializes — a trained TensorFlow/Keras model as a portable, platform-independent artifact (Week 1, LAB | Build Simple Neural Network)

CIFAR-10  
CIFAR-10 — benchmarks — image classification models on 10 real-world object categories (Week 1, LAB | Build Simple Neural Network)

MNIST-STYLE DIGITS  
MNIST-style digits — benchmark — handwritten-digit classification models (Week 1, ML & Neural Networks (Notebooks))

TENSORFLOW VS HUGGING FACE  
TensorFlow ecosystem — contrasts-with — Hugging Face ecosystem on custom training flexibility vs. pre-trained model access (Week 1, Neural Networks Fundamentals)

---

### Generative AI & APIs

GENERATIVE AI  
Generative AI — produces — new text, images, or audio by sampling from learned probability distributions (Week 1, Generative AI)  
Generative AI — relies-on — LLMs for text generation tasks (Week 1, same)

LLM APIS  
LLM APIs — expose — model inference over HTTP using role-tagged JSON message arrays (Week 1, Generative AI)

ENCODER–DECODER ARCHITECTURE  
Encoder–decoder — transforms — an input sequence into a context vector and decodes it into an output sequence (Week 1, Generative AI)  
Encoder–decoder — passes — encoded context via attention to the decoder at each step (Week 1, same)

ATTENTION MECHANISM  
Attention mechanism — weights — token relevance across a sequence for context integration (Week 1, Generative AI)  
Attention mechanism — enables — long-range dependencies that recurrent architectures cannot capture (Week 1, same)

CHAT COMPLETIONS API  
Chat Completions API — structures — LLM interactions as a sequence of role-tagged message turns (Week 1, Generative AI)  
Chat Completions API — supersedes — raw Completions for conversational and instruction-following tasks (Week 1, same)

MESSAGE ROLES  
Message roles — categorize — prompt turns as system, user, or assistant (Week 1, Generative AI)  
System role — establishes — model behavior, persona, and constraints for the entire session (Week 1, same)

SYSTEM PROMPT  
System prompt — constrains — LLM behavior, persona, and output format across all turns in a session (Week 1, Generative AI; Week 2, Prompt Engineering Fundamentals)  
System prompt — overridden-by — prompt injection attacks that insert conflicting instructions (Week 4, Agent Fundamentals)  
System prompt — preferred-when — consistent behavior must be enforced regardless of user turn content (Week 1–2, same)  
System prompt — see-also — Message roles, Prompt engineering, Guardrails (output)

TEMPERATURE  
Temperature — controls — LLM token sampling randomness during decoding (Week 1, Generative AI; Week 2, LAB | Prompt Engineering Lab)  
Temperature — trades-off — output creativity against determinism (Week 1–2, same)

JSON MODE  
JSON mode — constrains — LLM output to syntactically valid JSON (Week 1, Generative AI)

STRUCTURED OUTPUT  
Structured output — validates — LLM-generated fields against a declared schema (Week 1, LAB | API Calling with JSON)

PYDANTIC  
Pydantic — validates — structured output by enforcing typed field schemas on LLM responses (Week 1, LAB | API Calling with JSON)  
Pydantic — used-by — LangChain output parsers to validate and coerce structured LLM responses (Week 1–3, LAB | API Calling with JSON + LangChain Integration)  
Pydantic — used-by — MCP tool schemas to enforce typed input/output contracts for LLM-callable tools (Week 3, MCP Introduction)  
Pydantic — depended-on-by — tool validation in agentic pipelines to confirm tool outputs before downstream use (Week 5, Project 3 Brief)

OPENAI PYTHON LIBRARY  
OpenAI Python library — wraps — Chat Completions, embeddings, and other API endpoints for programmatic access (Week 1, Generative AI + LAB | API Calling to ChatGPT)

VISION API  
Vision API — processes — base64-encoded images alongside text in multimodal LLM prompts (Week 1, LAB | API Calling to ChatGPT)

HUGGING FACE  
Hugging Face — hosts — pre-trained models, tokenizers, and benchmark datasets as open artifacts (Week 1, LAB | API Calling to ChatGPT)  
Hugging Face — contrasts-with — OpenAI on open-source vs. API-only model access (Week 1, Neural Networks Fundamentals)

GPT-5  
GPT-5 — represents — current frontier of OpenAI API text and reasoning capabilities (Week 1, Generative AI)

---

### Speech

SPEECH-TO-TEXT (STT)  
STT — transcribes — spoken audio into text via acoustic and language modeling (Week 1, Speech Recognition Fundamentals)  
STT — specializes — speech recognition for downstream language understanding tasks (Week 1, same)

WHISPER  
Whisper — implements — STT via transformer-based audio encoding (Week 1, Speech Recognition Fundamentals + LAB | Whisper STT Implementation)  
Whisper — handles — long-form audio through sequential chunked transcription (Week 1, same)

GOOGLE SPEECH-TO-TEXT  
Google Speech-to-Text — implements — STT via Google Cloud speech models and REST API (Week 1, LAB | Compare Whisper vs Google STT)

TEXT-TO-SPEECH (TTS)  
TTS — synthesizes — speech audio from text input (Week 1, Speech Recognition Fundamentals)  
TTS providers — include — OpenAI TTS, ElevenLabs, and Google Cloud TTS (Week 1–2, Speech Recognition Fundamentals + Project 1 Kickoff)

WORD ERROR RATE (WER)  
WER — measures — STT transcription accuracy at the word level (Week 1, Speech Recognition Fundamentals + LAB | Compare Whisper vs Google STT)  
WER — computed-as — (substitutions + deletions + insertions) divided by reference word count (Week 1, same)

CHARACTER ERROR RATE (CER)  
CER — measures — STT transcription accuracy at the character level (Week 1, Speech Recognition Fundamentals)  
CER — more-sensitive-than — WER for morphologically rich languages (Week 1, same)

AUDIO CHUNKING  
Audio chunking — splits — long audio recordings into short segments for sequential STT processing (Week 1, LAB | Whisper STT Implementation)

DIGITAL SOUND BASICS  
Digital sound — represents — audio as discrete samples at a given sample rate and bit depth (Week 1, Speech Recognition Fundamentals)

TRANSFORMER MODELS FOR AUDIO  
Transformer (audio) — applies — self-attention to audio spectrograms for classification and transcription (Week 1, Speech Recognition (Notebooks))

---

## Week 2 — Mini-project, Project 1, prompting, low-code Python, APIs, RAG intro

### Podcast Studio & Project 1

PODCAST STUDIO  
Podcast Studio — assembles — an end-to-end pipeline from text input to synthesized audio output (Week 2, Project 1 Kickoff)

GRADIO  
Gradio — builds — lightweight web UIs for LLM and ML demos without a full frontend stack (Week 2, Project 1 Kickoff)

ELEVENLABS API  
ElevenLabs API — generates — high-quality, voice-cloneable audio from text input (Week 2, Project 1 Kickoff + MINI-PROJECT | Generate a Small Podcast from Notes)

END-TO-END AUTOMATION  
End-to-end automation — chains — LLM generation, TTS synthesis, and audio delivery in a single pipeline (Week 2, MINI-PROJECT | Generate a Small Podcast from Notes)

---

### Prompt engineering

PROMPT ENGINEERING  
Prompt engineering — shapes — LLM behavior through carefully structured input instructions (Week 2, Prompt Engineering Fundamentals)  
Prompt engineering — combines — system prompts, task framing, and in-context examples (Week 2, same)

FEW-SHOT PROMPTING  
Few-shot prompting — primes — LLM behavior by embedding worked examples directly in the prompt (Week 2, Prompt Engineering Fundamentals + LAB | Prompt Engineering Lab)  
Few-shot prompting — implements — in-context learning without parameter updates (Week 2, same)  
Few-shot prompting — preferred-when — desired output format is hard to describe abstractly but easy to demonstrate (Week 2, same)  
Few-shot prompting — see-also — Chain-of-thought prompting, System prompt, Dynamic prompting

CHAIN-OF-THOUGHT PROMPTING  
Chain-of-thought — elicits — step-by-step reasoning from the LLM before it produces a final answer (Week 2, Prompt Engineering Fundamentals)  
Chain-of-thought — improves — accuracy on multi-step arithmetic and logical reasoning tasks (Week 2, same)

MODEL BIASES  
Model biases — skew — LLM outputs toward patterns dominant in training data (Week 2, Prompt Engineering Fundamentals)

SYSTEMATIC PROMPT TESTING  
Systematic testing — evaluates — prompt variants by running N repetitions and comparing output distributions (Week 2, LAB | Prompt Engineering Lab)

---

### Python for low-code

REFACTORING  
Refactoring — restructures — existing code for clarity and maintainability without altering external behavior (Week 2, Python for Low Code Fundamentals + LAB | Python for Low Code Lab)

MODULAR CODE  
Modular code — organizes — program logic into independently testable, reusable units (Week 2, Python for Low Code Fundamentals)

ERROR HANDLING  
Error handling — catches — runtime exceptions to prevent pipeline crashes (Week 2, Python for Low Code Fundamentals)  
Error handling — enables — graceful degradation in API-dependent workflows (Week 2, same)

LOGGING  
Logging — records — runtime events, warnings, and errors for debugging and operational monitoring (Week 2, Python for Low Code Fundamentals)

UNIT TESTING  
Unit testing — verifies — individual function behavior against expected outputs (Week 2, Python for Low Code Fundamentals)  
Unit testing — reduces — regression risk when refactoring or extending shared code (Week 2, same)

---

### API fundamentals & integration

TOKEN ECONOMICS  
Token economics — governs — the cost structure of LLM API calls, where providers bill separately for input and output tokens (Week 2, API and Integration Patterns Fundamentals)  
Token economics — determines — per-request cost as a function of prompt length, output length, and model tier (Week 2, same)  
Token economics — see-also — Token budget manager, Prompt caching, Batch inference, Streaming

LATENCY VS THROUGHPUT  
Latency — measures — elapsed time from request submission to first token or full response (Week 2, API and Integration Patterns Fundamentals)  
Throughput — measures — requests or tokens processed per unit of time across concurrent calls (Week 2, same)  
Latency vs throughput — trades-off — single-request responsiveness against aggregate processing capacity (Week 2, same)  
Streaming — reduces — perceived latency by delivering tokens incrementally before the full response is ready (Week 2, same)  
Batch inference — increases — throughput at the cost of per-request latency (Week 2, same)

API RATE LIMIT  
API rate limit — caps — requests, tokens, or concurrent connections per time window at the provider level (Week 2, API and Integration Patterns Fundamentals)  
API rate limit — mitigated-by — exponential backoff, jitter, and request queuing in client code (Week 2, same)  
API rate limit — see-also — Exponential backoff, Jitter, Circuit breaker, Provider fallback

EXPONENTIAL BACKOFF  
Exponential backoff — spaces-out — retry attempts with progressively longer delays (Week 2, API and Integration Patterns Fundamentals)

JITTER  
Jitter — randomizes — retry intervals to prevent synchronized retry storms (Week 2, API and Integration Patterns Fundamentals)

CIRCUIT BREAKER  
Circuit breaker — halts — outbound requests to a failing service to prevent cascading failures (Week 2, API and Integration Patterns Fundamentals)

MULTI-PROVIDER LLM  
Multi-provider LLM integration — abstracts — a unified interface over OpenAI, Anthropic, Gemini, and Cohere (Week 2–3, Integration Patterns + LangChain Integration)  
Multi-provider integration — enables — provider fallback and per-request cost optimization (Week 2–3, same)

PROVIDER FALLBACK  
Provider fallback — reroutes — LLM requests to a secondary provider when the primary fails or is rate-limited (Week 2, Integration Patterns)

TOKEN BUDGET MANAGER  
Token budget manager — tracks — token consumption per request against allocated limits (Week 2, Integration Patterns)  
Token budget manager — reduces-cost — by truncating or summarizing context before hitting token ceilings (Week 2, same)

STREAMING  
Streaming — delivers — LLM output tokens to the client incrementally as they are generated (Week 2, Integration Patterns)  
Streaming — reduces-latency — perceived wait time by showing partial output before completion (Week 2, same)

BATCH INFERENCE  
Batch inference — groups — multiple LLM requests into a single asynchronous job for off-peak processing (Week 2, API and Integration Patterns Fundamentals; Week 7, A/B Testing & KPI (Notebooks))  
Batch inference — reduces-cost — relative to synchronous calls by using provider off-peak pricing tiers (Week 2, same)  
Batch inference — avoid-when — real-time user response is required (Week 2, same)  
Batch inference — see-also — Streaming, Token economics, Token budget manager

REST-STYLE HTTP APIS  
REST API — transmits — requests and responses as JSON over HTTP using standard verbs (GET, POST, etc.) (Week 2, LAB | API and Integration Patterns Lab)

---

### RAG business case & introduction

RAG (RETRIEVAL-AUGMENTED GENERATION)  
RAG — grounds — LLM responses in retrieved, domain-specific document passages (Week 2–3, RAG Introduction)  
RAG — queries — a vector database to retrieve relevant chunks before generation (Week 2–3, same)  
RAG — reduces — hallucination by anchoring outputs to retrieved evidence (Week 2–3, same)  
RAG — fails-when — retrieval quality is low or chunks are poorly formed and irrelevant passages dominate the context (Week 2–3, same)  
RAG — preferred-when — domain knowledge changes frequently or is proprietary and must not enter model weights (Week 2–3, same)  
RAG — avoid-when — latency is critical and the knowledge base is static (in that case prefer fine-tuning) (Week 2–3, same)  
RAG — see-also — Fine-tuning, Grounding, RAG pipeline, Vector database

RAG PIPELINE  
RAG pipeline — orchestrates — document ingestion, chunking, embedding, indexing, retrieval, and generation (Week 2–3, RAG Introduction + RAG Pipeline)  
RAG pipeline — increases-cost — relative to direct LLM calls due to embedding and retrieval steps (Week 2–3, same)  
RAG pipeline — reduces-cost — relative to fine-tuning for frequently updated or proprietary knowledge bases (Week 2–3, same)  
RAG pipeline — fails-when — chunk overlap is zero and the answer spans a segment boundary (Week 3, RAG Pipeline)  
RAG pipeline — consumed-by — LangChain retriever chains as the retrieval backbone (Week 3, LangChain Integration)  
RAG pipeline — depended-on-by — AI Content Creator project for primary knowledge base retrieval (Week 3, Project 2 Brief)  
RAG pipeline — depended-on-by — autonomous research agent for semantic company-data retrieval (Week 5, Project 3 Brief)

EMBEDDINGS  
Embeddings — represent — text as dense numerical vectors in a continuous semantic space (Week 2–3, RAG Introduction)  
Embeddings — enable — similarity-based retrieval via vector distance metrics (Week 2–3, same)  
Embeddings — degrades-when — input text exceeds the embedding model's maximum token window (Week 2–3, same)  
Embeddings — used-by — RAG pipeline for similarity-based chunk retrieval (Week 2–3, RAG Introduction + RAG Pipeline)  
Embeddings — used-by — semantic search as the representation layer for nearest-neighbor queries (Week 2–3, RAG Introduction)  
Embeddings — used-by — HyDE as the vector form of the generated hypothetical document (Week 3, RAG Pipeline)  
Embeddings — indexed-by — Pinecone for managed large-scale approximate nearest-neighbor retrieval (Week 2–3, same)  
Embeddings — indexed-by — Chroma for lightweight local retrieval (Week 3, LangChain Integration)  
Embeddings — produced-by — OpenAI embeddings API (`text-embedding-3-*` model family) (Week 2–3, RAG Introduction)  
Embeddings — produced-by — Hugging Face sentence-transformers for open-source embedding generation (Week 2–3, same)

VECTOR DATABASE  
Vector database — indexes — embeddings for approximate nearest-neighbor retrieval at scale (Week 2–3, RAG Introduction)

PINECONE  
Pinecone — implements — managed vector database for embedding storage and retrieval (Week 2–3, RAG Introduction + LangChain Integration)  
Pinecone — offers — serverless and pod-based index tiers for production-scale ANN retrieval (Week 2–3, same)  
Pinecone — known-for — real-time upsert and approximate nearest-neighbor query at scale (Week 2–3, same)  
Pinecone — used-by — RAG pipeline as the production vector index for chunk retrieval (Week 2–3, RAG Introduction + RAG Pipeline)  
Pinecone — used-by — autonomous research agent for semantic retrieval of company research embeddings (Week 5, Project 3 Brief)  
Pinecone — queried-by — LangChain retriever via the `PineconeVectorStore` integration (Week 3, LangChain Integration)  
Pinecone — queried-by — LangGraph agent nodes during the retrieval step of the ReAct loop (Week 4–5, LangGraph Integration)

CHROMA  
Chroma — implements — local vector database as a lightweight embedding store alternative (Week 3, LangChain Integration)

CHUNKING  
Chunking — splits — source documents into smaller text segments for embedding and retrieval (Week 2, RAG Introduction + LAB | Different Ways to Chunk Podcast and PDF)

FIXED-SIZE CHUNKING  
Fixed-size chunking — specializes — chunking by segmenting text at a fixed character or token count (Week 2, LAB | Different Ways to Chunk Podcast and PDF)  
Fixed-size chunking — loses — semantic coherence when splits occur mid-sentence or mid-idea (Week 2, same)  
Fixed-size chunking — preferred-when — documents are uniform in structure and processing speed is the priority (Week 2, same)  
Fixed-size chunking — see-also — Recursive character chunking, Token-based chunking, Semantic chunking, Chunk overlap

RECURSIVE CHARACTER CHUNKING  
Recursive character chunking — specializes — chunking by progressively splitting on structure-aware delimiters (Week 2, LAB | Different Ways to Chunk Podcast and PDF)  
Recursive character chunking — preferred-when — documents mix prose and code with varying structural nesting (Week 2, same)  
Recursive character chunking — trades-off — split precision for broad structural awareness without semantic modeling (Week 2, same)

TOKEN-BASED CHUNKING  
Token-based chunking — specializes — chunking by segmenting at LLM token boundaries (Week 2, LAB | Different Ways to Chunk Podcast and PDF)  
Token-based chunking — preferred-when — prompt token budgets must be precisely controlled (Week 2, same)  
Token-based chunking — avoid-when — semantic coherence within each chunk is more important than token count accuracy (Week 2, same)

SEMANTIC CHUNKING  
Semantic chunking — specializes — chunking by detecting meaning shifts between sentences (Week 2, LAB | Different Ways to Chunk Podcast and PDF)  
Semantic chunking — preferred-when — documents have variable-density content and retrieval precision matters more than speed (Week 2, same)  
Semantic chunking — trades-off — higher embedding compute cost per chunk for better retrieval coherence (Week 2, same)  
Semantic chunking — increases-cost — relative to fixed-size chunking due to embedding every sentence boundary (Week 2, same)

CHUNK OVERLAP  
Chunk overlap — preserves — cross-boundary context by sharing tokens between adjacent chunks (Week 2, LAB | Different Ways to Chunk Podcast and PDF)

SEMANTIC SEARCH  
Semantic search — retrieves — documents by embedding similarity rather than keyword match (Week 2, RAG Introduction)

GROUNDING  
Grounding — reduces — hallucination by anchoring LLM outputs to retrieved, tool-verified, or externally supplied facts (Week 2–3, RAG Introduction + RAG Pipeline)  
Grounding — implemented-via — RAG retrieval, function calling, or structured knowledge injection (Week 2–3, same)  
Grounding — contrasts-with — parametric knowledge baked into model weights at training time (Week 2–3, same)  
Grounding — fails-when — retrieved context is outdated, incomplete, or semantically distant from the query (Week 2–3, same)  
Grounding — preferred-when — the answer must be traceable to a specific source document or verified tool output (Week 2–3, same)  
Grounding — avoid-when — all required knowledge is stable, fully represented in model weights, and retrieval latency is prohibitive (Week 2–3, same)  
Grounding — see-also — RAG, Fine-tuning, Hallucination, Dynamic prompting

RAG BUSINESS CASE  
RAG business case — justifies — augmented retrieval over API-only LLM access for enterprise knowledge management (Week 2, Business Case: Real-World RAG Applications)

DYNAMIC PROMPTING  
Dynamic prompting — injects — retrieved context into prompt templates at query time (Week 2, RAG Introduction (Notebooks))

RAG SYSTEM ARCHITECTURE  
RAG system architecture — composed-of — document loader, chunker, embedder, vector index, retriever, optional reranker, and generation LLM (Week 2–3, RAG Introduction + RAG Pipeline)  
RAG system architecture — implements — a retrieve-then-generate pattern where context is injected dynamically at inference time (Week 2–3, same)  
RAG system architecture — contrasts-with — fine-tuning architecture: RAG is modular and updateable; fine-tuned models bake knowledge into weights at training time (Week 2–3, same)  
RAG system architecture — fails-when — any stage produces low-quality output: bad chunks corrupt retrieval; bad retrieval corrupts generation (Week 3, RAG Pipeline)

---

## Week 3 — Project 2, LangChain, RAG pipeline, MCP

### Project 2 — AI Content Creator

PRIMARY KNOWLEDGE BASE  
Primary knowledge base — grounds — brand-specific content generation in the AI Content Creator project (Week 3, Project 2 Brief)

MARKDOWN PARSING  
Markdown parsing — ingests — documents as structured text for downstream LLM processing (Week 3, Project 2 Brief)

AI-SLOP  
AI-Slop — defines — homogenized, generic LLM output lacking brand voice or differentiation (Week 3, Project 2 Brief)  
AI-Slop — motivates — brand-aware prompting strategies and primary knowledge base usage (Week 3, same)

---

### LangChain

LANGCHAIN  
LangChain — orchestrates — LLM calls, tool invocations, and memory into composable chains (Week 3, LangChain Integration)  
LangChain — abstracts — multiple LLM providers behind a unified interface (Week 3, same)  
LangChain — implements — RAG pipeline via retrievers, prompt templates, and model chains (Week 3, same)  
LangChain — offers — LangChain OSS framework, LangGraph orchestration library, and LangSmith observability platform (Week 3–4–7, LangChain Integration + LangGraph Integration)  
LangChain — known-for — pioneering composable LLM orchestration and establishing the chain-and-agent pattern (Week 3, same)  
LangChain — used-by — LangGraph as the underlying chain and tool execution layer for each graph node (Week 4, LangGraph Integration)  
LangChain — used-by — RAG pipeline implementations for retriever, prompt template, and model chain composition (Week 3, same)  
LangChain — depended-on-by — multi-provider LLM integration layer for chain orchestration (Week 2–3, Integration Patterns + LangChain Integration)

LANGCHAIN TOOL BINDING  
LangChain tool binding — attaches — callable functions to an LLM, enabling it to invoke external APIs (Week 3, LangChain Integration)  
Tool calling — enables — LLM to select and execute external tools during reasoning (Week 3, same)

FUNCTION CALLING  
Function calling — enables — LLM to invoke structured, schema-defined API calls as part of a generation step (Week 3, LangChain Integration)  
Function calling — implements — the API-primitive layer that tool binding and agent tool use depend on (Week 3, same)  
Function calling — contrasts-with — free-form text generation: outputs are validated JSON matching a declared schema (Week 3, same)  
Function calling — see-also — LangChain tool binding, Tool design, Structured output, Pydantic

LANGCHAIN AGENTS  
LangChain agents — autonomously-select — tools and execute multi-step plans (Week 3, LangChain Integration)  
LangChain agents — driven-by — ReAct-style planning loops (Week 3, same)  
LangChain agents — avoid-when — the workflow requires explicit state management, branching, or human-in-the-loop approval (Week 3–4, LangChain Integration + LangGraph Integration)

LANGCHAIN MEMORY  
LangChain memory — persists — conversation history across turns for contextual multi-turn replies (Week 3, LangChain Integration)

LANGCHAIN INVOCATION MODES  
Invoke — executes — a single synchronous LLM call (Week 3, LangChain Integration)  
Batch — executes — multiple LLM calls in parallel (Week 3, same)  
Stream — delivers — LLM output tokens incrementally to the caller (Week 3, same)

PROMPT CACHING  
Prompt caching — reuses — precomputed prompt prefix KV-cache to reduce API latency and token cost (Week 3, LangChain Integration)  
Prompt caching — supported-by — OpenAI and Gemini APIs via explicit or implicit prefix matching (Week 3, same)  
Prompt caching — reduces-cost — by up to 90% on repeated long-prefix API calls (Week 3, same)  
Prompt caching — reduces-latency — on subsequent calls that reuse the same cached prefix (Week 3, same)  
Prompt caching — fails-when — the prompt prefix changes between calls, invalidating the cached KV state (Week 3, same)

RATE LIMITING  
Rate limiting — caps — API requests per time window on the provider side (Week 3, LangChain Integration)  
Rate limiting — mitigated-by — exponential backoff and request queuing in client code (Week 3, same)

COHERE RERANKER  
Cohere reranker — re-orders — a retrieved chunk set by relevance score via a dedicated rerank API (Week 3, LangChain Integration + LAB | Relevance Scoring and Rerankers)

---

### RAG pipeline (advanced)

HYDE (HYPOTHETICAL DOCUMENT EMBEDDINGS)  
HyDE — generates — a hypothetical answer document to use as the retrieval query embedding (Week 3, RAG Pipeline)  
HyDE — improves — retrieval recall for questions with sparse keyword overlap in the corpus (Week 3, same)  
HyDE — see-also — Query expansion, Query rewriting, Step-back prompting, Sub-query decomposition

RERANKER  
Reranker — re-scores — an initial retrieval set to surface the most contextually relevant chunks (Week 3, RAG Pipeline + LAB | Relevance Scoring and Rerankers)  
Reranker — trades-off — additional query latency for higher retrieval precision (Week 3, same)  
Reranker — avoid-when — the corpus contains fewer than ~100 documents and first-pass retrieval is already precise (Week 3, same)  
Reranker — adds-latency — approximately 100–300ms per query depending on corpus size and reranker model (Week 3, same)  
Reranker — increases-cost — by one additional API call per retrieval step (Week 3, same)

CROSS-ENCODER RERANKER  
Cross-encoder — scores — query–document pairs jointly, producing higher-fidelity relevance scores than bi-encoder dot products (Week 3, RAG Pipeline)

METADATA FILTERING  
Metadata filtering — constrains — vector retrieval to documents matching structured field conditions (Week 3, RAG Pipeline)  
Metadata filtering — reduces — irrelevant candidates before reranking (Week 3, same)

PARENT DOCUMENT RETRIEVAL  
Parent document retrieval — returns — the larger parent chunk after locating a matching smaller child chunk (Week 3, RAG Pipeline)  
Parent document retrieval — balances — retrieval precision (small chunks) with generation context (large chunks) (Week 3, same)

QUERY EXPANSION  
Query expansion — generates — multiple alternative phrasings of the user query to broaden retrieval coverage (Week 3, RAG Pipeline)

QUERY REWRITING  
Query rewriting — reformulates — the user query for better semantic alignment with indexed document vocabulary (Week 3, RAG Pipeline)

STEP-BACK PROMPTING  
Step-back prompting — abstracts — a specific query into a higher-level concept for broader, more reliable retrieval (Week 3, RAG Pipeline)

SUB-QUERY DECOMPOSITION  
Sub-query decomposition — breaks — a complex question into independent simpler sub-questions for parallel retrieval (Week 3, RAG Pipeline)  
Sub-query decomposition — aggregates — per-sub-question results into a comprehensive final answer (Week 3, same)

RELEVANCE SCORING  
Relevance scoring — ranks — retrieved chunks by semantic or structural match to the query (Week 3, LAB | Relevance Scoring and Rerankers)

---

### MCP (Model Context Protocol)

MCP (MODEL CONTEXT PROTOCOL)  
MCP — standardizes — how LLM agents connect to external data sources, tools, and prompt templates (Week 3, MCP Introduction)  
MCP — fails-when — the MCP server is unavailable or misconfigured at agent startup (Week 3, same)  
MCP — used-by — autonomous research agent to access external APIs as discoverable, schema-validated tool calls (Week 5, Project 3 Brief)  
MCP — queried-by — LangGraph agent nodes during the tool-selection step of the ReAct reasoning loop (Week 4–5, LangGraph Integration + Project 3 Brief)

MCP SERVER  
MCP server — exposes — tools, resources, and prompts to any MCP-compliant client (Week 3, MCP Introduction)

MCP TOOLS  
MCP tools — implement — callable actions the LLM can invoke via the protocol (Week 3, MCP Introduction)

MCP RESOURCES  
MCP resources — provide — read-only data surfaces that can be injected into the LLM context (Week 3, MCP Introduction)

MCP PROMPTS  
MCP prompts — package — reusable, pre-built instruction templates for common LLM task patterns (Week 3, MCP Introduction)

MCP SECURITY  
MCP security considerations — mitigate — prompt injection and unauthorized server access risks (Week 3, MCP Introduction)

---

## Week 4 — LangGraph, n8n, autonomous agents

### LangGraph & agent fundamentals

LANGGRAPH  
LangGraph — models — agent control flow as a directed graph of stateful nodes and typed edges (Week 4, LangGraph Integration)  
LangGraph — routes — execution via conditional edges based on runtime state or LLM decisions (Week 4, same)  
LangGraph — manages — shared state across all graph traversals in a single typed object (Week 4, same)  
LangGraph — implements — human-in-the-loop checkpoints that pause execution for approval (Week 4, LAB | LangChain Guardrails)  
LangGraph — integrates-with — n8n for event-driven production orchestration (Week 4, LangGraph and n8n Integration)  
LangGraph — preferred-when — the workflow requires explicit branching, persistent state, or human-in-the-loop approval steps (Week 4, LangGraph Integration)  
LangGraph — avoid-when — the task is simple and linear with no conditional routing or state management needed (Week 4, same)  
LangGraph — used-by — autonomous research agent as the stateful multi-step planning engine (Week 5, Project 3 Brief)  
LangGraph — used-by — human-in-the-loop guardrail workflows to implement approval checkpoints (Week 4, LAB | LangChain Guardrails)  
LangGraph — used-by — n8n integration as the AI reasoning layer called by n8n workflow nodes (Week 4, LangGraph and n8n Integration)

LANGGRAPH VS LANGCHAIN AGENTS  
LangGraph — surpasses — LangChain agents for workflows requiring explicit state and branching control (Week 4, LangGraph Integration)  
LangChain agents — suited-for — simpler linear tool-use tasks without complex branching (Week 4, same)

CONDITIONAL EDGES (LANGGRAPH)  
Conditional edges — route — graph execution to different nodes based on evaluated runtime conditions (Week 4, LangGraph Integration)

ROUTING (LANGGRAPH)  
Routing — implemented-via — conditional edges in LangGraph to direct agent execution flow (Week 4, LangGraph Integration)  
Routing — see-also — Conditional edges (LangGraph), State machine, LangGraph

CONTEXT ENGINEERING  
Context engineering — manages — what information occupies the LLM context window at each reasoning step (Week 4, Agent Fundamentals)  
Context engineering — mitigates — context rot and loss of critical task information (Week 4, same)

CONTEXT ROT  
Context rot — degrades — agent reasoning as irrelevant, repeated, or stale tokens accumulate (Week 4, Agent Fundamentals)

ATTENTION BUDGET  
Attention budget — constrains — the effective number of tokens an LLM can attend to per call (Week 4, Agent Fundamentals)

PII DETECTION  
PII detection — identifies — personally identifiable information in agent inputs and outputs (Week 4, LAB | LangChain Guardrails)  
PII detection — prevents — privacy leakage in agentic pipelines (Week 4, same)

TOOL DESIGN  
Tool design — specifies — the interface, description, and input–output contract of an LLM-callable function (Week 4, Agent Fundamentals)  
Tool design — determines — how reliably an LLM selects and invokes the correct tool (Week 4, same)

GUARDRAILS (OUTPUT)  
Guardrails (output) — constrains — model outputs via schema validation, content filtering, and policy enforcement (Week 4, LAB | LangChain Guardrails)  
Guardrails (output) — composed-of — schema validators (Pydantic), PII detectors, safety classifiers, and HITL checkpoints (Week 4, same)  
Guardrails (output) — preferred-when — automated pipelines operate in regulated domains or handle sensitive user data (Week 4, same)  
Guardrails (output) — see-also — Human-in-the-loop, PII detection, Structured output, Prompt injection

PROMPT INJECTION  
Prompt injection — exploits — LLM instruction-following to embed adversarial commands inside user inputs that override system-level instructions (Week 4, Agent Fundamentals; Week 8, LAB | Red-Teaming for Bias: Adversarial Prompts and LangSmith)  
Prompt injection — risks — unauthorized tool invocations, data exfiltration, and policy bypass in agentic pipelines (Week 4–8, same)  
Prompt injection — mitigated-by — input sanitization, privileged instruction separation, and MCP security controls (Week 4, same)  
Prompt injection — see-also — MCP security, Adversarial prompts, Red teaming, System prompt

HUMAN-IN-THE-LOOP (GUARDRAILS)  
Human-in-the-loop — inserts — a human approval or override step within an automated agent workflow (Week 4, LAB | LangChain Guardrails)  
Human-in-the-loop — mitigates — unsafe or irreversible agent actions before execution (Week 4, same)

---

### n8n workflow automation

N8N  
n8n — automates — multi-step workflows by connecting nodes that represent services, transformations, and triggers (Week 4, LangGraph and n8n Integration + Advanced n8n Workflows)  
n8n — offers — open-source self-hosted and cloud-managed workflow automation with native code execution nodes (Week 4, Advanced n8n Workflows)  
n8n — known-for — being an open-source alternative to Zapier with Python execution, AI agent nodes, and self-hosting options (Week 4, same)  
n8n — contrasts-with — Zapier on self-hosting flexibility, code execution capability, and open-source licensing (Week 4, same)  
n8n — used-by — arXiv research summarizer pipeline for scheduled fetch, LLM summarization, and Notion storage (Week 4, LAB | arXiv Research Summarizer (n8n + Notion))  
n8n — used-by — Slack alert integration for automated channel notifications from workflow events (Week 4, LAB | Multi-App Integration (Slack + Sheets))  
n8n — used-by — Jira automation for issue creation and status sync (Week 6, LAB | Project 4: n8n Jira Integration)  
n8n — used-by — autonomous research agent deployment as the event-driven production trigger layer (Week 5, Project 3 Brief)

WEBHOOK (N8N)  
Webhook — triggers — an n8n workflow via an inbound HTTP POST from an external event source (Week 4, Advanced n8n Workflows)

WEBHOOK SECURITY (HMAC)  
Webhook security — verifies — inbound webhook payload authenticity by comparing a provider-signed HMAC digest against a locally computed signature (Week 4–5, Advanced n8n Workflows + Project 3 Brief)  
HMAC signature — prevents — replay attacks and spoofed webhook deliveries in production n8n workflows (Week 4–5, same)  
Webhook security — see-also — Credential management (n8n), OAuth 2.0 (n8n), MCP security

SCHEDULE TRIGGER  
Schedule trigger — fires — an n8n workflow at defined cron-based time intervals (Week 4, Advanced n8n Workflows)

OAUTH 2.0 (N8N)  
OAuth 2.0 — authorizes — n8n access to SaaS services on behalf of a user without sharing passwords (Week 4, Advanced n8n Workflows)

CREDENTIAL MANAGEMENT (N8N)  
Credential management — stores — API keys and OAuth tokens in encrypted n8n credential objects (Week 4, Advanced n8n Workflows)

SET NODE (N8N)  
Set node — transforms — workflow payload fields, mapping or mocking data between nodes (Week 4, LAB | Multi-App Integration (Slack + Sheets))

AI AGENT NODE (N8N)  
AI Agent node — executes — LLM-driven agentic logic as a first-class node within n8n workflows (Week 4, Advanced n8n Workflows)  
AI Agent node — connects-to — external tools and memory stores from within the n8n workflow graph (Week 4, same)

ERROR TRIGGER NODE (N8N)  
Error trigger node — captures — workflow execution failures and routes them to a dedicated error-handling branch (Week 4, Advanced n8n Workflows)

IDEMPOTENCY  
Idempotency — guarantees — that re-executing a workflow produces the same final state without duplicate side effects (Week 4, Advanced n8n Workflows)

N8N MONITORING  
n8n monitoring — inspects — workflow execution history, run status, and error logs via the n8n UI (Week 4, Advanced n8n Workflows)

ARXIV API (N8N)  
arXiv API — supplies — academic paper metadata and abstracts to n8n HTTP request nodes (Week 4, LAB | arXiv Research Summarizer (n8n + Notion))

NOTION DATABASE (N8N)  
Notion database — stores — structured records written by n8n workflows via the Notion API (Week 4, LAB | arXiv Research Summarizer (n8n + Notion))

SLACK INTEGRATION (N8N)  
Slack integration — sends — automated messages and alerts to workspace channels from n8n workflows (Week 4, LAB | Multi-App Integration (Slack + Sheets))

LANGGRAPH + N8N INTEGRATION  
LangGraph + n8n — separates — AI reasoning (LangGraph) from workflow orchestration and event triggers (n8n) (Week 4, LangGraph and n8n Integration)

---

### Autonomous agents

AUTONOMOUS AGENT  
Autonomous agent — specializes — agentic AI that operates without continuous human supervision (Week 4, Autonomous AI Systems)  
Autonomous agent — requires — clear scope and success metrics to avoid unbounded task expansion (Week 4, same)  
Autonomous agent — fails-when — success metrics are absent or ambiguous, allowing unconstrained sub-goal pursuit (Week 4, same)

REACT PATTERN  
ReAct pattern — interleaves — reasoning steps and tool-action invocations in a loop until completion (Week 4–5, Agent Fundamentals + Project 3 Brief)  
ReAct pattern — produces — an auditable chain of (Thought → Action → Observation) steps (Week 4–5, same)  
ReAct pattern — fails-when — tool descriptions are imprecise and the model selects or invokes the wrong tool (Week 4–5, same)  
ReAct pattern — trades-off — higher latency per step for improved auditability and intermediate error recovery (Week 4–5, same)

SCOPE CREEP (AGENTS)  
Scope creep — occurs-when — an agent pursues sub-goals beyond its defined task boundary (Week 4, Autonomous AI Systems)  
Success metrics — constrain — autonomous agent behavior within acceptable scope (Week 4, same)  
Scope creep — mitigated-by — explicit success criteria and tool-call auditing before execution (Week 4, same)  
Scope creep — detected-by — execution trace review comparing intended vs. actual tool call sequence (Week 4, same)

---

## Week 5 — Project 3

PROJECT 3 — AUTONOMOUS RESEARCH AGENT  
Autonomous research agent — performs — company research by chaining LangGraph planning, MCP tool calls, and Pinecone retrieval (Week 5, Project 3 Brief)  
n8n — deploys — the agent into production with scheduled and event-driven triggers (Week 5, same)  
Pinecone — stores — research embeddings for semantic retrieval during agent operation (Week 5, same)  
MCP — connects — the agent to external APIs as standardized, discoverable tool calls (Week 5, same)  
ReAct — drives — the agent's multi-step planning loop (Week 5, same)

RESEARCH AGENT ARCHITECTURE  
Research agent architecture — composed-of — LangGraph state graph, MCP tool server, Pinecone retrieval, and n8n event triggers (Week 5, Project 3 Brief)  
Research agent architecture — implements — ReAct reasoning loop as the control mechanism for multi-step company research (Week 5, same)  
Research agent architecture — integrates-with — external news and financial APIs via MCP tool definitions (Week 5, same)

EXECUTE COMMAND NODE (N8N)  
Execute Command node — runs — Python scripts as discrete steps within an n8n workflow (Week 5, Project 3 Brief)  
Python runner in n8n — enables — full programmatic code execution inside a no-code orchestration layer (Week 5, same)  
Execute Command node — risks — arbitrary code execution and sandbox escape if user-supplied input reaches the command string (Week 5, same)

TOOL VALIDATION & FAILURE HANDLING  
Tool validation — confirms — that tool outputs conform to expected schemas before downstream use (Week 5, Project 3 Brief)  
Tool validation — fails-when — the tool returns a partial response, a null, or an unexpected field structure (Week 5, same)  
Tool validation — preferred-when — the agent takes irreversible actions (write, send, delete) that cannot be undone without human review (Week 5, same)  
Failure handling — catches — tool errors and retries with exponential backoff, or escalates gracefully to avoid silent agent failures (Week 5, same)  
Failure handling — implements — a retry strategy with a maximum attempt ceiling before escalating to the error branch (Week 5, same)  
Failure handling — escalates — unresolved errors to a human-in-the-loop checkpoint or alert notification (Week 5, same)

---

## Week 6 — Classical PM, Agile, SilverTrust, migration

### Classical project management

CLASSICAL PROJECT MANAGEMENT  
Classical project management — structures — project delivery through sequential phases with fixed scope and upfront planning (Week 6, Classical Project Management: Scoping and Basics)

WORK BREAKDOWN STRUCTURE (WBS)  
WBS — decomposes — project objectives into a hierarchy of measurable, assignable deliverables (Week 6, Classical Project Management: Scoping and Basics)

STAKEHOLDER ANALYSIS  
Stakeholder analysis — maps — project stakeholders by influence and interest level (Week 6, Classical Project Management: Scoping and Basics)  
Stakeholder analysis — informs — communication plan and requirement prioritization (Week 6, same)  
Stakeholder analysis — composed-of — stakeholder register, interest–influence matrix, and engagement strategy (Week 6, same)  
Stakeholder analysis — required-before — communication plan, risk matrix, and requirements prioritization (Week 6, same)  
Stakeholder analysis — fails-when — key decision-makers are excluded or misclassified by influence level (Week 6, same)

RISK MANAGEMENT (PM)  
Risk management — identifies — project risks and prescribes mitigation or contingency actions for each (Week 6, Classical Project Management: Scoping and Basics)

COST MANAGEMENT  
Cost management — tracks — budget allocation and expenditure across project phases (Week 6, Classical Project Management: Scoping and Basics)

QUALITY MANAGEMENT  
Quality management — defines — acceptance criteria and review gates for project deliverables (Week 6, Classical Project Management: Scoping and Basics)

ORGANIZATIONAL STRUCTURES  
Organizational structures — determine — how authority, communication, and resources flow within a project (Week 6, Classical Project Management: Scoping and Basics)

PESTLE ANALYSIS  
PESTLE analysis — scans — political, economic, social, technological, legal, and environmental factors for strategic decisions (Week 6, LAB | Scoping Lab)  
PESTLE analysis — informs — AI infrastructure and vendor selection decisions (Week 6, same)  
PESTLE analysis — applied-to — AI compliance readiness assessment by mapping legal and regulatory axes to EU AI Act obligations (Week 6, same)

VERTEX AI VS OPENAI (SCOPING)  
Vertex AI / Gemini — contrasts-with — OpenAI stack on cost, data residency, and ecosystem lock-in (Week 6, LAB | Scoping Lab)

IMPACT ANALYSIS  
Impact analysis — quantifies — business and technical risk exposure when restructuring tooling or organization (Week 6, LAB | Project 4: Restructuring Impact Analysis)  
Impact analysis — used-in — vendor migration scoping to enumerate dependencies and integration points (Week 6, same)  
Impact analysis — outputs — a risk-ranked change inventory that informs sprint planning and stakeholder sign-off (Week 6, same)  
Impact analysis — required-when — a migration, restructuring, or new AI deployment affects existing system integrations (Week 6, same)  
Impact analysis — composed-of — dependency mapping, risk rating, cost estimation, and timeline assessment (Week 6, same)  
Impact analysis — fails-when — system dependencies are undocumented or data lineage across services is unclear (Week 6, same)

SHADOW AI  
Shadow AI — defines — the unsanctioned use of AI tools by employees outside approved organizational processes (Week 6, Classical Project Management: Scoping and Basics; Week 8, EU AI Act for Consultants)  
Shadow AI — risks — data leakage when sensitive information is submitted to external LLM APIs without data-handling agreements (Week 6–8, same)  
Shadow AI — mitigated-by — organizational AI policy, approved tool lists, and employee training (Week 6–8, same)  
Shadow AI — see-also — GDPR, EU AI Act, Data controller, Privacy by design

CHANGE MANAGEMENT  
Change management — manages — human and organisational resistance when introducing new tools, processes, or roles (Week 6, Classical Project Management: Scoping and Basics)  
Change management — composed-of — stakeholder communication, training, incremental rollout, and feedback loops (Week 6, same)  
Change management — fails-when — stakeholders are not identified or engaged before the change is announced (Week 6, same)  
Change management — preferred-when — AI tools alter existing workflows, job roles, or data-handling responsibilities (Week 6, same)  
Change management — produces — communication plan, training program, and adoption success metrics (Week 6, same)

---

### Agile methodologies

SCRUM  
Scrum — structures — iterative delivery into time-boxed sprints with defined roles, artifacts, and ceremonies (Week 6, Agile Management: Scrum)  
Scrum — see-also — Extreme Programming (XP), Kanban, Lean, Backlog, Sprint lifecycle, Velocity

BACKLOG  
Backlog — prioritizes — all planned work items as a ranked, living list for upcoming sprints (Week 6, Agile Management: Scrum)

USER STORIES  
User stories — express — feature requirements from the end user's perspective in a structured format (Week 6, Agile Management: Scrum)

ACCEPTANCE CRITERIA  
Acceptance criteria — define — testable conditions a user story must satisfy to be considered complete (Week 6, Agile Management: Scrum)

DEFINITION OF DONE  
Definition of Done — defines — the shared team-level completion criteria that any user story or increment must meet before it can be accepted (Week 6, Agile Management: Scrum)  
Definition of Done — contrasts-with — acceptance criteria: DoD applies to all stories; acceptance criteria are story-specific (Week 6, same)  
Definition of Done — reduces — rework and ambiguity about when work is truly finished (Week 6, same)

SPRINT PLANNING  
Sprint planning — produces — the sprint goal and the committed backlog slice a team will deliver within the sprint (Week 6, Agile Management: Scrum)  
Sprint planning — consumes — velocity, backlog priority, and team capacity as inputs (Week 6, same)

SPRINT LIFECYCLE  
Sprint lifecycle — sequences — planning, execution, review, and retrospective into a repeating time-boxed cycle (Week 6, Agile Management: Scrum)

STORY POINTS  
Story points — estimate — relative effort and complexity of a user story as a dimensionless unit (Week 6, Agile Management: Scrum)  
Story points — measured-by — team velocity to forecast future sprint capacity (Week 6, same)  
Story points — contrasts-with — hour-based estimates on abstracting uncertainty rather than clock time (Week 6, same)

TECHNICAL DEBT  
Technical debt — accumulates-when — short-term shortcuts defer proper design, testing, or refactoring (Week 6, Agile Management: Scrum)  
Technical debt — reduces — future delivery speed by increasing the cost of each subsequent change (Week 6, same)  
Technical debt — managed-by — dedicating a portion of each sprint to refactoring and debt reduction (Week 6, same)

BURNDOWN CHART  
Burndown chart — visualizes — remaining work versus elapsed sprint time to forecast completion (Week 6, Agile Management: Scrum)

VELOCITY (SCRUM)  
Velocity — measures — story points completed per sprint to forecast future team capacity (Week 6, Agile Management: Scrum)

EXTREME PROGRAMMING (XP)  
Extreme Programming — specializes — Agile with engineering practices such as TDD, continuous integration, and pair programming (Week 6, Agile Management: XP & Lean)

KANBAN  
Kanban — specializes — Agile flow management through a continuous pull-based board (Week 6, Agile Management: XP & Lean)

LEAN  
Lean — specializes — Agile by eliminating waste and optimizing end-to-end value delivery (Week 6, Agile Management: XP & Lean)

JIRA  
Jira — manages — agile boards, sprints, backlogs, and burndown reports for project tracking (Week 6, LAB | Setting up Agile Workflow in Jira for SilverTrust Project)

N8N–JIRA INTEGRATION  
n8n–Jira integration — automates — issue creation and status updates in Jira via n8n workflow nodes (Week 6, LAB | Project 4: n8n Jira Integration)

JIRA → TRELLO MIGRATION  
Jira REST API — contrasts-with — Trello API on data model, authentication, and migration path (Week 6, LAB | Project 4: Migrating from Jira to Trello)  
Jira–Trello migration — produces — a Trello board that reproduces the original Jira project structure (Week 6, same)

---

## Week 7 — Evaluation, A/B testing, BI, Project 5

### Model evaluation

MODEL EVALUATION  
Model evaluation — assesses — LLM output quality across accuracy, coherence, groundedness, and task completion (Week 7, Introduction to Model Evaluation)

BENCHMARKS  
Benchmarks — standardize — LLM comparison across reasoning, code generation, math, and long-context tasks (Week 7, Introduction to Model Evaluation)

BENCHMARK CONTAMINATION  
Benchmark contamination — invalidates — evaluation results when test data appears in model training data (Week 7, Introduction to Model Evaluation)

BENCHMARK SATURATION  
Benchmark saturation — signals — that a benchmark can no longer discriminate between state-of-the-art models (Week 7, Introduction to Model Evaluation)

HALLUCINATION  
Hallucination — defines — LLM output that is fluent and confident but factually incorrect or unsupported by any provided context (Week 7, Introduction to Model Evaluation; Week 2–3, RAG Introduction)  
Hallucination — produced-when — the model lacks retrieval grounding and relies solely on parametric memory for specific facts (Week 2–3, RAG Introduction)  
Hallucination — reduced-by — RAG grounding, function calling, and structured output validation (Week 2–7, same)  
Hallucination — contrasts-with — Grounding: grounding anchors outputs to verifiable facts, directly preventing the condition hallucination describes (Week 2–3, same)  
Hallucination — see-also — Grounding, RAG, Confidence score, LLM-as-judge

PRECISION AND RECALL  
Precision — measures — the fraction of retrieved or predicted positives that are actually correct (Week 7, Introduction to Model Evaluation)  
Recall — measures — the fraction of actual positives that the model successfully retrieved or predicted (Week 7, same)  
Precision vs recall — trades-off — false-positive rate against false-negative rate; the optimal balance depends on domain cost asymmetry (Week 7, same)  
F1 score — harmonizes — precision and recall into a single metric for imbalanced classification (Week 7, same)

BLEU  
BLEU — measures — n-gram overlap between generated text and human reference translations (Week 7, Introduction to Model Evaluation)  
BLEU — preferred-when — a human reference corpus is available and surface-form fidelity matters (Week 7, same)  
BLEU — avoid-when — paraphrase quality and semantic correctness are more important than word-level overlap (Week 7, same)  
BLEU — see-also — ROUGE, Precision and Recall, LLM-as-judge

ROUGE  
ROUGE — measures — recall-oriented n-gram overlap for summarization and generation quality assessment (Week 7, Introduction to Model Evaluation)  
ROUGE — preferred-when — a human reference corpus is available and surface-form fidelity matters (Week 7, same)  
ROUGE — avoid-when — paraphrase quality and semantic correctness are more important than word-level overlap (Week 7, same)  
ROUGE — see-also — BLEU, Precision and Recall, LLM-as-judge

CONFIDENCE SCORE  
Confidence score — measures — a model's estimated certainty for a predicted class or generated token (Week 7, Introduction to Model Evaluation)  
Confidence score — used-by — calibration analysis to verify that stated confidence aligns with empirical accuracy (Week 7, same)  
Confidence score — see-also — Calibration, Hallucination, Token-based evaluation

LLM-AS-JUDGE  
LLM-as-judge — evaluates — model outputs by prompting a separate LLM to score or rank them (Week 7, Introduction to Model Evaluation)  
LLM-as-judge — enables — scalable reference-free evaluation without human annotation per sample (Week 7, same)  
LLM-as-judge — risks — systematic positional and verbosity bias when judge and evaluated model share training data (Week 7, same)  
LLM-as-judge — fails-when — the evaluation rubric is ambiguous or not grounded in a structured scoring schema (Week 7, same)  
LLM-as-judge — see-also — Ground truth evaluation, Reference-free evaluation, Human-in-the-loop evaluation, Ablation studies

GROUND TRUTH EVALUATION  
Ground truth evaluation — compares — model outputs against human-verified reference answers (Week 7, Introduction to Model Evaluation)

REFERENCE-FREE EVALUATION  
Reference-free evaluation — scores — model outputs on quality dimensions without a gold-standard reference (Week 7, Introduction to Model Evaluation)

HUMAN-IN-THE-LOOP EVALUATION  
Human-in-the-loop evaluation — incorporates — human annotators to validate or correct model outputs (Week 7, LAB | Human-in-the-loop Evaluations)

ABLATION STUDIES  
Ablation studies — isolate — the contribution of individual components to overall model or pipeline performance (Week 7, Introduction to Model Evaluation)

CALIBRATION  
Calibration — measures — alignment between a model's predicted token probabilities and actual outcome frequencies (Week 7, Introduction to Model Evaluation)

TOKEN-BASED EVALUATION  
Token-based evaluation — uses — model log-probabilities to compare output preferences without explicit scoring prompts (Week 7, Introduction to Model Evaluation)

VALIDATION SET  
Validation set — evaluates — model checkpoints during training to guide hyperparameter selection (Week 7, Introduction to Model Evaluation)

ARGILLA  
Argilla — implements — human annotation workflows for preference labeling and model feedback collection (Week 7, LAB | Human-in-the-loop Evaluations)

DATA ENHANCING  
Data enhancing — extracts — structured information from unstructured dark data via LLM extraction pipelines (Week 7, LAB | Data Enhancing)

---

### A/B testing & statistics

A/B TESTING  
A/B testing — compares — two model or prompt variants on a shared population to measure differential impact (Week 7, Introduction to Model Evaluation + LAB | Statistical Analysis)

T-TEST  
t-test — tests — whether the means of two independent groups differ to a statistically significant degree (Week 7, LAB | Statistical Analysis)

FISHER'S EXACT TEST  
Fisher's exact test — tests — independence between two categorical variables under small-sample conditions (Week 7, LAB | Statistical Analysis)

MULTIPLE COMPARISONS CORRECTION  
Multiple comparisons correction — adjusts — significance thresholds to control false discovery rate across repeated tests (Week 7, LAB | Statistical Analysis)

POWER ANALYSIS  
Power analysis — determines — the minimum sample size required to detect a target effect at a given confidence level (Week 7, LAB | Statistical Analysis)

---

### Tooling

LANGSMITH  
LangSmith — traces — LLM and agent execution chains for debugging and experiment comparison (Week 7, LAB | LangSmith + A/B Testing & KPI (Notebooks))  
LangSmith — tracks — evaluation datasets and experiment run history over time (Week 7, same)  
LangSmith — enables — red-team tracing and bias detection across adversarial prompt runs (Week 8, LAB | Red-Teaming for Bias: Adversarial Prompts and LangSmith)  
LangSmith — enables — production monitoring of live agent execution and latency distributions (Week 7, same)  
LangSmith — preferred-when — reproducible experiment comparison across prompt variants or pipeline configurations is required (Week 7, same)

OPENEVALS  
OpenEvals — provides — an open harness for running standardized, reproducible LLM evaluation experiments (Week 7, A/B Testing & KPI (Notebooks))  
OpenEvals — implements — a unified evaluation interface compatible with multiple judges and scoring rubrics (Week 7, same)

STATISTICS SIMULATION NOTEBOOK  
Statistics simulation notebook — implements — A/B testing and significance calculation workflows programmatically (Week 7, A/B Testing & KPI (Notebooks))

---

### BI & business impact

POWER BI  
Power BI — visualizes — business metrics and model evaluation results in interactive, shareable dashboards (Week 7, Data Visualization & Reporting Tools)

TABLEAU  
Tableau — visualizes — data distributions and KPI trends for stakeholder reporting (Week 7, Data Visualization & Reporting Tools)

KPI  
KPI — quantifies — a specific business outcome used to measure AI system value delivery (Week 7, Business Impact)

BUSINESS IMPACT  
Business impact — translates — model performance metrics into ROI and strategic value for executive stakeholders (Week 7, Business Impact)

EVALUATION DASHBOARD  
Evaluation dashboard — surfaces — model performance distributions and variant comparison charts for decision-makers (Week 7, LAB | Evaluation Dashboard)

PROJECT 5 — STRATEGIC AI PITCH (CHLEO SCENARIO)  
Sector research — grounds — a strategic AI deployment pitch for CEO-level stakeholders (Week 7, Project 5 Brief)  
Transparency narrative — communicates — AI system accountability and compliance stance to non-technical audiences (Week 7, same)

---

## Week 8 — Green tech, EU AI Act, GDPR, final project kickoff

### Green software & sustainable AI

GREEN SOFTWARE FOUNDATION (GSF)  
Green Software Foundation — defines — principles and measurement standards for environmentally sustainable software (Week 8, Green Software & Sustainable AI)

SOFTWARE CARBON INTENSITY (SCI)  
SCI — measures — a software system's carbon emissions per unit of functional output (Week 8, Green Software & Sustainable AI)  
SCI — guides — architectural optimization toward lower-carbon, energy-efficient designs (Week 8, same)

CARBON EFFICIENCY  
Carbon efficiency — minimizes — CO₂ emitted per unit of work performed by software (Week 8, Green Software & Sustainable AI)

ENERGY EFFICIENCY  
Energy efficiency — minimizes — electricity consumed per unit of computation (Week 8, Green Software & Sustainable AI)

HARDWARE EFFICIENCY  
Hardware efficiency — maximizes — utilization of physical compute resources to reduce embodied carbon waste (Week 8, Green Software & Sustainable AI)

PUE (POWER USAGE EFFECTIVENESS)  
PUE — measures — total datacenter power consumed divided by IT equipment power, with 1.0 being perfect efficiency (Week 8, LAB | Public Sustainability Scan for Your Stack)  
PUE — used-by — datacenter sustainability assessments to compare provider energy efficiency (Week 8, same)  
PUE — see-also — Datacenter sustainability, SCI, Carbon efficiency

SCOPE 1 EMISSIONS  
Scope 1 emissions — covers — direct greenhouse gas emissions from sources owned or controlled by the organization (Week 8, Green Software & Sustainable AI)  
Scope 1 emissions — see-also — Scope 2 emissions, Scope 3 emissions, GHG Protocol Framework

SCOPE 2 EMISSIONS  
Scope 2 emissions — covers — indirect emissions from purchased electricity used by the organization's compute infrastructure (Week 8, Green Software & Sustainable AI)  
Scope 2 emissions — see-also — Scope 1 emissions, Scope 3 emissions, GHG Protocol Framework

SCOPE 3 EMISSIONS  
Scope 3 emissions — covers — indirect upstream and downstream emissions including supply chain and cloud provider embodied carbon (Week 8, Green Software & Sustainable AI)  
Scope 3 emissions — see-also — Scope 1 emissions, Scope 2 emissions, GHG Protocol Framework

GHG PROTOCOL FRAMEWORK  
GHG Protocol Framework — composed-of — Scope 1, Scope 2, and Scope 3 emission categories (Week 8, Green Software & Sustainable AI)  
GHG Protocol Framework — used-by — software organizations to account for total AI infrastructure carbon footprint (Week 8, same)

CARBON OFFSETTING  
Carbon offsetting — compensates — residual emissions by purchasing credits representing verified CO₂ reductions elsewhere (Week 8, Green Software & Sustainable AI)  
Carbon offsetting — contrasts-with — carbon efficiency: offsetting addresses residual emissions; efficiency reduces emissions at source (Week 8, same)

DATACENTER SUSTAINABILITY  
Datacenter sustainability — measures — cloud provider carbon commitments, PUE, and renewable energy sourcing (Week 8, LAB | Public Sustainability Scan for Your Stack)

---

### EU AI Act

AI SYSTEM (EU AI ACT)  
AI system — defined-as — a machine-based system designed to operate with varying degrees of autonomy, making predictions, recommendations, or decisions for explicit or implicit objectives (Week 8, EU AI Act for Consultants)  
AI system definition — scopes — the EU AI Act's applicability to a given product or service (Week 8, same)  
AI system — see-also — EU AI Act, High-risk AI obligations, GPAI, Prohibited practices

EU AI ACT  
EU AI Act — regulates — AI systems deployed or placed on the EU market across all risk tiers (Week 8, EU AI Act for Consultants)  
EU AI Act — classifies — AI systems as unacceptable, high-risk, limited-risk, or minimal-risk (Week 8, same)  
EU AI Act — see-also — High-risk AI obligations, GPAI, Prohibited practices, Conformity assessment, Transparency obligations

HIGH-RISK AI OBLIGATIONS  
High-risk AI obligations — require — conformity assessment, logging, transparency, and human oversight before deployment (Week 8, EU AI Act for Consultants)

CONFORMITY ASSESSMENT  
Conformity assessment — certifies — that a high-risk AI system satisfies EU AI Act technical and governance requirements (Week 8, EU AI Act for Consultants)  
Conformity assessment — required-when — a system is classified as high-risk under Annex III of the EU AI Act (Week 8, same)

GPAI (GENERAL-PURPOSE AI)  
GPAI — specializes — foundation-model regulatory tier introduced by the EU AI Act (Week 8, EU AI Act for Consultants)  
GPAI — subject-to — systemic risk provisions for models exceeding 10²⁵ training FLOPs (Week 8, same)

PROHIBITED PRACTICES (ARTICLE 5)  
Prohibited practices — enumerate — AI uses banned by the EU AI Act including social scoring and subliminal manipulation (Week 8, EU AI Act for Consultants)

TRANSPARENCY OBLIGATIONS (EU AI ACT)  
Transparency obligations — require — disclosure when end users interact with AI systems or AI-generated content (Week 8, EU AI Act for Consultants)

DEPLOYER VS PROVIDER (EU AI ACT)  
AI provider — bears — conformity and technical-documentation obligations for systems placed on the market (Week 8, EU AI Act for Consultants)  
AI deployer — bears — operational compliance obligations for high-risk AI systems in use (Week 8, same)

FUNDAMENTAL RIGHTS IMPACT ASSESSMENT (FRIA)  
FRIA — required-when — a high-risk AI system is deployed in areas that may adversely affect fundamental rights of individuals (Week 8, EU AI Act for Consultants)  
FRIA — contrasts-with — DPIA: DPIA focuses on data protection risks; FRIA covers broader fundamental rights (Week 8, same)  
FRIA — produces — a documented assessment of affected rights, harm likelihood, and mitigation measures (Week 8, same)

POST-MARKET MONITORING  
Post-market monitoring — obligates — AI providers to continuously track performance, incidents, and near-misses of deployed high-risk AI systems (Week 8, EU AI Act for Consultants)  
Post-market monitoring — produces — serious incident reports submitted to competent national authorities (Week 8, same)  
Post-market monitoring — see-also — Conformity assessment, AI system (EU AI Act), Notifying authority

NOTIFYING AUTHORITY  
Notifying authority — designates — the national body responsible for assessing and authorizing conformity assessment bodies under the EU AI Act (Week 8, EU AI Act for Consultants)  
Notifying authority — enforces — market surveillance and post-market monitoring obligations in each EU member state (Week 8, same)

MODEL CARD  
Model card — documents — a model's intended use, training data sources, performance characteristics, limitations, and known biases (Week 8, EU AI Act for Consultants)  
Model card — implements — the transparency obligation for AI providers to communicate model properties to deployers and users (Week 8, same)  
Model card — see-also — Transparency obligations (EU AI Act), Conformity assessment, LLM-as-judge

RED TEAMING  
Red teaming — probes — model outputs for harmful, biased, or policy-violating behavior via adversarial scenarios (Week 8, LAB | Red-Teaming for Bias: Adversarial Prompts and LangSmith)

ADVERSARIAL PROMPTS  
Adversarial prompts — craft — inputs designed to bypass safety filters or elicit disallowed model outputs (Week 8, LAB | Red-Teaming for Bias: Adversarial Prompts and LangSmith)

---

### GDPR & EU privacy stack

GDPR  
GDPR — governs — the collection, processing, and transfer of personal data in the EU (Week 8, GDPR & EU Data / Privacy Stack)  
GDPR — grants — data subjects rights of access, rectification, erasure, portability, and objection (Week 8, same)  
GDPR — see-also — DPIA, Privacy by design, Layered compliance model, Data Act, ePrivacy Directive

DATA PROTECTION IMPACT ASSESSMENT (DPIA)  
DPIA — required-when — processing is likely to result in high risk to data subjects' rights and freedoms (Week 8, GDPR & EU Data / Privacy Stack)  
DPIA — documents — processing purposes, necessity, proportionality, and residual risk mitigation (Week 8, same)  
DPIA — fails-when — the risk assessment is not updated after material changes to processing scope or technology (Week 8, same)

LAWFUL BASIS (ARTICLE 6)  
Lawful basis — justifies — each personal data processing activity under GDPR Article 6 (Week 8, GDPR & EU Data / Privacy Stack)  
Lawful basis — covers — consent, contract, legal obligation, vital interests, public task, and legitimate interests (Week 8, same)

SPECIAL CATEGORY DATA (ARTICLE 9)  
Special category data — requires — explicit consent or a specific listed exception for lawful processing (Week 8, GDPR & EU Data / Privacy Stack)  
Special category data — includes — health, biometric, genetic, racial/ethnic, political, and religious data (Week 8, same)

DATA CONTROLLER  
Data controller — determines — the purposes and means of personal data processing (Week 8, GDPR & EU Data / Privacy Stack)  
Data controller — bears — primary accountability obligations under GDPR (Week 8, same)

DATA PROCESSOR  
Data processor — processes — personal data solely under instructions from the controller (Week 8, GDPR & EU Data / Privacy Stack)  
Data processor — required-to — sign a data processing agreement with the controller (Week 8, same)

PRIVACY BY DESIGN  
Privacy by design — embeds — data protection measures into system architecture from inception rather than as an afterthought (Week 8, GDPR & EU Data / Privacy Stack)

LAYERED COMPLIANCE MODEL  
Layered compliance model — stacks — GDPR obligations with sector-specific laws and AI Act requirements (Week 8, Applying the EU Data and Privacy Stack)

DATA ACT (EU)  
Data Act — governs — rights of access to and portability of data generated by IoT devices (Week 8, Applying the EU Data and Privacy Stack)

EPRIVACY DIRECTIVE  
ePrivacy Directive — governs — electronic communications metadata and browser cookie consent rules (Week 8, Applying the EU Data and Privacy Stack)

---

### Final project kickoff

FINAL PROJECT BRIEF  
Final project — requires — a strategic deployment plan, compliance pack, and low-code POC (Week 8–9, Final Project Brief)

STRATEGIC DEPLOYMENT PLAN  
Strategic deployment plan — documents — phased rollout timeline, success metrics, and risk mitigation steps (Week 8–9, Final Project Brief)

RISK MATRIX  
Risk matrix — classifies — identified AI risks by likelihood and impact for regulatory and stakeholder reporting (Week 8–9, Final Project Brief)

---

## Week 9 — Final project delivery

COMPLIANCE PACK  
Compliance pack — bundles — EU AI Act conformity evidence and GDPR documentation for the deployed system (Week 9, Final Project Deliverables)  
Compliance pack — demonstrates — regulatory adherence to simulated client stakeholders (Week 9, same)

LOW-CODE POC  
Low-code POC — demonstrates — solution feasibility using n8n, Make, Zapier, or Copilot Studio without full production code (Week 9, Final Project Deliverables)

PROOF OF CONCEPT (POC)  
POC — validates — that a proposed technical solution can achieve the core functional requirement before full investment (Week 9, Final Project Deliverables)  
POC — contrasts-with — production system: a POC proves feasibility; a production system meets scalability, security, and reliability standards (Week 9, same)  
POC — preferred-when — stakeholders require evidence of feasibility before committing budget to full development (Week 9, same)

EXECUTIVE SUMMARY  
Executive summary — communicates — the project's business problem, proposed solution, key risks, and recommended next steps to senior decision-makers (Week 9, Final Project Deliverables)  
Executive summary — composed-of — business context, AI system description, compliance stance, and cost-benefit framing (Week 9, same)

CLIENT PRESENTATION  
Client presentation — communicates — AI system value, compliance stance, and deployment plan to simulated executive stakeholders (Week 9, Final Project Deliverables)

HANDOVER DOCUMENTATION  
Handover documentation — transfers — system architecture, configuration decisions, operational runbooks, and known issues to the client or operations team (Week 9, Final Project Deliverables)  
Handover documentation — includes — API key management procedures, environment variable references, and escalation contacts (Week 9, same)

STAKEHOLDER SIGN-OFF  
Stakeholder sign-off — gates — project delivery by requiring formal approval from accountable decision-makers before a phase closes or a system goes live (Week 9, Final Project Deliverables)  
Stakeholder sign-off — documented-via — signed acceptance criteria, meeting minutes, or digital approval records (Week 9, same)  
Stakeholder sign-off — see-also — Definition of Done, Acceptance criteria, Compliance pack

---

## Providers & Organisations

*Entries model each provider as a first-class node with offerings, differentiation, and decision-relevant contrasts. Providers whose primary identity is a course tool (Pinecone, LangChain, n8n) are documented under their respective week entries above.*

OPENAI  
OpenAI — offers — GPT-4o, GPT-4.1, o3, Whisper, TTS, DALL-E, and text-embedding-3 models via API (Week 1–4, Generative AI + LangChain Integration)  
OpenAI — known-for — leading chat completions API, developer ecosystem, and function calling support (Week 1, Generative AI)  
OpenAI — contrasts-with — Anthropic on safety emphasis, model transparency, and Constitutional AI methodology (Week 2, API and Integration Patterns Fundamentals)  
OpenAI — billed-by — input and output tokens separately, with prompt caching discounts for repeated prefixes (Week 2–3, same)

ANTHROPIC  
Anthropic — offers — Claude 3.5 Sonnet, Claude 3 Opus, and Haiku via API and Claude.ai interface (Week 2, API and Integration Patterns Fundamentals)  
Anthropic — known-for — Constitutional AI training methodology and safety-focused model development (Week 2, same)  
Anthropic — contrasts-with — OpenAI on open research publication and emphasis on model interpretability (Week 2, same)  
Anthropic — billed-by — input and output tokens with extended context window pricing tiers (Week 2, same)

GOOGLE  
Google — offers — Gemini model family (Gemini 1.5 Pro, Flash) via Vertex AI and Google AI Studio (Week 2, API and Integration Patterns Fundamentals)  
Google — known-for — multimodal capability, long context windows, and enterprise data residency via Vertex AI (Week 2, same)  
Google — contrasts-with — OpenAI on ecosystem lock-in: Vertex AI integrates with Google Cloud; OpenAI targets cross-cloud API consumers (Week 6, LAB | Scoping Lab)

COHERE  
Cohere — offers — Command R+ generation models, Embed API, and Rerank API (Week 3, LangChain Integration + LAB | Relevance Scoring and Rerankers)  
Cohere — known-for — enterprise-grade multilingual embeddings and dedicated reranking endpoint (Week 3, same)  
Cohere — preferred-when — retrieval quality and reranking precision are the primary use case and multilinguality is required (Week 3, same)

HUGGING FACE  
Hugging Face — offers — model hub, serverless Inference API, Datasets library, and Spaces for demo hosting (Week 1, LAB | API Calling to ChatGPT)  
Hugging Face — known-for — open-source model hosting, fine-tuning pipelines, and community benchmark leaderboards (Week 1, Neural Networks Fundamentals)  
Hugging Face — contrasts-with — OpenAI on open-access model distribution vs. API-only closed model access (Week 1, same)

ELEVENLABS  
ElevenLabs — offers — voice cloning, multilingual TTS, and voice design API with speaker-customizable models (Week 2, Project 1 Kickoff)  
ElevenLabs — known-for — highest-quality neural TTS with voice cloning and emotional prosody control (Week 2, same)  
ElevenLabs — contrasts-with — OpenAI TTS on voice variety and cloning capability vs. simplicity and lower latency (Week 2, same)
