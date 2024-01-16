# prime number
number = int(input("Input number : "))
is_prime = True
numbers = input("Input first second number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if number < 2:
    print(f'{number} is NOT prime number!')
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
for number in range(n1, n2+1):
    is_prime = True

    if is_prime:
        print(f'{number} is prime number')
    if number < 2:
        pass
    else:
        print(f'{number} is NOT prime number!')
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime: print(number, end=' ')