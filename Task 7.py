r=float(input('Enter the radius: '))
print(f'The diameter is equal to: {r*2}')


a=[]
for i in range(100,501):
    a.append(i)
print(f'The sum of all integers from 100 to 500: {sum(a)}')


b=[]
c=int(input('Enter the number: '))
for j in range(c,501):
    b.append(j)
print(f'The sum of all integers from your {c} to 500: {sum(b)}')