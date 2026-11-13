class FakeUsage:
    def __init__(self, prompt: int, completion: int):
        self.prompt_tokens = prompt
        self.completion_tokens = completion


class FakeMessage:
    def __init__(self, content: str):
        self.role = "assistant"
        self.content = content


class FakeChoice:
    def __init__(self, content: str):
        self.message = FakeMessage(content)


class FakeResponse:
    def __init__(self, content: str):
        self.choices = [FakeChoice(content)]
        self.usage = FakeUsage(10, 5)


class Completions:
    def create(self, model: str, messages: list, temperature: float = 0):
        # настоящий SDK здесь делает HTTP-запрос; мы возвращаем заглушку
        return FakeResponse(f"эхо: {messages[-1]['content']}")


class Chat:
    def __init__(self):
        self.completions = Completions()  # атрибут holding объект


class MyClient:
    def __init__(self, api_key: str):
        self.chat = Chat()                # атрибут holding объект


if __name__ == "__main__":
    client = MyClient(api_key="fake")
    resp = client.chat.completions.create(
        model="fake", messages=[{"role": "user", "content": "привет"}], temperature=0
    )
    print(resp.choices[0].message.content)
    print(resp.usage.prompt_tokens)