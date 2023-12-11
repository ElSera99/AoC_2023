import re

def get_input(file_path):
    data = []
    with open(file_path, 'r', encoding="UTF-8") as file:
        for line in file:
            data.append(line)
    print(data)
    return data


def get_numbers(input_data):
    my_regex = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    equivalents = {"one": '1',
                   "two": '2',
                   "three": '3',
                   "four": '4',
                   "five": '5',
                   "six": '6',
                   "seven": '7',
                   "eight": '8',
                   "nine": '9'}
    
    my_numbers = []

    increase = 1
    for line in input_data:
        number = ""
        try:
            coincidences = re.findall(my_regex, line)
            first_digit = equivalents.get(coincidences[0], coincidences[0])
            second_digit = equivalents.get(coincidences[-1], coincidences[-1])
            number = first_digit + second_digit
            increase += 1
        except:
            pass
        my_numbers.append(number)
    
    print(my_numbers)
    return my_numbers


def get_result(string_numbers):
    added = 0
    for element in string_numbers:
        try:
            added += int(element)
        except:
            added += 0
    print(added)
    return added


data_test = get_input('input.txt')
numbers = get_numbers(data_test)
result = get_result(numbers)
