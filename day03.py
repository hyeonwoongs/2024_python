# prime number
number = int(input("Input number : "))
is_prime = True
univ = "inha"
i = 0
while i < len(univ):
    print(univ[i], end=' ')
    i = i + 1

if number < 2:
    print(f'{number} is NOT prime number!')
else:
    i = 2
    while i < number:
        if number % i == 0:
            is_prime = False
            break
        i = i + 1
print()

    if is_prime:
        print(f'{number} is prime number')
    else:
        print(f'{number} is NOT prime number!')
for letter in univ:
    print(letter, end=' ')

print()

#for k in range(0, len(univ), 1):
#for k in range(0, len(univ)):
for k in range(len(univ)):
    print(univ[k], end=' ')