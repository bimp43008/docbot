from pathlib import Path

DOCS = {
    "contract_car.txt": "ДОГОВОР КУПЛИ-ПРОДАЖИ ТС № 17\nПродавец: Смирнов Алексей Игоревич.\nПокупатель: Кузнецова Мария Дмитриевна.\nАвто: Toyota Camry 2019, VIN XW7BF4FKX0S123456.\nЦена: 1 850 000 рублей.\nДата подписания: 02.11.2026.",
    "act_handover.txt": "АКТ ПРИЁМА-ПЕРЕДАЧИ к договору № 17\nПродавец передал, покупатель принял автомобиль Toyota Camry 2019.\nVIN XW7BF4FKX0S123456.\nПретензий к состоянию нет.\nДата передачи: 03.11.2026.",
    "invoice.txt": "СЧЁТ № 5 от 02.11.2026\nПлательщик: Кузнецова Мария Дмитриевна.\nУслуга: оформление договора купли-продажи.\nСумма: 15 000 рублей.\nСрок оплаты: до 12.11.2026.",
}

docs_dir = Path("docs")
docs_dir.mkdir(exist_ok=True)
for name, text in DOCS.items():
    (docs_dir / name).write_text(text, encoding="utf-8")
    print("wrote", name)