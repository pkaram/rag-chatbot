# LLM

LLM model to be used for question answering with langchain using Opensearch as vector database.

1.  Build image from Dockerfile

```
docker build -t llm:rag .
```

2. Create container from image

```
docker run -p 8080:8080 llm:rag
```

3. Make a question on the available documents

```
curl -X POST "http://localhost:8080/qa_chain" -H "Content-Type: application/json" -d '{"text":"What are the future plans of NASA?"}'
```