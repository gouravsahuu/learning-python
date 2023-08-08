sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

ans = {}

for key in keys :
    ans[key] = sample_dict[key]

print(ans)