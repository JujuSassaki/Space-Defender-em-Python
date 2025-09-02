    def show_win_screen():
    screen.fill((0, 100, 0))
    
    win_text = font_large.render("PARABÉNS! VOCÊ VENCEU!", True, YELLOW)
    score_text = font_medium.render(f"Moedas coletadas: {player.score}", True, WHITE)
    restart_text = font_medium.render("Pressione R para jogar novamente", True, WHITE)
    quit_text = font_medium.render("Pressione ESC para sair", True, WHITE)
    
    screen.blit(win_text, (WIDTH//2 - win_text.get_width()//2, 200))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 300))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, 350))
    screen.blit(quit_text, (WIDTH//2 - quit_text.get_width()//2, 400))
    
pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Reiniciar
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    return False