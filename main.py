import curses
import random
import time

def game_loop(window, game_speed):
    # Setup inicial
    curses.curs_set(0)
    snake = [
        [10, 15],
        [9, 15],
        [8, 15],
        [7, 15]
    ] 
    fruit = get_new_fruit(window=window) 
    current_direction = curses.KEY_DOWN
    snake_ate_fruit = False
    score = 0
    
    while True:
        draw_screen(window=window)
        draw_snake(snake=snake,window=window)
        draw_actor(actor=fruit, window=window, char="@")
        direction = get_new_direction(window=window, timeout=game_speed)
        if direction is None:
            direction = current_direction
        if direction_is_opposite(direction=direction, current_direction=current_direction):
            direction = current_direction
        move_snake(snake=snake, direction=direction, snake_ate_fruit=snake_ate_fruit)
        if snake_hit_border(snake=snake, window=window):
            break
        if snake_hit_itself(snake=snake):
            break    
        if snake_hit_fruit(snake=snake, fruit=fruit):
            snake_ate_fruit = True
            fruit = get_new_fruit(window=window)
            score += 1
        else:
            snake_ate_fruit = False
        current_direction = direction
    
    finish_game(window=window, score=score)

def finish_game(window, score):
    height, width = window.getmaxyx()
    s = f'Game Over! Score: {score} fruits'
    y = int(height / 2)
    x = int((width - len(s)) / 2)
    window.addstr(y, x, s)
    window.refresh()
    time.sleep(3)

def direction_is_opposite(direction, current_direction):
    match direction:
            case curses.KEY_UP:
                return current_direction == curses.KEY_DOWN
            case curses.KEY_DOWN:
                return current_direction == curses.KEY_UP
            case curses.KEY_LEFT:
                return current_direction == curses.KEY_RIGHT
            case curses.KEY_RIGHT:
                return current_direction == curses.KEY_LEFT


def get_new_fruit(window):
     height, width = window.getmaxyx()
     return [random.randint(1, height - 2), random.randint(1, width - 2)]

def snake_hit_border(snake, window):
    head = snake[0]
    return actor_hit_border(actor=head, window=window)

def snake_hit_fruit(snake, fruit):
    return fruit in snake

def snake_hit_itself(snake):
    head = snake[0]
    body = snake[1:]
    return head in body

def draw_screen(window):
    window.clear()
    window.border(0)

def draw_snake(snake, window):
    head = snake[0]
    draw_actor(actor=head, window=window, char=curses.ACS_DIAMOND)
    body = snake[1:]
    for body_part in body:
        draw_actor(actor=body_part, window=window, char="x")

def draw_actor(actor, window, char):
    window.addch(actor[0], actor[1], char)


def get_new_direction(window, timeout):
        window.timeout(timeout)
        direction = window.getch()
        if direction in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_RIGHT]:
            return direction
        return None    

def move_snake(snake, direction, snake_ate_fruit):
    head = snake[0].copy()
    move_actor(actor=head, direction=direction)
    snake.insert(0, head)
    if not snake_ate_fruit:
        snake.pop()

def move_actor(actor, direction):
    match direction:
        case curses.KEY_UP:
            actor[0] -= 1
        case curses.KEY_DOWN:
            actor[0] += 1
        case curses.KEY_LEFT:
            actor[1] -= 1
        case curses.KEY_RIGHT:
            actor[1] += 1


def actor_hit_border(actor, window):
        height, width = window.getmaxyx()
        if (actor[0] <= 0) or (actor[0] >= height - 1):
            return True 
        if (actor[1] <= 0) or (actor[1] >= width - 1):
            return True
        return False
       
def select_dificult():
    difficult = {
        "easy": 1000,
        "medium": 100,
        "hard": 10
    }
    while True:
        answer = input("Select the dificult: (easy, medium, hard)").lower()
        if answer in difficult:
            return difficult[answer]
        else:
            print("Invalid answer")

#Executa o jogo quando o arquivo é executado diretamente
if __name__ == '__main__':
    curses.wrapper(game_loop, game_speed=select_dificult()) #Cria uma tela interagivel no terminal

