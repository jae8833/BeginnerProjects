from tkinter import Y
import pygame
import sys
import random

WIDTH = 800
HEIGHT = 400
SCORE = [0, 0]

class Puck(pygame.sprite.Sprite):
    def __init__(self,userWin):
        super().__init__()
        self.image = pygame.image.load("pong-2.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center = (WIDTH / 2, HEIGHT / 2))
        num1 = random.randint(5, 7)
        num2 = 8 - num1
        if random.randint(0,1) == 0:
            num2 *= -1
        if not userWin:
            num1 *= -1
        self.x_speed = num1
        self.y_speed = num2

    def changeDirection(self, isX):
        if isX:
            self.x_speed *= random.uniform(-1.05, -1.15)
        else:
            self.y_speed *= random.uniform(-1.15, -1.25)

    def glide(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def update(self):
        self.glide()

class Computer(pygame.sprite.Sprite):
    def __init__(self,puck):
        super().__init__()
        self.image = pygame.image.load("pong-1.jpeg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 50))
        self.rect = self.image.get_rect(midright = (WIDTH - 25, HEIGHT / 2))
        self.puck = puck

    def still(self):
        puck_position = self.puck.sprite.rect.y
        movement = self.rect.y - puck_position
        self.rect.y += movement * 0.25

    def move(self):
        puck_position = self.puck.sprite.rect.y
        movement = self.rect.y - puck_position
        self.rect.y -= movement * 0.20

    def update(self):
        self.move()

def collision(user, computer, puck):
    if puck.sprite.rect.left < -200 or puck.sprite.rect.right > WIDTH + 200:
        if puck.sprite.rect.left < 0:
            computer.sprite.still()
            userWin = False
            SCORE[1] += 1
        else:
            computer.sprite.still()
            userWin = True
            SCORE[0] += 1
        puck.sprite.kill()
        puck.add(Puck(userWin))
    elif puck.sprite.rect.top < 0 or puck.sprite.rect.bottom > HEIGHT:
        puck.sprite.changeDirection(False)
    if user.sprite.rect.top < 0:
        user.sprite.rect.top = 0
    if user.sprite.rect.bottom > HEIGHT:
            user.sprite.rect.bottom = HEIGHT
    if computer.sprite.rect.top < 0:
        computer.sprite.rect.top = 0
    if computer.sprite.rect.bottom > HEIGHT:
            computer.sprite.rect.bottom = HEIGHT
    if pygame.sprite.collide_rect(user.sprite, puck.sprite):
        puck.sprite.changeDirection(True)
        puck.sprite.changeDirection(False)
    elif pygame.sprite.collide_rect(puck.sprite, computer.sprite):
        puck.sprite.changeDirection(True)
        puck.sprite.changeDirection(False)

class User(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pong-1.jpeg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 50))
        self.rect = self.image.get_rect(midleft = (25, HEIGHT / 2))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 10
        elif keys[pygame.K_DOWN]:
            self.rect.y += 10
        
    def update(self):
        self.player_input()


class Game():
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption("Pong")
        self.game_active = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 50)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((0, 0, 0))
        self.display = pygame.image.load("pong-3.jpeg").convert()
        self.display = pygame.transform.scale(self.display, (WIDTH, HEIGHT))
        self.user = pygame.sprite.GroupSingle()
        self.user.add(User())
        self.puck = pygame.sprite.GroupSingle()
        self.puck.add(Puck(True))
        self.computer = pygame.sprite.GroupSingle()
        self.computer.add(Computer(self.puck))
        self.user_score = self.font.render(f"{SCORE[0]}", False, "white")
        self.user_score_rect = self.user_score.get_rect(center = (200, 50))
        self.comp_score = self.font.render(f"{SCORE[1]}", False, "white")
        self.comp_score_rect = self.comp_score.get_rect(center = (600, 50))
        pygame.mixer.music.load("bg-music.wav")
        pygame.mixer.music.play(-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key ==pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

            if self.game_active:
                self.screen.blit(self.display,(0,0))
                for i in range(0, HEIGHT, 50):
                    pygame.draw.lines(self.screen, "white", False, [(WIDTH / 2, i + 12.5),(WIDTH / 2, i + 37.5)], width=1)
                self.user.draw(self.screen)
                self.user.update()
                self.computer.draw(self.screen)
                self.computer.update()
                self.puck.draw(self.screen)
                self.puck.update()
                collision(self.user,self.computer,self.puck)
                self.user_score = self.font.render(f"{SCORE[0]}", False, "white")
                self.user_score_rect = self.user_score.get_rect(center = (200, 50))
                self.comp_score = self.font.render(f"{SCORE[1]}", False, "white")
                self.comp_score_rect = self.comp_score.get_rect(center = (600, 50))
                self.screen.blit(self.user_score,self.user_score_rect)
                self.screen.blit(self.comp_score,self.comp_score_rect)

if __name__ == "__main__":
    game = Game()
    game.run()