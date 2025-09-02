score_text = font_medium.render(f"Moedas: {player.score}/{player.coins_to_win}", True, BLACK)
        screen.blit(score_text, (20, 20))
        
        instructions = font_small.render("← → Mover | ESPAÇO Pular | ESC Sair", True, BLACK)
        screen.blit(instructions, (WIDTH - instructions.get_width() - 20, 20))
        
        pygame.display.flip()