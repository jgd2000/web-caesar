alphabet = 'abcdefghijklmnopqrstuvwxyz'
def alphabet_position(letter):
    """ receives string of one char letter
    and returns num value within alphabet
    """

    for idx in range( len(alphabet)):
        if letter == alphabet[idx] or letter == alphabet[idx].upper():
            return idx


def rotate_character(char, rot):
    # receives a 1 char string and an int for num of positions to rotate that char
    if char.isalpha():
        encrypted = ''
        new_ind = alphabet_position(char) + rot
        if new_ind < 26:
            encrypted = encrypted + alphabet[new_ind]
        else:
            encrypted = encrypted + alphabet[new_ind % 26]

        if char.isupper():
            return encrypted.upper()
        else:
            return encrypted

    return char


def encrypt(text, rot):

    out_text=[]
    for i in range(len(text)):
        for j in range(len(text[i])):

            out_text.append( rotate_character(text[i][j],rot) )

    out_text="".join(out_text)
    return out_text
