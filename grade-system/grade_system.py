def main():
    print("--- Student Grading System ---")
    
    # 1. Take input and handle edge cases (non-numbers)
    user_input = input("Enter a mark (0 to 100): ").strip()
    
    try:
        # Convert input to a float to handle both integers and decimals
        mark = float(user_input)
    except ValueError:
        print(f"Error: '{user_input}' is not a valid number. Please restart and enter a numeric value.")
        return

    # 2. Handle edge cases (numbers out of the 0-100 range)
    if mark < 0 or mark > 100:
        print(f"Error: The mark {mark} is out of bounds. Please enter a value between 0 and 100.")
        return

    # 3. Determine the grade using the requested grading scale
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "E"

    # 4. Print a clear output message
    print(f"\nSuccess: For a mark of {mark}, the resulting grade is: {grade}")

if __name__ == "__main__":
    main()
