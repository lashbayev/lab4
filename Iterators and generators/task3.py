class DivisibleBy3And4:
    def __init__(self, n):
        self.n = n
        self.current = 0  

    def __iter__(self):
        return self  

    def __next__(self):
        while self.current <= self.n:
            num = self.current
            self.current += 1  

            if num % 3 == 0 and num % 4 == 0:
                return num  
        
        raise StopIteration  


n = int(input("Enter a number: "))
divisible_numbers = DivisibleBy3And4(n)

for num in divisible_numbers:
    print(num)
