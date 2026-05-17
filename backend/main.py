from scraping.scraper import fetch_html
from scraping.extractor import extract_content
from scraping.cleaner import clean_text
from scraping.utils import save_to_json

url = "https://example.com"

print("Fetching HTML...")
html = fetch_html(url)

if html:

    print("Extracting content...")
    data = extract_content(html)

    print("Cleaning content...")
    data["content"] = clean_text(data["content"])

    print("Saving JSON...")
    save_to_json(data)

    print("\nFINAL OUTPUT:\n")
    print(data)