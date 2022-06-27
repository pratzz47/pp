class Name:
    def Hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')

obj = Name()
obj.Hello()
obj.Hello("Ravindra")


class calculate:
    def add(self):
        print(5+15)

class calc(calculate):
    def add(self):
        print('GP'+' Pune')

print('The method add here is overridden in the code')
# Invoking Child class through object r
r = calc()
r.add()

# Invoking Parent class through object r
r = calculate()
r.add()
