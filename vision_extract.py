import base64
from pathlib import Path
from extract import extract
from schemas import VehicleContract

img = base64.b64encode(Path(__file__).parent.joinpath("contract.jpg").read_bytes()).decode()

if __name__ == "__main__":
    content = [
        {"type": "text", "text": "Извлеки данные из договра на изображении."},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img}"}},
    ]
    data = extract(content, VehicleContract)
    print(data)
    print(data.model_dump_json(indent=2))
