# To-do: CASTLING!3
# To-do: En passant!
# To-do: decode classical way of inputting moves
# To-do: fix invalid moves bug (Done in Chess2)
# To-do: invalid move error messages (they are messed up) (Done in Chess2)
# To-do: nice interface (More or less done in Chess2)
# To-do: remake the whole code using DRY (Kinda done in Chess2)

chess_board = [[['R', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['R', 'b']],
               [['N', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['N', 'b']],
               [['B', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['B', 'b']],
               [['Q', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['Q', 'b']],
               [['K', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['K', 'b']],
               [['B', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['B', 'b']],
               [['N', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['N', 'b']],
               [['R', 'w'], ['p', 'w'], None, None, None, None, ['p', 'b'], ['R', 'b']]]

# To check if the move is off board to avoid errors
chess_board_positions = []
for i in range(8):
    for j in range(8):
        chess_board_positions += [[i, j]]


# Almost 300 lines about finding all the moves the piece on pos can make
def valid_moves(pos):
    possible_moves = []
    chess_type = chess_board[pos[0]][pos[1]][0]
    side = chess_board[pos[0]][pos[1]][1]

    if chess_type == 'R':
        for m in range(1, 8 - pos[0]):
            if not chess_board[pos[0] + m][pos[1]]:
                possible_moves += [[pos[0] + m, pos[1]]]
            elif (m == 1 and chess_board[pos[0] + m][pos[1]][1] != side) or \
                    (chess_board[pos[0] + m][pos[1]][1] != side and not chess_board[pos[0] + m - 1][pos[1]]):
                possible_moves += [[pos[0] + m, pos[1]]]
            else:
                break

        for m in range(1, 8 - pos[1]):
            if not chess_board[pos[0]][pos[1] + m]:
                possible_moves += [[pos[0], pos[1] + m]]
            elif (m == 1 and chess_board[pos[0]][pos[1] + m][1] != side) or \
                    (chess_board[pos[0]][pos[1] + m][1] != side and not chess_board[pos[0]][pos[1] + m - 1]):
                possible_moves += [[pos[0], pos[1] + m]]
            else:
                break

        for m in range(1, pos[1] + 1):
            if not chess_board[pos[0]][pos[1] - m]:
                possible_moves += [[pos[0], pos[1] - m]]
            elif (m == 1 and chess_board[pos[0]][pos[1] - m][1] != side) or \
                    (chess_board[pos[0]][pos[1] - m][1] != side and not chess_board[pos[0]][pos[1] - m + 1]):
                possible_moves += [[pos[0], pos[1] - m]]
            else:
                break

        for m in range(1, pos[0] + 1):
            if not chess_board[pos[0] - m][pos[1]]:
                possible_moves += [[pos[0] - m, pos[1]]]
            elif (m == 1 and chess_board[pos[0] - m][pos[1]][1] != side) or \
                    (chess_board[pos[0] - m][pos[1]][1] != side and not chess_board[pos[0] - m + 1][pos[1]]):
                possible_moves += [[pos[0] - m, pos[1]]]
            else:
                break

    elif chess_type == 'B':
        for m in range(1, 8):
            try:
                if not chess_board[pos[0] + m][pos[1] + m]:
                    possible_moves += [[pos[0] + m, pos[1] + m]]
                elif (m == 1 and chess_board[pos[0] + m][pos[1] + m][1] != side) or \
                        (chess_board[pos[0] + m][pos[1] + m][1] != side
                         and not chess_board[pos[0] + m - 1][pos[1] + m - 1]):
                    possible_moves += [[pos[0] + m, pos[1] + m]]
            except IndexError:
                break

        for m in range(1, 8):
            try:
                if not chess_board[pos[0] - m][pos[1] - m]:
                    possible_moves += [[pos[0] - m, pos[1] - m]]
                elif (m == 1 and chess_board[pos[0] - m][pos[1] - m][1] != side) or \
                        (chess_board[pos[0] - m][pos[1] - m][1] != side
                         and not chess_board[pos[0] - m + 1][pos[1] - m + 1]):
                    possible_moves += [[pos[0] - m, pos[1] - m]]
                else:
                    break
            except IndexError:
                break

        for m in range(1, 8):
            try:
                if not chess_board[pos[0] - m][pos[1] + m]:
                    possible_moves += [[pos[0] - m, pos[1] + m]]
                elif (m == 1 and chess_board[pos[0] - m][pos[1] + m][1] != side) or \
                        (chess_board[pos[0] - m][pos[1] + m][1] != side
                         and not chess_board[pos[0] - m + 1][pos[1] + m - 1]):
                    possible_moves += [[pos[0] - m, pos[1] + m]]
                else:
                    break
            except IndexError:
                break

        for m in range(1, 8):
            try:
                if not chess_board[pos[0] + m][pos[1] - m]:
                    possible_moves += [[pos[0] + m, pos[1] - m]]
                elif (m == 1 and chess_board[pos[0] + m][pos[1] - m][1] != side) or \
                        (chess_board[pos[0] + m][pos[1] - m][1] != side
                         and not chess_board[pos[0] + m - 1][pos[1] - m + 1]):
                    possible_moves += [[pos[0] + m, pos[1] - m]]
                else:
                    break
            except IndexError:
                break

    elif chess_type == 'N':
        for m in [-2, 2]:
            for t in [-1, 1]:
                if [pos[0] + m, pos[1] + t] in chess_board_positions:
                    if not chess_board[pos[0] + m][pos[1] + t]:
                        possible_moves += [[pos[0] + m, pos[1] + t]]
                    elif chess_board[pos[0] + m][pos[1] + t][1] != side:
                        possible_moves += [[pos[0] + m, pos[1] + t]]

                if [pos[0] + t, pos[1] + m] in chess_board_positions:
                    if not chess_board[pos[0] + t][pos[1] + m]:
                        possible_moves += [[pos[0] + t, pos[1] + m]]
                    elif chess_board[pos[0] + t][pos[1] + m][1] != side:
                        possible_moves += [[pos[0] + t, pos[1] + m]]

    elif chess_type == 'Q':
        # Bishop moves
        for m in range(1, 8):
            try:
                if not chess_board[pos[0] + m][pos[1] + m]:
                    possible_moves += [[pos[0] + m, pos[1] + m]]
                elif (m == 1 and chess_board[pos[0] + m][pos[1] + m][1] != side) or \
                        (chess_board[pos[0] + m][pos[1] + m][1] != side
                         and not chess_board[pos[0] + m - 1][pos[1] + m - 1]):
                    possible_moves += [[pos[0] + m, pos[1] + m]]
            except IndexError:
                break

        for m in range(1, 8):
            try:
                if not chess_board[pos[0] - m][pos[1] - m]:
                    possible_moves += [[pos[0] - m, pos[1] - m]]
                elif (m == 1 and chess_board[pos[0] - m][pos[1] - m][1] != side) or \
                        (chess_board[pos[0] - m][pos[1] - m][1] != side
                         and not chess_board[pos[0] - m + 1][pos[1] - m + 1]):
                    possible_moves += [[pos[0] - m, pos[1] - m]]
                else:
                    break
            except IndexError:
                break

        for m in range(1, 8):
            try:
                if not chess_board[pos[0] - m][pos[1] + m]:
                    possible_moves += [[pos[0] - m, pos[1] + m]]
                elif (m == 1 and chess_board[pos[0] - m][pos[1] + m][1] != side) or \
                        (chess_board[pos[0] - m][pos[1] + m][1] != side
                         and not chess_board[pos[0] - m + 1][pos[1] + m - 1]):
                    possible_moves += [[pos[0] - m, pos[1] + m]]
                else:
                    break
            except IndexError:
                break

        for m in range(1, 8):
            try:
                if not chess_board[pos[0] + m][pos[1] - m]:
                    possible_moves += [[pos[0] + m, pos[1] - m]]
                elif (m == 1 and chess_board[pos[0] + m][pos[1] - m][1] != side) or \
                        (chess_board[pos[0] + m][pos[1] - m][1] != side
                         and not chess_board[pos[0] + m - 1][pos[1] - m + 1]):
                    possible_moves += [[pos[0] + m, pos[1] - m]]
                else:
                    break
            except IndexError:
                break

        # Rook moves
        for m in range(1, 8 - pos[0]):
            if not chess_board[pos[0] + m][pos[1]]:
                possible_moves += [[pos[0] + m, pos[1]]]
            elif (m == 1 and chess_board[pos[0] + m][pos[1]][1] != side) or \
                    (chess_board[pos[0] + m][pos[1]][1] != side and not chess_board[pos[0] + m - 1][pos[1]]):
                possible_moves += [[pos[0] + m, pos[1]]]
            else:
                break

        for m in range(1, 8 - pos[1]):
            if not chess_board[pos[0]][pos[1] + m]:
                possible_moves += [[pos[0], pos[1] + m]]
            elif (m == 1 and chess_board[pos[0]][pos[1] + m][1] != side) or \
                    (chess_board[pos[0]][pos[1] + m][1] != side and not chess_board[pos[0]][pos[1] + m - 1]):
                possible_moves += [[pos[0], pos[1] + m]]
            else:
                break

        for m in range(1, pos[1] + 1):
            if not chess_board[pos[0]][pos[1] - m]:
                possible_moves += [[pos[0], pos[1] - m]]
            elif (m == 1 and chess_board[pos[0]][pos[1] - m][1] != side) or \
                    (chess_board[pos[0]][pos[1] - m][1] != side and not chess_board[pos[0]][pos[1] - m + 1]):
                possible_moves += [[pos[0], pos[1] - m]]
            else:
                break

        for m in range(1, pos[0] + 1):
            if not chess_board[pos[0] - m][pos[1]]:
                possible_moves += [[pos[0] - m, pos[1]]]
            elif (m == 1 and chess_board[pos[0] - m][pos[1]][1] != side) or \
                    (chess_board[pos[0] - m][pos[1]][1] != side and not chess_board[pos[0] - m + 1][pos[1]]):
                possible_moves += [[pos[0] - m, pos[1]]]
            else:
                break

    elif chess_type == 'K':
        for m in range(-1, 2):
            if [pos[0] + m, pos[1] + m] in chess_board_positions:
                if not chess_board[pos[0] + m][pos[1] + m]:
                    possible_moves += [[pos[0] + m, pos[1] + m]]
                elif chess_board[pos[0] + m][pos[1] + m][1] != side:
                    possible_moves += [[pos[0] + m, pos[1] + m]]

            if [pos[0] + m, pos[1] - m] in chess_board_positions:
                if not chess_board[pos[0] + m][pos[1] - m]:
                    possible_moves += [[pos[0] + m, pos[1] - m]]
                elif chess_board[pos[0] + m][pos[1] - m][1] != side:
                    possible_moves += [[pos[0] + m, pos[1] - m]]

            if [pos[0] + m, pos[1]] in chess_board_positions:
                if not chess_board[pos[0] + m][pos[1]]:
                    possible_moves += [[pos[0] + m, pos[1]]]
                elif chess_board[pos[0] + m][pos[1]][1] != side:
                    possible_moves += [[pos[0] + m, pos[1]]]

            if [pos[0], pos[1] + m] in chess_board_positions:
                if not chess_board[pos[0]][pos[1] + m]:
                    possible_moves += [[pos[0], pos[1] + m]]
                elif chess_board[pos[0]][pos[1] + m][1] != side:
                    possible_moves += [[pos[0], pos[1] + m]]

    elif chess_type == 'p':
        # Check whether the pawn ever moved
        if pos in [[y, 1] for y in range(0, 8)] and side == 'w':
            if not chess_board[pos[0]][pos[1] + 2] and not chess_board[pos[0]][pos[1] + 1]:
                possible_moves = [[pos[0], pos[1] + 1], [pos[0], pos[1] + 2]]
            elif not chess_board[pos[0]][pos[1] + 1]:
                possible_moves = [[pos[0], pos[1] + 1]]

        elif pos in [[y, 6] for y in range(0, 8)] and side == 'b':
            if not chess_board[pos[0]][pos[1] - 2] and not chess_board[pos[0]][pos[1] - 1]:
                possible_moves = [[pos[0], pos[1] - 1], [pos[0], pos[1] - 2]]
            elif not chess_board[pos[0]][pos[1] - 1]:
                possible_moves = [[pos[0], pos[1] - 1]]

        elif side == 'w' and not chess_board[pos[0]][pos[1] + 1]:
            possible_moves = [[pos[0], pos[1] + 1]]
        elif side == 'b' and not chess_board[pos[0]][pos[1] - 1]:
            possible_moves = [[pos[0], pos[1] - 1]]

        # Check whether the pawn can attack enemy piece(s)
        if [pos[0] + 1, pos[1] + 1] in chess_board_positions:
            if chess_board[pos[0] + 1][pos[1] + 1] and side == 'w':
                if chess_board[pos[0] + 1][pos[1] + 1][1] != side:
                    possible_moves += [[pos[0] + 1, pos[1] + 1]]

        if [pos[0] - 1, pos[1] + 1] in chess_board_positions:
            if chess_board[pos[0] - 1][pos[1] + 1] and side == 'w':
                if chess_board[pos[0] - 1][pos[1] + 1][1] != side:
                    possible_moves += [[pos[0] - 1, pos[1] + 1]]

        if [pos[0] - 1, pos[1] - 1] in chess_board_positions:
            if chess_board[pos[0] - 1][pos[1] - 1] and side == 'b':
                if chess_board[pos[0] - 1][pos[1] - 1][1] != side:
                    possible_moves += [[pos[0] - 1, pos[1] - 1]]

        if [pos[0] + 1, pos[1] - 1] in chess_board_positions:
            if chess_board[pos[0] + 1][pos[1] - 1] and side == 'b':
                if chess_board[pos[0] + 1][pos[1] - 1][1] != side:
                    possible_moves += [[pos[0] + 1, pos[1] - 1]]

    # Delete moves off board
    for m in sorted(possible_moves, reverse=True):
        if m not in chess_board_positions:
            del possible_moves[possible_moves.index(m)]

    # Pops out moves with no move
    for m in range(possible_moves.count([pos[0], pos[1]])):
        possible_moves.pop(possible_moves.index([pos[0], pos[1]]))

    return possible_moves


def is_check(side):
    king_pos = []

    # Find player's King's position
    for u in range(8):
        for y in range(8):
            if chess_board[u][y]:
                if chess_board[u][y][1] == side and chess_board[u][y][0] == 'K':
                    king_pos = [u, y]

    # Scan for every possible move to see whether it coincides with King's position
    for u in range(8):
        for y in range(8):
            if chess_board[u][y]:
                if chess_board[u][y][1] != side:
                    if king_pos in valid_moves([u, y]):
                        return True
    return False


def is_mate_stalemate(side):
    if is_check(side):
        result = 'M'
        # If any move on the board you can make saves you from check then it's not mate
        for u in range(8):
            for y in range(8):
                if chess_board[u][y]:
                    if chess_board[u][y][1] == side:
                        for t in valid_moves([u, y]):
                            piece_on_to_pos = chess_board[t[0]][t[1]]

                            chess_board[t[0]][t[1]] = chess_board[u][y]
                            chess_board[u][y] = None

                            if not is_check(side):
                                result = False

                            chess_board[u][y] = chess_board[t[0]][t[1]]
                            chess_board[t[0]][t[1]] = piece_on_to_pos
    else:
        result = 'S'
        # If you can make any move on the board without being checked then it's not stalemate
        for u in range(8):
            for y in range(8):
                if chess_board[u][y]:
                    if chess_board[u][y][1] == side:
                        for t in valid_moves([u, y]):
                            piece_on_to_pos = chess_board[t[0]][t[1]]

                            chess_board[t[0]][t[1]] = chess_board[u][y]
                            chess_board[u][y] = None

                            if not is_check(side):
                                result = False

                            chess_board[u][y] = chess_board[t[0]][t[1]]
                            chess_board[t[0]][t[1]] = piece_on_to_pos

    return result


def start():
    whose_turn = 'w'

    while True:
        if whose_turn == 'w':
            # Prints formatted chess board (graphical interface is too difficult)
            print("\n*****************************************")
            print(' ', end=' ')
            for b in range(1, 9):
                print("{: ^4}".format(str(b)), end=' ')
            print()
            for b in range(8):
                print(b + 1, end=' ')
                for v in chess_board[b]:
                    if type(v) is list:
                        print("{: ^4}".format(f"{str(v[1])}{str(v[0])}"), end=' ')
                    else:
                        print("{: ^4}".format('NoN'), end=' ')
                print()
            print("*****************************************")

            from_pos_string = input("White moves from position: ")
            to_pos_string = input("To position: ")

            # Converts the input into usable form
            try:
                from_pos = [int(p) - 1 for p in from_pos_string.split(' ')]
                to_pos = [int(p) - 1 for p in to_pos_string.split(' ')]
            except ValueError:
                print("Invalid input. Input 2 numbers (position on x and y) putting space between them")
                continue

            if from_pos not in chess_board_positions or to_pos not in chess_board_positions:
                print("Invalid input.")
                continue

            # Makes the move
            if chess_board[from_pos[0]][from_pos[1]]:
                if chess_board[from_pos[0]][from_pos[1]][1] == whose_turn and to_pos in valid_moves(from_pos):
                    # First it makes move
                    piece_on_to_pos = chess_board[to_pos[0]][to_pos[1]]

                    chess_board[to_pos[0]][to_pos[1]] = chess_board[from_pos[0]][from_pos[1]]
                    chess_board[from_pos[0]][from_pos[1]] = None

                    # And then returns it if it's invalid
                    if is_check('w'):
                        print('Invalid move.')
                        chess_board[from_pos[0]][from_pos[1]] = chess_board[to_pos[0]][to_pos[1]]
                        chess_board[to_pos[0]][to_pos[1]] = piece_on_to_pos
                        continue

                    # Converts pawns into preferred pieces when they reach the end of the board
                    for h in range(8):
                        if chess_board[h][7]:
                            if chess_board[h][7][0] == 'p' and chess_board[h][7][1] == 'w':
                                chess_board[h][7][0] = input(f"What to turn white pawn on ({h + 1} 8) into? ")

                    # Checks for mate and stalemate
                    mate_or_stalemate = is_mate_stalemate('b')
                    if mate_or_stalemate == 'M':
                        exit("White wins!")
                    elif mate_or_stalemate == 'S':
                        exit("Stalemate!")

                    whose_turn = 'b'
                else:
                    print("Invalid input.")
            else:
                print("Invalid input.")

        # Almost exactly the same copy of previous if-statement's block
        elif whose_turn == 'b':
            print("\n*****************************************")
            print(' ', end=' ')
            for b in range(1, 9):
                print("{: ^4}".format(str(b)), end=' ')
            print()
            for b in range(8):
                print(b + 1, end=' ')
                for v in chess_board[b]:
                    if type(v) is list:
                        print("{: ^4}".format(f"{str(v[1])}{str(v[0])}"), end=' ')
                    else:
                        print("{: ^4}".format('NoN'), end=' ')
                print()
            print("*****************************************")

            from_pos_string = input("Black moves from position: ")
            to_pos_string = input("To position: ")

            try:
                from_pos = [int(p) - 1 for p in from_pos_string.split(' ')]
                to_pos = [int(p) - 1 for p in to_pos_string.split(' ')]
            except ValueError:
                print("Invalid input. Input 2 numbers (position on x and y) putting space between them")
                continue

            if from_pos not in chess_board_positions or to_pos not in chess_board_positions:
                print("Invalid input.")
                continue

            if chess_board[from_pos[0]][from_pos[1]]:
                if chess_board[from_pos[0]][from_pos[1]][1] == whose_turn and to_pos in valid_moves(from_pos):
                    piece_on_to_pos = chess_board[to_pos[0]][to_pos[1]]

                    chess_board[to_pos[0]][to_pos[1]] = chess_board[from_pos[0]][from_pos[1]]
                    chess_board[from_pos[0]][from_pos[1]] = None

                    if is_check('b'):
                        print('Invalid move.')
                        chess_board[from_pos[0]][from_pos[1]] = chess_board[to_pos[0]][to_pos[1]]
                        chess_board[to_pos[0]][to_pos[1]] = piece_on_to_pos
                        continue

                    for h in range(8):
                        if chess_board[h][0]:
                            if chess_board[h][0][0] == 'p' and chess_board[h][0][1] == 'b':
                                chess_board[h][0][0] = input(f"What to turn black pawn on ({h + 1} 1) into?")

                    mate_or_stalemate = is_mate_stalemate('w')
                    if mate_or_stalemate == 'M':
                        exit("Black wins!")
                    elif mate_or_stalemate == 'S':
                        exit("Stalemate!")

                    whose_turn = 'w'
                else:
                    print("Black only moves black pieces.")
            else:
                print("Invalid input.")


start()
