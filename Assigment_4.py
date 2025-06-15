import random

def verification(guess, secret_word):
    result= []
    i = 0
    while i < word_len:
        if guess[i] == secret_word[i]:
            result.append('correct')
        elif guess[i] in secret_word:
            result.append('present')
        else:
            result.append('absent')
        i += 1  
    return result

def print_secret_word(result, guess):
    display = []
    i = 0
    g = 0
    while i < word_len:
        if result[i] == 'correct':
            display.append("[" + guess[i].upper() + "]")
        elif result[i] == 'present':
            display.append("(" + guess[i] + ")")
        else:
            display.append(" " + guess[i] + " ")
        i += 1
    print("Result:", " ".join(display))

def choice_word(words):
    x = random.random()
    y = x * len(words)
    z = int(y)
    return words[z]


words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
tries = 6
word_len = 5

print("Welcome to Wordle!")
print("Guess the",word_len ,"-letter word. You have", tries, "tries.")

while tries != 0:
    guess = input(f"Attempt {7 - tries}/6 – Enter guess: ").lower()

    if not guess.isalpha():
        print("Not number")
        continue
    
    if len(guess) != word_len:
        print("Wrong length. Expected", word_len)
        continue

    if tries == 6:
        secret_word = choice_word(words)
    
    if guess == secret_word:
        print("You win!!!")
        answer = input("If you want play one more time print \"play\"  ")
        if answer == "play":
            tries = 6
            continue
        else:
            break
        
    print_secret_word(verification(secret_word, guess), guess)

    tries -= 1

    if tries == 0:
        print("You lose! The word was:", secret_word)
        answer = input("If you want play one more time, print \"play\"  ")
        if answer == "play":
            tries = 6
            continue
        else:
            break

"""
            Що ще можна було би вдосконалити
Замість:
def choice_word(words):
    x = random.random()
    y = x * len(words)
    z = int(y)
    return words[z]

Можна було би написати:
secret_word = random.choice(words)

Замість:
def verification(guess, secret_word):
    result= []
    i = 0
    while i < word_len:
        if guess[i] == secret_word[i]:
            result.append('correct')
        elif guess[i] in secret_word:
            result.append('present')
        else:
            result.append('absent')
        i += 1
    return result

def print_secret_word(result, guess):
    display = []
    i = 0
    while i < word_len:
        if result[i] == 'correct':
            display.append("[" + guess[i].upper() + "]")
        elif result[i] == 'present':
            display.append("(" + guess[i] + ")")
        else:
            display.append(" " + guess[i] + " ")
        i += 1
    print("Result:", " ".join(display))

Можна було би написати:
def print_secret_word(secret_word, guess):
    display = []
    i = 0
    while i < word_len:
        if guess[i] == secret_word[i]:
           display.append("[" + guess[i].upper() + "]") 
        elif guess[i] in secret_word:
            display.append("(" + guess[i].upper() + ")")
        else:
            display.append(" " + guess[i] + " ")
        i += 1
    print("Result:", " ".join(display))

Ці зміни допомогли би зменшити кількість коду та збільшити читабельність

Також я прибрав частину коду, яку вважав зайвою.

junk = ''.join([c for c in display if c])


"""
