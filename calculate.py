import json

def count_phrases_in_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        total_phrases = 0

        for entry in data:
            phrase_count = len(entry.get("phrases", []))
            total_phrases += phrase_count
            print(f'Video: {entry.get("video", "Unknown")} — Phrases: {phrase_count}')

        print(f'\nTotal phrases across all entries: {total_phrases}')

    except Exception as e:
        print(f"Error reading or processing file: {e}")

count_phrases_in_json("dataset.json")
