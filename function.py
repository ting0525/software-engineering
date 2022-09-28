import pygame
from Class.Variable import Variable
from Class.Rock import Rock

var = Variable()


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(var.font_name, size)
    text_surface = font.render(text, True, var.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


def new_rock():
    r = Rock()
    var.all_sprites.add(r)
    var.rocks.add(r)


def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, var.GREEN, fill_rect)
    pygame.draw.rect(surf, var.WHITE, outline_rect, 2)


def draw_lives(surf, lives, img, x, y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 32 * i  # (⾶機圖⽚的間隔)
        img_rect.y = y
        surf.blit(img, img_rect)


def draw_init():
    var.screen.blit(background_img, (0, 0))
    draw_text(screen, '太空⽣存戰!', 64, var.WIDTH / 2, var.HEIGHT / 4)
    draw_text(screen, '← →移動⾶船 空⽩鍵發射⼦彈~', 22, var.WIDTH / 2, var.HEIGHT / 2)
    draw_text(screen, '按任意鍵開始遊戲!', 18, var.WIDTH / 2, var.HEIGHT * 3 / 4)
    pygame.display.update()
    waiting = True
    while waiting:
        clock.tick(var.FPS)
        # 取得輸⼊
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            elif event.type == pygame.KEYDOWN:
                waiting = False
                return False
