import random
#Это переменная, выдающая одно слово из списка

spisok = ["cat", "dog", "pasha", "misha", "govno", "pidor"]
randspisok = random.choice(spisok)


def hangman(word):
    #primer iz uchebnika,
    #в его случает таблица внутри функции, а у меня вне ее:
'''
    word_list = ["cat", "dog", "pasha", "misha", "govno", "pidor"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
'''
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to the execute!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "vvedite bukvy: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win, the word is: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("you lose, the word was: {}".format(word))

hangman(randspisok)
