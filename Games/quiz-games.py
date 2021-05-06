def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('----------------')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter your answer: ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
#------------
def display_score(correct_guesses, guesses):
    print('----------------')
    print("Results: ")
    print('----------------')
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses/len(questions)*100)
    print("Your score is: " + str(score)+"%")
#------------
def play_again():
    response = input("Dou you want to play again? yes/no ")
    response = response.lower()
    if response == "yes":
        return True
    else:
        return False
#------------

questions = {
    "Meu nome": "C",
    "Quantos anos tenho": "A",
    "Quantas irmãs eu tenho": "A"    
}

options = [["A. Luna", "B. Gustavo", "C. Gabriel"],
            ["A. 21", "B. 20", "C. 22"],
            ["A. 1", "B. 2", "C. 3"]]



new_game()

while play_again():
    new_game(

print("Byeeee")