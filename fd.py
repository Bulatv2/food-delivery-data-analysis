import json

with open("fddata.json", "r") as file:
    text = json.load(file)
    #print(text)
for i in text["cafe"]:
    d1 = {}
    print("cafe ","min", min(i["price"]), "average", sum(i["price"]) // len(i["price"]), "max", max(i["price"]), "total orders", len(i["price"]), "total amount", sum(i["price"]))
    for j in i.keys():
        if j != "price":
            d1[j] = sum(i[j])
        else:
            continue
    listd1 = list(d1.items())
    listd1.sort(key = lambda i: i[1])
    for i in listd1:
        print(i[0], "-", i[1])
for i in text["burgerking"]:
    print("burgerking ","min", min(i["price"]), "average", sum(i["price"]) // len(i["price"]), "max", max(i["price"]), "total orders", len(i["price"]), "total amount", sum(i["price"]))
    d2 = {}
    for j in i.keys():
        if j != "price":
            d2[j] = sum(i[j])
        else:
            continue
    listd2 = list(d2.items())
    listd2.sort(key = lambda i: i[1])
    for i in listd2:
        print(i[0], "-", i[1])
for i in text["macdonalds"]: 
    print("macdonalds ","min", min(i["price"]), "average", sum(i["price"]) // len(i["price"]), "max", max(i["price"]), "total orders", len(i["price"]), "total amount", sum(i["price"]))
    d3 = {}
    for j in i.keys():
        if j != "price":
            d3[j] = sum(i[j])
        else:
            continue
    listd3 = list(d3.items())
    listd3.sort(key = lambda i: i[1])
    for i in listd3:
        print(i[0], "-", i[1])
for i in text["cafe"]:
    p1 = len(i["price"])
    s1 = sum(i["price"])
    for i in text["burgerking"]:
        p2 = len(i["price"])
        s2 = sum(i["price"])
        for i in text["macdonalds"]:
            p3 = len(i["price"])
            s3 = sum(i["price"])
            print("all ", "average", (s1 + s2 + s3) // (p1 + p2 + p3), "total oders", p1 + p2 + p3, "total amount", s1 + s2 + s3)
