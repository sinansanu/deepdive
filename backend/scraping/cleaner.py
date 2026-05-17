import re


def clean_text(text):
    """
    Cleans extracted webpage text.
    """

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)

    # Remove strange characters
    text = re.sub(r'[^a-zA-Z0-9\s.,!?()-]', '', text)

    return text.strip()