def count_frequency(input_list):
    frequency_count = {}

    for element in input_list:
        frequency_count[element] = frequency_count.get(element, 0) + 1

    return frequency_count

input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
result = count_frequency(input_list)

print(f"Input List: {input_list}")
print(f"Frequency count: {result}")