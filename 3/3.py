file = open('3/input.txt', 'r')
lines = file.readlines()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def solution_part_1():
    sum_of_priorities = 0

    for line in lines:
        string1 = slice(0, len(line) // 2)
        string2 = slice(len(line) // 2, len(line))

        part1 = line[string1].replace("\n", "").replace("\r", "");
        part2 = line[string2].replace("\n", "").replace("\r", "");

        for letter in part1:
            if letter in part2:
                priority = letters.index(letter) + 1
                #print(letter + " " + str(priority))
                sum_of_priorities += priority
                break


        # for priority, letter in enumerate(letters): 
        #     #print(str(priority) + " : " + letter)

        #print(part1 + " a " + part2)

    print(sum_of_priorities)

#solution_part_1()

def solution_part_2():

    sum_of_priorities = 0
    groups = []
    new_group = []

    for index, line in enumerate(lines):
        
        line_ = line.replace("\n", "").replace("\r", "");
        new_group.append(line_)

        if ((index + 1) % 3) == 0: 
            groups.append(new_group)
            new_group = []

    #print(groups)

    for group in groups:

        string_1 = group[0]
        string_2 = group[1]
        string_3 = group[2]

        for letter in string_1:
            if letter in string_2 and letter in string_3:
                priority = letters.index(letter) + 1
                #print(letter + " " + str(priority))
                sum_of_priorities += priority
                break
        
        #print(" ") 
    print(sum_of_priorities)

solution_part_2()


file.close()