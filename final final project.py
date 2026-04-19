#Harsh Bhavasar(2403310)                  draw snakes and ladder
#Nirmal Meena (2403126)                   logic of coordinates
#Patil Shradha Sushil (2403128)           draw board 
#Bhushan Kamble (2403109)                 logic of move player and update player 
#Naman Solanki (2403123)                  logic of screen and game logic
#Amarpreet Samra (2403103)                Assemble code


import turtle
import random

coordinates_dic={100:(-180,180), 99:(-140,180), 98:(-100,180), 97:(-60,180), 96:(-20,180), 95:(20,180), 94:(60,180), 93:(100,180), 92:(140,180), 91:(180,180), 90:(180,140), 89:(140,140), 88:(100,140), 87:(60,140), 86:(20,140), 85:(-20,140), 84:(-60,140), 83:(-100,140), 82:(-140,140), 81:(-180,140), 80:(-180,100), 79:(-140,100), 78:(-100,100), 77:(-60,100), 76:(-20,100), 75:(20,100), 74:(60,100), 73:(100,100), 72:(140,100), 71:(180,100), 70:(180,60), 69:(140,60), 68:(100,60), 67:(60,60), 66:(20,60), 65:(-20,60), 64:(-60,60), 63:(-100,60), 62:(-140,60), 61:(-180,60), 60:(-180,20), 59:(-140,20), 58:(-100,20), 57:(-60,20), 56:(-20,20), 55:(20,20), 54:(60,20), 53:(100,20), 52:(140,20), 51:(180,20), 50:(180,-20), 49:(140,-20), 48:(100,-20), 47:(60,-20), 46:(20,-20), 45:(-20,-20), 44:(-60,-20), 43:(-100,-20), 42:(-140,-20), 41:(-180,-20), 40:(-180,-60), 39:(-140,-60), 38:(-100,-60), 37:(-60,-60), 36:(-20,-60), 35:(20,-60), 34:(60,-60), 33:(100,-60), 32:(140,-60), 31:(180,-60), 30:(180,-100), 29:(140,-100), 28:(100,-100), 27:(60,-100), 26:(20,-100), 25:(-20,-100), 24:(-60,-100), 23:(-100,-100), 22:(-140,-100), 21:(-180,-100), 20:(-180,-140), 19:(-140,-140), 18:(-100,-140), 17:(-60,-140), 16:(-20,-140), 15:(20,-140), 14:(60,-140), 13:(100,-140), 12:(140,-140), 11:(180,-140), 10:(180,-180), 9:(140,-180), 8:(100,-180), 7:(60,-180), 6:(20,-180), 5:(-20,-180), 4:(-60,-180), 3:(-100,-180), 2:(-140,-180), 1:(-180,-180)}
board_size = 400
square_size = 40
num_squares = 10
winning_position = 100

players = []
player_positions = []


snakes = {
    16: 6,
    46: 25,
    49: 20,
    62: 19,
    64: 60,
    74: 53,
    89: 68,
    92: 88,
    95: 75,
    99: 80
}

ladders = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    78: 98,
    87: 94
}

screen = turtle.Screen()
screen.title("Snakes and Ladders")
screen.setup(width=board_size + 100, height=board_size + 100)

board = turtle.Turtle()
board.speed(0)
board.hideturtle()
board.penup()

def draw_board():
    board.goto(-board_size / 2, -board_size / 2)
    board.pendown()
    square_num = 1

    for i in range(num_squares):                      #Inspired from interactive textbook
        for j in range(num_squares):
            for _ in range(4):
                board.forward(square_size)
                board.left(90)

            board.penup()
            board.forward(square_size / 2)
            board.left(90)
            board.forward(square_size / 2)
            
            if (i % 2 == 0):
                num_to_write=square_num                          
            else:
                num_to_write=((i + 1) * num_squares - j)          # This logic taken from chatgpt

            board.write(num_to_write, align="center", font=("Arial", 12, "normal"))     # writing style taken from google colab
            board.backward(square_size / 2)
            board.right(90)
            board.forward(square_size / 2)
            board.pendown()

            square_num += 1

        board.penup()
        board.goto(-board_size / 2, -board_size / 2 + (i + 1) * square_size)
        board.pendown()

def draw_snake(start, end):

    start_x, start_y=coordinates_dic[start]
    end_x, end_y=coordinates_dic[end]
    
    board.goto(start_x, start_y)
    board.pendown()
    board.pensize(5)
    board.color("red")
    board.goto(end_x, end_y)
    board.penup()
    

def draw_ladder(start, end):
    start_x, start_y=coordinates_dic[start]
    end_x, end_y=coordinates_dic[end]
    
    board.goto(start_x, start_y)
    board.pendown()
    board.pensize(5)
    board.color("green")
    board.goto(end_x, end_y)
    board.penup()
    

# Initialize players
def intialize_players():                                                            #Taken from chatgpt
    num_players = int(screen.numinput("Number of Players", "Enter number of players (2-4):", 2, minval=2, maxval=4))
    for i in range(num_players):
        name = screen.textinput("Player Name", f"Enter name for player {i + 1}:")
        color = screen.textinput("Player Color", f"Enter color for {name} (e.g., 'red', 'blue'):")
        players.append({'name': name, 'color': color, 'position': 0})
        player_positions.append(turtle.Turtle())
        player_positions[-1].color(color)
        player_positions[-1].shape("circle")
        player_positions[-1].penup()
        player_positions[-1].goto(-200,-200)

# Move player
def move_player(player, steps):
    if player['position']+steps > winning_position:
        pass
    elif player['position']+steps==winning_position:
        player['position'] = winning_position
    else:
        player['position'] += steps

    update_player_position(player)

def update_player_position(player):
    pos = players.index(player)
    x,y=coordinates_dic[player['position']]
    player_positions[pos].goto(x, y)

def check_snakes_and_ladders(player):
    if player['position'] in snakes:
        print(f"{player['name']} got bitten by a snake!")
        player['position'] = snakes[player['position']]
        update_player_position(player)
    elif player['position'] in ladders:
        print(f"{player['name']} climbed a ladder!")
        player['position'] = ladders[player['position']]
        update_player_position(player)

# Game Logic
def play_game():
    intialize_players()
    
    while True:
        for i in players:
            input(f"{i['name']}'s turn. Press Enter to roll the dice...")
            dice_roll = random.randint(1, 6)
            print(f"{i['name']} rolled a {dice_roll}.")
            move_player(i, dice_roll)
            check_snakes_and_ladders(i)

            if i['position'] == winning_position:
                print(f"{i['name']} wins!")
                return
                

draw_board()
board.penup()
for start, end in ladders.items():
    draw_ladder(start, end)
for start, end in snakes.items():
    draw_snake(start, end)
play_game()
turtle.done()
