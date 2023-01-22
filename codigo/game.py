list_two_tank[1][7][3] = False
list_two_tank[0][7][3] = False
respawn = False
for event in pygame.event.get():

    # print(event)
    if event.type == pygame.QUIT:
        loop = False

    exec(open("game_keys.py").read())

counter = pygame.time.get_ticks()
screen.fill(orange)

exec(open("moves_and_fire.py").read())

# draw walls
wall1 = pygame.draw.rect(screen, yellow, (0, 100, 900, 20))
wall2 = pygame.draw.rect(screen, yellow, (0, 630, 900, 20))
wall3 = pygame.draw.rect(screen, yellow, (0, 100, 20, 800))
wall4 = pygame.draw.rect(screen, yellow, (880, 100, 20, 800))

# draw hud
hud1_text = hud_font.render(str(list_two_tank[0][11]), True, green, orange)
hud2_text = hud_font.render(str(list_two_tank[1][11]), True, red, orange)
screen.blit(hud1_text, hud1_text_rect)
screen.blit(hud2_text, hud2_text_rect)

if victory1:
    screen.fill(black)
    screen.blit(victory_text1, victory_text1_rect)
if victory2:
    screen.fill(black)
    screen.blit(victory_text2, victory_text2_rect)

# update screen
pygame.display.flip()
clock.tick(120)