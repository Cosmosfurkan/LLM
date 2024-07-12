with open("LLM.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

from langchain.text_splitter import TokenTextSplitter

text_splitter = TokenTextSplitter(
    chunk_size=1000,
    chunk_overlap=20,
    length_function = len
)

texts = text_splitter.create_documents(transcript)

from langchain.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/msmarco-bert-base-dot-v5"
)

text = texts[0].page_content
query_result = embedding.embed_query(text)