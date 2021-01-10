import pygame
import os
import sys
import random


# Игральная кость
class Dice:
    def __init__(self):
        self.val_1 = 0
        self.val_2 = 0

    def roll(self):
        self.val_1 = random.randint(1, 6)
        self.val_2 = random.randint(1, 6)


# Шашка
class Checker:
    def __init__(self, x_pos, y_pos, side, sprite, clicked=False):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.side = side
        self.sprite = sprite
        self.clicked = clicked


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def draw_menu():
    screen.fill((255, 255, 255))
    screen.blit(title, ((width - title.get_width()) // 2, 0))

    screen.blit(quit_text, (quit_x, quit_y))
    pygame.draw.rect(screen, (255, 255, 255), quit_button, 1)

    screen.blit(begin_text, (begin_x, begin_y))
    pygame.draw.rect(screen, (255, 255, 255), begin_button, 1)

    screen.blit(o_text, (o_x, o_y))
    pygame.draw.rect(screen, (255, 255, 255), o_button, 1)

    screen.blit(r_text, (r_x, r_y))
    pygame.draw.rect(screen, (255, 255, 255), r_button, 1)


def process_options():
    global b_p, op_text, options
    while options:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if op_button.collidepoint(mouse_pos):
                    if b_p.split('-')[1] == 'True':
                        with open("config.txt", "w") as conf:
                            conf.write('begin_position-False')
                        with open("config.txt", "r") as conf:
                            b_p = conf.read()
                        op_text = o_font.render("Начальное положение шашек", True, (200, 200, 200))
                    elif b_p.split('-')[1] == 'False':
                        with open("config.txt", "w") as conf:
                            conf.write('begin_position-True')
                        with open("config.txt", "r") as conf:
                            b_p = conf.read()
                        op_text = o_font.render("Начальное положение шашек", True, (10, 10, 10))
                if back_button.collidepoint(mouse_pos):
                    options = False

        screen.fill((255, 255, 255))

        screen.blit(op_text, (op_x, op_y))
        pygame.draw.rect(screen, (255, 255, 255), op_button, 1)

        screen.blit(back_text, (back_x, back_y))
        pygame.draw.rect(screen, (255, 255, 255), back_button, 1)

        clock.tick(fps)
        pygame.display.flip()


def process_rules():
    os.system("start rules.txt")


def draw_board():
    # Рисование доски
    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, (0, 0, 0), ((0, height), (50, (height // 2) + 40), (100, height)))
    pygame.draw.polygon(screen, (0, 0, 0), ((100, height), (150, (height // 2) + 40), (200, height)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((200, height), (250, (height // 2) + 40), (300, height)))
    pygame.draw.polygon(screen, (0, 0, 0), ((300, height), (350, (height // 2) + 40), (400, height)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((400, height), (450, (height // 2) + 40), (500, height)))
    pygame.draw.polygon(screen, (0, 0, 0), ((500, height), (550, (height // 2) + 40), (600, height)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((600, height), (650, (height // 2) + 40), (700, height)))
    pygame.draw.polygon(screen, (0, 0, 0), ((700, height), (750, (height // 2) + 40), (800, height)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((800, height), (850, (height // 2) + 40), (900, height)))
    pygame.draw.polygon(screen, (0, 0, 0), ((900, height), (950, (height // 2) + 40), (1000, height)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((1000, height), (1050, (height // 2) + 40), (1100, height)))
    pygame.draw.polygon(screen, (0, 0, 0), ((1100, height), (1150, (height // 2) + 40), (1200, height)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((0, 0), (50, (height // 2) - 40), (100, 0)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((100, 0), (150, (height // 2) - 40), (200, 0)))
    pygame.draw.polygon(screen, (0, 0, 0), ((200, 0), (250, (height // 2) - 40), (300, 0)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((300, 0), (350, (height // 2) - 40), (400, 0)))
    pygame.draw.polygon(screen, (0, 0, 0), ((400, 0), (450, (height // 2) - 40), (500, 0)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((500, 0), (550, (height // 2) - 40), (600, 0)))
    pygame.draw.polygon(screen, (0, 0, 0), ((600, 0), (650, (height // 2) - 40), (700, 0)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((700, 0), (750, (height // 2) - 40), (800, 0)))
    pygame.draw.polygon(screen, (0, 0, 0), ((800, 0), (850, (height // 2) - 40), (900, 0)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((900, 0), (950, (height // 2) - 40), (1000, 0)))
    pygame.draw.polygon(screen, (0, 0, 0), ((1000, 0), (1050, (height // 2) - 40), (1100, 0)), 1)
    pygame.draw.polygon(screen, (0, 0, 0), ((1100, 0), (1150, (height // 2) - 40), (1200, 0)))

    pygame.draw.line(screen, (0, 0, 0), (1200, 0), (1200, height), 4)

    pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, height), 4)

    # Рисование "Бросить кости"
    screen.blit(d_text, (1230, 700))

    # Рисование костей
    if dice.val_1 == 1:
        screen.blit(dice_one_sprite.image, (1250, 100))
    elif dice.val_1 == 2:
        screen.blit(dice_two_sprite.image, (1250, 100))
    elif dice.val_1 == 3:
        screen.blit(dice_three_sprite.image, (1250, 100))
    elif dice.val_1 == 4:
        screen.blit(dice_four_sprite.image, (1250, 100))
    elif dice.val_1 == 5:
        screen.blit(dice_five_sprite.image, (1250, 100))
    elif dice.val_1 == 6:
        screen.blit(dice_six_sprite.image, (1250, 100))

    if dice.val_2 == 1:
        screen.blit(dice_one_sprite.image, (1250, 300))
    elif dice.val_2 == 2:
        screen.blit(dice_two_sprite.image, (1250, 300))
    elif dice.val_2 == 3:
        screen.blit(dice_three_sprite.image, (1250, 300))
    elif dice.val_2 == 4:
        screen.blit(dice_four_sprite.image, (1250, 300))
    elif dice.val_2 == 5:
        screen.blit(dice_five_sprite.image, (1250, 300))
    elif dice.val_2 == 6:
        screen.blit(dice_six_sprite.image, (1250, 300))

    # Рисование шашек
    for checker in checkers:
        screen.blit(checker.sprite.image, (checker.x_pos, checker.y_pos))

    # Рисование снятых фишек
    screen.blit(white_sprite.image, (1250, 500))
    screen.blit(count_w_text, (1325, 505))

    screen.blit(black_sprite.image, (1250, 600))
    screen.blit(count_b_text, (1325, 605))


if __name__ == '__main__':
    # Init
    pygame.init()
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)

    # Основные окна
    menu = True
    options = True
    game = True
    w_win = False
    b_win = False

    # FPS
    fps = 120
    clock = pygame.time.Clock()

    # Кнопки и названия в меню
    title_font = pygame.font.Font(None, 120)
    title = title_font.render("Нарды", True, (10, 10, 10))

    q_font = pygame.font.Font(None, 50)
    quit_text = q_font.render("Выйти", True, (100, 100, 100))
    quit_x = (width - quit_text.get_width()) // 2
    quit_y = 700
    quit_button = pygame.Rect(quit_x, quit_y, quit_text.get_width(), quit_text.get_height())

    b_font = pygame.font.Font(None, 80)
    begin_text = b_font.render("Начать", True, (10, 10, 10))
    begin_x = (width - begin_text.get_width()) // 2
    begin_y = 200
    begin_button = pygame.Rect(begin_x, begin_y, begin_text.get_width(), begin_text.get_height())

    o_font = pygame.font.Font(None, 60)
    o_text = o_font.render("Настройки", True, (10, 10, 10))
    o_x = (width - o_text.get_width()) // 2
    o_y = 350
    o_button = pygame.Rect(o_x, o_y, o_text.get_width(), o_text.get_height())

    r_font = pygame.font.Font(None, 60)
    r_text = r_font.render("Правила", True, (10, 10, 10))
    r_x = (width - r_text.get_width()) // 2
    r_y = 500
    r_button = pygame.Rect(r_x, r_y, r_text.get_width(), r_text.get_height())

    # Считывание настроек
    with open("config.txt", "r") as conf:
        b_p = conf.read()
        print(b_p)

    # Кнопки настроек
    op_font = pygame.font.Font(None, 60)
    if b_p.split('-')[1] == 'True':
        op_text = o_font.render("Начальное положение шашек", True, (10, 10, 10))
    else:
        op_text = o_font.render("Начальное положение шашек", True, (200, 200, 200))
    op_x = (width - op_text.get_width()) // 2
    op_y = 300
    op_button = pygame.Rect(op_x, op_y, op_text.get_width(), op_text.get_height())

    back_font = pygame.font.Font(None, 50)
    back_text = back_font.render("Назад", True, (100, 100, 100))
    back_x = (width - back_text.get_width()) // 2
    back_y = 600
    back_button = pygame.Rect(back_x, back_y, back_text.get_width(), back_text.get_height())

    # Меню
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if quit_button.collidepoint(mouse_pos):
                    quit_text = q_font.render("Выйти", True, (150, 150, 150))
                    clock.tick(fps)
                    quit()
                # Выход
                if begin_button.collidepoint(mouse_pos):
                    begin_text = b_font.render("Начать", True, (150, 150, 150))
                    clock.tick(fps)
                    menu = False
                # Настройки
                if o_button.collidepoint(mouse_pos):
                    options = True
                    process_options()
                # Правила
                if r_button.collidepoint(mouse_pos):
                    process_rules()
        draw_menu()
        clock.tick(fps)
        pygame.display.flip()

    pygame.display.flip()

    # Считывание настроек
    with open("config.txt", "r") as conf:
        b_p = conf.read()
        print(b_p)

    # Изменение размеров
    size = width, height = 1400, 800
    screen = pygame.display.set_mode(size)

    # Текстуры
    black_sprites = pygame.sprite.Group()
    black_sprite = pygame.sprite.Sprite()
    black_sprite.image = load_image("black_texture.png")
    black_sprite.rect = black_sprite.image.get_rect()

    white_sprites = pygame.sprite.Group()
    white_sprite = pygame.sprite.Sprite()
    white_sprite.image = load_image("white_texture.png")
    white_sprite.rect = white_sprite.image.get_rect()

    # Кости
    dice_sprites = pygame.sprite.Group()

    dice_one_sprite = pygame.sprite.Sprite()
    dice_one_sprite.image = load_image("one_dice.png")
    dice_one_sprite.rect = dice_one_sprite.image.get_rect()

    dice_two_sprite = pygame.sprite.Sprite()
    dice_two_sprite.image = load_image("two_dice.png")
    dice_two_sprite.rect = dice_two_sprite.image.get_rect()

    dice_three_sprite = pygame.sprite.Sprite()
    dice_three_sprite.image = load_image("three_dice.png")
    dice_three_sprite.rect = dice_three_sprite.image.get_rect()

    dice_four_sprite = pygame.sprite.Sprite()
    dice_four_sprite.image = load_image("four_dice.png")
    dice_four_sprite.rect = dice_four_sprite.image.get_rect()

    dice_five_sprite = pygame.sprite.Sprite()
    dice_five_sprite.image = load_image("five_dice.png")
    dice_five_sprite.rect = dice_five_sprite.image.get_rect()

    dice_six_sprite = pygame.sprite.Sprite()
    dice_six_sprite.image = load_image("six_dice.png")
    dice_six_sprite.rect = dice_six_sprite.image.get_rect()

    dice = Dice()
    dice.val = 1

    # Шашки
    checkers = []

    # Начальное положение
    if b_p.split('-')[1] == 'True':
        # Определение слева направо
        checkers.append(Checker(31, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31, 20 * 1, 'white', white_sprite))
        checkers.append(Checker(31, 20 * 2, 'white', white_sprite))
        checkers.append(Checker(31, 20 * 3, 'white', white_sprite))
        checkers.append(Checker(31, 20 * 4, 'white', white_sprite))

        checkers.append(Checker(31, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31, 800 - 38 - (20 * 1), 'black', black_sprite))
        checkers.append(Checker(31, 800 - 38 - (20 * 2), 'black', black_sprite))
        checkers.append(Checker(31, 800 - 38 - (20 * 3), 'black', black_sprite))
        checkers.append(Checker(31, 800 - 38 - (20 * 4), 'black', black_sprite))

        checkers.append(Checker(31 + 400, 20 * 0, 'black', black_sprite))
        checkers.append(Checker(31 + 400, 20 * 1, 'black', black_sprite))
        checkers.append(Checker(31 + 400, 20 * 2, 'black', black_sprite))

        checkers.append(Checker(31 + 400, 800 - 38 - (20 * 0), 'white', white_sprite))
        checkers.append(Checker(31 + 400, 800 - 38 - (20 * 1), 'white', white_sprite))
        checkers.append(Checker(31 + 400, 800 - 38 - (20 * 2), 'white', white_sprite))

        checkers.append(Checker(31 + 600, 20 * 0, 'black', black_sprite))
        checkers.append(Checker(31 + 600, 20 * 1, 'black', black_sprite))
        checkers.append(Checker(31 + 600, 20 * 2, 'black', black_sprite))
        checkers.append(Checker(31 + 600, 20 * 3, 'black', black_sprite))
        checkers.append(Checker(31 + 600, 20 * 4, 'black', black_sprite))

        checkers.append(Checker(31 + 600, 800 - 38 - (20 * 0), 'white', white_sprite))
        checkers.append(Checker(31 + 600, 800 - 38 - (20 * 1), 'white', white_sprite))
        checkers.append(Checker(31 + 600, 800 - 38 - (20 * 2), 'white', white_sprite))
        checkers.append(Checker(31 + 600, 800 - 38 - (20 * 3), 'white', white_sprite))
        checkers.append(Checker(31 + 600, 800 - 38 - (20 * 4), 'white', white_sprite))

        checkers.append(Checker(31 + 1100, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31 + 1100, 20 * 1, 'white', white_sprite))

        checkers.append(Checker(31 + 1100, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31 + 1100, 800 - 38 - (20 * 1), 'black', black_sprite))

    else:
        checkers.append(Checker(31, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31, 20 * 1, 'white', white_sprite))
        checkers.append(Checker(31, 20 * 2, 'white', white_sprite))
        checkers.append(Checker(31, 20 * 3, 'white', white_sprite))
        checkers.append(Checker(31 + 100, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31 + 200, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31 + 300, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31 + 400, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31 + 500, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31 + 600, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31 + 700, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31 + 800, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31 + 900, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31 + 1000, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31 + 1100, 20 * 0, 'white', white_sprite))
        checkers.append(Checker(31, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31, 800 - 38 - (20 * 1), 'black', black_sprite))
        checkers.append(Checker(31, 800 - 38 - (20 * 2), 'black', black_sprite))
        checkers.append(Checker(31, 800 - 38 - (20 * 3), 'black', black_sprite))
        checkers.append(Checker(31 + 100, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31 + 200, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31 + 300, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31 + 400, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31 + 500, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31 + 600, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31 + 700, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31 + 800, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31 + 900, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31 + 1000, 800 - 38 - (20 * 0), 'black', black_sprite))
        checkers.append(Checker(31 + 1100, 800 - 38 - (20 * 0), 'black', black_sprite))

    # Счёт
    count_b = 0
    count_b_font = pygame.font.Font(None, 50)
    count_b_text = count_b_font.render(str(count_b), True, (255, 100, 100))

    count_w = 0
    count_w_font = pygame.font.Font(None, 50)
    count_w_text = count_w_font.render(str(count_w), True, (255, 100, 100))

    # Бросок кости
    d_font = pygame.font.Font(None, 30)
    d_text = d_font.render("Бросить кость", True, (255, 100, 100))
    d_button = pygame.Rect(1230, 700, d_text.get_width(), d_text.get_height())

    # Игра
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if d_button.collidepoint(mouse_pos):
                    dice.roll()
            for checker in checkers:

                # Счёт чёрных
                count_b_font = pygame.font.Font(None, 50)
                count_b_text = count_b_font.render(str(count_b), True, (255, 100, 100))

                # Счёт белых
                count_w_font = pygame.font.Font(None, 50)
                count_w_text = count_w_font.render(str(count_w), True, (255, 100, 100))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if pygame.Rect(checker.x_pos, checker.y_pos, 38, 38).collidepoint(
                            mouse_pos):
                        if checker.clicked:
                            checker.clicked = False
                        else:
                            checker.clicked = True
                        print(checker.clicked)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        mouse_pos = pygame.mouse.get_pos()
                        if pygame.Rect(checker.x_pos, checker.y_pos, 38, 38).collidepoint(
                                mouse_pos):
                            if checker.side == 'white':
                                count_w += 1
                            elif checker.side == 'black':
                                count_b += 1
                            checkers.remove(checker)
                if checker.clicked:
                    mouse_pos = pygame.mouse.get_pos()
                    checker.x_pos = mouse_pos[0]
                    checker.y_pos = mouse_pos[1]

        draw_board()
        clock.tick(fps)
        pygame.display.flip()
        loose = []
        for checker in checkers:
            if checker.side == 'black':
                loose.append('b')
            else:
                loose.append('w')
        if 'b' in loose and 'w' in loose:
            game = True
        else:
            if 'b' in loose:
                w_win = True
            else:
                b_win = True
            game = False

    w_win_font = pygame.font.Font(None, 120)
    w_win_text = w_win_font.render("ПОБЕДА БЕЛЫХ", True, (10, 10, 10))

    qw_font = pygame.font.Font(None, 80)
    qw_text = qw_font.render("Выйти", True, (100, 100, 100))
    qw_button = pygame.Rect((width - qw_text.get_width()) // 2, 600, qw_text.get_width(), qw_text.get_height())

    # Белые победили
    while w_win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if qw_button.collidepoint(mouse_pos):
                    qw_text = qw_font.render("Выйти", True, (150, 150, 150))
                    clock.tick(fps)
                    quit()
        screen.fill((255, 255, 255))
        screen.blit(w_win_text, ((w_win_text.get_width() // 2), 280))
        screen.blit(qw_text, (((width - qw_text.get_width()) // 2), 600))
        pygame.display.flip()

    b_win_font = pygame.font.Font(None, 120)
    b_win_text = b_win_font.render("ПОБЕДА ЧЁРНЫХ", True, (10, 10, 10))

    # Чёрные победили
    while b_win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if qw_button.collidepoint(mouse_pos):
                    qw_text = qw_font.render("Выйти", True, (150, 150, 150))
                    clock.tick(fps)
                    quit()
        screen.fill((255, 255, 255))
        screen.blit(b_win_text, ((b_win_text.get_width() // 2), 280))
        screen.blit(qw_text, (((width - qw_text.get_width()) // 2), 600))
        pygame.display.flip()
