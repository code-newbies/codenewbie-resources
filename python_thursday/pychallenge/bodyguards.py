import re


text = ""

with open("guys", "+r") as f:
    text = f.read()

results = re.finditer(r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", text)

other_results = [x.group(1)  for x in results]

print(other_results)
