import pygame
import sys

white = (255,255,255)
black = (0,0,0)

map_size = 500

pygame.init()
screen = pygame.display.set_mode((map_size, map_size))
pygame.display.set_caption("TicTacToe")

pygame.font.init()
screen.fill((141,141,141))
finish = False

def create_map():
  global screen_size

  x = int(map_size / 3)
  y = 10

  pygame.draw.line(screen, black, (x,0),(x, map_size), y)
  pygame.draw.line(screen, black, (x * 2, 0), (x * 2, map_size), y)
  pygame.draw.line(screen, black, (0,x),(map_size, x), y)
  pygame.draw.line(screen, black, (0, x * 2), (map_size, x * 2), y)

create_map()

main_Font = pygame.font.SysFont('Calibri', 170)
banner_font = pygame.font.SysFont('Calibri',100)

map = [
  [None, None, None],
  [None, None, None],
  [None, None, None]
]

def mouse_to_map():
  (x, y) = pygame.mouse.get_pos()
  row_column_size = int(map_size / 3)

  column = get_num(row_column_size, x)
  row = get_num(row_column_size, y)
  return column, row

def get_num(row_column_size, x):
  if x < row_column_size:
    column = 0
  elif row_column_size <= x < row_column_size * 2:
    column = 1
  else:
    column = 2
  return column

def draw_map (map):
  for y in range(3):
    for x in range(3):
      banner = main_Font.render(map[y][x], False, black)
      screen.blit(banner, (y * int(map_size / 3) + int(map_size / 18), x * int(map_size / 3)))

def check_the_map_ending(map):
  for y in range(3):
    for x in range(3):
      if map[y][x] is None:
        return False
  return True

def check_winner(map):
  if (map[1][1] is not None and map[0][0] == map[1][1] and map[1][1] == map[2][2]):
    return map[1][1]
  if (map[1][1] is not None and map[0][2] == map[1][1] and map[1][1] == map[2][0]):
    return map[1][1]

  for i in range(3):
    if (map[i][0] is not None and map[i][0] == map[i][1] and map[i][1] == map[i][2]):
      return map[i][0]
  
  for i in range(3):
    if (map[0][i] is not None and map[0][i] == map[1][i] and map[1][i] == map[2][i]):
      return map[0][i]
  
  return None

def end_game():
  pygame.quit()
  sys.exit()

def win_the_game():
    global finish

    mark_win = str(winner)
    screen.blit(banner_font.render(mark_win + " WYGRAŁ!", False, white), (20, int(map_size / 2) - int(map_size / 10)))
    finish = True

def start_game():
  map [[None, None, None], [None, None, None], [None, None, None]]
  screen.fill(backgroundColor)
  draw_lines()
  return map

move = 'X'

def change_player():
  global move

  if move == 'X':
    move = 'O'
  else:
    move = 'X'
  return move

while True:

  for action in pygame.event.get():
    if action.type == pygame.QUIT:
      end_game()

    if not finish and action.type is pygame.MOUSEBUTTONDOWN:
      (column, row) = mouse_to_map()

      if map[column][row] is None:
        map[column][row] = move
        move = change_player()
        draw_map(map)
        winner = check_winner(map)

        if winner is not None:
          win_the_game()

        if winner is None and check_the_map_ending(map):
          banner = banner_font.render("REMIS!", False, white)
          screen.blit(banner, (500 // 7, 500 // 2 - 500 // 11))

  pygame.display.update()