#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH


class EntityFactory:

    #a EntityFactory nunca irá utilizar a função para instanciar e sim para invocar outros objetos para ser instanciados. Então não precisa do def __init__
    #def __init__(self):
    #   pass

    @staticmethod
    def get_entity(entity_name: str, position = (0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0))) #PARA REPETIÇÃO das imagens
                return list_bg
