def main():
    show_start_screen()
    
    while True:
        restart = game_loop()
        if not restart:
            break
    
    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()