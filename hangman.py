def hangman(word):
    wrong = 0 # wrong keeps track of incorrect guesses
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word) #track remaining letters
    board = ["__"] * len(word) #list of strings to keep track of game board is 3
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages - 1): #starts at 0 < 8-1
        print("\n")
        msg = "Guess a letter"
        char = input(msg) #char is the letter guessed
        if char in rletters:
            cind = rletters.index(char) #if guess c the index is 1
            board[cind] = char #replace underscore in board list with letter
            rletters[cind] = '$' #replace guess with $ "$" "a" "t"
        else:
            wrong += 1
            print((" ".join(board)))
        e = wrong + 1 #0 + 1
        print("\n".join(stages[0: e])) #slice stages list to print hangman first 0 + 1
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

hangman("cat")
