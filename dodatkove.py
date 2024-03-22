import math
a = int(input())
b = int(input())
m = int(input())

def funk(a, b, m):
    klass = []
    
    if math.gcd(a, m) > b and math.gcd(a, m) % b != 0:
        return klass
    elif math.gcd(a, m) < b and b % math.gcd(a, m) != 0:
        return klass

    add = m // math.gcd(a, m)

    funk = b + m
    while funk % a != 0:
        funk += m
    x_0 = funk // a

    print(f"y = {x_0} + {add}x")
    
    for i in range(-3, 4):
        el = x_0 + add * i
        klass.append(el)
    
    return klass

print("general form:", end="")
array = funk(a, b, m)
print("...")
for n in array:
    print(n, end=", ")
print("...")
print("numbers that smaller than mod:")
for n in array:
    if(n > 0 and n < m):
        print(n, end =", ")




