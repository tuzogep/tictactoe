from brain import print_table, compact_check

# Creating the dictionary for the values
col = ["a", "b", "c"]
row = ["1", "2", "3"]

s = {}
for c in col:
    for r in row:
        coord = c + r
        s[coord] = "   "

print("Welcome to Peter's Tic Tac Toe Game!")
print_table(s)
list_xo = ["O", "X"]
game_on = True
n = 0
while game_on:
    retry = False
    if "   " not in s.values():
        print("There are no more targets. Draw!")
        game_on = False
    else:
        symbol = list_xo[n]
        target = input(f'Player "{symbol}", give the coordinates of your target (e.g."b3"): ')
        # Secret exit code
        if target == "exit":
            game_on = False
        # Checking for typos in user input
        elif target not in s.keys():
            print("You made a typo. Try again!")
            retry = True
        else:
            s[target] = f" {symbol} "
            print_table(s)
            result = compact_check(s, col, row, symbol)
            if result:
                game_on = False
        if not retry:
            if n == 0:
                n = 1
            else:
                n = 0
