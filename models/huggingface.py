import requests

HF_API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
HF_TOKEN = "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"  # 🔑 Replace with your real Hugging Face token

def summarize_with_hf(text: str, max_length: int = 500, min_length: int = 50) -> str:
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "inputs": text,
        "parameters": {"max_length": max_length, "min_length": min_length, "do_sample": False}
    }
    response = requests.post(HF_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0 and "summary_text" in data[0]:
            return data[0]["summary_text"]
        elif isinstance(data, dict) and "summary_text" in data:
            return data["summary_text"]
        elif isinstance(data, dict) and "error" in data:
            return f"HuggingFace Error: {data['error']}"
        else:
            return "No summary generated (empty response)."
    else:
        return f"API Error: {response.status_code} {response.text}"
