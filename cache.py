import hashlib
import redis

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def _key(question: str) -> str:
    return "rag:" + hashlib.md5(question.encode("utf-8")).hexdigest()

def get_answer(question: str):
    return r.get(_key(question))

def set_answer(question: str, answer: str, ttl: int = 3600) -> None:
    r.setex(_key(question), ttl, answer)

def rate_limit(user_id: str, limit: int = 10, window: int = 60) -> bool:
    key = f"rl:{user_id}"
    count = r.incr(key)
    if count ==1:
        r.expire(key, window)
    return count <= limit