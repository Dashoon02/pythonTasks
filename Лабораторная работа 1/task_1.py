numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
new_numbers = numbers[:4] + numbers[5:]
average = [sum(new_numbers)/(len(new_numbers)+1)]
end_numbers = []
end_numbers += numbers[:4]
end_numbers += average
end_numbers += numbers[5:]
print("Измененный список:", end_numbers)
