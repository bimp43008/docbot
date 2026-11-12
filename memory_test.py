from llm import client


messages = [{"role": "system", "content": "Ты краткий ассистент."}]

messages.append({"role": "user", "content": "Меня зовут Кирилл, я учу Python."})
r1 = client.chat.completions.create(model="deepseek-chat", messages=messages, temperature=0)
print(f"[r1] prompt={r1.usage.prompt_tokens} completion={r1.usage.completion_tokens}")

messages.append({"role": "assistant", "content": r1.choices[0].message.content})
messages.append({"role": "user", "content": "Как меня зовут и что я учу?"})
r2 = client.chat.completions.create(model="deepseek-chat", messages=messages, temperature=0)
print("A2:", r2.choices[0].message.content)
print(f"[r2] prompt={r2.usage.prompt_tokens} completion={r2.usage.completion_tokens}")

r3 = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Как меня зовут и что я учу?"}],
    temperature=0,
)

print("A3 (без памяти):", r3.choices[0].message.content)
print(f"[r3] prompt={r3.usage.prompt_tokens} completion={r3.usage.completion_tokens}")