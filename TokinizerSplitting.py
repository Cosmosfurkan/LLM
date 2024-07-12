with open("LLM.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

from langchain.text_splitter import TokenTextSplitter
import tiktoken
tex_splitter = TokenTextSplitter(
    chunk_size=2000,
    chunk_overlap=400,
    length_function=len,
)
texts = tex_splitter.create_documents([transcript])

encoding = tiktoken.get_encoding("cl100k_base")

print(f"total Number of Chunks Created => {len(texts)}")
print(f"Totel number of tokens in the document => {len(encoding.encode(transcript))} tokens")
print(f"First Chunk => {len(encoding.encode(texts[0].page_content))} characters")
print(f"Last Chunk => {len(encoding.encode(texts[-1].page_content))} characters")