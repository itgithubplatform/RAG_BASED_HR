import os
import fitz
import hashlib
import requests

from pinecone import Pinecone ,ServerlessSpec
from dotenv import load_dotenv


load_dotenv()

# configure Pinecone
DATA_FOLDER = os.path.abspath("data/hr_policies")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "hr-policies-project")
EMBEDDING_MODEL = "nomic-embed-text"
EMBEDDING_DIM = 768  # nomic-embed-text produces 768-dimension embeddings


pc=Pinecone(api_key=PINECONE_API_KEY)


# check if index exists,  if not create or recereate with correct dimensions

