from flask import Flask ,render_template , jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI, ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os 
from langchain_community.chat_models import ChatOpenRouter



app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = "pcsk_tcVhe_UNxCvkWUa1d5fTpKNjqp5aq7FtRC62y44Ek3Rs53wJxN2WeborV6PaSm8vVd44S"
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

OPENAI_API_KEY = "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"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"


embeddings = download_hugging_face_embeddings()

index_name = "medicalchatbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriver = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 5})


llm = ChatOpenAI(
    model="deepseek/deepseek-r1-0528:free",  
    base_url="https://openrouter.ai/api/v1",  
    api_key=os.environ["OPENAI_API_KEY"],
    temperature=0.4 ,
    max_tokens= 500,
     openai_api_key=os.environ["OPENAI_API_KEY"],
    openai_api_base=os.environ["OPENAI_API_BASE"],
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriver, question_answer_chain)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get" ,methods=["GET","POST"])
def chat():
    message = request.form["msg"]
    input = message
    print(input)
    response = rag_chain.invoke({"input": message})
    print("Response :" , response["answer"])
    return str(response["answer"])