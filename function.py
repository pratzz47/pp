def area(l, b, h):
    print('Area of triangle is : ', l*b*h)

area(10,10,10)

def swaping(a, b):
    print('Value before swaping')
    print('value of a : ', a)
    print('value of b : ', b)
    a, b = b, a
    print('Value after swaping')
    print('value of a : ', a)
    print('value of b : ', b)

swaping(10, 20)

fact = []
def factors(num):
    i = 2
    while i <= num / 2:

        if num % i == 0:
            fact.append(i)
        i = i + 1
    return fact

num = int(input("Enter number to check factors : "))
print("Factors of ", num, " : ", factors(num))
