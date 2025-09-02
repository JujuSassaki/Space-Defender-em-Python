class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 300, 40, 60)
        self.velocity_y = 0
        self.jumping = False
        self.speed = 5
        self.score = 0
        self.coins_to_win = 10
    def update(self, platforms):
        # Gravidade
        self.velocity_y += 0.5
        self.rect.y += self.velocity_y