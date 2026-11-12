from openai import OpenAI
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    deepseek_api_key: str
    deepseek_base_url: str = "https://api.deepseek.com"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
client = OpenAI(api_key=settings.deepseek_api_key, base_url=settings.deepseek_base_url)

def ask(question: str) -> str:
    resp = client.chat.completions.create(
         model="deepseek-chat",
         messages=[
            {"role": "system", "content": "Ты краткий ассистент. Отвечай по-русски."},
            {"role": "user", "content": question},
        ],
        temperature=1.5,
    )
    u = resp.usage
    print(f"[usage] prompt={u.prompt_tokens}, comletion={u.completion_tokens}, tottal={u.total_tokens}")
    return resp.choices[0].message.content

if __name__ == "__main__":
    print(ask("Что такое DL? И для чего он используется?"))