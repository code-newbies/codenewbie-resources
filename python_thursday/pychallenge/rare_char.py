import re


text = ""

with open("glob_a_name", "+r") as f:
    text = f.read()

results = re.findall(r"[A-Za-z0-9]+", text)

print(results)
