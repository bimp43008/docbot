from extract import extract
from schemas import VehicleContract
from db import init_db, save_extraction, list_recent
from cache import get_answer, set_answer, rate_limit
from rag_answer import rag_answer

CONTRACT = """ДОГОВОР КУПЛИ-ПРОДАЖИ ТС № 17
г. Казань, 02 ноября 2026 года
Продавец: Смирнов Алексей Игоревич
Покупатель: Кузнецова Мария Дмитриевна
Авто: Toyota Camry 2019, VIN XW7BF4FKX0S123456.
Цена: 1 850 000 рублей. Дата: 02.11.2026."""

init_db()
data = extract(f"Извлеки данные:\n{CONTRACT}", VehicleContract)
new_id = save_extraction("contract_car.txt", "vehicle", data)
print("saved id:", new_id)
print("recent:", list_recent(3))

q = "Кто продал автомобиль и почём?"
if not rate_limit("user1"):
    print("rate limited")
else:
    cached = get_answer(q)
    if cached:
        print("CACHE HIT:", cached)
    else:
        ans = rag_answer(q)
        set_answer(q, ans)
        print("FRESH:", ans)
        print("cached now?", get_answer(q) is not None)