import pygame as pg

from src.game_server import GameServer
from src.resource import RESOURCE as RSC


class Application:
    def __init__(self):
        pg.init()
        self.size = (self.width, self.height) = (RSC['width'], RSC['height'])
        self.display = pg.display.set_mode(self.size)
        pg.display.set_caption("No thanks")
        icon_img = pg.image.load("src/img/icon.png")
        pg.display.set_icon(icon_img)

        self.vgame = None

    def run(self):
        clock = pg.time.Clock()
        running = True
        self.display.fill('darkgreen', (0, 0, self.width, self.height))
        pg.display.update()
        while running:
            # # изменения модели
            # self.vgame.model_update()
            # # отрисовка изменений
            # self.vgame.redraw(self.display)
            # # реакция на клавиши и мышь
            for event in pg.event.get():
                if event.type == pg.QUIT or \
                        event.type == pg.KEYDOWN and event.key == pg.K_q:
                    running = False
                # self.vgame.event_processing(event)
            clock.tick(RSC["FPS"])


if __name__ == '__main__':
    app = Application()

    # run строго после связки с game_server
    app.run()
