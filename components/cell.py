import pygame as pg

class Cell:
    def __init__(self, rect, position, state):
        pg.init()
        self.x, self.y, self.width, self.height = rect
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.row, self.column = position
        self.state = state
        self.next_state = None

    def draw(self, surface):
        pg.draw.rect(surface, pg.Color('black'), self.rect, self.state)

    def pressed(self, mouse):
        if self.rect.topleft[0] < mouse[0] < self.rect.bottomright[0] and self.rect.topleft[1] < mouse[1] < \
                self.rect.bottomright[1]:
            return True
        else:
            return False

    def count_neighbours(self, cells):
        row_limit = len(cells)
        col_limit = len(cells[0])
        total = 0
        for row in [-1, 0, 1]:
            for col in [-1, 0, 1]:
                if not row == col == 0 and cells[self.row - row % row_limit][self.column - col % col_limit].state == 1:
                    total += 1
        return total
