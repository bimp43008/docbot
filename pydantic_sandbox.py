import json
from pydantic import ValidationError
from schemas import VehicleContract


# 1. Валидное создание
c = VehicleContract(seller_name="Иванов И.И.", vehicle_year=2019, price=1850000)
print(c.seller_name, c.vehicle_year, type(c.vehicle_year))

# 2. Приведение типов: строки превращаются в числа
c2 = VehicleContract(seller_name="Петров П.П.", vehicle_year="2019", price="1850000")
print(c2.vehicle_year, type(c2.vehicle_year), type(c2.price))

# 3. Необязательное поле не передали
print(c.sign_date)

# 4. Забыли обязательное поле
try:
    VehicleContract(vehicle_year=2019, price=100)
except ValidationError as e:
    print("ОШИБКА:", e.errors()[0]["loc"], e.errors()[0]["msg"])

# 5. Мусор вместо числа
try:
    VehicleContract(seller_name="X", vehicle_year="не число", price=100)
except ValidationError as e:
    print("ОШИБКА:", e.errors()[0]["loc"], e.errors()[0]["msg"])

# 6. Объект наружу: dict и JSON-строка
print(c.model_dump())
print(c.model_dump_json())

# 7. Класс → JSON-схема (именно её мы потом покажем модели)
print(json.dumps(VehicleContract.model_json_schema(), ensure_ascii=False, indent=2))

# 8. JSON-строка внутрь: хорошая и плохая
good = '{"seller_name": "Сидоров С.С.", "vehicle_year": 2020, "price": 500000}'
print(VehicleContract.model_validate_json(good))

bad = '{"seller_name": "X", "vehicle_year": "abc", "price": 500000}'
try:
    VehicleContract.model_validate_json(bad)
except ValidationError as e:
    print("ОШИБКА:", e.errors()[0]["loc"], e.errors()[0]["msg"])