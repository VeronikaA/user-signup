from sys import exit
import string  #needed  for string.ascii_letters()

from helpers import alphabet_position, rotate_character
    
# Full Vigenere function
def encrypt(message, text):
    """Receives a message and an alpha key as input. Calculates the numerical place in the alphabet of each character.
    Returns the result of rotating each letter in a message to the right by said numerical value."""

    # Create list of keys from key word. Call alphabet_position helper fx.
    new_key = [alphabet_position(c) for c in text]
    key_len = len(text)
    
    # Use new_key values to rotate text in message
    result = ""
    idx = 0
    cypher = []
    for d in message:
        if d.isalpha():
            result = result + rotate_character(d, new_key[idx])
            idx = (idx + 1) % key_len
        elif d not in string.ascii_letters:
            result = result + d
    # print(result)
    return result

def main(): 
    """ Receives input from user. """
    # message = input("Type a message: ")
    message = ("coffee")
    # text = input("Encryption key: ")
    text = ("greetings")
    cypher = encrypt(message, text)
if __name__ == '__main__':
    main()
