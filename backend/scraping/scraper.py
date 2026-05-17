import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def fetch_html(url):
    """
    Downloads raw HTML from a webpage.
    """

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        response.raise_for_status()

        return response.text

    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch page: {e}")

        return None