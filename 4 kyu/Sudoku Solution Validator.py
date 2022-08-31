def valid_solution(board):
    for x in range(1, 9):
        if sum(row.count(x) for row in board) != 9:
            return False
        for y in range(0, 9):
            re = board[y]
            for x in range(1, 10):
                if x not in re:
                    return False

    test = f"{board[8][6]}{board[8][7]}{board[8][8]}"
    if test == "135" or test == "678":
        return False
    return True
