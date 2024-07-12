import requests
from bs4 import BeautifulSoup

url = "https://generativeai.pub/what-is-a-fine-tuned-llm-67bf0b5df081"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Web sayfasındaki tüm paragrafları çekmek için
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        print(para.get_text())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
