import turtle
import random
import math

# ============================================================
# GAME SETTINGS
# ============================================================

WIDTH = 500
HEIGHT = 500

GRID_SIZE = 20
FOOD_SIZE = 10

DELAY = 100

# Movement offsets
OFFSETS = {
    "up": (0, GRID_SIZE),
    "down": (0, -GRID_SIZE),
    "left": (-GRID_SIZE, 0),
    "right": (GRID_SIZE, 0)
}


# ============================================================
# GAME VARIABLES
# ============================================================

snake = []
snake_direction = "up"

food_pos = (0, 0)

game_over = False
score = 0


# ============================================================
# RESET GAME
# ============================================================

def reset():
    global snake
    global snake_direction
    global food_pos
    global game_over
    global score

    # Create snake with evenly spaced segments
    snake = [
        [0, -40],
        [0, -20],
        [0, 0],
        [0, 20],
        [0, 40]
    ]

    snake_direction = "up"

    score = 0
    game_over = False

    food_pos = get_random_food_pos()
    food.goto(food_pos)

    draw_snake()
    screen.update()

    # Start movement
    screen.ontimer(move_snake, DELAY)


# ============================================================
# MOVE SNAKE
# ============================================================

def move_snake():
    global snake
    global game_over

    # Stop movement after game over
    if game_over:
        return

    # --------------------------------------------------------
    # Calculate new head
    # --------------------------------------------------------

    dx, dy = OFFSETS[snake_direction]

    new_head = [
        snake[-1][0] + dx,
        snake[-1][1] + dy
    ]

    # --------------------------------------------------------
    # Screen wrapping
    # --------------------------------------------------------

    if new_head[0] > WIDTH // 2 - GRID_SIZE:
        new_head[0] = -WIDTH // 2

    elif new_head[0] < -WIDTH // 2:
        new_head[0] = WIDTH // 2 - GRID_SIZE

    if new_head[1] > HEIGHT // 2 - GRID_SIZE:
        new_head[1] = -HEIGHT // 2

    elif new_head[1] < -HEIGHT // 2:
        new_head[1] = HEIGHT // 2 - GRID_SIZE

    # --------------------------------------------------------
    # Self collision
    # --------------------------------------------------------

    if new_head in snake:
        end_game()
        return

    # --------------------------------------------------------
    # Add new head
    # --------------------------------------------------------

    snake.append(new_head)

    # --------------------------------------------------------
    # Food collision
    # --------------------------------------------------------

    if food_collision():
        increase_score()

    else:
        # Remove tail if food wasn't eaten
        snake.pop(0)

    # --------------------------------------------------------
    # Draw snake
    # --------------------------------------------------------

    draw_snake()

    screen.update()

    # Schedule next movement
    screen.ontimer(move_snake, DELAY)


# ============================================================
# DRAW SNAKE
# ============================================================

def draw_snake():
    pen.clearstamps()

    for index, segment in enumerate(snake):

        pen.goto(segment[0], segment[1])

        # Different color for head
        if index == len(snake) - 1:
            pen.color("lime")
        else:
            pen.color("yellow")

        pen.stamp()


# ============================================================
# FOOD COLLISION
# ============================================================

def food_collision():
    global food_pos

    distance = get_distance(snake[-1], food_pos)

    if distance < GRID_SIZE:

        # Generate new food position
        food_pos = get_random_food_pos()

        food.goto(food_pos)

        return True

    return False


# ============================================================
# RANDOM FOOD POSITION
# ============================================================

def get_random_food_pos():

    possible_positions = []

    # Create positions aligned with the snake grid
    for x in range(
        -WIDTH // 2 + GRID_SIZE,
        WIDTH // 2,
        GRID_SIZE
    ):
        for y in range(
            -HEIGHT // 2 + GRID_SIZE,
            HEIGHT // 2,
            GRID_SIZE
        ):
            possible_positions.append((x, y))

    # Remove positions occupied by snake
    available_positions = [
        position
        for position in possible_positions
        if list(position) not in snake
    ]

    # Safety check
    if not available_positions:
        return (0, 0)

    return random.choice(available_positions)


# ============================================================
# DISTANCE CALCULATION
# ============================================================

def get_distance(pos1, pos2):

    x1, y1 = pos1
    x2, y2 = pos2

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )


# ============================================================
# SCORE
# ============================================================

def increase_score():
    global score

    score += 1

    score_writer.clear()

    score_writer.goto(
        0,
        HEIGHT // 2 - 40
    )

    score_writer.write(
        f"Score: {score}",
        align="center",
        font=("Arial", 16, "bold")
    )


# ============================================================
# GAME OVER
# ============================================================

def end_game():
    global game_over

    game_over = True

    # Stop drawing snake
    pen.clearstamps()

    # Draw final snake
    for index, segment in enumerate(snake):

        pen.goto(segment[0], segment[1])

        if index == len(snake) - 1:
            pen.color("red")
        else:
            pen.color("yellow")

        pen.stamp()

    # Game over text
    game_over_writer.clear()

    game_over_writer.goto(
        0,
        20
    )

    game_over_writer.write(
        "GAME OVER",
        align="center",
        font=("Arial", 28, "bold")
    )

    game_over_writer.goto(
        0,
        -20
    )

    game_over_writer.write(
        f"Score: {score}",
        align="center",
        font=("Arial", 18, "normal")
    )

    game_over_writer.goto(
        0,
        -60
    )

    game_over_writer.write(
        "Press R to restart",
        align="center",
        font=("Arial", 14, "normal")
    )

    screen.update()


# ============================================================
# RESTART
# ============================================================

def restart():
    if game_over:
        game_over_writer.clear()
        reset()


# ============================================================
# CONTROLS
# ============================================================

def go_up():
    global snake_direction

    if snake_direction != "down":
        snake_direction = "up"


def go_down():
    global snake_direction

    if snake_direction != "up":
        snake_direction = "down"


def go_left():
    global snake_direction

    if snake_direction != "right":
        snake_direction = "left"


def go_right():
    global snake_direction

    if snake_direction != "left":
        snake_direction = "right"


# ============================================================
# SCREEN
# ============================================================

screen = turtle.Screen()

screen.setup(
    width=WIDTH,
    height=HEIGHT
)

screen.title("Snake Game")

screen.bgcolor("black")

# Turn off automatic animation
screen.tracer(0)


# ============================================================
# SNAKE PEN
# ============================================================

pen = turtle.Turtle("square")

pen.penup()

pen.speed(0)

pen.color("yellow")


# ============================================================
# FOOD
# ============================================================

food = turtle.Turtle("circle")

food.penup()

food.speed(0)

food.color("red")

food.shapesize(
    FOOD_SIZE / 20
)


# ============================================================
# SCORE WRITER
# ============================================================

score_writer = turtle.Turtle()

score_writer.hideturtle()

score_writer.penup()

score_writer.color("white")


# ============================================================
# GAME OVER WRITER
# ============================================================

game_over_writer = turtle.Turtle()

game_over_writer.hideturtle()

game_over_writer.penup()

game_over_writer.color("white")


# ============================================================
# KEYBOARD CONTROLS
# ============================================================

screen.listen()

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

screen.onkey(restart, "r")
screen.onkey(restart, "R")


# ============================================================
# START GAME
# ============================================================

reset()

turtle.done()