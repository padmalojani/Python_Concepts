from __future__ import annotations

from grade_system import GradeSystem


def display_menu() -> None:
    print("\nGrade System")
    print("1. Add student")
    print("2. Add score")
    print("3. Show report")
    print("4. Show rankings")
    print("5. Exit")


def main() -> None:
    system = GradeSystem()

    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            name = input("Student name: ").strip()
            scores_raw = input("Scores (comma separated, optional): ").strip()
            scores = [float(item.strip()) for item in scores_raw.split(",") if item.strip()] if scores_raw else []
            try:
                system.add_student(name, scores)
                print(f"Added {name}.")
            except ValueError as exc:
                print(f"Error: {exc}")

        elif choice == "2":
            name = input("Student name: ").strip()
            score = input("Score: ").strip()
            try:
                student = system.add_score(name, float(score))
                print(f"Added score for {student.name}. Average: {student.average:.2f}")
            except (ValueError, KeyError) as exc:
                print(f"Error: {exc}")

        elif choice == "3":
            name = input("Student name: ").strip()
            try:
                report = system.student_report(name)
                print(report)
            except KeyError as exc:
                print(f"Error: {exc}")

        elif choice == "4":
            if not system.students:
                print("No students available.")
                continue
            for rank, (name, average) in enumerate(system.ranked_students(), start=1):
                print(f"{rank}. {name}: {average:.2f}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
