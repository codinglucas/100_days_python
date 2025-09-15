guess_word = list("hello")
life = 6
counter = 0 
list_index = []
output = ["_"] * (len(guess_word))


while life != 0:
    letter = str(input("Guess a leter: "))
    if letter in guess_word:
        print("Great guess!")
        for x in guess_word:
            if x == letter:
                list_index.append(counter)
            counter += 1
        
        # make sure list_index is all int values
        for x in list_index:
            x = int(x)

        # sort list_index
        list_index = sorted(list_index)

        # replace output with guess_word char
        for c in list_index:
            output[c] = guess_word[c]   
        list_index = []    
        print("".join(output))

        # check win condition
        if "_" not in output:
            break

        # prepare for new iteration
        counter = 0 
    else:
        print(f"The letter {letter} is not in the word! You lost one life")
        print("".join(output))
        life -= 1

print("You won!")
    
