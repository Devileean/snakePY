import pygame

# CONSTANTS
SIZE_BLOCK = 20  # размер нашего блока
FRAME_COLOR = (46, 139, 87)  # переменная цвета в rgb  формате
SKY_BLUE = (135, 206, 235)  # цвет наших блоков
COUNT_BLOCKS = 20  # количество болоков
MARGIN = 1

size = [440, 440]  # указываем размер нашего будущего игрового окна

screen = pygame.display.set_mode(size)  # screen  наша переменная для окна чтобы в будущем ее использовать
pygame.display.set_caption('Змейка')  # создадим заголово нашей программе

while True:  # создаем бесконечный цикл чтобы наше окошко игры не закрывалось

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
    screen.fill(FRAME_COLOR)  # закрашиваем наше окно с помощью нашей переменной frame_color

    for row in range(COUNT_BLOCKS):  # цикл для отрисовки рядов
        for column in range(COUNT_BLOCKS):  # цикл для отрисовки колонок
            # if (row + column) % 2 == 0:  #  если мы захотим переменно подкрашивать наши блоки по чет нечетё
            #     color = BLUE
            # else:
            #     color = SKY_BLUE
            pygame.draw.rect(screen, SKY_BLUE, [10 + column * SIZE_BLOCK + MARGIN * (column + 1),
                                                10 + row * SIZE_BLOCK + MARGIN * (row + 1),
                                                SIZE_BLOCK,
                                                SIZE_BLOCK])

    pygame.display.flip()  # нужен чтобы наши изменения вступили в силу -^
