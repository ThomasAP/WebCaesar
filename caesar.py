

def encrypt(string, rot):
    en_string = ''

    for char in string:
        en_char = rotate_character(char, rot)
        en_string += en_char
    return en_string

def alphabet_position(char):
    #from 0 find letter's position in the alphabet
    letter = char.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.find(letter)

def rotate_character(char, rot):
    #Shift given character 'rot' number of indexes to the right
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    en_char = ""

    alpha_pos = alphabet_position(char)

    if char not in alpha and char not in alpha.upper():
        en_char += char
    else:
        en_char += alpha[((alpha_pos + int(rot)) % 26)]

    if char in alpha.upper():
        en_char = en_char.upper()
    return en_char


def main():
    from sys import argv
    print("This is what the user typed on the command line:", argv)
    # ... the rest of your code ...

    if len(argv) < 2 or argv[1].isdigit() == False:
        print('usage: python caesar.py n \n Arguments: -n : The integer to be used as a "key" to encrypt your message.  Only accepts integer.')
        exit()

    message = input('Type a message: ')



    #not necessary thanks to sys import argv
    #rotation = int(input('Rotate by: '))

    #argv stores the arguments entered by index with argv[0] being caesar ,because i enter caesar.py as my first argument and argv[1] is the rotation argument since it's the second value entered
    #for some reason, argv had to be typecast
    print(encrypt(message, int(argv[1])))

if __name__ == '__main__':
    main()
