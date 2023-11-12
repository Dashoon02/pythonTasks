import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def csv_to_json(input_file, output_file):
    with open(input_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

def task() -> None:
    csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")