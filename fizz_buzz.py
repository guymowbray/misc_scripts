import time

lst = [i for i in range(1,16)]

class Output:
    def __init__(self, number):
        self.number = number

    def what_is_it(self):
        if (self.number/3).is_integer() and (self.number/5).is_integer():
            return "fizz_buzz"
        elif (self.number/3).is_integer():
            return "buzz"
        elif (self.number/5).is_integer():
            return "fizz"
        else:
            return self.number

for i in lst:
    time.sleep(0.1)
    print(Output(i).what_is_it())
