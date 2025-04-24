from pygame import *
from random import *

# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота
WIN_W = 700
WIN_H = 500
FPS = 60
step = 10
x1 = 10
y1 = 250
x2 = 680
y2 = 250
x3 = 300
y3 = 250
x4 = -99
y4 = -10
x5 = 698
y5 = -10
size1 = 100
size2 = 100
size3 = 100
size4 = 550
size5 = 10
size6 = 100
PLATFORMS = 2
GRANS = 2
RED = (255, 0, 0)

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h):
        super().__init__()
        self.image = transform.scale(
            image.load(img),
            # здесь - размеры картинки
            (w, h)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, img,x,y,w,h, step = step):
        super().__init__(img,x,y,w,h)
        self.step = step

    def update(self, up, down):
        keys_pressed = key.get_pressed()

        keys = key.get_pressed()

        if keys[up] and self.rect.y > 0:
            self.rect.y -= self.step

        if keys[down] and self.rect.y < WIN_H - self.rect.width:
            self.rect.y += self.step


class Ball(GameSprite):
    def __init__(self, img,x,y,w,h, speed = 3, direction = 'left'):
        super().__init__(img,x,y,w,h)
        self.speed_x = speed
        self.speed_y = speed
    def update(self):
        if self.rect.x <= 0 or self.rect.x >= WIN_W - self.rect.width:
            self.speed_x *= -1
        self.rect.x += self.speed_x
        if self.rect.y <= 0 or self.rect.y >= WIN_H - self.rect.width:
            self.speed_y *= -1
        self.rect.y += self.speed_y

class Gran(GameSprite):
    def __init__(self, img,x,y,w,h, speed = 2, direction = 'left'):
        super().__init__(img,x,y,w,h)





platform1 = Player('Vertical-Line-PNG-Clipart.png', x1, y1, size5, size6)
platform2 = Player('Vertical-Line-PNG-Clipart.png', x2, y2, size5, size6)
ball = Ball('1aa5fa42e58381cf66fbcb6d66676f18.png', x3, y3, size1, size2)
gran1 = Gran('Vertical-Line-PNG-Clipart.png', x4, y4, size3, size4)
gran2 = Gran('Vertical-Line-PNG-Clipart.png', x5, y5, size3, size4)

# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))
# создание таймера
clock = time.Clock()

# название окна
display.set_caption(".")


font.init()
title_font = font.SysFont('papyrus', 70)
lost = title_font.render('Поражение!', True, RED)

# задать картинку фона такого же размера, как размер окна
background = transform.scale(
    image.load("286233-Ultra-Victoria-Stenova-1536x928.jpg"),
    # здесь - размеры картинки
    (WIN_W, WIN_H)
)

grans = sprite.Group()
grans.add(gran1)
grans.add(gran2)

platforms = sprite.Group()
platforms.add(platform1)
platforms.add(platform2)
# игровой цикл
game = True
finish = False
while game:
    # отобразить картинку фона


    if not finish:
        window.blit(background, (0, 0))

        platform1.draw(window)
        platform1.update(K_w, K_s)

        platform2.draw(window)
        platform2.update(K_UP, K_DOWN)

        ball.draw(window)
        ball.update()

        gran1.draw(window)
        gran1.update()

        gran2.draw(window)
        gran2.update()

        if sprite.spritecollide(ball, grans, False):
            window.blit(lost, (100, 200))
            display.update()
            finish = True

        if sprite.spritecollide(ball, platforms, False):
            display.update()
            ball.speed_x *= -1
            ball.speed_y *= -1

    else:
        for p in platforms:
            p.kill()
        
        for g in grans:
            g.kill()
        time.delay(1500)

        grans = sprite.Group()
        grans.add(gran1)
        grans.add(gran2)

        platforms = sprite.Group()
        platforms.add(platform1)
        platforms.add(platform2)

        finish = False

    # слушать события и обрабатывать
    for e in event.get():
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False



    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick(FPS)