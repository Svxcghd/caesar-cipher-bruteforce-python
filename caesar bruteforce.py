cyphertext = 'PUT THE TEXT HERE'
for move in range(1,26):
    result = ''
    for letter in cyphertext:
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord ('a')
            new = chr((ord(letter)- base - move ) %26 + base)
            result += new
        else :
            result += letter

            print(f"{move} {result}")