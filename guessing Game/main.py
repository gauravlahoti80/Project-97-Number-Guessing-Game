#importing modules
import random
import pyttsx3

#welcome screen
input_speak = pyttsx3.init()
input_speak.say("Enter your name: ")
input_speak.runAndWait()

#taking name input from the user
user_name = input("Enter your name: ")

#showing hello to the user
input_speak.say(f"Hello,{user_name}")
input_speak.runAndWait()
print(f'Hello , {user_name}.')

#chances
chances = 5
print(f"You have {chances} chances to win the game.")

#random number
max_number = 10
min_number = 1
random_number = random.randint(min_number , max_number)

#taking input for number
input_speak.say("Enter any number from 1 to 10: ")
input_speak.runAndWait()
guessed_number = int(input("Enter any number from 1 to 10: "))

while True: 
    #checking the numbers
    if guessed_number == random_number:
        input_speak.say(f"Congrats, {user_name} you have guessed the number in {chances} chances.")
        input_speak.runAndWait()
        print(f"Congrats, {user_name} you have guessed the number in {chances} chances")
        break

    #if the user looses
    elif chances == 1:
        input_speak.say(f"sorry you were not able to guess the number. The number is {random_number}")
        input_speak.runAndWait()
        print(f"sorry you were not able to guess the number. The number is {random_number}")
        break

    #checking the numbers for high anf low
    else:
        if random_number > guessed_number:
            input_speak.say("that was too low.")
            input_speak.runAndWait()
            print('That was too low.')
        else:
            input_speak.say("that was too high.")
            input_speak.runAndWait()
            print('That was too high.')

        #taking the input again on wrong guessed
        chances -= 1
        print(f'You have {chances} chances left.')
        guessed_number = int(input('Guess again: '))