def load_sound(path):
    try:
        if os.path.exists(path):
            return pygame.mixer.Sound(path)
        else:
            # Retornar um som vazio
            return pygame.mixer.Sound(pygame.sndarray.array([0] * 44100))
    except:
        return pygame.mixer.Sound(pygame.sndarray.array([0] * 44100))