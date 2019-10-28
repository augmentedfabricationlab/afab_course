def check_winner(list_ttt):
    comb_three = []
    for i,row in enumerate(list_ttt):
        comb_three.append(row)
    for j, el in enumerate(list_ttt[0]):
        comb_three.append([list_ttt[0][j],  list_ttt[1][j], list_ttt[2][j]])
    comb_three.append([list_ttt[0][0], list_ttt[1][1], list_ttt[2][2]])
    comb_three.append([list_ttt[0][2], list_ttt[1][1], list_ttt[2][0]])
    
    
    for comb in comb_three:
        if type(comb[0]) == str:
            if all(x == comb[0] for x in comb):
                print("Winner")
                return True
    return False


def play():
    row_1 = input("row nb X ")
    column_1 = input("column_nb X ")
    tictactoe_list[int(row_1)][int(column_1)] = "X"
#    print_ttt(tictactoe_list)

    win_test = check_winner(tictactoe_list)
    if win_test == True:
        print("You won!!")
        return True

    row_2 = input("row nb O ")
    column_2 = input("column_nb O ")
    tictactoe_list[int(row_2)][int(column_2)] = "O"
#    print_ttt(tictactoe_list)

    win_test = check_winner(tictactoe_list)
    if win_test == True:
        print("You won!!")
        return True
    
    return False
    
    
tictactoe_list = [[1,1,1],
                 [1,1,1],
                 [1,1,1]]

for i in range(10):
    win_test = play()
#     print("win output", win_test)
    if win_test == True:
        print("You won!!")
        break