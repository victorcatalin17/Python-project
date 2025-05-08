import sys
from process_data import process_grades

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py students.csv")
        return
    input_file = sys.argv[1]
    process_grades(input_file)

if __name__ == '__main__':
    main()
