n = int(input("Enter decimal number: "))
while n > 0:
    digit = n / 2
    rem = [n % 2]
rem = rem[::-1]
print(rem)
