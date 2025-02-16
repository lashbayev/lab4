def countdown(n):
    for i in range(n, -1, -1): 
        yield i


n = int(input("Enter a number: "))

print(f"Countdown from {n} to 0:")
for num in countdown(n):
    print(num)
