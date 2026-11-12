import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("results.txt")

SUBJECTS = ["Maths", "Physics", "Chemistry"]


# Load Student Records
def load_records():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


# Save Student Records
def save_records(records):
    with open(DATA_FILE, "w") as file:
        json.dump(records, file, indent=4)


# Calculate Result
def calculate_result(marks):

    total = sum(marks.values())

    percentage = (total / 300) * 100

    if all(mark >= 40 for mark in marks.values()):
        result = "Pass"
    else:
        result = "Fail"

    return total, percentage, result


# Add Student
def add_student(records):

    print("\n--- Add Student ---")

    roll = input("Enter Roll Number: ").strip()

    if not roll:
        print("Roll number cannot be empty.")
        return

    for student in records:
        if student["roll_no"].casefold() == roll.casefold():
            print("Roll number already exists.")
            return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    marks = {}

    for subject in SUBJECTS:

        while True:
            try:
                mark = int(input(f"Enter {subject} Marks: "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Enter a valid number.")

    total, percentage, result = calculate_result(marks)

    student = {
        "roll_no": roll,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "result": result
    }

    records.append(student)

    save_records(records)

    print("\nRecord Added Successfully!")
    print("Total:", total)
    print("Percentage:", f"{percentage:.2f}%")
    print("Result:", result)


# View All Records
def view_records(records):

    print("\n--- All Student Records ---")

    if not records:
        print("No Records Found.")
        return

    for student in records:

        print("\nRoll Number:", student["roll_no"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Percentage:",
              f'{student["percentage"]:.2f}%')
        print("Result:", student["result"])


# Rank List
def rank_list(records):

    print("\n--- Rank List ---")

    if not records:
        print("No Records Found.")
        return

    sorted_records = sorted(
        records,
        key=lambda x: x["total"],
        reverse=True
    )

    for rank, student in enumerate(sorted_records, 1):

        print(
            f"Rank {rank} | "
            f'{student["roll_no"]} | '
            f'{student["name"]} | '
            f'{student["total"]} | '
            f'{student["percentage"]:.2f}% | '
            f'{student["result"]}'
        )


# Main Function
def main():

    records = load_records()

    while True:

        print("\n================================")
        print(" EXAM RESULT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Student")
        print("2. View All Records")
        print("3. Rank List")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_student(records)

        elif choice == "2":
            view_records(records)

        elif choice == "3":
            rank_list(records)

        elif choice == "4":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()