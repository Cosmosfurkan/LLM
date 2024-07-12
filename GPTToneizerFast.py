with open("LLM.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

from transformers import GPT2TokenizerFast
from langchain.text_splitter import RecursiveCharacterTextSplitter

tokanizer = GPT2TokenizerFast.from_pretrained("gpt2")
text_splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
    tokanizer,
    chunk_size=100,
    chunk_overlap=0
)
texts = text_splitter.split_text(transcript)

print(texts[0])
print(texts[1])