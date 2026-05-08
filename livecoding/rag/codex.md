Overview of our goal:

 Create a RAG that is capable of answering questions about a sport in an accurate and accessible manner for beginners.


Target pdf: 20171026174027.pdf (ONLY this pdf)
Coding style: native to langchain principles, beginner friendly code with explanations

Steps

1. Imports

details:
 Import our .env file with load_dot_env
 Use langchain 1.0 and compatilble libraries (langchain_openai, langchain_pinecone)
 We will process a pdf (library to be decided)


2. Process the PDF


 - Keep each section together (no chunking) [PARTIAL]
 - exclude: tables, lists, footnotes, empty pages, anything that would need OCR [DONE]


[MISSING]
 - Sections are defined by the number  (i.e 1. Governing Rules), the document has a structure that migth be able to be explored to do this automatically (idents for subsections)
 - Metadata should contain: name, page, section, section name, previous section_id, foward_section_id
 -For the images in the pdf, call open ai to provide a detail description of the image and embbed that description. Add the image to the metadata (raw image path)
- normalize the metadata 

3. Embbed the chunk 
- embbed small from openai [DONE]

4. Upsert them in pinecone
- index_name = 'sports_rules'[DONE]
- existing pinecone index [DONE]

5. Build a retriever in langchain 
 
- Langchain_pinecone
- Add the retriever as tool for the agent (langchain_pinecone)
- retriever should return image and text 

6. Test it
- manual process 

Technological stack

- dotenv
- langchain
- pinecone
- openai