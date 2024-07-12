from langchain_community.document_loaders import YoutubeLoader

loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=zjkBMFhNj_g&t=9s",
    add_video_info=True
)
doc = loader.load()

# Transkript metnini alma
transcript = doc[0].page_content

# Transkript metnini bir txt dosyasına kaydetme
with open("LLM.txt", "w", encoding="utf-8") as file:
    file.write(transcript)

print("Transkript başarıyla kaydedildi.")