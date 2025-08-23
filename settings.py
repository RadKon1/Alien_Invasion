class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""
    
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        #Ustawienia ekranu.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (168,184,159)
        
        #Ustawienia dotyczące statku.
        self.ship_speed = 1.5
        
        #Ustawienia dotyczące pocisków.
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 4
        
        