for coin in coins:
            if not coin.collected and player.rect.colliderect(coin.rect):
                coin.collected = True
                player.score += 1
                coin_sound.play()