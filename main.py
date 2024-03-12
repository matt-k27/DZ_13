import string

print('DZ13')

inputtedText = str(input('Enter your name of variable pls: '))

i = 0
for letter in string.ascii_letters:
    if string.ascii_letters.find(inputtedText[0]) <= i <= string.ascii_letters.find(inputtedText[-1]):
        print(letter, end='')
    i += 1