import random

print("Welcome to The Game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay Let's Play")
score = 0

# Define the paths to the questions and answers files
questions_path = "D:\\Python Projects\\Quiz\\questions.txt"
answers_path = "D:\\Python Projects\\Quiz\\answers.txt"

try:
    # Read questions from the file
    with open(questions_path, 'r') as file:
        questions = file.readlines()

    # Read answers from the file
    with open(answers_path, 'r') as file:
        answers = file.readlines()

    # Ensure both lists have the same number of items
    if len(questions) != len(answers):
        print("Error: The number of questions and answers do not match.")
        quit()

    # Create a list of question-answer pairs
    qa_pairs = list(zip(questions, answers))

    # Select 10 random question-answer pairs
    selected_pairs = random.sample(qa_pairs, 10)

    # Iterate through the selected questions and answers
    for question, correct_answer in selected_pairs:
        question = question.strip()
        correct_answer = correct_answer.strip().lower()

        answer = input(question + " ").strip().lower()
        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print("Incorrect")

    print(f"Your final score is: {score}/10")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")