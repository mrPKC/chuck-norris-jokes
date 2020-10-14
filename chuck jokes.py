import requests
import json
import pandas as pd

n = []
for i in range(473):
    n.append(input())

joke_lis = []
for i in n:
    url = "http://api.icndb.com/jokes/{}".format(i)
    res = requests.get(url)
    # print(res.content)
    json_data = json.loads(res.content)

    json_strings = json.dumps(json_data)

    joke = json_data["value"]["joke"]
    joke_lis.append(joke)
    joke = ""

file_name = "chuck jokes.csv"
with open(file_name, "w") as f:
    head = "ID,Joke\n"
    f.write(head)
    a = 0
    for j in range(473):
        a += 1

        if 1 <= a <= 5 or 8 <= a <= 10 or a == 13:
            row_string = f"{n[j]},{joke_lis[j]}\n"
            f.write(row_string)
        else:
            l = '"{}"'.format(joke_lis[j])
            row_string = f"{n[j]}," f"{l}\n"
            f.write(row_string)
        if a == 0 or a == 15:
            a = 0

