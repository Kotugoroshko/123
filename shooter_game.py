#Створи власний Шутер!

from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
           self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
           self.rect.x += self.speed

    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.y, 15, 30, -15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global lost, score
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(80, 620)
            lost += 1
        if sprite.spritecollide(self, bullets, False):
            score+=1
            self.rect.y = 0
            self.rect.x = randint(80, 620)

class Label():
    def set_text(self, text, fsize = 12, text_color = (0,0,0)):
        self.image = font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x = 0, shift_y = 0):
        window.blit(self.image, (shift_x,shift_y))

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

score = 0
lost = 0

font.init()



rocket = Player("rocket.png", 315, 385, 65, 80, 7)

# enemy = Enemy('ufo.png', randint(80, 620), 0, 80, 50, randint(3,10))

enemies = sprite.Group()
for i in range (1,6):
    enemy = Enemy('ufo.png', randint(80, 620), 0, 80, 50, randint(3,5))
    enemies.add(enemy)

bullets = sprite.Group()

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

sound_fire = mixer.Sound("fire.ogg")
lost_text=Label()
score_text=Label()

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.fire()
                sound_fire.play()

    if finish!= True:
        window.blit(background,(0,0))
        rocket.update()
        rocket.reset()
        bullets.update()
        enemies.update()
        enemies.draw(window)
        bullets.draw(window)
        # enemy.update()

        # enemy.reset()
        lost_text.set_text("Пропущено: "+ str(lost), 20, (255, 255, 255))
        lost_text.draw(10,10)

        score_text.set_text("Рахунок: "+ str(score), 20, (90, 167, 255))
        score_text.draw(10,60)

            # sprite.groupcollide(enemies, bullets, False, True)
                    

    if sprite.spritecollide(rocket, enemies, False) or lost >= 10:
        loss = Label()
        loss.set_text('YOU LOSS', 60, (250, 0, 0))
        window.blit(background,(0,0))
        loss.draw(300, 250)
        finish = True
    if score >= 10:
        finish = True
        win = Label()
        win.set_text('YOU WIN', 60, (255, 215, 0))
        window.blit(background,(0,0))
        loss.draw(300, 250)
        finish = True
    
        

    display.update()
    clock.tick(FPS)