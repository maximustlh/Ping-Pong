from pygame import *

from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#Game Scene
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

#Flags responsible for game state
game = True
finish = False
clock = time.Clock()
FPS = 60

#Egg and Spatula
spatula1 = Player("spatula.png", 30, 200, 4, 125, 175)
spatula2 = Player("spatula.png", 520, 200, 4, 125, 175)
egg = GameSprite("egg.png", 200, 200, 4, 75, 75)

#Font
font.init()
font = font.SysFont("Arial", 35)

#Lose title
lose1 = font.render("PLAYER 1 - YOU LOSE!", True, (180, 0, 0))
lose2 = font.render("PLAYER 2 - YOU LOSE!", True, (180, 0, 0))

speed_x = 3
speed_y = 3

#Gameloop
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)

        spatula1.update_l()
        spatula2.update_r()

        egg.rect.x += speed_x
        egg.rect.y += speed_y

        #if egg hits the spatula
        if sprite.collide_rect(spatula1, egg) or sprite.collide_rect(spatula2, egg):
            speed_x *= -1
            speed_y *= -1 

        #if ball reaches edge of screen
        if egg.rect.y > 425 or egg.rect.y < 0:
            speed_y *= -1

        #if ball reach the left (lose condition for player 1)
        if egg.rect.x < 0:
            finish = True
            window.blit(lose1, (135, 200))
            game_over = True

        #if ball reach the right (lose condition for player 2) 
        if egg.rect.x > 600:
            finish = True
            window.blit(lose2, (135, 200))
            game_over = True

        spatula1.reset()
        spatula2.reset()
        egg.reset()

        display.update()
        clock.tick(FPS)
