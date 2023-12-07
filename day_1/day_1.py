def get_input(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(line)
    print(data)
    return data


def get_numbers(input_data):
    integers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    my_numbers = []
    for line in input_data:
        number = ""
        for element in line:
            if element in integers:
                number += element
                break
        for element in line[::-1]:
            if element in integers:
                number += element
                break
        my_numbers.append(number)
    print(my_numbers)
    return my_numbers


def get_result(string_numbers):
    added = 0
    for element in string_numbers:
        added += int(element)
        print(f"{added} - {type(added)}")
    print(added)
    return added


data_test = get_input('input.txt')
numbers = get_numbers(data_test)
result = get_result(numbers)
