import json
from schemas import VehicleContract

schema_json = json.dumps(VehicleContract.model_json_schema(), ensure_ascii=False)
system_msg = f"Извлекай данные из документов. Верни ТОЛЬКО валидный JSON по этой схеме: {schema_json}"
print(system_msg)