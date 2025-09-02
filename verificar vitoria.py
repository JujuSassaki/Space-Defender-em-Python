if player.score >= player.coins_to_win:
            if show_win_screen():
                return True  # Reiniciar
            else:
                running = False
    