display = []
word_length = len("Shuyeb")
for _ in range(word_length):
    display += "_"
    #print(display)


chosen_word = "shuyeb"

for position in range(6):
    letter = chosen_word[position]
    print(letter)

    if letter == "s":
        display[position] = letter
        print(display)



print(display)