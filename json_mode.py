import json
from pydantic import ValidationError
from llm import client
from schemas import VehicleContract

CONTRACT = """
ДОГОВОР КУПЛИ-ПРОДАЖИ ТРАНСПОРТНОГО СРЕДСТВА № 17
г. Казань, 02 ноября 2026 года
Продавец: Смирнов Алексей Игоревич
Покупатель: Кузнецова Мария Дмитриевна
Транспортное средство: марка Toyota, модель Camry, год выпуска 2019,
VIN XW7BF4FKX0S123456, цвет белый.
Цена продажи: 1 850 000 (один миллион восемьсот пятьдесят тысяч) рублей.
Подписи сторон: 02.11.2026.
"""

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "Ти извлекаешь данные из документов. Отвечай только валидным JSON."},
        {"role": "user", "content": f"Извлеки продавца, год выпуска, и дату подписания. Верни JSON.\n{CONTRACT}"}
    ],
    response_format={"type": "json_object"},
    temperature=0,
)

raw = resp.choices[0].message.content
print("RAW:", raw)

data = json.loads(raw)
print("DICT:", data)

try:
    obj = VehicleContract.model_validate_json(raw)
    print("OBJ:", obj)
except ValidationError as e:
    print("СХЕМА НЕ СОШЛАСЬ:", e.errors())