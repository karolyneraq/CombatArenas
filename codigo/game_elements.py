# victory text
font = pygame.font.Font('assets/PressStart2P.ttf', 45)
victory_text1 = font.render("player green win", True, green, black)
victory_text2 = font.render("player red win", True, red, black)
victory_text1_rect = victory_text1.get_rect()
victory_text2_rect = victory_text2.get_rect()
victory_text1_rect.center = (450, 275)
victory_text2_rect.center = (450, 275)

# hud
hud_font = pygame.font.Font('assets/PressStart2P.ttf', 45)
hud1_text = hud_font.render("3", True, green, orange)
hud2_text = hud_font.render("3", True, red, orange)
hud1_text_rect = hud1_text.get_rect()
hud2_text_rect = hud2_text.get_rect()
hud1_text_rect.center = (70, 30)
hud2_text_rect.center = (830, 30)
score1 = 3
score2 = 3

# sounds
shoot_sound = pygame.mixer.Sound("assets/tiger.wav")
tank_explode = pygame.mixer.Sound("assets/tank_explode.wav")
bounce_ball = pygame.mixer.Sound("assets/bounce_ball.wav")
tank_walk = pygame.mixer.Sound("assets/tank_walk.wav")
time_sound = tank_walk.get_length()
time_stop = 0
