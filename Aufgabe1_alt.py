import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time


def is_valid(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == '0'


def find_next_cell(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '0' and not is_connected(i, j, board):
                return (i, j)
    return None


def is_connected(x, y, board):
    value = board[x][y]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i != x or j != y) and board[i][j] == value:
                return True
    return False


def solve(board, x, y, target_x, target_y, value):
    if (x, y) == (target_x, target_y):
        return True
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y, board):
            board[new_x][new_y] = value
            if solve(board, new_x, new_y, target_x, target_y, value):
                return True
            board[new_x][new_y] = '0'
    return False


def arukone_solver(board):
    cell = find_next_cell(board)
    if not cell:
        return True
    x, y = cell
    value = board[x][y]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == value and (i != x or j != y):
                board_copy = [row[:] for row in board]
                if solve(board_copy, x, y, i, j, value):
                    board[:] = board_copy
                    if arukone_solver(board):
                        return True
    return False


def plot_board(board):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Finde den anderen Partner der gegebenen Zahl
    def find_pair(x, y, board):
        num = board[x][y]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == num and (i, j) != (x, y):
                    return (i, j)
        return None

    # Verwende BFS, um den Pfad zwischen zwei Punkten zu finden
    def find_path(start, end, board, num):
        queue = [start]
        visited = set()
        prev = {start: None}

        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < len(board)) and (0 <= ny < len(board[0])) and (nx, ny) not in visited:
                    if board[nx][ny] in ('0', num):
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        prev[(nx, ny)] = (x, y)
                        if (nx, ny) == end:
                            path = []
                            while (nx, ny) != start:
                                path.append((nx, ny))
                                nx, ny = prev[(nx, ny)]
                            path.append(start)
                            return path[::-1]
        return []

    # Zeichne das Board und Pfade
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '0':
                ax.text(j, i, board[i][j], ha='center', va='center', fontsize=14)
                if (i, j) < find_pair(i, j, board):
                    path = find_path((i, j), find_pair(i, j, board), board, board[i][j])
                    for k in range(1, len(path)):
                        x1, y1 = path[k - 1]
                        x2, y2 = path[k]
                        ax.plot([y1, y2], [x1, x2], color='red')

    ax.set_xticks(range(len(board[0])))
    ax.set_yticks(range(len(board)))
    ax.grid(which='both')
    ax.axis('tight')
    plt.gca().invert_yaxis()
    plt.show()


board = [
    ['1', '0', '2', '4', '0', '0'],
    ['0', '0', '3', '0', '5', '0'],
    ['0', '0', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '4'],
    ['0', '2', '0', '0', '0', '0'],
    ['0', '0', '0', '3', '0', '5']
]

if arukone_solver(board):
    plot_board(board)
else:
    print("No solution found.")