def main():
    print("--- Student Grading System (Type 'exit' to quit) ---")
    
    while True:
        # 1. Take input and strip any extra whitespace
        user_input = input("\nEnter a mark (0 to 100) or 'exit': ").strip()
        
        # Check if the user wants to close the program
        if user_input.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
            
        # 2. Handle edge cases (non-numbers)
        try:
            mark = float(user_input)
        except ValueError:
            print(f"Error: '{user_input}' is not a valid number. Please try again.")
            continue

        # 3. Handle edge cases (numbers out of the 0-100 range)
        if mark < 0 or mark > 100:
            print(f"Error: The mark {mark} is out of bounds. Must be between 0 and 100.")
            continue

        # 4. Determine the grade using the requested grading scale
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

        # 5. Print a clear output message
        print(f"Result -> Mark: {mark} | Grade: {grade}")

if __name__ == "__main__":
    main()
