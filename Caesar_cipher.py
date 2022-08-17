logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift, direction):
    result = ""
    for letter in text:
        if letter not in alphabet:
            result += letter
        else:
            position = alphabet.index(letter)
            if direction == 'encode':
                position += shift
                if position < len(alphabet):
                    result += alphabet[position] #Since the position in smaller than the lenght of the list, it won't generate an error.
                else:
                    position = position % 26 # For numbers higher than the length of the alphabet, we need to take the modulus of the position to access its index
                    result += alphabet[position]
            elif direction == "decode":
                position -= shift
                if len(alphabet) > position >= 0: #Now we're going backwards, so the position must be higher or equal to 0 and lower than the lenght of the list.
                    result += alphabet[position]
                else:
                    position = position % 26
                    result += alphabet[position]
    if direction == 'encode':
        print(f'The encoded text is {result}.')
    elif direction == 'decode':
        print(f'The decoded text is {result}.')

status = True
print(logo)
while status:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ['encode', 'decode']:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(text, shift, direction)
    answer = input('Would you like to do this again? [yes, no]\n').lower()
    while answer not in ['yes', 'no']:
        answer = input('Would you like to do this again? [yes, no]\n').lower()
    if answer == 'no':
        status = False
print('Goodbye.')




