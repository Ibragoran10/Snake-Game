#import modules nece
import random
import curses

# initialize the curses library to create our screen
screen = curses.initscr()

# hide the mouse cursor
curses.curs_set(0)


# getmax screen height and width 
screen_height , screen_width = screen.getmaxyx()


# create a new window
window = curses.newwin(screen_height , screen_width , 0 , 0)


# allow window to receive input from the keyboard
window.keypad(1)

# set the delay  for updating the screen
window.timeout(100)


# set the x,y coordinates of the initial position of snake's head
snk_x = screen_width//4 # 500/4 125 = 
snk_y = screen_height//2 # 600/2 = 300

# define the initial position of the snake body
snake = [

  [snk_y , snk_x],
  [snk_y , snk_x-1],
  [snk_y , snk_x-2]
]

# create the food in the middle of window
food = [screen_height//2 , screen_width//2] #[600//2 , 400//2]= food=[300,200]


# add the food by using PI character to right
window.addch(food[0] , food[1] , curses.ACS_PI)


# set initial movement direction to right
key = curses.KEY_RIGHT



# create game loop that loops forever until player loses or quits the game
while True:
  
  # get the key that will be pressed by user
  next_key = window.getch()


# if user dosen't input anything, key remains same, else key will be set to the new pressed key
  key = key if next_key == -1 else next_key

#if next_key == -1:
 # key = key

#else:
 # key = next_key


# check if snake collided with the walls or itself
  if snake[0][0] in [0 , screen_height ] or snake[0][1] in [0 , screen_width] or snake[0] in snake[1:]:

    curses.endwin() # closing the window
    quit() # exit the program


# set the new poisition of the snake head based on the direction 
  new_head = [snake[0][0] , snake [0][1]]

  if key == curses.KEY_DOWN:
    new_head[0] +=1

  if key == curses.KEY_UP:
    new_head[0] -=1

  if key == curses.KEY_RIGHT:
   new_head[1] +=1

  if key == curses.KEY_LEFT:
    new_head[1] -=1
  

  # insert the new head to the first poisiton of snake list
  snake.insert(0 , new_head)


# check if snake ate the food
  if snake[0] == food:
    food = None # remove food if snake ate it

    
    # while food is removed, generate new food in a random place on screen
    while food is None:
         new_food = [
         random.randint(1 , screen_height-1), #600-1 = 599
         random.randint(1 , screen_width-1) #400-1 = 399
      
        ]

         food = new_food if new_food not in snake else None
    window.addch(food[0] , food[1] , curses.ACS_PI)

# otherwise remove the last segment of snake body
  else:
    tail = snake.pop()
    window.addch(tail[0], tail[1], ' ')    


# update the position of snake on the screen
  window.addch(snake[0][0] , snake[0][1] , curses.ACS_CKBOARD)



