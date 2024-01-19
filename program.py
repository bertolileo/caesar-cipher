alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    word = ""
    for letter in text:
        position = alphabet.index(letter)
        if position + shift >= len(alphabet):
            position = (position + shift) - len(alphabet)
            word += alphabet[position]
        else:
            word += alphabet[position + shift]
    print("The encoded text is " + word)
  
def decrypt(text, shift):
    word = ""
    for letter in text:
        position = alphabet.index(letter)
        if position - shift < 0:
            position = (position - shift) + len(alphabet)
            word += alphabet[position]
        else:
            word += alphabet[position - shift]

    print("The decoded text is " + word)

if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)
