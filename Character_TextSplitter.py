with open("transcript.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size = 1000,
    chunk_overlap = 100,
    length_function = len,
    is_separator_regex=False
)
texts = text_splitter.create_documents(transcript)

print(texts[0])
print(texts[1])