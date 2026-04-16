score = 0

print('Guess the animal!')


def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer!")
            score = score + 3 - attempt  # 3 points for first attempt, 2 for second, 1 for third
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Wrong answer! Try again: ")
            attempt = attempt + 1

    if attempt == 3:
        print("The correct answer is: " + answer)


guess1 = input('1. What is the tallest land animal? ')
check_guess(guess1, 'Giraffe')

guess2 = input('2. What is the fastest land animal? ')
check_guess(guess2, 'Cheetah')

guess3 = input(
    '3. Answer True or False: \n The sloth is the slowest animal in the world. ')
check_guess(guess3, 'True')

guess4 = input(
    '4. Which of the following is a fish? \n A) Dolphin \n B) Shark \n C) Whale \n D) Octopus \n Type A, B, C, or D: ')
check_guess(guess4, 'B' or 'Shark')

guess5 = input(
    '5. Which of the following is a mammal? \n A) Frog \n B) Snake \n C) Bat \n D) Spider \n Type A, B, C, or D: ')
check_guess(guess5, 'C' or 'Bat')

guess6 = input(
    '6. Which bear lives in the North Pole? \n A) Polar Bear \n B) Grizzly Bear \n C) Panda Bear \n D) Black Bear \n Type A, B, C, or D: '
)
check_guess(guess6, 'A' or 'Polar Bear')

guess7 = input(
    '7. Which of the following is a bird? \n A) Penguin \n B) Ostrich \n C) Eagle \n D) All of the above \n Type A, B, C, or D: '
)
check_guess(guess7, 'D')

guess8 = input(
    '8. Which of the following is the largest mammal? \n A) Elephant \n B) Blue Whale \n C) Giraffe \n D) Hippopotamus \n Type A, B, C, or D: '
)
check_guess(guess8, 'B')

guess9 = input(
    '9. Which of the following is a reptile? \n A) Snake \n B) Frog \n C) Salamander \n D) All of the above \n Type A, B, C, or D: '
)
check_guess(guess9, 'A')

guess10 = input(
    '10. Which of the following is a type of insect? \n A) Tick \n B) Spider \n C) Ant \n D) All of the above \n Type A, B, C, or D: '
)
check_guess(guess10, 'C')

print("Your final score is: " + str(score) + " out of 30.")

print("Thanks for playing!")
print("Try again to improve your score!")
