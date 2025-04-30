from typing import List, Tuple

def show_history() -> None:
    print("\n== Program that Computes the Average Score of Students ==")

def get_names_score() -> Tuple[List[str], List[float]]:
    while True:
        try:
            count = int(input("Number of students: "))
            if count <= 0:
                print("Please enter a number greater than zero")
                continue
            break
        except ValueError:
            print("Invalid input")

    names_of_students = []
    scores = []

    print("\nEnter student names and their scores:")
    for i in range(count):
        name = input(f'Student {i + 1} name: ').strip()
        if not name:
            name = f'Student {i + 1}'
        names_of_students.append(name)

        while True:
            try:
                score = float(input(f'Enter the score for {name}: '))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100")
            except ValueError:
                print("Invalid input")

    return names_of_students, scores

def calculate_average(scores: List[float]) -> float:
    return sum(scores) / len(scores)

def main():
    show_history()
    names, scores = get_names_score()
    average = calculate_average(scores)
    print(f"\nThe average score of students is: {average:.2f}")

if __name__ == "__main__":
    main()