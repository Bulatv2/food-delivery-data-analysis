import json

with open("yedata.json", "r") as file:
    text = json.load(file)
    print(text)

for i in text["cafe"]:
    print("cafe ", min(i["price"]), sum(i["price"]) // len(i["price"]), max(i["price"]), len(i["price"]), sum(i["price"]))

for i in text["burgerking"]:
    print("burgerking ", min(i["price"]), sum(i["price"]) // len(i["price"]), max(i["price"]), len(i["price"]),sum(i["price"]) )

for i in text["macdonalds"]: 
    print("macdonalds ", min(i["price"]), sum(i["price"]) // len(i["price"]), max(i["price"]), len(i["price"]),sum(i["price"]) )

for i in text["cafe"]:
    l1 = len(i["price"])
    s1 = sum(i["price"])
    for i in text["burgerking"]:
        l2 = len(i["price"])
        s2 = sum(i["price"])
        for i in text["macdonalds"]:
            l3 = len(i["price"])
            s3 = sum(i["price"])
            print("all ", (s1 + s2 + s3) // (l1 + l2 + l3), l1 + l2 + l3, s1 + s2 + s3)
