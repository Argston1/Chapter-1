a=float(input('Enter the distance in kilometers: '))
b=float(input('Enter the distance in meters: '))
c=a*1000
if c>b:
    print(f"The smallest distance: {b} meters")
elif c<b:
    print(f"The smallest distance: {a} kilometers")
else:
    print('The distances are the same')