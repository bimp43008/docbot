import json
from llm import client

VIN_DB = { # фейковая база
    "XW7BF4FKX0S123456": {"make": "Toyota", "model": "Camry", "year": 2019},
}

tools = [{
    "type": "function",
    "function": {
        "name": "lookup_vin",
        "description": "Возвращает марку, модель и год автомобиля по VIN-коду",
        "parameters": {
            "type": "object",
            "properties": {"vin": {"type": "string", "description": "VIN-код для автомобиля"}},
            "required": ["vin"]
        },
    },
}]

def lookup_vin(vin: str) -> dict:
    return VIN_DB.get(vin, {"error": "VIN не найден"})


messages = [{"role": "user", "content": "Какая марка и год у автомобиля с VIN XW7BF4FKX0S123456"}]

resp = client.chat.completions.create(model="deepseek-chat", messages=messages, tools=tools, temperature=0)
choice = resp.choices[0]
msg = choice.message
print("finish reason:", choice.finish_reason)

if msg.tool_calls:
    call = msg.tool_calls[0]
    args = json.loads(call.function.arguments)
    result = lookup_vin(**args)
    print("MODEL ASKED:", call.function.name, args, "->", result)
    messages.append(msg)
    messages.append({"role": "tool", "tool_call_id": call.id, "content": json.dumps(result)})
    final = client.chat.completions.create(model="deepseek-chat", messages=messages, tools=tools, temperature=0)
    print("ANSWER:", final.choices[0].message.content)
else:
    print("NO TOOL CALL:", msg.content)