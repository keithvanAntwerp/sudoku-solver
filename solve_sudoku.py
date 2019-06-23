import time
from puzzle_set import puzzle_dict

def extract_None_address(sudoku_puzzle):
    '''Return a list of addresses of None in a list
    of 9 lists each with 9 values in the set
    {None, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    '''
    none_address_list = []
    for row in range(9):
        for col in range(9):
            if not sudoku_puzzle[row][col]:
                none_address_list.append((row, col))

    return none_address_list

def solve_sudoku(sudoku_puzzle):
    '''Return a solutions to to given Sudoku Puzzle
    '''
    t0 = time.time() #keep track of time
    sol_vect = extract_None_address(sudoku_puzzle)
    
    l = len(sol_vect) #length of solution vector
    ind = 0 #initialize index to 0
    iteration = 0 #keep track of iterations

    #check compatability of given puzzle
    if not check_all(sudoku_puzzle):
        print("Puzzle Not Valid")
        return None

    while ind < l:
        
        if check_all(sudoku_puzzle) and sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] == None: #check contraints for puzzle
            
            sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = 1
                
        if check_all(sudoku_puzzle) and sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 2: #if it works,
            
            ind += 1
            continue
        elif sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 2:
            sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = 2
                
        if check_all(sudoku_puzzle) and sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 3:
            #print(str(sol_vect[ind]) + "COND 3")
            ind += 1
            continue
        elif sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 3:
            sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = 3
                
        if check_all(sudoku_puzzle) and sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 4:
            #print(str(sol_vect[ind]) + "COND 4")
            ind += 1
            continue
        elif sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 4:
            sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = 4
                
        if check_all(sudoku_puzzle) and sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 5:
            #print(str(sol_vect[ind]) + "COND 5")
            ind += 1
            continue
        elif sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 5:
             sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = 5
                
        if check_all(sudoku_puzzle) and sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 6:
            #print(str(sol_vect[ind]) + "COND 6: " + str(sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]]))
            ind += 1
            continue
        elif sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 6:
            sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = 6
                
        if check_all(sudoku_puzzle) and sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 7:
            #print(str(sol_vect[ind]) + "COND 7")
            ind += 1
            continue
        elif sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 7:
            sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = 7

        if check_all(sudoku_puzzle) and sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 8:
            #print(str(sol_vect[ind]) + "COND 8")
            ind += 1
            continue
        elif sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 8: 
            sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = 8
                
        if check_all(sudoku_puzzle) and sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 9:
            #print(str(sol_vect[ind]) + "COND 9")
            ind += 1
            continue
        elif sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] < 9:
             sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = 9
                
        if check_all(sudoku_puzzle):
            #print(str(sol_vect[ind]) + "COND 10")
            ind += 1
            continue
                
                #if we come to this, we must back track
        else:
            #print(str(sol_vect[ind]) + "COND 11")
            sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = None #reset the last None checked to None
            ind -= 1

            if sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] != 9: #check previous None for reaching 9
                #print("COND 12: previous not equal to 9")
                sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] += 1
                
            else: 
                #print("COND 13: previous equal to 9")
                sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = None
                ind -= 1
                if sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] != 9:
                    sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] += 1
                    #time.sleep(4)
                    #print("FLAG", sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]])
                else: 
                    sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = None
                    ind -= 1
                    #time.sleep(4)
                    if sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] != 9:
                        sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] += 1
                    else: 
                        sudoku_puzzle[sol_vect[ind][0]][sol_vect[ind][1]] = None
                        ind -= 1
                        time.sleep(3)
                    

    
        #print(ind, iteration, sol_vect[ind])
        #print(sudoku_puzzle[0:3])
        iteration += 1
        #print(iteration)
        #time.sleep(0.001)
    tf = time.time()
    print("Time to Complete: " + str(tf-t0) + "\n" + "Number of Iterations: " + str(iteration))
    
    return sudoku_puzzle
                
def check_constraint(cons):
    '''Return True if a constraint is compatible (not necessarily complete)
    and False if a constraint is violated
    '''
    c1 = len(cons) - cons.count(None)
    set2 = set(cons)
    if None in set2:
        set2.remove(None)
    c2 = len(set2)
    if int(c1) == int(c2):
        return True
    else:
        return False

def check_all(sudoku_puzzle):
    '''Return True if sudoku Puzzle has not violated constraint
    Check until a constraint is violated and return False if violation.
    '''
    for item in list_sod_constraints(sudoku_puzzle):
        if not check_constraint(item):
            return False
    return True

def list_sod_constraints(sudoku_puzzle):
    '''Return a list of 27 constraints to check with check_constraint
    '''
    # THE 9 INNER BOXES
    b1 = []
    for row in range(3):
        for col in range(3):
            b1.append(sudoku_puzzle[row][col])

    b2 = []
    for row in range(3):
        for col in range(3,6):
            b2.append(sudoku_puzzle[row][col])

    b3 = []
    for row in range(3):
        for col in range(6,9):
            b3.append(sudoku_puzzle[row][col])

    b4 = []
    for row in range(3, 6):
        for col in range(3):
            b4.append(sudoku_puzzle[row][col])

    b5 = []
    for row in range(3, 6):
        for col in range(3, 6):
            b5.append(sudoku_puzzle[row][col])

    b6 = []
    for row in range(3, 6):
        for col in range(6, 9):
            b6.append(sudoku_puzzle[row][col])

    b7 = []
    for row in range(6,9):
        for col in range(3):
            b7.append(sudoku_puzzle[row][col])

    b8 = []
    for row in range(6,9):
        for col in range(3,6):
            b8.append(sudoku_puzzle[row][col])

    b9 = []
    for row in range(6,9):
        for col in range(6,9):
            b9.append(sudoku_puzzle[row][col])

    #The 9 rows
    h1 = sudoku_puzzle[0]
    h2 = sudoku_puzzle[1]
    h3 = sudoku_puzzle[2]
    h4 = sudoku_puzzle[3]
    h5 = sudoku_puzzle[4]
    h6 = sudoku_puzzle[5]
    h7 = sudoku_puzzle[6]
    h8 = sudoku_puzzle[7]
    h9 = sudoku_puzzle[8]
    
    #The 9 columns
    c1,c2,c3,c4,c5,c6,c7,c8,c9 = [],[],[],[],[],[],[],[],[]

    for row in range(9):
        c1.append(sudoku_puzzle[row][0])

    for row in range(9):
        c2.append(sudoku_puzzle[row][1])

    for row in range(9):
        c3.append(sudoku_puzzle[row][2])

    for row in range(9):
        c4.append(sudoku_puzzle[row][3])
    
    for row in range(9):
        c5.append(sudoku_puzzle[row][4])

    for row in range(9):
        c6.append(sudoku_puzzle[row][5])

    for row in range(9):
        c7.append(sudoku_puzzle[row][6])

    for row in range(9):
        c8.append(sudoku_puzzle[row][7])
    
    for row in range(9):
        c9.append(sudoku_puzzle[row][8])

    return [c1,c2,c3,c4,c5,c6,c7,c8,c9,h1,h2,h3,h4,h5,h6,h7,h8,h9,b1,b2,b3,b4,b5,b6,b7,b8,b9]

if __name__ == "__main__":
    puzzle = input("empty, easy, medium, hard, or hardest?: ")
    print("Solving...")
    print(*puzzle_dict[puzzle], sep = '\n')
    sod_solution = solve_sudoku(puzzle_dict[puzzle])
    print(*sod_solution, sep = '\n')
