def print_table(s):
    table = f"""
        a   b   c
     1 {s["a1"]}|{s["b1"]}|{s["c1"]}
       ---+---+---
     2 {s["a2"]}|{s["b2"]}|{s["c2"]}
       ---+---+---
     3 {s["a3"]}|{s["b3"]}|{s["c3"]}

    """
    print(table)


def check_col(s, col, row, symbol):
    """Checks shots in columns"""
    col_list = []
    for c in col:
        points = 0
        for r in row:
            coord = c + r
            if s[coord] == f" {symbol} ":
                points += 1
        col_list.append(points)
    if 3 in col_list:
        return True
    else:
        return False


def check_row(s, col, row, symbol):
    """Checks shots in rows"""
    row_list = []
    for r in row:
        points = 0
        for c in col:
            coord = c + r
            if s[coord] == f" {symbol} ":
                points += 1
        row_list.append(points)
    if 3 in row_list:
        return True
    else:
        return False


def check_diag(s, col, symbol):
    """Check shots diagonally"""
    points = 0
    row_num = 1
    for c in col:
        coord = c + str(row_num)
        if s[coord] == f" {symbol} ":
            points += 1
        row_num += 1
    if points == 3:
        return True
    else:
        return False


def check_anti_diag(s, col, symbol):
    """Checks shots anti diagonally"""
    points = 0
    row_num = 3
    for c in col:
        coord = c + str(row_num)
        if s[coord] == f" {symbol} ":
            points += 1
        row_num -= 1
    if points == 3:
        return True
    else:
        return False


def compact_check(s, col, row, symbol):
    """All the checks and evaluation combined"""
    #         Check columns:
    col_check = check_col(s, col, row, symbol)
    #       Check rows:
    row_check = check_row(s, col, row, symbol)
    #         Check diag:
    diag_check = check_diag(s, col, symbol)
    #         Check anti diag:
    anti_diag_check = check_anti_diag(s, col, symbol)

    # Evaluating the winner:
    if col_check or row_check or diag_check or anti_diag_check:
        print(f"The winner is: {symbol}")
        return True
