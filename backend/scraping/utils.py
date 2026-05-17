import json


def save_to_json(data, filename="output.json"):
    """
    Saves scraped data to JSON file.
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"[INFO] Data saved to {filename}")