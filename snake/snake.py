from curses import KEY_DOWN
from json.encoder import ESCAPE
import time
import pygame
import random
from pygame.locals import *

SIZE = 25

class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.picture = pygame.image.load("snake-game-apple.jpeg").convert()
        self.picture = pygame.transform.scale(self.picture, (SIZE, SIZE))
        self.x = SIZE * 5
        self.y = SIZE * 5

    def draw(self):
        self.screen.blit(self.picture, (self.x, self.y))

    def move(self):
        self.x = random.randint(0, 15) * SIZE
        self.y = random.randint(0, 11) * SIZE

class Snake:
    def __init__(self, screen, length):
        self.screen = screen
        self.length = length
        self.block = pygame.image.load("snake-game-block.png").convert()
        self.block = pygame.transform.scale(self.block, (SIZE, SIZE))
        self.x = [0]*length
        self.y = [0]*length
        self.direction = "right"

    def draw(self):
        self.screen.fill((146, 20, 180))
        for i in range(self.length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))

    def moveUp(self):
        self.direction = "up"
    def moveDown(self):
        self.direction = "down"
    def moveRight(self):
        self.direction = "right"
    def moveLeft(self):
        self.direction = "left"

    def walk(self):

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "up":
            self.y[0] -= SIZE
        elif self.direction == "down":
            self.y[0] += SIZE
        elif self.direction == "right":
            self.x[0] += SIZE
        elif self.direction == "left":
            self.x[0] -= SIZE
        self.draw()

    def increaseLength(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((800, 600))
        self.display.fill((146, 20, 180))
        self.snake = Snake(self.display, 1)
        self.apple = Apple(self.display)
        self.snake.draw()
        self.apple.draw()

    def collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200,200,200))
        self.display.blit(score, (650, 10))

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.update()
        if self.collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.apple.move()
            self.snake.increaseLength()
        for i in range(1, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game Over"
        if not (0 <= self.snake.x[0] <= 800 and 0 <= self.snake.y[0] <= 600):
                raise "Game Over"

    def game_over(self):
        self.display.fill((146, 20, 180))
        font = pygame.font.SysFont('arial', 30)
        s = font.render(f"Game over. Score: {self.snake.length}", True, (200,200,200))
        self.display.blit(s, (250, 250))
        s2 = font.render("To play again, press Enter. To exit, press Escape.", True, (200,200,200))
        self.display.blit(s2, (100, 350))
        pygame.display.update()

    def reset(self):
        self.snake = Snake(self.display, 1)
        self.apple = Apple(self.display)

    def run(self):
        open = True
        pause = False

        while open:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        open = False
                    elif event.key == K_RETURN:
                        pause = False
                    elif event.key == K_UP:
                        self.snake.moveUp()
                    elif event.key == K_DOWN:
                        self.snake.moveDown()
                    elif event.key == K_RIGHT:
                        self.snake.moveRight()
                    elif event.key == K_LEFT:
                        self.snake.moveLeft()
                if event.type == pygame.QUIT:
                    open = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.game_over()
                pause = True
                self.reset()

            time.sleep(0.15)
            
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
    quit()



