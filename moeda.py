class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.collected = False
    def draw(self):
        if not self.collected:
            screen.blit(coin_img, self.rect)
            # pygame.draw.circle(screen, YELLOW, self.rect.center, 15)