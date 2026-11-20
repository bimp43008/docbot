import json 
import re
from rag_answer import rag_answer

def norm(s: str) -> str:
    return re.sub(r"\s+", "", s.lower())

REFUSAL_MARKERS = ["не нашел", "не знаю", "нет информации", "не могу ответить"]

def check(item: dict, answer: str) -> bool:
    a = norm(answer)
    if item.get("expect_refusal"):
        return any(norm(m) in a for m in REFUSAL_MARKERS)
    return all(norm(sub) in a for sub in item["expect_contains"])

def main():
    items = json.load(open("golden_set.json", encoding="utf-8"))
    fact = refus = fact_ok = refus_ok = 0
    for it in items:
        ans = rag_answer(it["q"])
        ok = check(it, ans)
        if it.get("expect_refusal"):
            refus += 1; refus_ok += ok
        else:
            fact +=1; fact_ok += ok
        print(f"{'PASS' if ok else 'FAIL'} | {it['q']}")
    print(f"\neccuracy           ={fact_ok}/{fact} ")
    print(f"refusal_accuracy= {refus_ok}/{refus}")

if __name__ == "__main__":
    main()
    from rag_answer import model
    print(f"[eval] model={model}")