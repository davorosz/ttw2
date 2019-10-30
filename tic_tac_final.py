
import os # Import external function libraries
import time
#################################
table = [] # Declaration of global variables
row = []
Running = True # runnin condition
move = 1 # whose round variable
playersign = "" # player sign
win_size = 3 # winning requirement


#################################
# My functions
#####
def table_set(size): # setting the table
    row = "·" * size
    for i in range(size):
        table.append(row)
#####
def step_conv(step): #converting from alpha to num
    tempstr = "ABCDEFGHIJ"
    return (str(tempstr.find(step[0])) + step[1])
#####
def full_check(): # The table is full?
    for i in table:
        for j in i:
            if j == "·":
                return True
    return False        
#####
def spot_check(step):
    if table[int((step_conv(step)[0]))][int(step_conv(step)[1])] == "·":
        return True
    else:
        return False 
#####
def step_check(step,table_size): # inputcheck
    rangeV = "ABCDEFGHIJ"
    rangeH = "0123456789"
    end = int(table_size)
    if step[0] in rangeV[0:end] and step[1] in rangeH[0:end] and len(step) == 2:
        return False
    else:
        print("Wrong input!")
        time.sleep(1)
        return True
#####
def step_save(step, playersign): # Saving the step
    global table
    table[int(step_conv(step)[0])] = string_replace_i(table[int(step_conv(step)[0])], int(step[1]), playersign)
#####
def input_step(size):
    step = input("Next step: ")
    return step
#####
def string_replace_i(string,where,what): # Character replacing at index in a string 
    tempS = ""
    for i in range(len(string)):
        if i != int(where):
            tempS += string[i]
        else:
            tempS += what
    return tempS
#####   
def visual(size): # Visual representation
    os.system("clear")
    ver = "  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |"
    v_l = "------------------------------------------------"
    hor = "ABCDEFGHIJ"
    size = str(int(size)-1)
    end = ver.find(size) + 1
    os.system("clear")
    print()
    print("TicTac (ver. Beta 1.01)")
    print()
    print("You need " + str(win_size) + " sign in a row to win!")
    print()
    print(v_l[0:end+4]) # line
    print("| " + ver[0:end+2]) # head
    print(v_l[0:end+4]) # line
    for i in range(int(size)+1): # table
        temp_row = ""
        for j in table[i]:
            temp_row += " | "
            temp_row += j 
        print("| " + hor[i:i+1] + temp_row + " |")
        print(v_l[0:end+4]) #line
#####
def again(): # Game again?
    global Running
    while True:
        print()
        end = input("Would you like to play again? (Y / N): ")
        if end == "N":
            Running = False
            os.system("clear")
            print()
            print("Thank you for the playing!")
            print()
            print("See you next time!")
            print()
            break
        elif end == "Y":
            break
        else:
            print("Wrong input!")
            time.sleep(1)
#####
def input_size():
    global win_size
    while True:
        table_size = input("Give me the size of the table (3 - 10): ")
        try:
            X = int(table_size)
        except TypeError:
            print("Wrong input!")
            time.sleep(1)
        except ValueError:
            print("Wrong input!")
            time.sleep(1)
        else:
            if int(table_size) >= 3 and int(table_size) <= 10:
                table_set(int(table_size))
                while True:
                    win_size = input("Winning requirement? (3 - " + str(table_size) + "): ")
                    try:
                        Y = int(win_size)
                    except TypeError:
                        print("Wrong input!")
                        time.sleep(1)
                    except ValueError:
                        print("Wrong input!")
                        time.sleep(1)
                    else:
                        if int(win_size) >= 3 and int(win_size) <= len(table):
                            break
                break
#####
def gen_pos_str(table): # generating all the possible strings
    plist = []
    for row in table:
        plist.append(row)
    column = ""
    for r in range(len(table)):
        column = ""
        for c in range(len(table)):
            column += table[c][r]
        plist.append(column)
    return plist
#####
def gen_diagonal_str(table):
    table2 = table.copy()
    table3 = table.copy()
    list = []

    buffer = len(table2)-1
    debuffer = 0
    for x in range(len(table2)):
        table2[x] = buffer * "B" + table2[x] + debuffer * "B"
        buffer -= 1
        debuffer += 1

    buffer = 0
    debuffer = len(table3)-1
    for x in range(len(table3)):
        table3[x] = buffer * "B" + table3[x] + debuffer * "B"
        buffer += 1
        debuffer -= 1

    for i in range((len(table2)*2)-1):
        tempstr = ""
        for j in range(len(table2)):
            tempstr += table2[j][i]
        list.append(tempstr.replace("B",""))

    for i in range((len(table3)*2)-1):
        tempstr = ""
        for j in range(len(table3)):
            tempstr += table3[j][i]
        list.append(tempstr.replace("B",""))
    return list
#####
def input_f():
    while True:
        global move
        visual(len(table))
        if move % 2 == 0:
            print()
            print("This is the O player's round!")
            print()
            playersign = "O"
        else:
            print()
            print("This is the X player's round!")
            print()
            playersign = "X"
        step = input_step(len(table))
        if step_check(step, len(table)) == False:
            if spot_check(step) == True:
                step_save(step,playersign)
                move += 1
                break
#####
def win_check(list,req):
    x_win = "X" * int(req)
    o_win = "O" * int(req)
    for items in list:
        if x_win in items:
            return "x-win"
        if o_win in items:
            return "o-win"
        if full_check() == False:
            return "tie"
    return "none"
        
############################################

# Main part start
while Running:
    os.system("clear")
    input_size()        
    while True:
        listofall = []
        input_f()
        visual(len(table))
        listofall.extend(gen_pos_str(table))
        listofall.extend(gen_diagonal_str(table))
        win = win_check(listofall, win_size)
        if win == "x-win":
            print()
            print("The X player is the winner!")
            break
        elif win == "o-win":
            print()
            print("The O player is the winner!")
            break
        elif win == "tie":
            print()
            print("It is a Tie!")
            break
    again()
    table = [] # Declaration of global variables
    row = []
    move = 1
    playersign = ""
