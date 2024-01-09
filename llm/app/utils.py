import requests
from langchain.llms import CTransformers
from langchain.vectorstores import OpenSearchVectorSearch
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


qa_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_qa_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=qa_template,
                            input_variables=['context', 'question'])
    return prompt


def get_embeddings(text):
    url = 'http://vectorizer:80/embeddings'
    myobj = {"text":text}
    x = requests.post(url, json = myobj)
    return x.json()['emb_vector']

class embedding_class:
    def __init__(self):
        self.embed_query = get_embeddings


def get_docsearch(os_url):
    embedding_func = embedding_class()
    docsearch = OpenSearchVectorSearch(
        index_name="article_index",
        embedding_function=embedding_func,
        opensearch_url=os_url,
        use_ssl = True,
        verify_certs = False,
    )
    return docsearch

def llm(config):
    llm_mistral = CTransformers(
        model='./models/mistral-7b-instruct-v0.1.Q5_K_M.gguf',
        model_type='mistral',
        config=config
    )
    return llm_mistral


def get_qa_chain(opensearch_url, llm_config):
    qa_prompt = set_qa_prompt()
    llm_model = llm(llm_config)
    docsearch = get_docsearch(opensearch_url)
    qa_chain = RetrievalQA.from_chain_type(
        llm_model, 
        chain_type="stuff", 
        retriever=docsearch.as_retriever(search_kwargs={'k': 3}),
        chain_type_kwargs={'prompt': qa_prompt}
    )
    return qa_chain