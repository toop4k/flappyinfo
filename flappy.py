import arcade
import random

WIDTH = 500
HEIGHT = 700
game_over = False  # Bandera para indicar si el juego ha finalizado

# Definimos la forma randomica en la que saldran las pipes
def pipe_random_height():
    pipe_h = [random.randint(50, (HEIGHT/2)-50), random.randint((HEIGHT/2)+110, HEIGHT)]
    return pipe_h

def on_draw():
    arcade.start_render()
    global score, player_pos, speed, pipe_pos, pipe_height, game_over

    speed += gravity
    speed *= 0.95
    player_pos[1] += speed

    if pipe_pos >= -20:
        pipe_pos -= 10
    else:
        pipe_pos = 700
        pipe_height = pipe_random_height()
        score += 1

    # Background / fondo
    arcade.set_background_color(arcade.color.BLUE)

    # Player / circulo naranja
    arcade.draw_circle_filled(player_pos[0], player_pos[1], 20, arcade.color.ORANGE_PEEL)

    # Pipe / tuberia
    arcade.draw_rectangle_filled(pipe_pos, 0, pipe_widht, pipe_height[0], arcade.color.GREEN)
    arcade.draw_rectangle_filled(pipe_pos, pipe_height[1], pipe_widht, 500, arcade.color.GREEN)

    if player_pos[1] <= pipe_height[0] or player_pos[1] >= pipe_height[1]:
        if player_pos[0] in list(range(pipe_pos, pipe_pos + pipe_widht)):
            print(f"Game Over. Score {score}")
            game_over = True  # Establecer la bandera game_over como True

    if player_pos[1] >= HEIGHT:
        player_pos[1] = HEIGHT
        speed = 0
    elif player_pos[1] <= 0:
        player_pos[1] = 0
        speed = 0

    if game_over:  # Verificar si el juego ha finalizado
        arcade.draw_text("Game Over", WIDTH // 2 - 50, HEIGHT // 2, arcade.color.WHITE, 24)
        arcade.draw_text(f"Score: {score}", WIDTH // 2 - 40, HEIGHT // 2 - 30, arcade.color.WHITE, 14)
        speed = 0
        #player_pos[1] = 0
        pipe_pos = 0
        return  # Salir de la función para evitar dibujar más elementos después del "Game Over"
    

    arcade.draw_text(f"Score: {score}", 10, HEIGHT-30, arcade.color.WHITE, 14)

def update(delta_time):
    pass

# Se usara tecla SPACE para hacer el salto 
def on_key_press(key, modifiers):
    global speed
    if key == arcade.key.SPACE:
        speed += jump

score = 0
player_pos = [100, 350]
gravity = -1
speed = 0
jump = 30

pipe_pos = 700
pipe_widht = 50
pipe_height = pipe_random_height()

window = arcade.Window(WIDTH, HEIGHT, "Flappy Bird")
window.on_draw = on_draw
window.update = update
window.on_key_press = on_key_press
arcade.run()