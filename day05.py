# Assignment ex 8.10
# squares = {n: pow(n, 2) for n in range(10)}
squares = {n: n**2 for n in range(10)}
# squares = {n: n*n for n in range(10)}
print(squares)

# univ = 'inha univerity'
# counts_alphabet = {letter: univ.count(letter) for letter in univ}  # dictionary comprehension
# print(counts_alphabet)

# univ = 'inha univerity'
# counts_alphabet = dict()
# for letter in univ:
#     counts_alphabet[letter] = univ.count(letter)
# print(counts_alphabet)