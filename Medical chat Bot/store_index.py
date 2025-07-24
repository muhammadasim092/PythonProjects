from src.helper import load_pdf ,text_split , download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os 


load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY


extracted_data = load_pdf(data='Data/')
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


from pinecone.grpc import PineconeGRPC as pinecone
from pinecone import ServerlessSpec

pc = pinecone(api_key=PINECONE_API_KEY)

index_name = "medicaltestbot"

if index_name not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=384,  # this must match your embedding output dim
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )


docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    index_name=index_name
)