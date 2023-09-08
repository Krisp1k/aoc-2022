file = open('6/input.txt', 'r')
lines = file.readlines()

def solution_1():
    
    x_log = 0
    signal_strength = 0
    signals = [20, 60, 100, 140, 180, 220]
    
    for line_index, line_ in enumerate(lines):
        line = line_.replace("\n", "").replace("\r", "")
        
        if (line != "noop"):
            
            x = int(line.split(" ")[1]) 
            x_log += x
            print(x_log)

            if (line_index in signals):
                print("signal++ a je " + str(x_log))
            

solution_1()

file.close()