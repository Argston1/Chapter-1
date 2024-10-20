a=float(input("Enter a number: "))
b=float(input("Enter 1, if the number is your number in bytes : "))
if b==1:
    print(f'Your number in kilobytes: {a/1024}')
else:
    print(f'Your number in bytes: {a*1024}')