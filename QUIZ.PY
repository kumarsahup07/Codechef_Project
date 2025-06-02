import time
import random

def get_python_questions():
    return [
        {"question": "Which keyword is used to define a function in Python?",
         "options": ["A) func", "B) define", "C) def", "D) function"], "answer": "C"},
        
        {"question": "What is the output of print(2 ** 3) in Python?", 
         "options": ["A) 6", "B) 8", "C) 9", "D) 10"], "answer": "B"},
        
        {"question": "Which data type is mutable in Python?", 
         "options": ["A) Tuple", "B) String", "C) List", "D) Integer"], "answer": "C"},
        
        {"question": "Which of the following is used to take input from the user?", 
         "options": ["A) input()", "B) print()", "C) scan()", "D) read()"], "answer": "A"},
        
        {"question": "What will be the output of len('Python')?",
         "options": ["A) 5", "B) 6", "C) 7", "D) Error"], "answer": "B"},
    ]

def countdown_timer():
    print("\nYou have 10 seconds to think...")
    for i in range(10, 0, -1):
        print(f"\rTime left: {i} seconds ", end="")
        time.sleep(1)
    print("\n")


def display_question(question_data, question_number):
    print("\n====================")
    print(f"Question {question_number}: {question_data['question']}")
    for option in question_data["options"]:
        print(option)

def get_user_answer():
    user_answer = input("Now enter your answer (A, B, C, D): ").strip().upper()
    if user_answer in ["A", "B", "C", "D"]:
        return user_answer
    else:
        return None
    
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Answer is correct!")
        return 1
    else:
        print(f"Your answer is wrong! The correct answer is {correct_answer}.")
        return 0

def update_score(score, result):
    if result == 1:
        score += 1  
    return score
    
def play_quiz():
    print("Welcome to Python Quiz!")
    questions = get_python_questions()
    random.shuffle(questions)
    score = 0
    i = 1

    for question in questions:
        display_question(question, i)
        countdown_timer()
        user_answer = get_user_answer()
        result =  check_answer(user_answer, question["answer"])
        score = update_score(score, result)
        i = i + 1

    print(f"Your final score is: {score} / {len(questions)}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_quiz()