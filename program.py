alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    word = list(text)
    for i in range(0, len(word)):
        letter = alphabet.index(word[i])
        if letter + shift >= len(alphabet):
            index = (letter + shift) - len(alphabet)
            word[i] = alphabet[index]
        else:
            word[i] = alphabet[letter + shift]
    
    print(f"The encoded text is {''.join(word)}")
  
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text, shift)
