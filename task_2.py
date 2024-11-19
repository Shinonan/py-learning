# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def csv_to_json(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':

    csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)

with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
