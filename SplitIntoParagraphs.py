import regex as re
import json

with open('bign2.txt', 'r', encoding="utf-8") as f:
    text = f.read()
    f.close()

matches = re.finditer(r'(?s)((?:[^\n][\n]?)+)', text)

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

d = []
for m in matches:
    d.append({"paragraph": striphtml(m.group())})

with open('ANDRA_PARAGRAPHS.json', 'w', encoding="utf-8") as f:
    json.dump(d, f,ensure_ascii=False, indent=4)
    f.close()
