test_input = open("fdsj", "r")
num_sum = 0
c = 0
for l in test_input.readlines():
    c += 1
    s = l.rstrip()
    num_indexes = {}
    num_string = ""
    num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
              "seven": 7, "eight": 8, "nine": 9}
    curr = ""
    for j in l:
        curr += j
        for n in num_dict.keys():
            if n in curr:
                num_string += f"{num_dict[n]}"
                curr = ""
        for n in "123456789":
            if n in curr:
                num_string += n
                curr = ""


    firstnum = num_string[0]
    secondnum = num_string[len(num_string) - 1]
    print(c, firstnum, secondnum)
    num_sum += int(f"{firstnum}{secondnum}")
print(num_sum)
