file = open('4/input.txt', 'r')
lines = file.readlines()

def solution_1():

    subsets = 0

    for index, line_ in enumerate(lines):
        line = line_.replace("\n", "").replace("\r", "");
        
        first_duo = line.split(",")[0]
        second_duo = line.split(",")[1]

        first_digit_1 = int(first_duo.split("-")[0])
        first_digit_2 = int(first_duo.split("-")[1])

        second_digit_1 = int(second_duo.split("-")[0])
        second_digit_2 = int(second_duo.split("-")[1])

        first_set = list(range(first_digit_1, first_digit_2 + 1))
        second_set = list(range(second_digit_1, second_digit_2 + 1))

        # print(index)
        # print(first_set)
        # print(second_set)
        #print(index)
        #print(first_set, second_set)

        if len(first_set) != 0 and len(second_set) != 0:
            if set(first_set).issubset(second_set) or set(second_set).issubset(first_set):
                subsets += 1

    print(subsets)


def solution_2():

    overlaps = 0

    for index, line_ in enumerate(lines):
        line = line_.replace("\n", "").replace("\r", "");
        
        first_duo = line.split(",")[0]
        second_duo = line.split(",")[1]

        first_digit_1 = int(first_duo.split("-")[0])
        first_digit_2 = int(first_duo.split("-")[1])

        second_digit_1 = int(second_duo.split("-")[0])
        second_digit_2 = int(second_duo.split("-")[1])

        first_set = list(range(first_digit_1, first_digit_2 + 1))
        second_set = list(range(second_digit_1, second_digit_2 + 1))

        # print(index)
        # print(first_set)
        # print(second_set)
        #print(index)
        #print(first_set, second_set)

        if len(first_set) != 0 and len(second_set) != 0:
            if not set(first_set).isdisjoint(second_set) or not set(second_set).isdisjoint(first_set):
                overlaps += 1


    print(overlaps)


solution_1() # 490  
solution_2() # 921

file.close()