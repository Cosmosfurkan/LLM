with open("LLM.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=400,
    length_function=len,
    is_separator_regex=False
)
texts = text_splitter.create_documents([transcript])

print(f"total Number of Chunks Created => {len(texts)}")
print(f"First Chunk => {len(texts[0].page_content)} characters")
print(f"Last Chunk => {len(texts[-1].page_content)} characters")