from random import randrange

board = [
    [1, 2, 3],
    [4, "X", 5],
    [6, 7, 8]
]

def display_board(board):
    print(
        f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
        """)    

def enter_move(board):
    while True:
        move = int(input("Ingrese la casilla que quiera marcar: "))
        if move not in range (1, 10):
            print("Ingrese una casilla que este en el tablero.")
            continue
        for i in range (3):
            for j in range (3):
                if board[i][j] == move:
                    board[i][j] = "O"
                    return
        print("Casilla ocupada, seleccione otra casilla.")
                     
def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                free_fields.append((i, j)) 
    return free_fields

def victory_for(board, sign):
    if sign == board[0][0] == board[1][0] == board[2][0] or \
    sign == board[0][1] == board[1][1] == board[2][1] or \
    sign == board[0][2] == board[1][2] == board[2][2] or \
    sign == board[0][0] == board[0][1] == board[0][2] or \
    sign == board[1][0] == board[1][1] == board[1][2] or \
    sign == board[2][0] == board[2][1] == board[2][2] or \
    sign == board[0][0] == board[1][1] == board[2][2] or \
    sign == board[0][2] == board[1][1] == board[0][2]:
        return True 
    else:
        return False 

def draw_move(board):
    casillas_libres = make_list_of_free_fields(board) 
    if casillas_libres:
        movimientos = len(casillas_libres)
        maquina = randrange(0, movimientos)
        i, j = casillas_libres[maquina]
        board[i][j] = "X"
    else:
        print("El tablero está lleno")

def empate(board):
    casillas = make_list_of_free_fields(board)
    if not casillas:
        return True
    else:
        return False
    
while True:
    display_board(board)
    enter_move(board)
    make_list_of_free_fields(board)
    draw_move(board)
    if victory_for(board, "O"):
        display_board(board)
        print("Gana el usuario.")
        break
    if victory_for(board, "X"):
        display_board(board)
        print("Gana la maquina.") 
        break
    if empate(board):
        print("Es un empate.")
        break