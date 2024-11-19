# TODO решите задачу

import json

json_file = 'input.json'
def task(json_file) -> float:
    with open(json_file, 'r') as file:
        data = json.load(file)

        total_sum = sum(num["score"] * num["weight"] for num in data)

        return round(total_sum, 3)

print(task(json_file))
