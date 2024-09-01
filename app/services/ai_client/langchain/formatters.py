import json
from typing import List

from langchain_core.documents import Document


def default_retriever_formatter(docs: List[Document]) -> str:
    formatted_docs = []
    for doc in docs:
        formatted_doc = f"Content: {doc.page_content}\n"
        formatted_doc += f"Metadata: {json.dumps(doc.metadata, indent=2)}"
        formatted_docs.append(formatted_doc)
    return "\n\n---\n\n".join(formatted_docs)
