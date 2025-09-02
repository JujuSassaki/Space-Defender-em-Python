surface = pygame.Surface(default_size)
            if "player" in path:
                surface.fill(BLUE)
            elif "coin" in path:
                surface.fill(YELLOW)
            elif "platform" in path:
                surface.fill(BROWN)
            else:
                surface.fill(GREEN)
            return surface
    except:
        surface = pygame.Surface(default_size)
        surface.fill(RED)
        return surface