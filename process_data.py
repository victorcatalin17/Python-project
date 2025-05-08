import csv
from utils import calculate_average, assign_grade, calculate_total

def process_grades(filename):
    students = []

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            for row in reader:
                if len(row) < 4:
                    print(f"Skipping incomplete row: {row}")
                    continue

                name, math, science, english = row

                try:
                    scores = [int(math), int(science), int(english)]
                except ValueError:
                    print(f"Skipping invalid score data: {row}")
                    continue

                total = calculate_total(scores)
                average = calculate_average(scores)
                grade = assign_grade(average)

                students.append([name, total, average, grade])

        # Write results to output file
        with open('student_results.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Total', 'Average', 'Grade'])
            writer.writerows(students)

        print("Results saved to student_results.csv")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
