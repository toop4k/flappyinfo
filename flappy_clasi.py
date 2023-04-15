import arcade
import random

WIDTH = 500
HEIGHT = 700

class Bird:
    def __init__(self):
        self.texture = arcade.load_texture("bird.png") # Carga la textura de la imagen del bird
        self.position = [100, 350] # Posición inicial del bird
        self.speed = 0 # Velocidad del ave
        self.gravity = -1 # Gravedad aplicada al bird
        self.jump = 30 # Fuerza de salto del bird

    def draw(self):
        arcade.draw_texture_rectangle(self.position[0], self.position[1], self.texture.width, self.texture.height,self.texture) # Dibuja el bird

    def update(self):
        self.speed += self.gravity # Aplica la gravedad a la velocidad del bird
        self.speed *= 0.95 # Reduce la velocidad del bird gradualmente
        self.position[1] += self.speed # Actualiza la posición vertical del bird

    def flap(self):
        self.speed += self.jump # Aplica la fuerza de salto al bird

class Pipe:
    def __init__(self):
        self.bot_texture = arcade.load_texture("pipe_bot.png") # Carga la textura de la imagen del pipe inferior
        self.top_texture = arcade.load_texture("pipe_top.png") # Carga la textura de la imagen del pipe superior
        self.position = [700, 0] # Posición inicial del pipe
        self.width = 50 # Ancho del pipe
        self.height = [] # Altura del espacio entre los pipes
        self.random_height() # Genera una altura aleatoria para el espacio entre los pipes

    def draw(self):
        arcade.draw_texture_rectangle(self.position[0], (self.height[0] / 2) - 100, self.bot_texture.width,
                                      self.bot_texture.height, self.bot_texture) # Dibuja el pipe inferior en la pantalla
        arcade.draw_texture_rectangle(self.position[0], ((self.height[1] + HEIGHT) / 2) + 100,
                                      self.top_texture.width, self.top_texture.height, self.top_texture) # Dibuja el pipe superior en la pantalla

    def update(self):
        if self.position[0] >= -20:
            self.position[0] -= 10 # Mueve el pipe hacia la izquierda
        else:
            self.position[0] = 700 # Reinicia la posición del pipe a la derecha de la pantalla
            self.random_height() # Genera una nueva altura aleatoria para el espacio entre los pipes

    def random_height(self):
        self.height = [random.randint(50, (HEIGHT / 2) - 50), random.randint((HEIGHT / 2) + 110, HEIGHT)] # Genera una altura aleatoria para el espacio entre los pipes

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bird = Bird() # Crea una instancia del bird
        self.pipe = Pipe() # Crea una instancia del pipe
        self.score = 0 # Inicializa el puntaje del juego
        self.game_over = False # Indica si el juego ha terminado o no

    def on_draw(self):
        arcade.start_render() # Inicia el renderizado

        # Fondo
        back_texture = arcade.load_texture("back.png")
        arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, back_texture.width, back_texture.height, back_texture)

        # Dibujar bird y pipes
        self.bird.draw()
        self.pipe.draw()

        # Verificar colisión del bird con las pipes
        if self.bird.position[1] <= self.pipe.height[0] or self.bird.position[1] >= self.pipe.height[1]:
            if self.bird.position[0] in list(range(self.pipe.position[0], self.pipe.position[0] + self.pipe.width)):
                print(f"Game Over. Score {self.score}")
                self.game_over = True

        # Verificar si el bird está fuera de los límites de la ventana
        if self.bird.position[1] >= HEIGHT or self.bird.position[1] <= 0:
            self.bird.position[1] = max(min(self.bird.position[1], HEIGHT), 0)
            self.bird.speed = 0

        # Mostrar pantalla de Game Over si el juego ha terminado
        if self.game_over:
            arcade.draw_text("Game Over", WIDTH // 2 - 50, HEIGHT // 2, arcade.color.WHITE, 24)
            arcade.draw_text(f"Score: {self.score}", WIDTH // 2 - 40, HEIGHT // 2 - 30, arcade.color.WHITE, 14)
            self.bird.speed = 0
            self.pipe.position[0] = 0
            return

    def update(self, delta_time):
           # Actualizar posición del bird y los pipes
           if not self.game_over:
            self.bird.update()
            self.pipe.update()

            # Incrementar puntaje si el bird pasa un pipe
            if self.bird.position[0] == self.pipe.position[0]:
                self.score += 1

            # Verificar colisión del bird con los pipes
            if self.bird.position[1] <= self.pipe.height[0] or self.bird.position[1] >= self.pipe.height[1]:
                if self.bird.position[0] in list(range(self.pipe.position[0], self.pipe.position[0] + self.pipe.width)):
                    print(f"Game Over. Score {self.score}")
                    self.game_over = True

            # Verificar si el bird está fuera de los límites de la ventana
            if self.bird.position[1] >= HEIGHT or self.bird.position[1] <= 0:
                self.bird.position[1] = max(min(self.bird.position[1], HEIGHT), 0)
                self.bird.speed = 0

    def on_key_press(self, key, modifiers):
        # Manejar evento de presionar la tecla SPACE para hacer que el bird "flapee" "salte"
        if not self.game_over:
            if key == arcade.key.SPACE:
                self.bird.flap()
        if self.game_over:
            if key == arcade.key.R:
                self.restart_game()

    def restart_game(self):
        # Reiniciar el juego
        self.bird = Bird()
        self.pipe = Pipe()
        self.score = 0
        self.game_over = False

def main():
    game = MyGame(WIDTH, HEIGHT, "Flappy Bird")
    arcade.run()

if __name__ == "__main__":
    main()

