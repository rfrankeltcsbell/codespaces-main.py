numbers=[1,2,2,3,3,4,4,4,4,5]
uniquenumbers= list(set(numbers))

print(uniquenumbers)

uniquenumbers2=[]

for num in numbers:
    if num not in uniquenumbers2:
        uniquenumbers2.append(num)

print(uniquenumbers2)
expectedoutput=[1,2,3,4,5]