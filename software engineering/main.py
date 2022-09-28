import pygame
# 遊戲迴圈
show_init = True
running = True
while running:
    if show_init:
        close = draw_init()
    if close:
        break
    show_init = False
    all_sprites = pygame.sprite.Group()
    rocks = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    powers = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for i in range(8):
        new_rock()
    score = 0
    clock.tick(FPS)
    # 取得輸⼊
    for event in pygame.event.get():
    if event.type == pygame.QUIT: