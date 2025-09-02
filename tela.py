          if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity_y = 0 
        on_ground = True
        return on_ground
    def jump(self):
        if not self.jumping:
            self.velocity_y = -12
            self.jumping = True
            jump_sound.play()
    def draw(self):
        screen.blit(player_img, self.rect)
        # Desenhar hitbox para debug (opcional)
        # pygame.draw.rect(screen, RED, self.rect, 2)