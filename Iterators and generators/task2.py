class Generator:
    def __iter__(self):
        self.a = int(input("Введите число: "))  
        self.current = 1  
        return self
    
    def __next__(self):
        while self.current <= self.a:
            num = self.current
            self.current += 1  

            if num % 2 == 0:  
                return num  

        raise StopIteration  


myclass = Generator()
myit = iter(myclass)

for i in myit:
    print(i)
