def encode(word, sn):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    len_alphabet = len(alphabet)-1
    word = list(word)
    current_index = []
    new_index = []
    output = ""

    for x in word:
        current_index.append(alphabet.index(x))

    for z in current_index:
        w = z + sn
        if w >= len_alphabet:
            w -= 1
            w = w % len_alphabet
        new_index.append(w)

    for y in new_index:
        output += alphabet[y]

    return output

def decode(word, sn):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    len_alphabet = len(alphabet)-1
    word = list(word)
    current_index = []
    new_index = []
    output = ""

    for x in word:
        current_index.append(alphabet.index(x))

    for z in current_index:
        w = z - sn
        new_index.append(w)

    for y in new_index:
        output += alphabet[y]

    return output

while True:
    choice = input("Encode or decode? ")
    if choice == "encode":
        print(" --- ENCODING --- ")
        word = input("Type word: ")
        sn = int(input("Shift Number: "))
        x = encode(word, sn)
        print(x)
    else:
        word = input("Type word: ")
        sn = int(input("Shift Number: "))
        x = decode(word, sn)
        print(x)
