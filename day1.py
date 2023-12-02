# Input file
test_input = open("input", "r")
num_sum = 0
c = 0

for l in test_input.readlines():
    c += 1
    s = l.rstrip()
    num_indexes = {}
    num_string = ""
    # spelled number dict for conversion to a regular integer (zero is not included)
    num_dict = {"one": 1, "two": 2, "three": 3,
                "four": 4, "five": 5, "six": 6,
                "seven": 7, "eight": 8, "nine": 9}
    
    # past and curr are used for combined spelled numbers, explained later in line 22
    past = ""
    curr = ""
    for j in l:
        curr += j
        for n in num_dict.keys():
            # a bit sloppy but gets the job done. the second expression in the or statement makes sure numbers
            # like "oneight" are interpreted correctly as "18"
            # though the input has no "threeight"s this would also work with those too
            if n in curr or (n in past + curr and n not in curr and n not in past):
                num_string += f"{num_dict[n]}"
                past = curr
                curr = ""
        # check for regular digits
        for n in "123456789":
            if n in curr:
                num_string += n
                past = curr
                curr = ""
                
    # puzzle states the sum includes the first and last numbers of each line
    firstnum = num_string[0]
    secondnum = num_string[len(num_string) - 1]
    num_sum += int(f"{firstnum}{secondnum}")

print(num_sum)
