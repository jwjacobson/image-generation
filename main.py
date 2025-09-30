import io

from decouple import config
from PIL import Image
import requests

API_TOKEN = config("API_TOKEN")
API_URL = config("API_URL")

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def generate_image(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "guidance_scale": 10,
            "num_inference_steps": 30
        }
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        return image
    else:
        print(f"Error: {response.status_code}")
        return None

prompt = input("What image do you want? ")
image = generate_image(prompt)

if image:
    image.save("generated_image.png")
    print("Image saved.")