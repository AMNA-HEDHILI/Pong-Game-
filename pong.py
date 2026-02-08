import pygame
import random

# constants for the windows width and height values
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# the RGB values for the colors used in the game
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_RED = (255, 50, 50)
COLOR_BLUE = (50, 150, 255)

# Game states
STATE_START = 0
STATE_PLAYING = 1
STATE_GAME_OVER = 2

def main(): 
  # GAME SETUP
  
  # initialize the PyGame library (this is absolutely necessary)
  pygame.init()

  # this creates the window for the game
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  # set the window's title
  pygame.display.set_caption('Pong')

  # create the clock object to keep track of the time
  clock = pygame.time.Clock()
  
  # Game state
  game_state = STATE_START
  
  # Player scores
  player1_score = 0
  player2_score = 0
  winning_score = 5  # Play to 5 points
  
  '''
  these are the players' game paddles
  the `Rect` function need the x, y, width and height
  of the rectangles we will be drawing
  '''
  paddle_1_rect = pygame.Rect(30, 0, 15, 100)
  paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 45, 0, 15, 100)

  # this is to track by how much the players' paddles will move per frame
  paddle_1_move = 0
  paddle_2_move = 0

  # this is the rectangle that represents the ball
  ball_rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 20, 20)

  # determine the x and y speed of the ball 
  ball_accel_x = random.randint(2, 4) * 0.1
  ball_accel_y = random.randint(2, 4) * 0.1

  # randomize the direction of the ball
  if random.randint(1, 2) == 1:
    ball_accel_x *= -1
  if random.randint(1, 2) == 1:
    ball_accel_y *= -1

  # Font for scores and text
  score_font = pygame.font.SysFont('Consolas', 48)
  message_font = pygame.font.SysFont('Consolas', 36)
  small_font = pygame.font.SysFont('Consolas', 24)

  # GAME LOOP
  while True:
    
    ''' 
    set the back ground color to black
    needs to be called every time the game updates
    '''
    screen.fill(COLOR_BLACK)
    
    # Draw center line (dashed)
    for y in range(0, SCREEN_HEIGHT, 30):
      pygame.draw.rect(screen, COLOR_GRAY, (SCREEN_WIDTH // 2 - 2, y, 4, 15))
    
    # START SCREEN
    if game_state == STATE_START:
      # Draw title
      title_font = pygame.font.SysFont('Consolas', 64, bold=True)
      title = title_font.render('PONG', True, COLOR_WHITE)
      title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
      screen.blit(title, title_rect)
      
      # Draw controls info
      controls_y = SCREEN_HEIGHT // 2 - 50
      
      player1_text = message_font.render('Player 1: W (Up) / S (Down)', True, COLOR_BLUE)
      player1_rect = player1_text.get_rect(center=(SCREEN_WIDTH // 2, controls_y))
      screen.blit(player1_text, player1_rect)
      
      player2_text = message_font.render('Player 2: ↑ (Up) / ↓ (Down)', True, COLOR_RED)
      player2_rect = player2_text.get_rect(center=(SCREEN_WIDTH // 2, controls_y + 50))
      screen.blit(player2_text, player2_rect)
      
      # Draw start instruction
      start_text = message_font.render('Press SPACE to Start', True, COLOR_WHITE)
      start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150))
      screen.blit(start_text, start_rect)
      
      # Draw objective
      objective_text = small_font.render(f'First to {winning_score} points wins!', True, COLOR_GRAY)
      objective_rect = objective_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
      screen.blit(objective_text, objective_rect)
      
      # update the display
      pygame.display.flip()
      clock.tick(60)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          return
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            game_state = STATE_PLAYING

    # GAME OVER SCREEN
    elif game_state == STATE_GAME_OVER:
      # Determine winner
      winner = "Player 1" if player1_score > player2_score else "Player 2"
      winner_color = COLOR_BLUE if winner == "Player 1" else COLOR_RED
      
      # Draw game over message
      game_over_font = pygame.font.SysFont('Consolas', 72, bold=True)
      game_over_text = game_over_font.render('GAME OVER', True, COLOR_WHITE)
      game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
      screen.blit(game_over_text, game_over_rect)
      
      # Draw winner
      winner_text = message_font.render(f'{winner} Wins!', True, winner_color)
      winner_rect = winner_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
      screen.blit(winner_text, winner_rect)
      
      # Draw final score
      score_text = message_font.render(f'Final Score: {player1_score} - {player2_score}', True, COLOR_WHITE)
      score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
      screen.blit(score_text, score_rect)
      
      # Draw restart instruction
      restart_text = message_font.render('Press R to Restart or Q to Quit', True, COLOR_WHITE)
      restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150))
      screen.blit(restart_text, restart_rect)
      
      pygame.display.flip()
      clock.tick(60)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          return
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_r:
            # Reset game
            game_state = STATE_PLAYING
            player1_score = 0
            player2_score = 0
            # Reset ball position
            ball_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            # Reset ball speed
            ball_accel_x = random.randint(2, 4) * 0.1
            ball_accel_y = random.randint(2, 4) * 0.1
            if random.randint(1, 2) == 1:
              ball_accel_x *= -1
            if random.randint(1, 2) == 1:
              ball_accel_y *= -1
          elif event.key == pygame.K_q:
            pygame.quit()
            return

    # PLAYING STATE
    elif game_state == STATE_PLAYING:
      '''
      get the time elapse between now and the last frame
      60 is an arbitrary number but the game runs smooth at 60 FPS
      '''
      delta_time = clock.tick(60)

      # checking for events
      for event in pygame.event.get():

        # if the user exits the window
        if event.type == pygame.QUIT:

          # exit the function, to finish the game
          return

        # if the user is pressing a key
        if event.type == pygame.KEYDOWN:

          # PLAYER 1
          # if the key is W, set the movement of paddle_1 to go up
          if event.key == pygame.K_w:
            paddle_1_move = -0.5

          # if the key is S, set the movement of paddle_1 to go down
          if event.key == pygame.K_s:
            paddle_1_move = 0.5

          # PLAYER 2
          # if the key is the up arrow, set the movement of paddle_2 to go up
          if event.key == pygame.K_UP:
            paddle_2_move = -0.5
          # if the key is the down arrow, set the movement of paddle_2 to go down
          if event.key == pygame.K_DOWN:
            paddle_2_move = 0.5

        # if the player released a key
        if event.type == pygame.KEYUP:
          # if the key released is w or s, stop the movement of paddle_1
          if event.key == pygame.K_w or event.key == pygame.K_s: 
            paddle_1_move = 0.0

          # if the key released is the up or down arrow, stop the movement of paddle_2
          if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            paddle_2_move = 0.0

      '''
      move paddle_1 and paddle_2 according to their `move` variables
      we also multiply the `move` variable by the delta time to keep movement consistent through frames
      '''
      paddle_1_rect.top += paddle_1_move * delta_time
      paddle_2_rect.top += paddle_2_move * delta_time

      # if paddle_1 is going out of the screen by the top, set it to the maximum to limit its movement
      if paddle_1_rect.top < 0:
        paddle_1_rect.top = 0
      
      # paddle_2 is going out of the screen by the bottom, do the same thing   
      if paddle_1_rect.bottom > SCREEN_HEIGHT:
        paddle_1_rect.bottom = SCREEN_HEIGHT

      # do the same thing with paddle_2
      if paddle_2_rect.top < 0:
        paddle_2_rect.top = 0
      if paddle_2_rect.bottom > SCREEN_HEIGHT:
        paddle_2_rect.bottom = SCREEN_HEIGHT      

      # if the ball is getting close to the top (15 is an arbitrary number, but I found that it worked great)
      if ball_rect.top < 0:
        # invert its vertical velocity 
        ball_accel_y *= -1
        # add a bit of y to it to not trigger the above code again
        ball_rect.top = 0
      # do the same thing with the bottom
      if ball_rect.bottom > SCREEN_HEIGHT - ball_rect.height:
        ball_accel_y *= -1
        ball_rect.top = SCREEN_HEIGHT - ball_rect.height

      # SCORING - when ball goes out of bounds
      if ball_rect.left <= 0:
        # Player 2 scores
        player2_score += 1
        # Reset ball
        ball_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # Reset ball speed (slightly faster each time)
        ball_accel_x = random.randint(3, 5) * 0.1
        ball_accel_y = random.randint(2, 4) * 0.1
        # Always start towards player who just scored
        ball_accel_x = abs(ball_accel_x)  # Positive = towards player 1
        if random.randint(1, 2) == 1:
          ball_accel_y *= -1
          
      if ball_rect.left >= SCREEN_WIDTH:
        # Player 1 scores
        player1_score += 1
        # Reset ball
        ball_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # Reset ball speed
        ball_accel_x = random.randint(3, 5) * 0.1
        ball_accel_y = random.randint(2, 4) * 0.1
        # Always start towards player who just scored
        ball_accel_x = -abs(ball_accel_x)  # Negative = towards player 2
        if random.randint(1, 2) == 1:
          ball_accel_y *= -1

      # Check for win condition
      if player1_score >= winning_score or player2_score >= winning_score:
        game_state = STATE_GAME_OVER

      '''
      if paddle_1_rect collides with the ball and the ball is in front of it, 
      change the speed of the ball and make it move a little in the other way
      '''
      if paddle_1_rect.colliderect(ball_rect) and paddle_1_rect.left < ball_rect.left:
        ball_accel_x *= -1.1  # Increase speed slightly on hit
        ball_rect.left += 5
      # do the same with paddle_2_rect
      if paddle_2_rect.colliderect(ball_rect) and paddle_2_rect.left > ball_rect.left:
        ball_accel_x *= -1.1  # Increase speed slightly on hit
        ball_rect.left -= 5

      # move the ball
      ball_rect.left += ball_accel_x * delta_time 
      ball_rect.top += ball_accel_y * delta_time

      # Draw player 1 and player 2's rects with colors
      pygame.draw.rect(screen, COLOR_BLUE, paddle_1_rect)
      pygame.draw.rect(screen, COLOR_RED, paddle_2_rect)

      # draw the ball with the white color
      pygame.draw.rect(screen, COLOR_WHITE, ball_rect)
      
      # Draw scores at top of screen
      score_text = f"{player1_score}  :  {player2_score}"
      score_surface = score_font.render(score_text, True, COLOR_WHITE)
      score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
      screen.blit(score_surface, score_rect)
      
      # Draw player labels under scores
      player1_label = small_font.render("Player 1", True, COLOR_BLUE)
      player1_label_rect = player1_label.get_rect(center=(SCREEN_WIDTH // 4, 100))
      screen.blit(player1_label, player1_label_rect)
      
      player2_label = small_font.render("Player 2", True, COLOR_RED)
      player2_label_rect = player2_label.get_rect(center=(3 * SCREEN_WIDTH // 4, 100))
      screen.blit(player2_label, player2_label_rect)
      
      # Draw winning score info
      win_info = small_font.render(f"First to {winning_score}", True, COLOR_GRAY)
      win_info_rect = win_info.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
      screen.blit(win_info, win_info_rect)

    # update the display (this is necessary for Pygame)
    pygame.display.update()

# run the game
if __name__ == '__main__':
  main()