import random
number_of_guesses = 0
guesses = []
max_guesses = 6
error = ""

def hangman():
    global max_guesses
    word = randomWord()
    initializeBoard(word)
    solved = False
    while not solved and number_of_guesses < max_guesses: 
        updateBoard(word)
        solved = checkSolved(word)
    if not solved:
        print("You lose! The idol was " + word.title())
    else:
        print("You win! The idol is " + word.title())
    
def randomWord():
    words = [
        "namjoon",
        "jungkook",
        "yoongi",
        "hoseok",
        "seokjin",
        "taehyung",
        "jimin",
        "nayeon",
        "momo",
        "jihyo",
        "dahyun",
        "sana",
        "mina",
        "jeonyeon",
        "chaeyoung",
        "tzuyu"
    ];
    word_id = random.randrange(len(words) - 1)
    return words[word_id]


def initializeBoard(word):
    print("Welcome to kpop hangman!")
    print("You have " + str(max_guesses) + " chances to guess the kpop idol!")
    print("Let's begin!")

    
def updateBoard(word):
    global number_of_guesses
    global guesses
    blanks = ""
    for char in word:
        if char in guesses and char in word:
            blanks += char
        else:
            blanks += "_"
    print(blanks)
    letter = guessLetter(word)
    if letter not in word:
        number_of_guesses += 1

        
def checkSolved(word):
    global guesses
    for letter in word:
        if letter not in guesses:
            return False
    return True
    
def guessLetter(name): 
    global guesses
    global error
    letter = getLetter()
    valid = validLetter(letter)
    while not valid:
        print("Whoops! " + error)
        letter = getLetter()
        valid = validLetter(letter)
    guesses.append(letter.lower())
    return letter.lower()      

def getLetter():
    letter_guessed = input("Guess a letter! ")
    return letter_guessed
        
def validLetter(letter):
    global guesses
    global error
    error = ""
    if len(letter) > 1:
        error += "Please enter one character at a time. "
    if not letter.isalpha():
        error += "Please choose a valid letter. "
    if letter in guesses:
        error += "You've already guessed this character. "
    if len(letter) == 1 and letter.isalpha() and letter not in guesses:
        return True
    else:
        return False
    
    
hangman()