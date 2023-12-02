test_input = open("puzzle_input", "r")
id_sum = 0
id_num = 0

possible_reds = 12
possible_greens = 13
possible_blues = 14

for line in test_input.readlines():
    print(line)
    id_num += 1
    # In this situation it's better to check
    # for false cases instead of true ones
    possible_game = True

    game = [g.split(",") for g in line.rstrip().split(":")[1].split(";")]

    for reveal in game:
        reds = blues = greens = 0
        for cubes in reveal:
            if "blue" in cubes:
                blues += int(cubes.split("blue")[0])
            elif "red" in cubes:
                reds += int(cubes.split("red")[0])
            else:
                greens += int(cubes.split("green")[0])
        if reds > possible_reds or greens > possible_greens or blues > possible_blues:
            possible_game = False
            break

    if possible_game:
        id_sum += id_num

print(id_sum)
