import random
def game_mod_select(main_dict):
    while True:
        game_mod=input("select game_mod:\n"
                       "P - PVP\n"
                       "C - PVC\n")
        if game_mod.lower() in ["c",'p']:
            break
        else:
            print('must chose game mode')
    main_dict['game_mode']=game_mod
    if main_dict['game_mode'].lower()=="p":
        print("you have chosen Player vs Player")
    if main_dict['game_mode'].lower()=="c":
        print("you have chosen Player vs Computer")
def shape_select(main_dict):
    def player1_select():
        import random
        print("player 1")
        while True:
            chosen_shape = input("chose [X,O] or 'R' random select ?\n")
            if chosen_shape.lower() in ['x', 'o', 'r']:
                break
            else:
                print('enter your chosen shape')
        if chosen_shape.upper() == 'R':
            chosen_shape = random.choice(['x', 'o'])
        return chosen_shape
    main_dict['player1_shape']= player1_select()
    if main_dict['player1_shape'].lower() =="x":
        main_dict['player2_shape']="o"
    elif main_dict['player1_shape'].lower() =="o":
        main_dict['player2_shape']="x"
    if main_dict['game_mode']=='p':
        print(f'player1={main_dict['player1_shape'].upper()}\n'
              f'player2={main_dict['player2_shape'].upper()}')
    if main_dict['game_mode'] == 'c':
        print(f'player1={main_dict['player1_shape'].upper()}\n'
              f'computer={main_dict['player2_shape'].upper()}')
    print("\n")
def print_board(main_dict):
    showboard=main_dict['show_board_list']
    print(f'\n{showboard[0]}|{showboard[1]}|{showboard[2]}\n'
          f'{showboard[3]}|{showboard[4]}|{showboard[5]}\n'
          f'{showboard[6]}|{showboard[7]}|{showboard[8]}\n')
def who_starts(main_dict):
    print("coin toss\n")
    import random
    main_dict['turn']=random.choice([1,2])
    if main_dict['turn']==1:
        print("Player 1 begins")
    else:
        print('Player 2 begins')
def turn(main_dict):
    if main_dict["turn"]==1:
        main_dict["turn"]=2
    elif main_dict["turn"]==2:
        main_dict["turn"] = 1
    else:
        print('turn_error')
def PVP_place_on_board(main_dict):
    def PVP_place_on_board_variables(main_dict):
        show_board = main_dict['show_board_list']
        vacant_spots = main_dict['vacant_spots']
        player_num = main_dict['turn']
        player_shape = ("")
        if player_num == 1:
            print("player 1 Play:\n")
            player_shape = main_dict['player1_shape'].upper()
        elif player_num == 2:
            print("player 2 Play:\n")
            player_shape = main_dict['player2_shape'].upper()
        return player_shape, show_board, vacant_spots
    player_shape, show_board, vacant_spots = PVP_place_on_board_variables(main_dict)
    print_board(main_dict)
    while True:
        chose_placement=input(f"chose where to place {vacant_spots}:\n")
        if chose_placement.isdigit():
            chose = int(chose_placement)
            if chose in vacant_spots:
                show_board[chose - 1] = player_shape
                vacant_spots.remove(chose)
                if player_shape == "X":
                    main_dict['X_list'].append(chose)
                elif player_shape == "O":
                    main_dict['O_list'].append(chose)
                break
            else:
                print('must be a number corresponding with a vacant spot on the board')
        else:
            print('Invalid Input')
    main_dict['vacant_spots']=vacant_spots
    main_dict['show_board_list']=show_board
    main_dict["round_num"]+=1
def PVC_place_on_board(main_dict):
    show_board = main_dict['show_board_list']
    vacant_spots = main_dict['vacant_spots']
    player_num = main_dict['turn']
    player_shape = ("")
    if player_num == 1:
        print("player 1 Play:\n")
        player_shape = main_dict['player1_shape'].upper()
        print_board(main_dict)
        while True:
            chose_placement = input(f"chose where to place {vacant_spots}:\n")
            if chose_placement.isdigit():
                chose = int(chose_placement)
                if chose in vacant_spots:
                    show_board[chose - 1] = player_shape
                    vacant_spots.remove(chose)
                    if player_shape == "X":
                        main_dict['X_list'].append(chose)
                    elif player_shape == "O":
                        main_dict['O_list'].append(chose)
                    break
                else:
                    print('must be a number corresponding with a vacant spot on the board')
            else:
                print('Invalid Input')
    elif player_num == 2:
        print("computer Play:\n")
        print_board(main_dict)
        player_shape = main_dict['player2_shape'].upper()
        chose=int(random.choice(vacant_spots))
        show_board[chose - 1] = player_shape
        vacant_spots.remove(chose)
        if player_shape == "X":
            main_dict['X_list'].append(chose)
        elif player_shape == "O":
            main_dict['O_list'].append(chose)


    main_dict['vacant_spots']=vacant_spots
    main_dict['show_board_list']=show_board
    main_dict["round_num"]+=1
def victory_tie_check(main_dict):
    vacant_spots=main_dict['vacant_spots']
    player1_shape=main_dict['player1_shape'].upper()
    O_list=main_dict['O_list']
    X_list=main_dict['X_list']
    win_dict=[[1,2,3],[4,5,6],[7,8,9],
              [1,4,5],[2,5,8],[3,6,9],
              [1,5,9],[3,5,7]]
    def X_win(X_list, main_dict, player1_shape, win_dict):
        for win in win_dict:
            check = 0
            for num in X_list:
                if num in win:
                    check += 1
            if check == 3:
                if player1_shape == "X":
                    main_dict['victory_val'] = 1
                elif player1_shape == "O":
                    main_dict['victory_val'] = 2
                break
    def O_win(O_list, main_dict, player1_shape, win_dict):
        for win in win_dict:
            check = 0
            for num in O_list:
                if num in win:
                    check += 1
            if check == 3:
                if player1_shape == "O":
                    main_dict['victory_val'] = 1
                elif player1_shape == "X":
                    main_dict['victory_val'] = 2
                break
    if main_dict['victory_val']==0:
        if main_dict['round_num'] == 9:
            main_dict['victory_val'] = 3
            print_board(main_dict)
    O_win(O_list, main_dict, player1_shape, win_dict)
    X_win(X_list, main_dict, player1_shape, win_dict)
def print_check_dict(main_dict):
    print("\n")
    for i in main_dict:
        print(f'{i}:{main_dict[i]}')
    print('\n')
def main_game():
    game_dict = {'O_list': [], 'X_list': [],
                 'show_board_list': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 'vacant_spots': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                 'player1_shape': "", 'player2_shape': "",
                 'game_mode': "", 'turn': "", "round_num": 0,
                 "victory_val": 0}
    game_mod_select(game_dict)
    shape_select(game_dict)
    who_starts(game_dict)
    while game_dict['victory_val']==0:
        if game_dict['game_mode']=="p":#PVP MODE
            PVP_place_on_board(game_dict)
            victory_tie_check(game_dict)
            turn(game_dict)
        elif game_dict['game_mode']=="c":#PVC
            PVC_place_on_board(game_dict)
            victory_tie_check(game_dict)
            turn(game_dict)
    if game_dict["victory_val"]==3:
        print("Its a Tie!")
    elif game_dict["victory_val"]==2:
        print("Player 2 Victory")
    elif game_dict["victory_val"]==1:
        print("Player 1 Victory")
    else:
        print('error')
    print_board(game_dict)
    print(50*"-")
main_game()

