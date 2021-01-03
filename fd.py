import json

with open("fddata.json", "r") as file:
    text = json.load(file)
    #print(text)
for i in text["cafe"]:
    print("cafe ", min(i["price"]), sum(i["price"]) // len(i["price"]), max(i["price"]), len(i["price"]), sum(i["price"]))
    for j in i.keys():
        if j != "price":
            print("{} - {}".format(j, len(i[j])))
        else:
            continue
for i in text["burgerking"]:
    print("burgerking ", min(i["price"]), sum(i["price"]) // len(i["price"]), max(i["price"]), len(i["price"]),sum(i["price"]) )
    for j in i.keys():
        if j != "price":
            print("{} - {}".format(j, len(i[j])))
        else:
            continue
for i in text["macdonalds"]: 
    print("macdonalds ", min(i["price"]), sum(i["price"]) // len(i["price"]), max(i["price"]), len(i["price"]),sum(i["price"]) )
    for j in i.keys():
        if j != "price":
            print("{} - {}".format(j, len(i[j])))
        else:
            continue
for i in text["cafe"]:
    p1 = len(i["price"])
    s1 = sum(i["price"])
    for i in text["burgerking"]:
        p2 = len(i["price"])
        s2 = sum(i["price"])
        for i in text["macdonalds"]:
            p3 = len(i["price"])
            s3 = sum(i["price"])
            print("all ", (s1 + s2 + s3) // (p1 + p2 + p3), p1 + p2 + p3, s1 + s2 + s3)
