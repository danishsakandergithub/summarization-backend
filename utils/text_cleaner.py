import re

def clean_text(text: str) -> str:
    text = re.sub(r"<[^>]*>|&[^;]+;", " ", text)  # remove HTML tags/entities
    text = re.sub(r"\s+", " ", text)  # normalize spaces
    return text.strip()
