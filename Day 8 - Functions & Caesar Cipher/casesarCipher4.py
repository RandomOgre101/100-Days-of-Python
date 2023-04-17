from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    end_text = ""

    if direction == "decode":
        shift *= -1
    
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            end_text += alphabet[new_position]
        else: end_text += char
        
    print(f"\nThe {direction}d text: {end_text}\n")

cont = True

print(logo)

while cont == True:

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))
    shift = shift%26

    caesar(text=text, shift=shift, direction=direction)

    restart = input("Would you like to restart the program? Type 'yes' or 'no' \n").lower()
    
    if restart == "no":
        cont = False

