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
