import math

text = input("Sisend: ").strip()

print(len(text))

if len(text) >= 7 and len(text) % 2 ==1:
    print("Vastab tingimustele")
    print(math.floor(len(text) / 2))
    i = math.floor(len(text) / 2)
    print(text[i-1], text[i], text[i+1])
else:
    print("Sisend ei vasta tingimustele")