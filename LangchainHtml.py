from langchain.text_splitter import HTMLHeaderTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

url = "https://medium.com/@abhinavkimothi/context-is-key-the-significance-of-rag-in-language-models-29a7e8610843"

header_split = [
    ('h1', 'Header 1'),
    ('h2', 'Header 2'),
    ('h3', 'Header 3'),
    ('h4', 'Header 4')
]

html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=header_split)

html_header_Split = html_splitter.split_text(url)

chunk_size = 5000
chunk_overlap = 300

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

#split 
texts = text_splitter.split_documents(html_header_Split)
len(texts)