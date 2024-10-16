def custom_sum(a, b, c):
    """Custom sum function for specific cases, no longer used for general summing."""
    return a + b + c

def printboard(xstate, zstate, size):
    """Prints the Tic-Tac-Toe board dynamically for any grid size."""
    for row in range(size):
        row_values = []
        for col in range(size):
            idx = row * size + col
            value = 'X' if xstate[idx] else ('Y' if zstate[idx] else idx)
            row_values.append(str(value))
        print(" | ".join(row_values))
        if row != size - 1:
            print("--" + "---" * (size - 1))

def checkwin(xstate, zstate, size):
    """Checks if there's a winning combination dynamically based on the grid size."""
    wins = []

    # Rows
    for row in range(size):
        wins.append([row * size + i for i in range(size)])

    # Columns
    for col in range(size):
        wins.append([col + size * i for i in range(size)])

    # Diagonals
    wins.append([i * (size + 1) for i in range(size)])  # Top-left to bottom-right
    wins.append([i * (size - 1) for i in range(1, size + 1)])  # Top-right to bottom-left

    # Check for wins
    for win in wins:
        if sum(xstate[i] for i in win) == size:  # Built-in sum now used
            print("X Wins")
            return 1
        if sum(zstate[i] for i in win) == size:  # Built-in sum now used
            print("Y Wins")
            return 0
    
    return -1

if __name__ == "__main__":
    size = int(input("Enter the size of the grid (e.g., 3 for 3x3): "))
    xstate = [0] * (size * size)
    zstate = [0] * (size * size)
    turn = 1
    print("Welcome to Tic Tac Toe")
    
    while True:
        printboard(xstate, zstate, size)
        if turn == 1:
            print("X's Chance")
            value = int(input(f"Please enter a value (0 to {size*size-1}): "))
            if xstate[value] == 0 and zstate[value] == 0:
                xstate[value] = 1
            else:
                print("Invalid move, try again.")
                continue
        else:
            print("Y's Chance")
            value = int(input(f"Please enter a value (0 to {size*size-1}): "))
            if xstate[value] == 0 and zstate[value] == 0:
                zstate[value] = 1
            else:
                print("Invalid move, try again.")
                continue

        cwin = checkwin(xstate, zstate, size)
        if cwin != -1:
            printboard(xstate, zstate, size)
            print("Match over")
            break
        turn = 1 - turn

