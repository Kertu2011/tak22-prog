fruits =["ploom", "pirn", "kirss" ]
print(fruits)
print(fruits[0])

fruits.append("õun")
print(fruits[-1])

fruits[2] = "apelsin"
print(fruits)

if "õun" in fruits:
    print("Jah, õun on listis")

print(len(fruits))
print(fruits[len(fruits)-1])

del fruits[1]
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)
