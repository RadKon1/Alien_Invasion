import pygame
import sys

import pygame.font

class Instructions:
    """Klasa zajmująca się wyświetleniem instrukcji w oknie pygame."""
    def __init__(self):
        """Initialization of classes attributes."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800,900))
        pygame.display.set_caption('Instructions')
        self.font = pygame.font.SysFont(None, 20)

        with open('instructions.txt', 'r', encoding='utf-8') as f:
            self.lines = f.readlines()

    def run_instructions(self):
        """Główna pętla instructions.py"""
        while True:
            self._check_events()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill((30, 30, 30))
        y_offset = 0
        for line in self.lines:
            rendered_line = self.font.render(line.strip(), True, (255, 255, 255))
            self.screen.blit(rendered_line, (10, y_offset))
            y_offset += rendered_line.get_height() + 5

        pygame.display.flip()

if __name__ == '__main__':
    ins = Instructions()
    ins.run_instructions()
