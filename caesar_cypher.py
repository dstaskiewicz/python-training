'''
Idea from: https://github.com/karan/Projects-Solutions/blob/master/README.md
Caesar cipher - Implement a Caesar cipher, both encoding and decoding. 
The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). 
The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). 
So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC". 
This simple "monoalphabetic substitution cipher" provides almost no security, 
because an attacker who has the encoded message can either use frequency analysis to guess the key, or just try all 25 keys.
'''

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
LEN_LETTERS = len(LETTERS)


def caesar_cypher(text: str, key: int) -> str:
    cyphered_text = ''
    for letter in text:
        index = LETTERS.index(letter)
        cyphered_text += LETTERS[(index + key) % LEN_LETTERS]
    return cyphered_text

if __name__ == '__main__':
    text_to_cypher = input('Insert the text to cypher: ')
    key = int(input('Insert key length: '))
    cyphered_text = caesar_cypher(text=text_to_cypher, key=key)
    print(cyphered_text)
