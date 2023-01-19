me = {
    "first_name": "Kertu",
    "last_name": "Beljäev",
    "birth_year": 2005,
    "place_of_living": "Mõnuste",
    "dessert": "pannkook"
}

# print(me.get("place_of_living"))
# print(me["place_of_living"])

me["dessert"] = "ice cream"

for k, v in me.items():
    print(k, v)
# me ["personal_code"] = "1234567890"

if "personal_code" in me: 
    print("Isikukood on olemas")
    else:
        print("Isikukoodi pole listis")