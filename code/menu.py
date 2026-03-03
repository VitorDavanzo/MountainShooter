#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, COLOR_ORANGE, COLOR_YELLOW, COLOR_WHITE, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(
            loops=-1)  # quando aparece o parametro laranjinha no nome, 'loops', por exemplo, ele pode ser desconsiderado = poderia ser somente '...play(-1)' -> esse -1 faz com que a musica fique se repetindo
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Mountain', COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, 'Shooter', COLOR_ORANGE, ((WIN_WIDTH / 2), 120))
            # esses códigos abaixo, eu mesmo criei, testando e achando que estava correto (o que está), mas o professor ensinou uma maneira mais prática com o 'for i in range(...)'
            # self.menu_text(20, 'NEW GAME 1P', COLOR_YELLOW, ((WIN_WIDTH / 2), 200))
            # self.menu_text(20, 'NEW GAME 2P - COOPERATIVE', COLOR_WHITE, ((WIN_WIDTH / 2), 225))
            # self.menu_text(20, 'NEW GAME 2P - COMPETITIVE', COLOR_WHITE, ((WIN_WIDTH / 2), 250))
            # self.menu_text(20, 'SCORE', COLOR_WHITE, ((WIN_WIDTH / 2), 275))
            # self.menu_text(20, 'EXIT', COLOR_WHITE, ((WIN_WIDTH / 2), 300))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get(): #Evento para fechar o jogo
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End Pygame
                if event.type == pygame.KEYDOWN: #Evento para selecionar as opções através das setas
                    if event.key == pygame.K_DOWN:#Seta para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:#Seta para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1
                    if event.key == pygame.K_RETURN: #para quanto clicar o Enter ele entra na opção selecionada
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
