import random
import pyautogui as ankan
password =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '%', '$', '!', '^', '&', '*', '(', ')', '_', '-', '+', '=', '|', '{', '}', '?', ]
user_password = ankan.prompt('Enter Password')
guess = ""
while(guess!=user_password):
    guess = ""
    for letter in range(len(user_password)):
        guess_letter = password[random.randint(0,25)]
        guess = str(guess_letter)+str(guess)
        print(guess)
ankan.alert("Your Correct Password is :: "+guess)
print("Your Correct Password is :: "+guess)