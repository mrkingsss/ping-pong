from pygame import *

#window size and background's color (rgb)
window = display.set_mode((600, 600))
back = (133, 5, 50)
window.fill(back)
#classes

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
    def update_Left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -50:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 520:
            self.rect.y += self.speed
    def update_Right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > -50:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 520:
            self.rect.y += self.speed

#fps 

clock = time.Clock()

display.update()
clock.tick(60)
