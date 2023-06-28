from pygame import Rect
import pygame


class Colisioner:
    @staticmethod
    def get_colisiones(personaje: Rect, paredes: list[Rect]):
        colisiones = []
        for pared in paredes:
            if pygame.Rect.colliderect(personaje, pared):
                colisiones.append(pared)
        return colisiones

    @staticmethod
    def comprobar_colision(personaje: Rect, personaje1: Rect) -> bool:
        return pygame.Rect.colliderect(personaje, personaje1)

    @staticmethod
    def tocar_suelo(personaje: Rect, paredes: list[Rect]) -> bool:
        for pared in paredes:
            if personaje.bottom == pared.top:
                if personaje.left < pared.right and personaje.right > pared.left:
                    return True
        return False

    @staticmethod
    def moviminento_prueba(personaje: Rect, paredes: list[Rect], movimiento: [int, int]):
        personaje.x += movimiento[0]
        colisiones = Colisioner.get_colisiones(personaje, paredes)
        for colision in colisiones:
            if movimiento[0] > 0:
                personaje.right = colision.left
            elif movimiento[0] < 0:
                personaje.left = colision.right
        personaje.y += movimiento[1]
        colisiones = Colisioner.get_colisiones(personaje, paredes)
        for colision in colisiones:
            if movimiento[1] > 0:
                personaje.bottom = colision.top
            elif movimiento[1] < 0:
                personaje.top = colision.bottom
        return personaje

    @staticmethod
    def move_gravity(character: Rect, walls: list[Rect], move: [int, int]):
        move[1] += 8
        return Colisioner.moviminento_prueba(character, walls, move)

