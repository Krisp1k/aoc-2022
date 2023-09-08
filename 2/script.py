
       # (A) rock       VS  (Y) paper - 2
       # (B) paper      VS  (Z) scissors - 3 
       # (C) scisorrs   VS  (X) rock - 1
       # 6 VÝHRA
       # 3 REMÍZA
       # 0 PROHRA

file = open("input.txt", "r")

def solution_part_1():

    points = 0

    for line in file:
        opponent_value =  (line.split(" ")[0]).strip()
        my_value = (line.split(" ")[1]).strip()
        
        win = 0

        # za použitou věc
        if my_value == "X":
            points += 1
        elif my_value == "Y":
            points += 2
        elif my_value == "Z":
            points += 3
        
        # remíza    
        if (my_value == "X" and opponent_value == "A") or (my_value == "Y" and opponent_value == "B") or (my_value == "Z" and opponent_value == "C"):
            points += 3
        # prohra
        elif (my_value == "X" and opponent_value == "B") or (my_value == "Y" and opponent_value == "C") or (my_value == "Z" and opponent_value == "A"):
            win = 0
        # výhra
        else:
            win = 1
            points += 6    
            
        #print(line + " " + str(points))
    return points

# print(solution_part_1()) # správně : 11449

def solution_part_2():
    
    points = 0

    for line in file:
        opponent_value =  (line.split(" ")[0]).strip()
        my_value = (line.split(" ")[1]).strip()

        win = 0
        remiza = 0
        loss = 0
        
        if (my_value == "X"):
            loss = 1
            points += 0

        elif (my_value == "Y"):
            remiza = 1
            points += 3

        elif (my_value == "Z"):
            win = 1
            points += 6  

        points += 1 

        # # remíza    
        # if (my_value == "X" and opponent_value == "A") or (my_value == "Y" and opponent_value == "B") or (my_value == "Z" and opponent_value == "C"):
        #     points += 3
        # # prohra
        # elif (my_value == "X" and opponent_value == "B") or (my_value == "Y" and opponent_value == "C") or (my_value == "Z" and opponent_value == "A"):
        #     points += 0
        # # výhra
        # else:
        #     points += 6  
    
        print(points)
        


    return points

print(solution_part_2())

file.close()