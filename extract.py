import json
from pydantic import BaseModel, ValidationError
from llm import client

def extract(user_content, schema: type[BaseModel], retries: int = 2) -> BaseModel:
    schema_json = json.dumps(schema.model_json_schema(), ensure_ascii=False)
    messages = [
        {"role": "system", "content": f"Извлекай данные из документов. Верини только валидный JSON по этой схеме: {schema_json}"},
        {"role": "user", "content": user_content},
    ]

    for attempt in range (retries + 1):
        resp = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            response_format={"type": "json_object"},
            temperature=0,
        )

        raw = resp.choices[0].message.content

        try:
            return schema.model_validate_json(raw)
        except ValidationError as e:
            if attempt == retries:
                raise ValueError(f"Не удалось полсе {retries} ретраев. Последняя ошибка: {e.errors}")
            messages.append({"role": "assistant", "content": raw})
            messages.append({"role": "user", "content": f"Ошибка валидации: {e.errors()}. Исправь и верни только JSON."})