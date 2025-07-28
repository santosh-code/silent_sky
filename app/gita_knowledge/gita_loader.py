import json
from langchain.schema import Document

def load_gita_documents(json_path: str) -> list[Document]:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []
    for chapter in data.get("chapters", []):
        chapter_num = chapter["number"]
        for shloka in chapter.get("shlokas", []):
            full_text = (
                f"Chapter {chapter_num}, Shloka {shloka['shloka_number']}\n"
                f"Sanskrit: {shloka.get('sanskrit_text', '')}\n"
                f"Meaning: {shloka.get('meaning', '')}\n"
                f"Interpretation: {shloka.get('interpretation', '')}\n"
                f"Application: {shloka.get('life_application', '')}"
            )
            documents.append(Document(
                page_content=full_text,
                metadata={
                    "chapter": chapter_num,
                    "shloka_number": shloka["shloka_number"],
                    "keywords": shloka.get("keywords", [])
                }
            ))

    return documents

# 🧪 TEST (you can comment this out after testing)
if __name__ == "__main__":
    docs = load_gita_documents("C:/Users/Square/Desktop/archive (4)/complete_Bhagavad_Gita.json")
    print("✅ Loaded shlokas:", len(docs))
    print("🔹 Sample:", docs[0].page_content)
