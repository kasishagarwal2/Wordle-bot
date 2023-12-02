import random
import requests

def checker(answer, guess):
    response = [0,0,0,0,0]
    answer = list(answer)
    guess = list(guess)
    for i in range(len(guess)):
        if answer[i] == guess[i]:
            response[i] = 2
            answer[i] = -1
    
    for i in range(len(guess)):
        if guess[i] in answer:
            index = answer.index(guess[i])
            answer[index] = -1
            response[i] = 1
        
    return response

def checker(answer, guessword):
        feedback = []
        for i,letter in enumerate(guessword):
            if letter not in answer:
                feedback.append(0)
            else:
                if letter == answer[i]:
                    feedback.append(2)
                else:
                    feedback.append(1)
        
        return feedback

def hasEnded(check):
    for i in check:
        if i != 2:
            return False
    return True


def updateGuesses(guesses, guess, res):
    for i in range(5):
        for word in guesses:
            if res[i] == 0:
                if guess[i] in word:
                    guesses.remove(word)
            elif res[i] == 2:
                if guess[i] != word[i]:
                    guesses.remove(word)
            elif res[i] == 1:
                if guess[i] not in word:
                    guesses.remove(word)
    
    return guesses



def generateGuess(n,res):
    if n == 0:
        return "arise"
    else:
        return random.choice(guesses)

flag = True

n = 0

res = [0,0,0,0,0]

words = requests.get('https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt').text.strip().split('\n')
guesses = words

answer = random.choice(words)


while(flag):
    if n == 0:
        guess = "arise"
    else:
        guess = generateGuess(n, res)
    
    if hasEnded(res):
        break

    res = checker(answer, guess)
    guesses = updateGuesses(guesses, guess, res)
    n+=1

if guess == answer:
    print("Congratulations the correct answer is {} and you guessed {} \nit took you {} tries".format(answer, guess, n))
else:
    print("lmao")
