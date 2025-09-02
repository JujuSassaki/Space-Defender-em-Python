def create_level():
    platforms = [
        Platform(100, 400, 200, 20),
        Platform(400, 350, 150, 20),
        Platform(200, 250, 200, 20),
        Platform(500, 200, 200, 20),
        Platform(100, 150, 150, 20),
        Platform(0, 500, WIDTH, 100)  # Chão
    ]
    coins = []
    for i in range(15):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(100, 400)
        coins.append(Coin(x, y))
    return platforms, coins