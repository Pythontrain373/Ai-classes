import requests
from Config4 import HF_API_KEY
from huggingface_hub import InferenceClient
from PIL import Image
from datetime import datetime

MODELS = [

"ByteDance/SDXL-Lightning",

"stabilityai/stable-diffusion-xl-base-1.0",

"stabilityai/sdxl-turbo",

"runwayml/stable-diffusion-v1-5", # Fallback 2

]
client=InferenceClient(api_key=HF_API_KEY)
print(f"Primary model: {MODELS[0]}")
print("Type 'quit' to exit\n")
while True:
    prompt=input("Enter prompt: ").strip()
    if prompt.lower() in ["quit","exit","q"]:
        break
    if not prompt:
        continue
    print("Generating image...")
    image=None
    for model in MODELS:
        try:
            image=client.text_to_image(prompt, model=model)
            break
        except Exception:
            print(f".   Executing next...")
            continue
    
    if image:
        timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
        filename=f"generate_{timestamp}.png"
        print(f"Image saved as {filename}")
        image.show()
        print()
    else:
        print("Error: All models failed. Check your API key.\n")

print("Goodbye!")