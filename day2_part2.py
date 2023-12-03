test_input = open("puzzle_input", "r")
id_sum = 0
num_sum = 0

for line in test_input.readlines():
    print(line)

    game = [g.split(",") for g in line.rstrip().split(":")[1].split(";")]
    max_reds = max_blues = max_greens = 0
    for reveal in game:
        reds = blues = greens = 0
        for cubes in reveal:
            if "blue" in cubes:
                blues += int(cubes.split("blue")[0])
            elif "red" in cubes:
                reds += int(cubes.split("red")[0])
            else:
                greens += int(cubes.split("green")[0])
        if reds > max_reds:
            max_reds = reds
        if greens > max_greens:
            max_greens = greens
        if blues > max_blues:
            max_blues = blues

    # Add power of sets to sum
    num_sum += max_reds * max_blues * max_greens


print(num_sum)
