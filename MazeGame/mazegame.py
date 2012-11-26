import pygame
import mazeclass

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size=[1000,500]
screen=pygame.display.set_mode(size)
 
# Set title of screen
pygame.display.set_caption("Maze Project")

# Get a new maze
mazegrid =  [[2,2,2,2,2,2,2,6,2,2,2,2,2,2,2,2,2,2,2,2],
             [2,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,2],
             [2,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1,1,0,2],
             [2,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,2],
             [2,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,2],
             [2,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,2],
             [2,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,2],
             [2,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,2],
             [2,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,2],
             [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]

the_maze = mazeclass.Maze(mazegrid)


##########################################################

# code to be implemented

def dfs(i,j):
    return

def setpath(i,j):
    return 

def shortestpath(i,j):
    return

# Loop until the user clicks the close button.
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while done==False:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN: # If user wants to perform an action
                if event.key == pygame.K_d:
                    the_maze.reset(mazegrid)
                    dfs(the_maze.bot_xcoord, the_maze.bot_ycoord)
                if event.key == pygame.K_s:
                    the_maze.reset(mazegrid)
                    setpath(the_maze.bot_xcoord, the_maze.bot_ycoord)
                if event.key == pygame.K_q:
                    the_maze.reset(mazegrid)
                    shortestpath(the_maze.bot_xcoord, the_maze.bot_ycoord)
     
        the_maze.display_maze(screen)
        # Limit to 20 frames per second
        clock.tick(50)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
# If you forget this line, the program will 'hang' on exit.
pygame.quit ()