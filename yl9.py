a = float(input("Sisesta 1. küljepikkus:"))
b = float(input("Sisesta 2. küljepikkus:"))
c = float(input("Sisesta 3. küljepikkus:"))

def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

def type_of_triangle(a,b,c):
    if a==b and b==c:
        print('Kolmnurk on võrdkülne.')
    elif a==b or b==c or a==c:
        print('Kolmnurk on võrdhaarne.')
    else:
        print('Kolmnurk on erikülgne')

if is_valid_triangle(a,b,c):
    type_of_triangle(a,b,c)
else:
    print('Kolmnurk ei ole sooritatav antud külgedega.')

