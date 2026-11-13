from extract import extract
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

if __name__ == "__main__":
    data = extract(f"Извлеки данные из договра:\n{CONTRACT}", VehicleContract)
    print(data)
    print(data.model_dump_json(indent=2))
    print(data.price, type(data.price))