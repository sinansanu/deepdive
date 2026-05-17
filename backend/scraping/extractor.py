from bs4 import BeautifulSoup


def extract_content(html):
    # Extracts title and paragraph text from HTML.

    soup = BeautifulSoup(html, "lxml")

    title = soup.title.string if soup.title else "No Title"

    paragraphs = soup.find_all("p")

    content = ""

    for p in paragraphs:
        content += p.get_text() + "\n"

    return {
        "title": title,
        "content": content
    }