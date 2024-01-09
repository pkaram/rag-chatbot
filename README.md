# rag-chatbot

This is a Retrieval Augmented Generation Chatbot with Mistral and Opensearch. It consists of:

* A vector database where documents are stored (Opensearch).
* A vector generation service built with FastAPI, which produces a vector from given text. 
* An llm service, where user can ask questions over the available documents. We use an open source model, called Mistral, which can be replace either by other open-source or paid solutions.


1. [Download mistral model](llm/models/download_file_instructions.txt)

2. Run the services 
```
docker-compose up -d
```

3. [Follow instructions](index_documents.ipynb) to create an opensearch index and store some documents.

4. Make questions on the documents 

```
curl -X POST "http://localhost:8080/qa_chain" -H "Content-Type: application/json" -d '{"text":"What are the future plans of NASA?"}'
```