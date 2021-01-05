import json

a = """{'a':123, 'b':144}"""

file = open("jason_file.txt", 'r', encoding="utf-8")
dic = json.load(file)
file.close()

print(dic)



