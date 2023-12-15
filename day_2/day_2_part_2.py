def create_structure(input_file):
    my_input = open(input_file, 'r', encoding='utf-8')
    data_structure = {}

    for line in my_input:
        game_number = line.split(":")[0]
        throws = line.split(": ")[1].split("; ")
        for element in game_number.split(" "):
            if element.isnumeric():
                data_structure[int(element)] = throws

    for key, value in data_structure.items():
        rgb_sorted_games = []
        for element in value:
            rgb_sorted_cubes = [0, 0, 0]
            color_separated = element.split(",")
            for cube in color_separated:
                if "red" in cube:
                    split_cube = cube.split(' ')
                    for character in split_cube:
                        if character.isnumeric():
                            rgb_sorted_cubes[0] = int(character)
                elif "green" in cube:
                    split_cube = cube.split(' ')
                    for character in split_cube:
                        if character.isnumeric():
                            rgb_sorted_cubes[1] = int(character)
                else:
                    split_cube = cube.split(' ')
                    for character in split_cube:
                        if character.isnumeric():
                            rgb_sorted_cubes[2] = int(character)

            rgb_sorted_games.append(rgb_sorted_cubes)

        data_structure[key] = rgb_sorted_games

    return data_structure


def get_max_values(data_structure):
    global_max_values = []
    for key, value in data_structure.items():
        local_max_values = None
        red = []
        green = []
        blue = []

        for element in value:
            red.append(element[0])
            green.append(element[1])
            blue.append(element[2])

        local_max_values = (max(red), max(green), max(blue))
        global_max_values.append(local_max_values)

    return global_max_values


def get_sum_of_powers(max_values):
    addition = 0
    for element in max_values:
        final_power = 1
        for number in element:
            final_power *= number
        addition += final_power

    return addition


my_structure = create_structure('input.txt')
my_max_values = get_max_values(my_structure)
result = get_sum_of_powers(my_max_values)
print(result)