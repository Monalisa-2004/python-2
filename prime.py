num = int(input("Enter a number: "))
Temp = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            Temp = True
            break
if Temp:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
