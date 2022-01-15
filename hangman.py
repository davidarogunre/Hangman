import time
import random
user = input('What is your name: ')

guess = ''

trys= 10
#welcomes the user

def welcome():
    print(''' ------------------------------------------
        Welcome '''+ user+ ''', get ready to start the game
        --------------------------------------------''')
        

if user.isdigit(): 
    print('We do not allow numbers therefore you are not welcome')
else:
    welcome()
time.sleep(1)
wordlist =['Python','Java','Javascript','C++', 'HTML']

def getword():
    return wordlist[random.randint(0, len(wordlist)-1)]

word = getword()

def gethint():
    if word == 'Python':
        return('It can do everything')

    elif word == 'Java':
        return('It is used to make apps')

    elif word == 'Javascript':
        return('It is next to C++')

    elif word == 'C++':
        return("It's very hard")

    elif word == 'HTML':

        return('Hyper Text Transfer Language')
time.sleep(1)
print(gethint())
time.sleep(0.5)
print('You word contains ' + str(len(word)) + ' letter')

# Find whether the answer is a full word or letter by letter
answer_type = input('Choose to answer word by word or letter by letter(word/letter): ')
#Iterator for Guess loop
i = 0

#Check if answer type is letter or word
if answer_type == 'letter':
    while i < len(word):
        letter= input('Make a guess: ')
        if letter.isdigit():
            print('Guess cannot be a digit')
            guess = ''

        elif len(letter) >1:
            print("Letter can't be more that one character")
            letter = ''

        if word[i].lower() == letter.lower():
            guess += letter
            i += 1
            print(guess)

            if(len(guess) == len(word)):
                print('You are correct')
                guess =''
                
        else:
            print('Try again')

elif answer_type == 'word':
    while trys >0:

        word_guess = input('Choose word: ')
        guess += word_guess

        if guess.lower() != word.lower():
            print('Try again')
            trys-=1

        else:
            score = 'correct'
            print(score)
            trys -=1
    else:
        print('''                ||||||||||    
                ||            
                ||    ||||| |-----| |---||---| |----      ______       ____
                ||       || |-----| |   ||   | |----     |      | |  ||____||_--
                ||||||||||| |     | |   ||   | |----     |______| |__||_____|''')
 
        

else:
    print('Wrong input')

