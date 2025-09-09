import os

class GameStats:
    """Monitorowanie danych statystycznych w grze 'Inwazja Obcych'."""

    def __init__(self, ai_game):
        """Inicjalizacja danych statystycznych."""
        self.settings = ai_game.settings
        self.reset_stats()

        #Wczytanie high score jeśli istnieje.
        self.high_score = self._load_high_score()

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, które mogą zmieniać się w trakcie gry."""
        self.ships_left = self.settings.ship_limit
        self.score = 0

    def _load_high_score(self):
        """Wczytaj high score z pliku, albo zwróć 0 jeśli brak pliku."""
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as f:
                return int(f.read())
        return 0

    def save_high_score(self):
        """Zapisz high score do pliku, po zakońćzeniu rozgrywki."""
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))
