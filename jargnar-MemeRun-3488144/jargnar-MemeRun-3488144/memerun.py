############################################################################################
###                                                                                      ###
### PyGame with a troll faced guy flying over an alien land trying to escape Zombies     ###
###                                                                                      ###
### Author: SUHAS SG                                                                     ###
### jargnar@gmail.com                                                                    ###
###                                                                                      ###
### suhased.wordpress.com                                                                ###
### twitter: @jargnar                                                                    ### 
### facebook: facebook.com/jargnar                                                       ###
###                                                                                      ###
###                                                                                      ###
### Disclaimer: The kelvinized font is not mine and I found it on the internet.          ###
### All the other images are mine.                                                       ###
###                                                                                      ###
### Do Enjoy the game!                                                                   ###
### You need to have Python and PyGame installed to run it.                              ###
###                                                                                      ###
### Run it by typing "python memerun.py" in the terminal                                 ###
###                                                                                      ###
###                                                                                      ###
############################################################################################

import sys,random,pygame
from collections import deque

pygame.init()

textcolor = 255,205,125
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("memeRun by Suhas")

class tree:
	'Doc: Class Tree represents the Physical Tree/Zombie and properties'
	def __init__(self):
		self.img = pygame.image.load("res/tree.png")
		self.rect = self.img.get_rect()
		self.rect = self.rect.move(730,305)
	def get_rectangle(self):
		return self.rect
	def left(self): 
		return self.rect.left
	def right(self):
		return self.rect.right
	def top(self):
		return self.rect.top
	def bottom(self):
		return self.rect.bottom
	def render(self):
		screen.blit(self.img,self.rect)
	def move(self,x,y):
		self.rect = self.rect.move(x,y)

bg = pygame.image.load("res/memebg.png")
bgrect = bg.get_rect()
screen.blit(bg,bgrect)

#play again? :)
def re_play():
	gover = pygame.image.load("res/gover.png")
	grect = gover.get_rect()

	#Play again please :D
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		screen.blit(bg,bgrect)
		screen.blit(gover,grect)
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_SPACE]: break
		pygame.display.flip()
	begin()

#oops gameover condition
def gameover(x,y):
	tempscreen = pygame.image.load("res/gameover.jpeg")
	trect = tempscreen.get_rect()
	boom = pygame.image.load("res/boom.png")
	brect = boom.get_rect()
	brect = brect.move(x,y)
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		screen.blit(tempscreen,trect)
		screen.blit(boom,brect)
		
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_RETURN]:break
		pygame.display.flip()

	re_play()


def begin():

	#init some important vars and load some images
	score = 0
	timer = 32
	trees = deque()
	trees.append(tree())

	meme = pygame.image.load("res/meme.png")
	mrect = meme.get_rect()
	mrect = mrect.move(200,330)

	leg3 = pygame.image.load("res/leg3.png")
	legs = pygame.image.load("res/legs.png")
	lr3 = leg3.get_rect()
	lrect = legs.get_rect()
	lr3 = lr3.move(200,350)
	lrect = lrect.move(160,350)

	myfont = pygame.font.Font("res/Kelvinized.ttf",18)
	#end of init-ing some important vars and loading some images

	while 1:
		for event in pygame.event.get():
			if event.type==pygame.QUIT: sys.exit()
		screen.blit(bg,bgrect)
		
		#render the scoreboard
		if pygame.time.get_ticks()%200: score = score + 1
		scoreline = "DISTANCE: "+str(score)
		scoreboard = myfont.render(scoreline,1,textcolor)
		
		screen.blit(scoreboard,scoreboard.get_rect())
		
		#render trees at random intervals of time
		if pygame.time.get_ticks() % (100*random.randint(1,3)) == 0:
			tree_o = tree()
			trees.append(tree_o)
		for Tree in trees:
			Tree.move(-4,0)
			Tree.render()
	
		if trees:
			if trees[0].right() < 0 : trees.popleft()
 	
		pressed = pygame.key.get_pressed()
		moved = 0
		
		#jump for sometime if up key is pressed
		if pressed[pygame.K_UP]:
			if timer < 25:
				screen.blit(meme,mrect)
				screen.blit(legs,lrect)
			if timer >= 25 and timer <  170:
				mrect = mrect.move(30,-90)
				lr3 = lr3.move(30,-90)
				screen.blit(meme,mrect)
				screen.blit(leg3,lr3)
				moved = 1

			elif timer >= 160:
				timer = 5
				screen.blit(meme,mrect)
				screen.blit(legs,lrect)
			
		else:
			screen.blit(meme,mrect)
			screen.blit(legs,lrect)
		
		#death condition 
		for Tree in trees:
			if Tree.left() <=274 and Tree.left() >= 258:
				if mrect.bottom == 395: 
					pygame.image.save(screen,"res/gameover.jpeg")
					x = Tree.get_rectangle()
					gameover(x[0],x[1])
		
			if Tree.left() <= 168 and Tree.left() >= 154:
				if mrect.bottom == 395: 
					pygame.image.save(screen,"res/gameover.jpeg")
					x = Tree.get_rectangle()
					gameover(x[0],x[1])
	
		if moved == 1:
			mrect = mrect.move(-30,90)
			lr3 = lr3.move(-30,90)
			timer = timer + 1

		if timer <= 25: timer = timer + 1
		

		pygame.display.flip()	


def main():
	
	#draw the welcome screen
	welcome = pygame.image.load("res/welcome.png")
	wrect = welcome.get_rect()
	wrect = wrect.move(40,40)

	#wait till the user presses "enter" key
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
	
                        screen.blit(welcome,wrect)
                        pressed = pygame.key.get_pressed()
		
                        if pressed[pygame.K_RETURN]: break
	
                        pygame.display.flip()
	
	#BEGIN THE GAME :D
	begin()

if __name__ == "__main__":
	main()
