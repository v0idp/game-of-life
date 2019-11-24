import pygame as pg

class Button:
    def __init__(self, rect, color, text, text_color):
        pg.init()
        pg.font.init()
        self.x, self.y, self.width, self.height = rect
        self.color = color
        self.text = text
        self.text_color = text_color
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pg.draw.rect(surface, pg.Color(self.color), self.rect, 0)
        font_size = int(self.width // len(self.text) / 1.8)
        font = pg.font.SysFont("Calibri", font_size, bold=True)
        text = font.render(self.text, True, pg.Color(self.text_color))
        surface.blit(text, ((self.x + self.width / 2) - text.get_width() / 2,
                            (self.y + self.height / 2) - text.get_height() / 2))

    def pressed(self, mouse):
        if self.rect.topleft[0] < mouse[0] < self.rect.bottomright[0] and self.rect.topleft[1] < mouse[1] < \
                self.rect.bottomright[1]:
            return True
        else:
            return False
