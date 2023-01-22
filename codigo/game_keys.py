# configuring game keys
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_p:
        loop = False
    if event.key == pygame.K_w:
        list_two_tank[0][7][0] = True
    if event.key == pygame.K_d:
        list_two_tank[0][7][1] = True
    if event.key == pygame.K_a:
        list_two_tank[0][7][2] = True
    if event.key == pygame.K_t and (not list_two_tank[0][7][4]):
        list_two_tank[0][7][3] = True
        list_two_tank[0][7][4] = True
        list_two_tank[0][8] = pygame.time.get_ticks()

    if event.key == pygame.K_UP:
        list_two_tank[1][7][0] = True
    if event.key == pygame.K_RIGHT:
        list_two_tank[1][7][1] = True
    if event.key == pygame.K_LEFT:
        list_two_tank[1][7][2] = True
    if event.key == pygame.K_l and (not list_two_tank[1][7][4]):
        list_two_tank[1][7][3] = True
        list_two_tank[1][7][4] = True
        list_two_tank[1][8] = pygame.time.get_ticks()

if event.type == pygame.KEYUP:
    if event.key == pygame.K_w:
        list_two_tank[0][7][0] = False
    if event.key == pygame.K_d:
        list_two_tank[0][7][1] = False
    if event.key == pygame.K_a:
        list_two_tank[0][7][2] = False

    if event.key == pygame.K_UP:
        list_two_tank[1][7][0] = False
    if event.key == pygame.K_RIGHT:
        list_two_tank[1][7][1] = False
    if event.key == pygame.K_LEFT:
        list_two_tank[1][7][2] = False
