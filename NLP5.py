from Config5 import HF_API_KEY
import time
import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO



MODELS = [
    "black-forest-labs/FLUX.1-dev",
    "stabilityai/stable-diffusion-xl-base-1.0",
]

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Accept": "image/png"
}


def generate_image_from_text(prompt):
    API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Accept": "image/png",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    while response.status_code == 503:
        print("Model loading... waiting...")
        time.sleep(5)
        response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(response.text)

    image = Image.open(BytesIO(response.content))
    return image
    raise Exception("All models failed")


def post_process_image(image):
    image = ImageEnhance.Brightness(image).enhance(1.2)
    image = ImageEnhance.Contrast(image).enhance(1.3)
    image = image.filter(ImageFilter.GaussianBlur(radius=2))
    return image


def main():
    print("Welcome to the Post-Processing Magic Workshop!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter description:\n")

        if user_input.lower() == "exit":
            break

        try:
            print("Generating image...")
            image = generate_image_from_text(user_input)

            print("Applying effects...")
            processed = post_process_image(image)

            processed.show()

            save = input("Save image? (yes/no): ")

            if save.lower() == "yes":
                name = input("File name: ")
                processed.save(f"{name}.png")
                print("Saved successfully!")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()    