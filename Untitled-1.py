from pygame import *



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
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


back = (0, 0, 128)
win_width = 1100
win_height = 750
window = display.set_mode((win_width,win_height))
window.fill(back)



game = True
finish = False
clock = time.Clock()
FPS = 60

mixer.init()


racket1 = Player('racket.png', 30, 200, 10, 50, 150) 
racket2 = Player('racket.png', 1000, 200, 10, 50, 150)
ball = GameSprite('tenis_ball.png', 550, 375, 1, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 7
speed_y = 7

kick = mixer.Sound("kick.ogg")

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        draw.rect(window, (255, 255, 255),(0, 0, 20, 750))
        draw.rect(window, (255, 255, 255),(1080, 0, 20, 750))
        draw.rect(window, (255, 255, 255),(0, 0, 1100, 20))
        draw.rect(window, (255, 255, 255),(0, 730, 1100, 20))
        draw.rect(window, (255, 255, 255),(550, 0, 25, 750))
        draw.rect(window, (255, 255, 255),(0, 375, 1100, 10))
        draw.rect(window, (0, 0, 0),(557, 20, 10, 710))

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        
        # если мяч достигает границ экрана меняем направление его движения
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        # если мяч улетел дальше ракетки, выводим условие проигрыша для первого игрока
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        # если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True        


        if sprite.collide_rect(racket2,ball) or sprite.collide_rect(racket1,ball ):
            game = True
            kick.play()       
       

        racket1.reset()
        racket2.reset()
        ball.reset()
    else:
        keys = key.get_pressed()
        if keys[K_KP_ENTER] :
            ball.rect.y = 375
            ball.rect.x = 550
            finish=False

    display.update()
    
    clock.tick(FPS)