file = open('1/input.txt', 'r')
lines = file.readlines()

## # # # # # # # # #  PART 1 # # # # # # # # 
all_elves = []
new_arr_of_elves = []
sum_elves = []

for index, value in enumerate(lines):

    if (value.isspace()):
        #print("---------------")
        all_elves.append(new_arr_of_elves)
        new_arr_of_elves = []

    split_value = value.replace("\n", "").replace("\r", "");

    if (split_value != ''):
        new_arr_of_elves.append(int(split_value))
        #print(int(split_value))

#print(all_elves)


for elf_array in all_elves:
    sum_of_array = sum(elf_array)
    sum_elves.append(sum_of_array)


#print(sum_elves)

the_best_elf = max(sum_elves)
#print(the_best_elf) # VÝSLEDEK PART 1 = 69626




## # # # # # # # # #  PART 2 # # # # # # # # 

sum_elves.sort(reverse=True)
top_three_elves = []

top_three_elves.append(sum_elves[0])
top_three_elves.append(sum_elves[1])
top_three_elves.append(sum_elves[2])

top_three_elves_sum = sum(top_three_elves)
print(top_three_elves_sum)

file.close()