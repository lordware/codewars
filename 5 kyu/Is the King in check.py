def get_piece_index(board, piece):
    return [(ix, iy) for ix, row in enumerate(board) for iy, i in enumerate(row) if i == piece]


def king_is_in_check(chessboard):
    king_pos = get_piece_index(chessboard, '♔')
    pawn_pos = get_piece_index(chessboard, '♟')
    queen_pos = get_piece_index(chessboard, '♛')
    bishop_pos = get_piece_index(chessboard, '♝')
    rock_pos = get_piece_index(chessboard, '♜')
    knight_pos = get_piece_index(chessboard, '♞')
    checked_pos = []

    # rock
    for rocky in rock_pos:
        for x in range(0, 8):
            if chessboard[x][rocky[1]] == ' ' or chessboard[x][rocky[1]] == '♜' or chessboard[x][rocky[1]] == '♔':
                checked_pos.append((x, rocky[1]))
            else:
                break
        for y in range(0, 8):
            if chessboard[rocky[0]][y] == ' ' or chessboard[rocky[0]][y] == '♜' or chessboard[rocky[0]][y] == '♔':
                checked_pos.append((rocky[0], y))
            else:
                break

    # knight
    for knighty in knight_pos:
        if knighty[0] + 2 < 8 and knighty[1] + 1 < 8:
            checked_pos.append((knighty[0] + 2, knighty[1] + 1))
        if knighty[0] + 2 < 8 and knighty[1] - 1 >= 0:
            checked_pos.append((knighty[0] + 2, knighty[1] - 1))
        if knighty[0] + 1 < 8 and knighty[1] + 2 < 8:
            checked_pos.append((knighty[0] + 1, knighty[1] + 2))
        if knighty[0] + 1 < 8 and knighty[1] - 2 >= 0:
            checked_pos.append((knighty[0] + 1, knighty[1] - 2))
        if knighty[0] - 2 >= 0 and knighty[1] + 1 < 8:
            checked_pos.append((knighty[0] - 2, knighty[1] + 1))
        if knighty[0] - 2 >= 0 and knighty[1] - 1 >= 0:
            checked_pos.append((knighty[0] - 2, knighty[1] - 1))
        if knighty[0] - 1 >= 0 and knighty[1] + 2 < 8:
            checked_pos.append((knighty[0] - 1, knighty[1] + 2))
        if knighty[0] - 1 >= 0 and knighty[1] - 2 >= 0:
            checked_pos.append((knighty[0] - 1, knighty[1] - 2))

    # pawn
    for pawny in pawn_pos:
        checked_pos.append((pawny[0] + 1, pawny[1] + 1))
        checked_pos.append((pawny[0] + 1, pawny[1] - 1))

    # queen
    for queeny in queen_pos:
        for x in range(0, 8):
            if chessboard[x][queeny[1]] == ' ' or chessboard[x][queeny[1]] == '♛' or chessboard[x][queeny[1]] == '♔':
                checked_pos.append((x, queeny[1]))
            else:
                break
        for y in range(0, 8):
            if chessboard[queeny[0]][y] == ' ' or chessboard[queeny[0]][y] == '♛' or chessboard[queeny[0]][y] == '♔':
                checked_pos.append((queeny[0], y))
            else:
                break

        for z in range(0, 8):
            if queeny[0] - z < 0 or queeny[1] + z >= 8:
                break
            if chessboard[queeny[0] - z][queeny[1] + z] == '♛' or chessboard[queeny[0] - z][queeny[1] + z] == ' ' or \
                    chessboard[queeny[0] - z][queeny[1] + z] == '♔':
                checked_pos.append((queeny[0] - z, queeny[1] + z))
            else:
                break

        for e in range(0, 8):
            if queeny[0] + e >= 8 or queeny[1] - e < 0:
                break
            if chessboard[queeny[0] + e][queeny[1] - e] == '♛' or chessboard[queeny[0] + e][queeny[1] - e] == ' ' or \
                    chessboard[queeny[0] + e][queeny[1] - e] == '♔':
                checked_pos.append((queeny[0] + e, queeny[1] - e))
            else:
                break

        for a in range(0, 8):
            if queeny[0] + a >= 8 or queeny[1] + a >= 8:
                break
            if chessboard[queeny[0] + a][queeny[1] + a] == '♛' or chessboard[queeny[0] + a][queeny[1] + a] == ' ' or \
                    chessboard[queeny[0] + a][queeny[1] + a] == '♔':
                checked_pos.append((queeny[0] + a, queeny[1] + a))
            else:
                break

        for b in range(0, 8):
            if queeny[0] + b >= 8 or queeny[1] - b < 0:
                break
            if chessboard[queeny[0] + b][queeny[1] - b] == '♛' or chessboard[queeny[0] + b][queeny[1] - b] == ' ' or \
                    chessboard[queeny[0] + b][queeny[1] - b] == '♔':
                checked_pos.append((queeny[0] + b, queeny[1] - b))
            else:
                break

        for c in range(0, 8):
            if queeny[0] - c < 0 or queeny[1] - c < 0:
                break
            if chessboard[queeny[0] - c][queeny[1] - c] == '♛' or chessboard[queeny[0] - c][queeny[1] - c] == ' ' or \
                    chessboard[queeny[0] - c][queeny[1] - c] == '♔':
                checked_pos.append((queeny[0] - c, queeny[1] - c))
            else:
                break
    # bishop
    for bishopy in bishop_pos:
        for x in range(0, 8):
            if bishopy[1] + x >= 8 or bishopy[0] + x >= 8:
                break
            if chessboard[bishopy[0] + x][bishopy[1] + x] == ' ' or chessboard[bishopy[0] + x][bishopy[1] + x] == '♝' or \
                    chessboard[bishopy[0] + x][bishopy[1] + x] == '♔':
                checked_pos.append((bishopy[0] + x, bishopy[1] + x))
            else:
                break
        for y in range(0, 8):
            print(bishopy[0] - y)
            if bishopy[0] - y < 0 or bishopy[1] - y < 0:
                break
            if chessboard[bishopy[0] - y][bishopy[1] - y] == ' ' or chessboard[bishopy[0] - y][bishopy[1] - y] == '♝' or \
                    chessboard[bishopy[0] - y][bishopy[1] - y] == '♔':
                checked_pos.append((bishopy[0] - y, bishopy[1] - y))
            else:
                break

        for z in range(0, 8):
            if bishopy[0] - z < 0 or bishopy[1] + z >= 8:
                break
            if chessboard[bishopy[0] - z][bishopy[1] + z] == ' ' or chessboard[bishopy[0] - z][bishopy[1] + z] == '♝' or \
                    chessboard[bishopy[0] - z][bishopy[1] + z] == '♔':
                checked_pos.append((bishopy[0] - z, bishopy[1] + z))
            else:
                break

        for q in range(0, 8):
            if bishopy[0] + q >= 8 or bishopy[1] + q >= 8 or bishopy[0] - q < 0 or bishopy[1] - q < 0:
                break
            if chessboard[bishopy[0] + q][bishopy[1] - q] == ' ' or chessboard[bishopy[0] + q][bishopy[1] - q] == '♝' or \
                    chessboard[bishopy[0] + q][bishopy[1] - q] == '♔':
                checked_pos.append((bishopy[0] + q, bishopy[1] - q))
            else:
                break
        for e in range(0, 8):
            if bishopy[0] + e >= 8 or bishopy[1] - 1 < 0:
                break
            if chessboard[bishopy[0] + e][bishopy[1] - e] == ' ' or chessboard[bishopy[0] + e][bishopy[1] - e] == '♝' or \
                    chessboard[bishopy[0] + e][bishopy[1] - e] == '♔':
                checked_pos.append((bishopy[0] + e, bishopy[1] - e))
            else:
                break

    print(knight_pos)
    print(checked_pos)
    return king_pos[0] in checked_pos
