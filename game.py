import os
import pygame as pg
from components.cell import Cell
from components.button import Button

class GameOfLife(object):
    def __init__(self):
        pg.init()
        self.rows = 60
        self.columns = 40
        self.screen = pg.display.set_mode((self.rows * 10, self.columns * 10 + 20))
        self.width, self.height = self.screen.get_size()
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.pause = True
        self.clock = pg.time.Clock()
        self.fps = 60
        self.color = pg.Color('white')
        self.title = pg.display.set_caption('Conway\'s Game of Life (by void*)')
        self.start_button = Button((self.width - self.width, self.height - 20, self.width / 3 - 10, 20),
                                   'gray', 'Start', 'black')
        self.pause_button = Button((self.width / 2 - self.width / 3 / 2 + 5, self.height - 20, self.width / 3 - 10, 20),
                                   'gray', 'Pause', 'black')
        self.reset_button = Button((self.width - self.width / 3 + 10, self.height - 20, self.width / 3 - 10, 20),
                                   'gray', 'Reset', 'black')
        self.cells = []
        self.last_updated_cell = None
        self.setupCells()

    def setupCells(self):
        self.cells = []
        for row in range(self.rows):
            self.cells.append([])
            for column in range(self.columns):
                self.cells[row].append(Cell((row * 10, column * 10, 10, 10), (row, column), 0))
        print()

    def drawCells(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column].draw(self.screen)

    def drawButtons(self):
        self.start_button.draw(self.screen)
        self.pause_button.draw(self.screen)
        self.reset_button.draw(self.screen)

    def next_generation(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.cells[row][column].state == 1 and \
                        (self.cells[row][column].count_neighbours(self.cells) == 2 or
                         self.cells[row][column].count_neighbours(self.cells) == 3):
                    self.cells[row][column].next_state = self.cells[row][column].state
                elif self.cells[row][column].state == 0 and self.cells[row][column].count_neighbours(
                        self.cells) == 3:
                    self.cells[row][column].next_state = 1
                else:
                    self.cells[row][column].next_state = 0

        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column].state = self.cells[row][column].next_state

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.start_button.pressed(pg.mouse.get_pos()):
                    self.pause = False
                    self.fps = 15
                elif self.pause_button.pressed(pg.mouse.get_pos()):
                    self.pause = True
                    self.fps = 60
                elif self.reset_button.pressed(pg.mouse.get_pos()):
                    self.setupCells()
            if event.type == pg.MOUSEBUTTONUP:
                self.last_updated_cell = None
            if pg.mouse.get_pressed()[0]:
                for row in range(self.rows):
                    for column in range(self.columns):
                        if self.cells[row][column].pressed(pg.mouse.get_pos()) and \
                                self.last_updated_cell != (row, column):
                            self.last_updated_cell = (row, column)
                            self.cells[row][column].state = not self.cells[row][column].state
            if event.type == pg.QUIT:
                self.done = True

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.screen.fill(self.color)
            if not self.pause:
                self.next_generation()
            self.drawCells()
            self.drawButtons()
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    run_it = GameOfLife()
    run_it.main_loop()
    pg.quit()
    os.sys.exit()
