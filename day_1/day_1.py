integers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

def get_input(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(line)
    
    return data

def get_numbers():
    # Get first and last digit
    pass

def addition_of_numbers():
    # Add all obtained numbers
    pass

data_test = get_input('input.txt')
print(data[1])