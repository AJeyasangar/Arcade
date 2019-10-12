import pygame


class Button():
    def __init__(self, txt, screen, location):
        self.color = (255, 255, 255)
        self.bg = (255, 255, 255)
        self.fg = (255, 255, 255)
        self.size = (150, 70)
        self.screen = screen
        self.font = pygame.font.SysFont(None, 16)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1,self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s // 2 for s in self.size])
        print("here")
        self.surface = pygame.surface.Surface(self.size)
        self.rect = self.surface.get_rect(center=location)

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        self.screen.blit(self.surface, self.rect)

    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = (200, 200, 200)