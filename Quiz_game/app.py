import qdata

def display_question_and_options(question, options):
    print(f"\n{question}")
    for option in options:
        print(option)

def get_user_answer(valid_options):
    while True:
        answer = input("What is the correct answer? A, B, C, or D ").upper()
        if answer in valid_options:
            return answer
        print("Please choose A, B, C, or D.")

def evaluate_user_response(user_answer, correct_answer, marks):
    if user_answer == correct_answer:
        print("Correct answer!")
        return marks + 1
    else:
        print(f"Sorry, the correct option is {correct_answer}")
        return marks

def calculate_score(marks, total_questions):
    return int((marks / total_questions) * 100)

    

if __name__ == "__main__":
    marks = 0
    valid_options = ['A', 'B', 'C', 'D']

    total_questions = len(qdata.questions)

    for idx, question in enumerate(qdata.questions):
        display_question_and_options(question, qdata.options[idx])
        user_answer = get_user_answer(valid_options)
        marks = evaluate_user_response(user_answer, qdata.answers[idx], marks)

    score = calculate_score(marks, total_questions)
    print(f"Your Score is {score}%")
