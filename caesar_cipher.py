def encode(word, sn):
    output = list(word)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    len_alphabet = len(alphabet)-1
    current_index = []
    new_index = []
    counter = 0
    letter_to_sub = []

    for x in output:
        if x in alphabet:
            letter_to_sub.append(counter)
            current_index.append(alphabet.index(x))
        counter += 1

    for z in current_index:
        w = z + sn
        if w >= len_alphabet:
            w -= 1
            w = w % len_alphabet
        new_index.append(w)

    for y, z in zip(new_index, letter_to_sub):
        output[z] = alphabet[y]

    return output

def decode(word, sn):
    output = list(word)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    len_alphabet = len(alphabet)-1
    current_index = []
    new_index = []
    counter = 0
    letter_to_sub = []

    for x in output:
        if x in alphabet:
            letter_to_sub.append(counter)
            current_index.append(alphabet.index(x))
        counter += 1

    for z in current_index:
        w = z - sn
        new_index.append(w)

    for y, z in zip(new_index, letter_to_sub):
        output[z] = alphabet[y]

    return output

while True:
    choice = input("Encode or decode? ")
    if choice == "encode":
        print(" --- ENCODING --- ")
        word = input("Type word: ")
        sn = int(input("Shift Number: "))
        x = encode(word, sn)
        print("".join(x))
    else:
        print(" --- DECODING --- ")
        word = input("Type word: ")
        sn = int(input("Shift Number: "))
        x = decode(word, sn)
        print("".join(x))
