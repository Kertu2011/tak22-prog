a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

def type_of_triangle(a,b,c):
    if a==b and b==c:
        print('Kolmnurk on võrdkülgne.')
    else:
        print('Kolmnurk on võrdhaarne')

