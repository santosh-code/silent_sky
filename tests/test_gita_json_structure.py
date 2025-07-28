import json

# 🔄 Load your full JSON file
with open("C:/Users/Square/Desktop/archive (4)/complete_Bhagavad_Gita.json", "r", encoding="utf-8") as f:
    gita_data = json.load(f)

# ✅ Check basic keys
print("✅ Keys present in root:", list(gita_data.keys()))

# ✅ Check number of chapters and one chapter summary
chapters = gita_data.get("chapters", [])
print(f"📖 Total Chapters: {len(chapters)}")

if chapters:
    print("\n🧩 First Chapter Info:")
    print("Name:", chapters[0]["name"])
    print("Summary:", chapters[0]["summary"])
    print("Total shlokas:", len(chapters[0].get("shlokas", [])))

    print("\n🧾 Sample Shloka:")
    first_shloka = chapters[0]["shlokas"][0]
    print("Chapter:", first_shloka["chapter"])
    print("Shloka Number:", first_shloka["shloka_number"])
    print("Meaning:", first_shloka["meaning"])
    print("Keywords:", first_shloka.get("keywords", []))

# ✅ Check emotion mapping
problem_map = gita_data.get("problem_solutions_map", {})
print(f"\n🧠 Emotion categories found: {list(problem_map.keys())[:5]} ...")

if "anger" in problem_map:
    print("\n🔥 Anger references:")
    for ref in problem_map["anger"]["references"]:
        print(f"- Chapter {ref['chapter']} → Shloka {ref['shloka']}")
