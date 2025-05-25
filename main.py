import pygame
import random
 
pygame.font.init()

bal = 0
wins = 0

level = 1

battle_deck = ["fireball"]
opponent_deck = ["fireball"]
 
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Math World")
 
White = (255, 255, 255)
Gray = (128, 128, 128)
Silver = (170, 170, 170)
Orange = (255, 165, 0)
Orange_Dark = (251, 79, 20)
 
font = pygame.font.SysFont(None, 32)
font2 = pygame.font.SysFont(None, 50)
font3 = pygame.font.SysFont(None, 40)
 
Blue_Knight_image = pygame.image.load("Assets/Blue_Knight_Standing.png")
Blue_Knight = pygame.transform.scale(Blue_Knight_image, (100, 100))

Castle_image = pygame.image.load("Assets/castle.png")
Castle = pygame.transform.scale(Castle_image, (200, 200))
 
Red_Knight_image = pygame.image.load("Assets/Red_Knight_Standing.png")
Red_Knight = pygame.transform.scale(Red_Knight_image, (100, 100))
 
Blue_Knight_left_image = pygame.image.load("Assets/Blue_Knight_face_left.png")
Blue_Knight_left = pygame.transform.scale(Blue_Knight_left_image, (100, 100))
 
Red_Knight_right_image = pygame.image.load("Assets/Red_Knight_face_right.png")
Red_Knight_right = pygame.transform.scale(Red_Knight_right_image, (100, 100))

menu1_image = pygame.image.load("Assets/menu1.png")
menu1 = pygame.transform.scale(menu1_image, (600, 400))

menu2_image = pygame.image.load("Assets/menu2.png")
menu2 = pygame.transform.scale(menu2_image, (600, 400))

menu3_image = pygame.image.load("Assets/menu3.png")
menu3 = pygame.transform.scale(menu3_image, (600, 400))

Background3_image = pygame.image.load("Assets/Background3.png")
Background3 = pygame.transform.scale(Background3_image, (600, 400))

Firecard_image = pygame.image.load("Assets/Fire_card.png")
Firecard = pygame.transform.scale(Firecard_image, (200, 200))

Elecard_image = pygame.image.load("Assets/elec_card.png")
Elecard = pygame.transform.scale(Elecard_image, (200, 200))

rockcard_image = pygame.image.load("Assets/rock_card.png")
rockcard = pygame.transform.scale(rockcard_image, (200, 200))

Fireball_image = pygame.image.load("Assets/Fireball.png")
Fireball = pygame.transform.scale(Fireball_image, (100, 100))

rockball_image = pygame.image.load("Assets/rock.png")
rockball = pygame.transform.scale(rockball_image, (100, 100))

Elecball_image = pygame.image.load("Assets/Elecball.png")
Elec_ball = pygame.transform.scale(Elecball_image, (100, 100))
 
Background_image = pygame.image.load("Assets/Background.png")
Staduim1 = pygame.transform.scale(Background_image, (600, 400))

Staduim2_image = pygame.image.load("Assets/Electric_staduim.png")
Staduim2 = pygame.transform.scale(Staduim2_image, (600, 400))

Staduim3_image = pygame.image.load("Assets/Rock_staduim.png")
Staduim3 = pygame.transform.scale(Staduim3_image, (600, 400))

msg2 = pygame.image.load("Assets/elec_box.png")
msg3 = pygame.image.load("Assets/las_msg.png")

Message_Box = pygame.image.load("Assets/Message_Box.png")
 
def lose_menu():
 global level
 global wins
 loss = random.randint(30, 50)
 if wins == 0:
   loss = 0
 if wins <= 50 and loss >= 30: 
   loss = wins
 wins = wins - loss
  
 if wins >= 1000 and wins <= 1999:
      Background = Staduim2
      level = 2
 elif wins >= 2000:
      Background = Background3
      level = 3
 
 else: 
      Background = Staduim1
 while True:
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       pygame.quit()
 
     mouse = pygame.mouse.get_pos()
 
     if event.type == pygame.MOUSEBUTTONDOWN:
       if 25 <= mouse[0] <= 25 + 120 and 15 <= mouse[1] <= 15 + 40:
         main_menu()
 
   window.blit(Background, (0, 0))
   pygame.draw.rect(window, Gray, [10, 10, 150, 37])
   mouse = pygame.mouse.get_pos()
 
   if 25 <= mouse[0] <= 25 + 120 and 15 <= mouse[1] <= 15 + 40:
     pygame.draw.rect(window, Silver, [10, 10, 150, 37])
  
   main_text = font.render('Main Menu', True, White)
   window.blit(main_text, (25, 15))

   wins_text = font.render(f'Trophies - {loss}', True, White)
   window.blit(wins_text, (250, 250))
 
   win_text = pygame.font.SysFont(None, 100).render('You lose.', True, White)
   window.blit(win_text, (220, 150))
   
   pygame.display.update()
 
def win_menu():
 global level
 global wins
 gain = random.randint(30, 50)
 wins = wins + gain
 if wins >= 1000 and wins <= 1999:
      Background = Staduim2
      level = 2
 elif wins >= 2000:
      Background = Background3
      level = 3

 else:
      Background = Staduim1
 while True:
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       pygame.quit()
 
     mouse = pygame.mouse.get_pos()
 
     if event.type == pygame.MOUSEBUTTONDOWN:
       if 25 <= mouse[0] <= 25 + 120 and 15 <= mouse[1] <= 15 + 40:
         main_menu()
 
   window.blit(Background, (0, 0))
   pygame.draw.rect(window, Gray, [10, 10, 150, 37])
   mouse = pygame.mouse.get_pos()
 
   if 25 <= mouse[0] <= 25 + 120 and 15 <= mouse[1] <= 15 + 40:
     pygame.draw.rect(window, Silver, [10, 10, 150, 37])

   main_text = font.render('Main Menu', True, White)
   window.blit(main_text, (25, 15))

   wins_text = font.render(f'Trophies + {gain}', True, White)
   window.blit(wins_text, (250, 250))
 
   win_text = pygame.font.SysFont(None, 100).render('You Win!', True, White)
   window.blit(win_text, (220, 150))
     
   pygame.display.update()

def game():
 global bal
 global level
 global wins
 bal = bal - 500
 RED_HIT = 1
 BLUE_HIT = 2
 blue_choice = ""
 damage = [1, 2, 1]
 choices = ["elecball", "Move left", "Move right"]
 red_choice = ""
 spells2 = ["elecball", "rock_ball", "fireball"]
 User_Elec = []
 Fireballs = []
 us_rock = []
 Elecballs = []
 Op_Fires = []
 op_rock = []
 JumpCount = 10
 Jump = 0
 text = ""
 Blue_Knight_rect = pygame.Rect(100, 227, 100, 100)
 Red_Knight_rect = pygame.Rect(400, 227, 100, 100)
 Blue_Knight_pos = Blue_Knight
 Red_Knight_pos = Red_Knight
 Blue_Knight_Health = 100
 Red_Knight_Health = 100
 Red_Knight_Vel = 20
 counter = 10
 if wins >= 1000 and wins <= 1999:
      Background = Staduim2
      battle_deck.append("elecball")
      opponent_deck.append("elecball")
      level = 2
 elif wins >= 2000:
      Background = Staduim3
      battle_deck.append("rock_ball")
      opponent_deck.append("rock_ball")
      level = 3

 else:
      Background = Staduim1
 Run = True
 while Run:
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       Run = False
       pygame.quit()

     if event.type == pygame.USEREVENT: 
       counter -= 1
       text = str(counter).rjust(3) if counter > 0 else ''

     if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_f:
        red_choice = "fireball"
        Fire_ball_rect = pygame.Rect(Blue_Knight_rect.x + Blue_Knight_rect.width, Blue_Knight_rect.y + Blue_Knight_rect.height//6 - 6, 10, 5)
        Fireballs.append(Fire_ball_rect)

       if event.key == pygame.K_w:
         Red_Knight_Health = 0

       if event.key == pygame.K_l:
         Blue_Knight_Health = 0

       if event.key == pygame.K_e and "elecball" in battle_deck:
        red_choice = random.choice(spells2)
        user_elec_rect = pygame.Rect(Blue_Knight_rect.x + Blue_Knight_rect.width, Blue_Knight_rect.y + Blue_Knight_rect.height//6 - 6, 10, 5)
        User_Elec.append(user_elec_rect)

       if event.key == pygame.K_r and "rock_ball" in battle_deck:
        red_choice = "rock_ball"
        user_rock_rect = pygame.Rect(Blue_Knight_rect.x + Blue_Knight_rect.width, Blue_Knight_rect.y + Blue_Knight_rect.height//6 - 6, 10, 5)
        us_rock.append(user_rock_rect)

     if red_choice == "elecball" and "elecball" in opponent_deck:
        red_choice = ""
        Elec_ball_rect = pygame.Rect(Red_Knight_rect.x + Red_Knight_rect.width, Red_Knight_rect.y + Red_Knight_rect.height//6 - 6, 10, 5)
        Elecballs.append(Elec_ball_rect)

     if red_choice == "fireball" and "fireball" in opponent_deck:
        red_choice = ""
        op_fire_rect = pygame.Rect(Red_Knight_rect.x + Red_Knight_rect.width, Red_Knight_rect.y + Red_Knight_rect.height//6 - 6, 10, 5)
        Op_Fires.append(op_fire_rect)

     if red_choice == "rock_ball" and "rock_ball" in opponent_deck:
        red_choice = ""
        op_rock_rect = pygame.Rect(Red_Knight_rect.x + Red_Knight_rect.width, Red_Knight_rect.y + Red_Knight_rect.height//6 - 6, 10, 5)
        op_rock.append(op_rock_rect)

     if text == "":
       red_choice = ""
       Blue_Knight_rect.clamp_ip(window.get_rect())
       Red_Knight_rect.clamp_ip(window.get_rect())
    
   keys = pygame.key.get_pressed()
 
   randmage = random.choice(damage)

   for Fire_ball_rect in Fireballs:
      if Blue_Knight_pos == Blue_Knight:
        Fire_ball_rect.x += 20

      if Blue_Knight_pos == Blue_Knight_left:
        Fire_ball_rect.x -= 20

      if Red_Knight_rect.colliderect(Fire_ball_rect):
            Red_Knight_Health = Red_Knight_Health - 1
            pygame.event.post(pygame.event.Event(RED_HIT))
            Fireballs.remove(Fire_ball_rect)
      elif Red_Knight_rect.x > width:
            Fireballs.remove(Fire_ball_rect)

   for user_elec_rect in User_Elec:
      if Blue_Knight_pos == Blue_Knight:
        user_elec_rect.x += 20

      if Blue_Knight_pos == Blue_Knight_left:
        user_elec_rect.x -= 20

      if Red_Knight_rect.colliderect(user_elec_rect):
            Red_Knight_Health = Red_Knight_Health - 2
            pygame.event.post(pygame.event.Event(RED_HIT))
            User_Elec.remove(user_elec_rect)
      elif Red_Knight_rect.x > width:
            User_Elec.remove(user_elec_rect)

   for user_rock_rect in us_rock:
      if Blue_Knight_pos == Blue_Knight:
        user_rock_rect.x += 20

      if Blue_Knight_pos == Blue_Knight_left:
        user_rock_rect.x -= 20

      if Red_Knight_rect.colliderect(user_rock_rect):
            Red_Knight_Health = Red_Knight_Health - 3
            pygame.event.post(pygame.event.Event(RED_HIT))
            us_rock.remove(user_rock_rect)
      elif Red_Knight_rect.x > width:
            us_rock.remove(user_rock_rect)

   for Elec_ball_rect in Elecballs:
      if Red_Knight_pos == Red_Knight:
        Elec_ball_rect.x -= 20

      if Red_Knight_pos == Red_Knight_right:
        Elec_ball_rect.x += 20

      if Blue_Knight_rect.colliderect(Elec_ball_rect):
            Blue_Knight_Health = Blue_Knight_Health - 3
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            Elecballs.remove(Elec_ball_rect)
      elif Blue_Knight_rect.x > width:
            Elecballs.remove(Elec_ball_rect)

   for op_fire_rect in Op_Fires:
      if Red_Knight_pos == Red_Knight:
        op_fire_rect.x -= 20

      if Red_Knight_pos == Red_Knight_right:
        op_fire_rect.x += 20

      if Blue_Knight_rect.colliderect(op_fire_rect):
            Blue_Knight_Health = Blue_Knight_Health - 2
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            Op_Fires.remove(op_fire_rect)
      elif Blue_Knight_rect.x > width:
            Op_Fires.remove(op_fire_rect)

   for op_rock_rect in op_rock:
      if Red_Knight_pos == Red_Knight:
        op_rock_rect.x -= 20

      if Red_Knight_pos == Red_Knight_right:
        op_rock_rect.x += 20

      if Blue_Knight_rect.colliderect(op_rock_rect):
            Blue_Knight_Health = Blue_Knight_Health - 4
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            op_rock.remove(op_rock_rect)
      elif Blue_Knight_rect.x > width:
            op_rock.remove(op_rock_rect)
  
   if not(Jump):
       if Red_Knight_rect.colliderect(Blue_Knight_rect) and blue_choice == "left":
          Red_Knight_Health = Red_Knight_Health - 1
          Blue_Knight_Health = Blue_Knight_Health - randmage
          Blue_Knight_rect.x += 60
          Red_Knight_rect.x -= 60
          Blue_Knight_pos = Blue_Knight_left
          Red_Knight_pos = Red_Knight_right
          red_choice = "Move right"
          Red_Knight_Vel += 1
          blue_choice = ""
 
       if Red_Knight_rect.colliderect(Blue_Knight_rect) and blue_choice == "right":
          Red_Knight_Health = Red_Knight_Health - 1
          Blue_Knight_Health = Blue_Knight_Health - randmage
          Blue_Knight_rect.x -= 60
          Red_Knight_rect.x += 60
          Red_Knight_pos = Red_Knight
          Blue_Knight_pos = Blue_Knight
          red_choice = "Move left"
          Red_Knight_rect.clamp_ip(300, 228, 600, 400)
          Red_Knight_Vel += 1
          blue_choice = ""
 
       if Red_Knight_rect.colliderect(Blue_Knight_rect) and blue_choice == "Jump":
          Red_Knight_Health = Red_Knight_Health - (randmage + randmage)
          Blue_Knight_Health = Blue_Knight_Health - randmage
          Blue_Knight_rect.x -= 60
          Blue_Knight_pos = Blue_Knight
          red_choice = "Move left"
          Red_Knight_Vel += 2
          blue_choice = ""
      
       if Blue_Knight_rect.colliderect(Red_Knight_rect) and red_choice == "Move left":
          Blue_Knight_Health = Blue_Knight_Health - 1
          Blue_Knight_rect.x += 60
          Red_Knight_rect.x -= 40
          Red_Knight_pos = Red_Knight
          Blue_Knight_pos = Blue_Knight_left
          red_choice = random.choice(choices)
 
       if Blue_Knight_rect.colliderect(Red_Knight_rect) and red_choice == "Move right":
          Blue_Knight_Health = Blue_Knight_Health - 1
          Blue_Knight_rect.x -= 60
          Red_Knight_rect.x += 40
          Red_Knight_pos = Red_Knight_right
          Blue_Knight_pos = Blue_Knight
          red_choice = random.choice(choices)
       
       if red_choice == "Move left":
         Red_Knight_rect.x -= Red_Knight_Vel
         Red_Knight_pos = Red_Knight
 
       if red_choice == "Move right":
         Red_Knight_rect.x += Red_Knight_Vel
         Red_Knight_pos = Red_Knight_right
 
       if keys[pygame.K_RIGHT]:
         blue_choice = "right"
         red_choice = "elecball"
         Blue_Knight_rect.x += 20
         Red_Knight_rect.clamp_ip(300, 228, 600, 400)
         Blue_Knight_pos = Blue_Knight
 
       if keys[pygame.K_LEFT]:
         blue_choice = "left"
         red_choice = "rock_ball"
         Blue_Knight_rect.x -= 20
         Red_Knight_rect.clamp_ip(300, 228, 600, 400)
         Blue_Knight_pos = Blue_Knight_left

       if keys[pygame.K_SPACE]:
           Jump = True

   else:
       if JumpCount >= -10:
           Blue_Knight_rect.y -= (JumpCount * abs(JumpCount)) * 1
           JumpCount -= 2
           blue_choice = "Jump"
 
       else:
           JumpCount = 10
           Jump = False
 
   Blue_Knight_rect.clamp_ip(window.get_rect())
   Red_Knight_rect.clamp_ip(window.get_rect())
      
   window.blit(Background, (0, 0))

   window.blit(Blue_Knight_pos, (Blue_Knight_rect.x, Blue_Knight_rect.y))
 
   window.blit(Red_Knight_pos, (Red_Knight_rect.x, Red_Knight_rect.y))

   for Fire_ball_rect in Fireballs:
      window.blit(Fireball, Fire_ball_rect)
   
   for Elec_ball_rect in Elecballs:
      window.blit(Elec_ball, Elec_ball_rect)

   for user_elec_rect in User_Elec:
      window.blit(Elec_ball, user_elec_rect)

   for user_rock_rect in us_rock:
      window.blit(rockball, user_rock_rect)
   
   for op_rock_rect in op_rock:
      window.blit(rockball, op_rock_rect)

   for op_fires_rect in Op_Fires:
      window.blit(Fireball, op_fires_rect)
 
   if Blue_Knight_Health <= 0:
     Blue_Knight_Health = 0
 
   Blue_Knight_text = font.render(f'Your Health: {Blue_Knight_Health}', True, White)
   window.blit(Blue_Knight_text, (10, 10))
 
   Red_Knight_text = font.render(f'Opponent Health: {Red_Knight_Health}', True, White)
   window.blit(Red_Knight_text, (360, 10))

   window.blit(font2.render(text, True, White), (280, 200))

   pygame.display.update()
 
   if Red_Knight_Health <= 0:
     win_menu()
  
   if Blue_Knight_Health <= 0:
     lose_menu()
     
def incorrect_menu():
  global level
  global wins
  if wins >= 1000 and wins <= 1999:
      Background_box = menu2
      level = 2
  elif wins >= 2000:
      Background_box = menu3
      level = 3

  else:
      Background_box = menu1
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

      mouse = pygame.mouse.get_pos()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if 250 <= mouse[0] <= 250 + 120 and 170 <= mouse[1] <= 170 + 40:
          earn_menu()

        if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
          deck_menu()     

        if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
          earn_menu() 

        if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
          main_menu()

    window.blit(Background_box, (0, 0))
    pygame.draw.rect(window, Gray, [30, 350, 150, 37])
    pygame.draw.rect(window, Gray, [220, 350, 150, 37])
    pygame.draw.rect(window, Gray, [400, 350, 150, 37])
    pygame.draw.rect(window, Orange, [250, 170, 150, 37])

    mouse = pygame.mouse.get_pos()

    if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [30, 350, 150, 37])

    if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [220, 350, 150, 37])

    if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [400, 350, 150, 37])

    if 250 <= mouse[0] <= 250 + 120 and 170 <= mouse[1] <= 170 + 40:
      pygame.draw.rect(window, Orange_Dark, [250, 170, 150, 37])

    shop_text = font.render('Sorry you got it incorrect.', True, (0, 0, 0))
    window.blit(shop_text, (190, 105))

    level_text = font.render(f'Level  {level}', True, White)
    window.blit(level_text, (18, 7))

    wins_text = font.render(f'{wins}', True, White)
    window.blit(wins_text, (265, 7))

    events_text = font.render(f'Events', True, White)
    window.blit(events_text, (375, 7))

    coins_text = font.render(f'{bal}', True, White)
    window.blit(coins_text, (490, 7))

    shop_text = font.render('Battle Deck', True, White)
    window.blit(shop_text, (36, 355))

    earn_text = font.render('Earn', True, White)
    window.blit(earn_text, (435, 355))

    play_text = font.render('Play', True, White)
    window.blit(play_text, (270, 355))

    Coins_text = font.render("New Problem", True, (0, 0, 0))
    window.blit(Coins_text, (257, 177))

    pygame.display.update()   

def correct_menu():
  global level
  global wins
  if wins >= 1000 and wins <= 1999:
      Background_box = menu2
      level = 2
  elif wins >= 2000:
      Background_box = menu3
      level = 3

  else:
      Background_box = menu1
  global bal
  coins = random.randint(200, 500)
  bal = bal + coins
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

      mouse = pygame.mouse.get_pos()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
          deck_menu()     

        if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
          earn_menu() 

        if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
          main_menu()

    window.blit(Background_box, (0, 0))
    pygame.draw.rect(window, Gray, [30, 350, 150, 37])
    pygame.draw.rect(window, Gray, [220, 350, 150, 37])
    pygame.draw.rect(window, Gray, [400, 350, 150, 37])
    pygame.draw.rect(window, Orange, [250, 170, 150, 37])

    mouse = pygame.mouse.get_pos()

    if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [30, 350, 150, 37])

    if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [220, 350, 150, 37])

    if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [400, 350, 150, 37])

    shop_text = font.render('Good Job! You got it Correct!', True, (0, 0, 0))
    window.blit(shop_text, (165, 105))

    level_text = font.render(f'Level  {level}', True, White)
    window.blit(level_text, (18, 7))

    wins_text = font.render(f'{wins}', True, White)
    window.blit(wins_text, (265, 7))

    events_text = font.render(f'Events', True, White)
    window.blit(events_text, (375, 7))

    coins_text = font.render(f'{bal}', True, White)
    window.blit(coins_text, (490, 7))

    shop_text = font.render('Battle Deck', True, White)
    window.blit(shop_text, (36, 355))

    earn_text = font.render('Earn', True, White)
    window.blit(earn_text, (435, 355))

    play_text = font.render('Play', True, White)
    window.blit(play_text, (270, 355))

    Coins_text = font.render(f'Coins + {coins}', True, (0, 0, 0))
    window.blit(Coins_text, (265, 177))

    pygame.display.update()   

def earn_menu():
    global level
    global wins
    if wins >= 1000 and wins <= 1999:
      Background = menu2
      Operator = " - "
      level = 2
    elif wins >= 2000:
      Operator = " x "
      Background = menu3
      level = 3
    
    else:
      Operator = " + "
      Background = menu1
    Num1 = random.randint(5, 10)
    Num2 = random.randint(1, 5)
    if Operator == " + ":
      Answer = Num1 + Num2
    if Operator == " - ":
      Answer = Num1 - Num2
    if Operator == " x ":
      Answer = Num1 * Num2
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(230, 100, 150, 37)
    color_inactive = pygame.Color('white')
    color_active = pygame.Color('black')
    color = color_inactive
    active = False
    text = ''
    Run = True
    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
            
            mouse = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
                  main_menu()
                
                if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
                  deck_menu()     
                
                if 268 <= mouse[0] <= 268 + 120 and 136 <= mouse[1] <= 136 + 40:
                  if str(Answer) == str(text):
                          correct_menu()

                  if str(Answer) != str(text):
                          incorrect_menu()  

                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if str(Answer) == str(text):
                          correct_menu()

                        if str(Answer) != str(text):
                          incorrect_menu()  
              
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        txt_surface = font.render(text, True, color)

        width = max(200, txt_surface.get_width()+10)
        input_box.w = width

        window.blit(Background, (0, 0))
        pygame.draw.rect(window, White, input_box)
        window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(window, Gray, [255, 150, 150, 37])
        pygame.draw.rect(window, Gray, [30, 350, 150, 37])
        pygame.draw.rect(window, Gray, [220, 350, 150, 37])
        pygame.draw.rect(window, Gray, [400, 350, 150, 37])

        mouse = pygame.mouse.get_pos()

        if 268 <= mouse[0] <= 268 + 120 and 136 <= mouse[1] <= 136 + 40:
          pygame.draw.rect(window, Silver, [255, 150, 150, 37])
        
        if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
          pygame.draw.rect(window, Silver, [30, 350, 150, 37])

        if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
          pygame.draw.rect(window, Silver, [220, 350, 150, 37])

        if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
          pygame.draw.rect(window, Silver, [400, 350, 150, 37])

        submit_text = font.render('Submit', True, White)
        window.blit(submit_text, (293, 156))

        question_text = font.render(f'What is {Num1}{Operator}{Num2}?', True, (0, 0, 0))
        window.blit(question_text, (250, 55))

        level_text = font.render(f'Level  {level}', True, White)
        window.blit(level_text, (18, 7))

        wins_text = font.render(f'{wins}', True, White)
        window.blit(wins_text, (265, 7))

        events_text = font.render(f'Events', True, White)
        window.blit(events_text, (375, 7))

        coins_text = font.render(f'{bal}', True, White)
        window.blit(coins_text, (490, 7))

        shop_text = font.render('Battle Deck', True, White)
        window.blit(shop_text, (36, 355))

        earn_text = font.render('Earn', True, White)
        window.blit(earn_text, (435, 355))

        play_text = font.render('Play', True, White)
        window.blit(play_text, (270, 355))

        pygame.draw.rect(window, color, input_box, 2)

        pygame.display.update()

def deck_menu():
  global level
  global wins
  if wins >= 1000 and wins <= 1999:
      Background = menu2
      battle_deck.append("elecball")
      level = 2
  elif wins >= 2000:
    level = 3
    Background = menu3
    battle_deck.append("rock_ball")

  else:
      Background = menu1
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

      mouse = pygame.mouse.get_pos()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
          earn_menu() 

        if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
          main_menu()
    
    window.blit(Background, (0, 0))
    pygame.draw.rect(window, Gray, [30, 350, 150, 37])
    pygame.draw.rect(window, Gray, [220, 350, 150, 37])
    pygame.draw.rect(window, Gray, [400, 350, 150, 37])

    mouse = pygame.mouse.get_pos()

    if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [30, 350, 150, 37])

    if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [220, 350, 150, 37])

    if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [400, 350, 150, 37])

    shop_text = font.render(' Your cards: ', True, (0, 0, 0))
    window.blit(shop_text, (200, 80))

    level_text = font.render(f'Level  {level}', True, White)
    window.blit(level_text, (18, 7))

    wins_text = font.render(f'{wins}', True, White)
    window.blit(wins_text, (265, 7))

    events_text = font.render(f'Events', True, White)
    window.blit(events_text, (375, 7))

    coins_text = font.render(f'{bal}', True, White)
    window.blit(coins_text, (490, 7))

    shop_text = font.render('Battle Deck', True, White)
    window.blit(shop_text, (36, 355))

    earn_text = font.render('Earn', True, White)
    window.blit(earn_text, (435, 355))

    play_text = font.render('Play', True, White)
    window.blit(play_text, (270, 355))

    if "fireball" in battle_deck:
      window.blit(Firecard, (100, 100))

    if "elecball" in battle_deck:
      window.blit(Elecard, (200, 100))

    if "rock_ball" in battle_deck:
      window.blit(rockcard, (300, 100))

    pygame.display.update() 

def not_money():
   global level
   global wins
   if wins >= 1000 and wins <= 1999:
      Background_box = menu2
      level = 2
   elif wins >= 2000:
      Background_box = menu3
      level = 3

   else:
      Background_box = menu1
   while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

      mouse = pygame.mouse.get_pos()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if 275 <= mouse[0] <= 275 + 120 and 207 <= mouse[1] <= 207 + 40:
          earn_menu()

        if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
          deck_menu()     

        if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
          earn_menu() 

        if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
          main_menu()

    window.blit(Background_box, (0, 0))
    pygame.draw.rect(window, Orange, [250, 200, 150, 37])
    pygame.draw.rect(window, Gray, [30, 350, 150, 37])
    pygame.draw.rect(window, Gray, [220, 350, 150, 37])
    pygame.draw.rect(window, Gray, [400, 350, 150, 37])

    mouse = pygame.mouse.get_pos()

    if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [30, 350, 150, 37])

    if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [220, 350, 150, 37])

    if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [400, 350, 150, 37])
    
    if 275 <= mouse[0] <= 275 + 120 and 207 <= mouse[1] <= 207 + 40:
      pygame.draw.rect(window, Orange_Dark, [250, 200, 150, 37])

    info_text = font.render("You don't have 500 coins.", True, (0, 0, 0))
    window.blit(info_text, (200, 130))

    level_text = font.render(f'Level  {level}', True, White)
    window.blit(level_text, (18, 7))

    wins_text = font.render(f'{wins}', True, White)
    window.blit(wins_text, (265, 7))

    events_text = font.render(f'Events', True, White)
    window.blit(events_text, (375, 7))

    coins_text = font.render(f'{bal}', True, White)
    window.blit(coins_text, (490, 7))

    shop_text = font.render('Battle Deck', True, White)
    window.blit(shop_text, (36, 355))

    earn_text = font.render('Earn', True, White)
    window.blit(earn_text, (435, 355))

    play_text = font.render('Play', True, White)
    window.blit(play_text, (270, 355))

    earn_text = font.render('Earn', True, (0, 0, 0))
    window.blit(earn_text, (300, 207))

    pygame.display.update() 

def setting_menu():
   global bal
   global level
   if wins >= 1000 and wins <= 1999:
      Background = menu2
      level = 2
     
   elif wins >= 2000:
      Background = menu3
      level = 3

   else:
      Background = menu1
   while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

      mouse = pygame.mouse.get_pos()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
          deck_menu()     

        if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
          earn_menu() 

        if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
          main_menu()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          bal = bal + 500
          
    window.blit(Background, (0, 0))
    pygame.draw.rect(window, Gray, [30, 350, 150, 37])
    pygame.draw.rect(window, Gray, [220, 350, 150, 37])
    pygame.draw.rect(window, Gray, [400, 350, 150, 37])

    mouse = pygame.mouse.get_pos()

    if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [30, 350, 150, 37])

    if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [220, 350, 150, 37])

    if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [400, 350, 150, 37])

    level_text = font.render(f'Level  {level}', True, White)
    window.blit(level_text, (18, 7))

    wins_text = font.render(f'{wins}', True, White)
    window.blit(wins_text, (265, 7))

    events_text = font.render(f'Events', True, White)
    window.blit(events_text, (375, 7))

    coins_text = font.render(f'{bal}', True, White)
    window.blit(coins_text, (490, 7))

    shop_text = font.render('Battle Deck', True, White)
    window.blit(shop_text, (36, 355))

    earn_text = font.render('Earn', True, White)
    window.blit(earn_text, (435, 355))

    play_text = font.render('Play', True, White)
    window.blit(play_text, (270, 355))

    all_text = font3.render('How to play:', True, White)
    window.blit(all_text, (240, 62))

    info_text = font3.render('You and your opponnent are battling', True, White)
    window.blit(info_text, (50, 102))
     
    info_text = font3.render('for trophies.', True, White)
    window.blit(info_text, (50, 142))
     
    info2_text = font3.render('In order to win, you must attack', True, White)
    window.blit(info2_text, (50, 182))

    info2_text = font3.render('until 0 health.', True, White)
    window.blit(info2_text, (50, 222))
     
    info3_text = font3.render('If you fail to do so, you will loose.', True, White)
    window.blit(info3_text, (50, 262))


    pygame.display.update() 

def main_menu():
   global bal
   global level
   global wins
   if wins >= 1000 and wins <= 1999:
      Background = menu2
      level = 2
     
   elif wins >= 2000:
      Background = menu3
      level = 3

   else:
      Background = menu1
   while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

      mouse = pygame.mouse.get_pos()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
          deck_menu()     

        if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
          earn_menu() 

        if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
          main_menu()
  
        if 250 <= mouse[0] <= 250 + 120 and 250 <= mouse[1] <= 250 + 40:
          if bal >= 500:
            game()
          else:
            not_money()

        if 45 <= mouse[0] <= 45 + 120 and 10 <= mouse[1] <= 10 + 40:
          setting_menu()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          bal = bal + 500

        if event.key == pygame.K_w:
          wins = wins + 1000
          
    window.blit(Background, (0, 0))
    window.blit(Castle, (220, 50))
    pygame.draw.rect(window, Gray, [30, 350, 150, 37])
    pygame.draw.rect(window, Gray, [220, 350, 150, 37])
    pygame.draw.rect(window, Gray, [400, 350, 150, 37])
    pygame.draw.rect(window, Orange, [250, 260, 150, 37])

    mouse = pygame.mouse.get_pos()

    if 30 <= mouse[0] <= 30 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [30, 350, 150, 37])

    if 220 <= mouse[0] <= 220 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [220, 350, 150, 37])

    if 400 <= mouse[0] <= 400 + 120 and 350 <= mouse[1] <= 350 + 40:
      pygame.draw.rect(window, Silver, [400, 350, 150, 37])

    if 250 <= mouse[0] <= 250 + 120 and 250 <= mouse[1] <= 250 + 40:
      pygame.draw.rect(window, Orange_Dark, [250, 260, 150, 37])

    level_text = font.render(f'Level  {level}', True, White)
    window.blit(level_text, (18, 7))

    wins_text = font.render(f'{wins}', True, White)
    window.blit(wins_text, (265, 7))

    events_text = font.render(f'Events', True, White)
    window.blit(events_text, (375, 7))

    coins_text = font.render(f'{bal}', True, White)
    window.blit(coins_text, (490, 7))

    shop_text = font.render('Battle Deck', True, White)
    window.blit(shop_text, (36, 355))

    earn_text = font.render('Earn', True, White)
    window.blit(earn_text, (435, 355))

    play_text = font.render('Play', True, White)
    window.blit(play_text, (270, 355))

    battle_text = font3.render('Battle', True, White)
    window.blit(battle_text, (285, 262))

    pygame.display.update() 
    
main_menu()
