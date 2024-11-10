import random


def generate_random_number(min_val, max_val):
    """
    Generate a random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)


def select_random_operator():
    """
    Randomly select and return an arithmetic operator from the list.
    """
    return random.choice(['+', '-', '*'])


def generate_problem_and_answer(num1, num2, operator):
    """
    Generate a math problem string and calculate the correct answer based on the operator.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer


def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 10)  # Ensure num2 is also an integer.
        operator = select_random_operator()

        problem, correct_answer = generate_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
