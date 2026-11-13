import base64
from llm import client
img = base64.b64encode(open("test.jpg", "rb").read()).decode()
resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": [
        {"type": "text", "text": "Что на изображении? Кратко."},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img}"}},
    ]}],
)
print(resp.choices[0].message.content)