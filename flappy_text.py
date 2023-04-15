import arcade
import random

WIDTH = 500
HEIGHT = 700
game_over = False  # Bandera para indicar si el juego ha finalizado

def pipe_random_height():
    # Generar una altura random para las tuberías
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

    # Dibujar fondo
    back_texture = arcade.load_texture("back.png")
    arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, back_texture.width, back_texture.height, back_texture)

    # Dibujar player / pajarito
    bird_texture = arcade.load_texture("bird.png")
    arcade.draw_texture_rectangle(player_pos[0], player_pos[1], bird_texture.width, bird_texture.height, bird_texture)

    # dibujar pipe / tuberia 
    pipe_bot_texture = arcade.load_texture("pipe_bot.png")
    arcade.draw_texture_rectangle(pipe_pos, (pipe_height[0]/2)-100 , pipe_bot_texture.width, pipe_bot_texture.height, pipe_bot_texture)
    pipe_top_texture = arcade.load_texture("pipe_top.png")
    arcade.draw_texture_rectangle(pipe_pos, ((pipe_height[1] + HEIGHT)/2)+100 , pipe_top_texture.width, pipe_top_texture.height, pipe_top_texture)

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
        pipe_pos = 0
        return  # Salir de la función para evitar dibujar más elementos
    
def update(delta_time):
    pass

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
