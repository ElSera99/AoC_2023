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


def get_possible_games(number_of_cubes, data_structure):
    filtered_data_structure = data_structure.copy()
    for key, value in data_structure.items():
        for element in value:
            if element[0] > number_of_cubes[0] or element[1] > number_of_cubes[1] or element[2] > number_of_cubes[2]:
                del filtered_data_structure[key]
                break
    return filtered_data_structure


#                       R, G, B
number_of_cubes_rule = (12, 13, 14)
my_structure = create_structure('input.txt')
possible_games = get_possible_games(number_of_cubes_rule, my_structure)
result = sum(possible_games.keys())
print(result)