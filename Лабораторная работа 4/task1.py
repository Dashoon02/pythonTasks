import json


def calculate_product_sum(json_file) -> float:
    with open(json_file, 'r') as file:
        data = json.load(file)

    product_sum = sum(entry["score"] * entry["weight"] for entry in data)

    return round(product_sum, 3)


# Пример использования функции
def task() -> float:
    json_file = "input.json"
    return calculate_product_sum(json_file)


print(task())
