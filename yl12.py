fruits = ["õun", "banaan", "pirn"]
print(fruits)
print(fruits[0])

fruits.append("mango")
print(fruits)
print(fruits[-1])


fruits[1] = "apelsin"
print(fruits)

if "õun" in fruits:
    print("Jah, õun on listis")

fruits.pop(1)
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)