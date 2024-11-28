# website/utils.py
import base64
from openai import OpenAI
from django.conf import settings

def process_image(image):
    image_data = image.read()
    base64_image = base64.b64encode(image_data).decode('utf-8')
    return base64_image

def get_openai_response(base64_image):
    client = OpenAI(api_key=settings.OPENAI_KEY)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "que hay en esta imagen?",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
    )
    return response.choices[0].message.content