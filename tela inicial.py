   def show_start_screen():
    screen.fill((30, 30, 50))
    
    title = font_large.render("SUPER PLATAFORMA DEMO", True, YELLOW)
    instructions = font_medium.render("Use ← → para mover e ESPAÇO para pular", True, WHITE)
    goal = font_medium.render("Colete 10 moedas para vencer!", True, GREEN)
    start_text = font_medium.render("Pressione ENTER para começar", True, RED)
    
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
    screen.blit(instructions, (WIDTH//2 - instructions.get_width()//2, 250))
    screen.blit(goal, (WIDTH//2 - goal.get_width()//2, 300))
screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, 400))
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()