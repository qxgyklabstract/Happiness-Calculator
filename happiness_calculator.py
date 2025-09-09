import random

def ask_questions():
    print("Welcome to the Happiness Calculator!")
    print("Answer these silly questions to find out how happy you are today.\n")

    questions = [
        "Do you like dancing penguins? (yes/no): ",
        "Have you ever eaten ice cream for breakfast? (yes/no): ",
        "Would you wear socks on your hands for a day? (yes/no): ",
        "Do you think llamas are secretly planning world domination? (yes/no): ",
        "Have you ever sung in the shower like a rockstar? (yes/no): "
    ]

    answers = []
    for q in questions:
        answer = input(q)
        answers.append(answer.strip().lower())

def calculate_happiness():
    happiness = random.randint(0, 100)
    print(f"\nYour happiness level is: {happiness}% 🎉")

if __name__ == "__main__":
    ask_questions()
    calculate_happiness()
