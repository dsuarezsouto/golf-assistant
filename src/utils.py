import logging
import pathlib
from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document

def load_document(temp_filepath: str) -> list[Document]:
    SUP_EXTENSIONS = ['.pdf']
    ext = pathlib.Path(temp_filepath).suffix
    if ext not in SUP_EXTENSIONS:
        raise ValueError(
            f"Invalid extension type {ext}, cannot load this type of file"
        )

    loaded = PyPDFLoader(temp_filepath)
    docs = loaded.load()
    return docs
