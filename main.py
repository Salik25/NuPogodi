# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from os import path
import random

img_dir = path.join(path.dirname(__file__), "texture")
pygame.font.init()
WIDTH = 560
HEIGHT = 680
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
font_name = pygame.font.match_font('arial')
clock = pygame.time.Clock()


def new_egg():
    egg = Egg()
    all_sprites.add(egg)
    eggs.add(egg)


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surf.blit(text_surface, text_rect)


def update_sr_mark(sr_mark, new_mark, len_of_marks):
    sr_mark = ((sr_mark * len_of_marks) + new_mark) / (len_of_marks + 1)
    return sr_mark, len_of_marks + 1


def update_list_of_kol_mark(list_of_mark, new_mark):
    if new_mark.mark == 1:
        list_of_mark[0] += 1
    elif new_mark.mark == 2:
        list_of_mark[1] += 1
    elif new_mark.mark == 3:
        list_of_mark[2] += 1
    elif new_mark.mark == 4:
        list_of_mark[3] += 1
    elif new_mark.mark == 5:
        list_of_mark[4] += 1
    return list_of_mark


def add(sr_mark, len_of_marks, list_of_marks):
    file = open("scores.txt", "w")
    file.write(str(sr_mark) + "|" + str(len_of_marks) + "|" + str(list_of_marks[0]) + '^' + str(list_of_marks[1])
               + '^' + str(list_of_marks[2]) + '^' + str(list_of_marks[3]) + '^' + str(list_of_marks[4]))
    file.close()


def readsc():
    file = open("scores.txt", "r")
    massiw = file.readline().split("|")
    massiw[2] = massiw[2].split("^")
    massiw[0] = float(massiw[0])
    massiw[1] = int(massiw[1])
    for x in massiw[2]:
        massiw[2][massiw[2].index(x)] = int(massiw[2][massiw[2].index(x)])
    file.close()
    return massiw


def hs(sr_mark, len_of_marks, list_of_marks):
    last_sr_mark, last_len_of_marks, last_list_of_marks = readsc()
    if sr_mark > last_sr_mark or sr_mark >= last_sr_mark and len_of_marks > last_len_of_marks:
        add(sr_mark, len_of_marks, list_of_marks)
    elif sr_mark >= last_sr_mark and list_of_marks[3] + list_of_marks[4] > last_list_of_marks[3] + last_list_of_marks[
        4] or sr_mark == last_sr_mark and (list_of_marks[3] + list_of_marks[4]) - (
            list_of_marks[0] + list_of_marks[1] + list_of_marks[2]) > (
            last_list_of_marks[3] + last_list_of_marks[4]) - (
            last_list_of_marks[0] + last_list_of_marks[1] + last_list_of_marks[2]):
        add(sr_mark, len_of_marks, list_of_marks)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(korz, (110, 80))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.radius = int(self.rect.width * 0.35 / 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)  # проверка хитбокса
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = (HEIGHT / 3) + 365
        self.speedx = 0

    def update(self):
        self.speedx = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_a]:
            self.speedx = -10
        elif key_state[pygame.K_d]:
            self.speedx = 10
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Fone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        pygame.draw.line(self.image, YELLOW, (0, HEIGHT / 4), ((WIDTH / 2) - 100, HEIGHT / 3), 10)
        pygame.draw.line(self.image, BLUE, (WIDTH, HEIGHT / 4), ((WIDTH / 2) + 100, HEIGHT / 3), 10)
        pygame.draw.line(self.image, BLUE, (WIDTH, (HEIGHT / 4) + 200), ((WIDTH / 2) + 100, (HEIGHT / 3) + 200), 10)
        pygame.draw.line(self.image, YELLOW, (0, (HEIGHT / 4) + 200), ((WIDTH / 2) - 100, (HEIGHT / 3) + 200), 10)


class Delets_elem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = (HEIGHT / 3) + 350


class Egg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.random_pos = random.randrange(100)
        if self.random_pos in range(0, 21):
            self.image = pygame.transform.scale(mark_1, (60, 60))
            self.mark = 1
        if self.random_pos in range(20, 41):
            self.image = pygame.transform.scale(mark_2, (60, 60))
            self.mark = 2
        if self.random_pos in range(40, 61):
            self.image = pygame.transform.scale(mark_3, (60, 60))
            self.mark = 3
        if self.random_pos in range(60, 81):
            self.image = pygame.transform.scale(mark_4, (60, 60))
            self.mark = 4
        if self.random_pos in range(80, 101):
            self.image = pygame.transform.scale(mark_5, (60, 60))
            self.mark = 5
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rigth_traektor = [-2, 1]
        self.left_traektor = [3, 2]
        self.pos = random.randrange(4)
        self.radius = int(self.rect.width * 0.55 / 2)
        # pygame.draw.circle(self.image, BLUE, self.rect.center, self.radius) #проверка хитбокса
        if self.pos == 0:
            self.rect.x, self.rect.bottom = (0, HEIGHT / 4)
            self.traekt_x, self.traekt_y = self.left_traektor
            # self.smena = ((WIDTH / 2) - 100, HEIGHT / 3)
        elif self.pos == 1:
            self.rect.x, self.rect.bottom = (WIDTH, HEIGHT / 4)
            self.traekt_x, self.traekt_y = self.rigth_traektor
            # self.speedy = random.randrange(1, 10)
        elif self.pos == 2:
            self.rect.x, self.rect.bottom = (WIDTH, (HEIGHT / 4) + 200)
            self.traekt_x, self.traekt_y = self.rigth_traektor
        elif self.pos == 3:
            self.rect.x, self.rect.bottom = (0, (HEIGHT / 4) + 200)
            self.traekt_x, self.traekt_y = self.left_traektor

    def update(self):
        self.rect.y += self.traekt_y
        self.rect.x += self.traekt_x
        if self.rect.y > HEIGHT / 3 and self.pos in [0, 1] and self.rect.left > (WIDTH / 2) - 100 and self.pos in [0,
                                                                                                                   1]:
            self.traekt_x = 0
        elif self.rect.y > (HEIGHT / 3) + 200 and self.pos in [2, 3] and self.rect.right < (
                WIDTH / 2) + 100 and self.pos in [2, 3]:
            self.traekt_x = 0
            self.traekt_y = 3


# текстуры
korz = pygame.image.load(path.join(img_dir, "korz.png")).convert()
mark_1 = pygame.image.load(path.join(img_dir, "1.png")).convert()
mark_2 = pygame.image.load(path.join(img_dir, "2.png")).convert()
mark_3 = pygame.image.load(path.join(img_dir, "3.png")).convert()
mark_4 = pygame.image.load(path.join(img_dir, "4.png")).convert()
mark_5 = pygame.image.load(path.join(img_dir, "5.png")).convert()

# Цикл игры
all_sprites = pygame.sprite.Group()
eggs = pygame.sprite.Group()
fone = Fone()
all_sprites.add(fone)
delets_elem = Delets_elem()
all_sprites.add(delets_elem)
player = Player()
all_sprites.add(player)
len_of_marks = 0
summa_of_marks = 0
list_of_mark = [0, 0, 0, 0, 0]  # 0 индекс - 1 , 1 индекс - 2 и т.д.
sr_mark = 0
best_sr_mark , best_len_of_marks , best_list_of_marks = readsc()
running = True
for x in range(5):
    new_egg()
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            hs(sr_mark,len_of_marks,list_of_mark)
            running = False
        elif event.type == pygame.KEYDOWN:
            pass
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, eggs, True, pygame.sprite.collide_circle)
    for x in hits:
        list_of_mark = update_list_of_kol_mark(list_of_mark, x)
        sr_mark, len_of_marks = update_sr_mark(sr_mark, x.mark, len_of_marks)
        new_egg()
    stolk = pygame.sprite.spritecollide(delets_elem, eggs, True)
    for x in stolk:
        new_egg()
    # Обновление
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    if sr_mark > best_sr_mark:
        hs(sr_mark, len_of_marks, list_of_mark)
        best_sr_mark, best_len_of_marks, best_list_of_marks = readsc()
    draw_text(screen, f"средний балл: {str(round(sr_mark, 2))}; лучший средний балл: {best_sr_mark}", 30, 10, 0)
    draw_text(screen, f"оценок 1: {list_of_mark[0]} оценок 2 : {list_of_mark[1]}", 30, 10, 45)
    draw_text(screen, f"оценок 3: {list_of_mark[2]} оценок 4 : {list_of_mark[3]}", 30, 10, 75)
    draw_text(screen, f"оценок 5: {list_of_mark[0]}", 30, 10, 100)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
pygame.quit()
