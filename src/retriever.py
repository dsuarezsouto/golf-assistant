"""Chat with retrieval and embeddings."""
import logging
import os

from langchain.chains import ConversationalRetrievalChain

from langchain.chains.base import Chain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import EmbeddingsFilter
from langchain.schema import BaseRetriever, Document
from langchain.vectorstores import Qdrant
from langchain.memory import ConversationBufferMemory

from utils import load_document
from config import set_environment

logging.basicConfig(encoding="utf-8", level=logging.INFO)
LOGGER = logging.getLogger()
set_environment()

LLM = ChatOpenAI(
    model_name="gpt-3.5-turbo", temperature=0, streaming=True
)

EMBEDDINGS = OpenAIEmbeddings()

MEMORY = ConversationBufferMemory(
    memory_key='chat_history',return_messages=True,output_key='answer'
)

def configure_retriever(
        docs: list[Document],
) -> BaseRetriever:
    """Retriever to use."""

    
    qdrant = Qdrant.from_documents(
        docs,
        EMBEDDINGS,
        location=":memory:",  # Local mode with in-memory storage only
        collection_name="golf_manuals",
    )
    
    retriever = qdrant.as_retriever(
        search_type="mmr", search_kwargs={
            "k": 5,
            "fetch_k": 7
        },
    )

    embeddings_filter = EmbeddingsFilter(
        embeddings=EMBEDDINGS, similarity_threshold=0.6
    )

    # Contextual compression allow us to pass to LLM just relevant documents related to the query
    # TODO: Should be filtered also the content inside the documents?
    return ContextualCompressionRetriever(
        base_compressor=embeddings_filter,
        base_retriever=retriever,
    )


def configure_chain(retriever: BaseRetriever) -> Chain:
    """Configure chain with a retriever.

    Passing in a max_tokens_limit amount automatically
    truncates the tokens when prompting your llm!
    """
    params = dict(
        llm=LLM,
        retriever=retriever,
        verbose=True,
        max_tokens_limit=4000,
        memory= MEMORY
    )
    return ConversationalRetrievalChain.from_llm(
        **params
    )

def configure_retrieval_chain() -> Chain:
    
    """Read documents, configure retriever, and the chain."""
    docs = []
    files_dir_path = os.path.join(os.path.dirname(__file__),'golf_manuals')
    filenames = os.listdir(files_dir_path)
    logging.info(f'Loading these documents: {filenames}')
    for file in filenames:
        filepath = os.path.join(files_dir_path, file)
        docs.extend(load_document(filepath))

    retriever = configure_retriever(docs=docs)
    chain = configure_chain(retriever=retriever)
    return chain