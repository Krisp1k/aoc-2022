file = open('input.txt', 'r')
lines = file.readlines()

# [B]                     [N]     [H]
# [V]         [P] [T]     [V]     [P]
# [W]     [C] [T] [S]     [H]     [N]
# [T]     [J] [Z] [M] [N] [F]     [L]
# [Q]     [W] [N] [J] [T] [Q] [R] [B]
# [N] [B] [Q] [R] [V] [F] [D] [F] [M]
# [H] [W] [S] [J] [P] [W] [L] [P] [S]
# [D] [D] [T] [F] [G] [B] [B] [H] [Z]
#  1   2   3   4   5   6   7   8   9 

def solution_1():
    
    col_1 = "DHNQTWVB"
    col_2 = "DWB"
    col_3 = "TSQWJC"
    col_4 = "FJRNZTP"
    col_5 = "GPVJMST"
    col_6 = "BWFTN"
    col_7 = "BLDQFHVN"
    col_8 = "HPFR"
    col_9 = "ZSMBLNPH"

    cols = [col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9]
    
    top_crates = ""
    
    for line_ in lines:
        line = line_.replace("\n", "").replace("\r", "")

        howmany_ = int(line.split(" ")[1]) 
        from_ = int(line.split(" ")[3])
        to_ = int(line.split(" ")[5]) 
        
        x = 0
        while x < howmany_:
            removed_char = cols[from_ - 1][-1]
            cols[to_ - 1] += removed_char
            cols[from_ - 1] = cols[from_ - 1][:-1]
            x += 1 
            #print(removed_char)
            
        #print("vem " + howmany_ + " z " + from_ + " a dej to do " + to_)
    
    for crate in cols:
        last_letter = crate[-1]
        top_crates += last_letter
        
    print("solution 1 : " + top_crates)
    
def solution_2():
    
    col_1 = "DHNQTWVB"
    col_2 = "DWB"
    col_3 = "TSQWJC"
    col_4 = "FJRNZTP"
    col_5 = "GPVJMST"
    col_6 = "BWFTN"
    col_7 = "BLDQFHVN"
    col_8 = "HPFR"
    col_9 = "ZSMBLNPH"

    cols = [col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9]
    
    top_crates = "" 
    
    for line_ in lines:
        line = line_.replace("\n", "").replace("\r", "")

        howmany_ = int(line.split(" ")[1]) 
        from_ = int(line.split(" ")[3])
        to_ = int(line.split(" ")[5]) 
        
        removed_chars = cols[from_ - 1][-howmany_:]
        cols[to_ - 1] += removed_chars
        cols[from_ - 1] = cols[from_ - 1][:-howmany_]
        
        #print(removed_chars)

    for crate in cols:
        last_letter = crate[-1]
        top_crates += last_letter
        
    print("solution 2 : " + top_crates)
    
solution_1()  
solution_2() 

file.close()