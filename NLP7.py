import base64
import requests
import os

from Config4 import HF_API_KEY

API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

MODELS = [
    "Qwen/Qwen2.5-VL-32B-Instruct",
    "Qwen/Qwen2.5-VL-72B-Instruct",
    "zai-org/GLM-4.5V",
    "google/gemma-3-27b-it",
]

def data_url(image_bytes: bytes) -> str:
    return "data:image/jpeg;base64," + base64.b64encode(image_bytes).decode("utf-8")

def extract_error(response: requests.Response) -> str:
    try:
        return response.json().get("error", {}).get("message", response.text)
    except Exception:
        return response.text or "Unknown error"

def caption_image():
    image_path = input("Enter image filename (default: test.jpg): ").strip() or "test.jpg"

    try:
        with open(image_path, "rb") as f:
            image_bytes = f.read()
    except Exception as e:
        print("❌ File error:", e)
        return

    base_payload = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Return exactly ONE short caption in one sentence. Maximum 12 words. No options."
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": data_url(image_bytes)}
                    }
                ]
            }
        ],
        "max_tokens": 120,
        "temperature": 0.2,
        "top_p": 0.9
    }

    last_error = None

    for model in MODELS:
        payload = dict(base_payload)
        payload["model"] = model

        try:
            response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=120)
        except requests.RequestException as e:
            last_error = str(e)
            continue

        if response.status_code != 200:
            last_error = extract_error(response)
            continue

        try:
            data = response.json()
        except Exception:
            last_error = "Invalid JSON response"
            continue

        caption = (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
            .strip()
        )

        if caption:
            print("\n🎉 Caption Generated:")
            print("🖼️ Image:", image_path)
            print("📝 Caption:", caption)
            return

        last_error = "Empty response"

    print("\n❌ Caption Failed.")
    print("Error:", last_error or "Unknown error")

if __name__ == "__main__":
    caption_image()