import pygame

size = [400, 600]  # указываем размер нашего будущего игрового окна

screen = pygame.display.set_mode(size)  # screen  наша переменная для окна чтобы в будущем ее использовать
pygame.display.set_caption('Змейка')  # создадим заголово нашей программе

while True: #  создаем бесконечный цикл чтобы наше окошко игры не закрывалось

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()

