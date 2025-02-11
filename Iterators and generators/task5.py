N = int(input())

class Squarednumbers:
    def __iter__(self):
        self.a = 1  
        return self

    def __next__(self):
        if self.a <= N:
            x = self.a ** 2  
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = Squarednumbers()
myit = iter(myclass)

for num in myit:
    print(num)
