#Snake Game!

#import modules include pygame
import pygame, sys, random, time 

#Error Checking for the pygame initialization 
errors_checking = pygame.init()
if errors_checking[1] > 0:
	print ("Warning: The program has {0} initializing errors, existing...".format (errors_checking))
	sys.exit(-1)
else:
	print ("Pygame successfully initialized!")

#Game Window Set up
Play_Surface = pygame.display.set_mode((720, 720)) #the size of game window
pygame.display.set_caption('Snake Game V1.0') #change the window title

#Colours definition
red = pygame.Color(255, 0, 0) #game over
purple = pygame.Color(153, 50, 204) #snake body color
teal = pygame.Color(0, 128, 128) #score
lightyellow = pygame.Color(255, 255, 224) #background
olive = pygame.Color(128, 128,0) #food

# FPS controller
fps_Controller = pygame.time.Clock() 

#variable initialize
snake_position = [360, 360]
snack_body_length = [[360,360],[350,360],[340,360]]
food_position = [random.randrange(4,68)*10,random.randrange(4,68)*10]
food_spawn = True 
direction = 'RIGHT' #initial direction 
changeto = direction 
score=0

#Game Over Function
def gameover():
	font = pygame.font.SysFont('monaco',54) #text font and size
	GOsurf = font.render('Game Over!',True, red) #text
	GOrect = GOsurf.get_rect() #get rectangle 
	GOrect.midtop = (360,150) #position
	Play_Surface.blit(GOsurf,GOrect)
	showscore(0) #score display 
	pygame.display.flip()
	time.sleep(4)
	pygame.quit()
	sys.exit()

#Show score function 
def showscore(choice=1):
	sfont = pygame.font.SysFont('monaco',30) #score font and size
	ssurf = sfont.render('Score:{0}'.format(score),True, teal) #score
	srect = ssurf.get_rect() #get rectangle 
	if choice == 1:
		srect.midtop = (80,10) 
	else: srect.midtop =(360,120)
	Play_Surface.blit (ssurf,srect)

#main logic of the game
while True:
	for event in pygame.event.get():
                #exit function
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit() 
		
		#keyboard enter
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'):
				changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))

	# direction set up
	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'

	#updating snake position [x,y] after change direction 
	if direction == 'RIGHT':
		snake_position[0] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10

	# snake body and food mechanism
	snack_body_length.insert(0, list (snake_position))
	if snake_position[0] == food_position[0] and snake_position[1] == food_position [1]:
		score += 1
		food_spawn = False
	else: 
		snack_body_length.pop()

	if food_spawn == False:
		food_position = [random.randrange(4,68)*10,random.randrange(4,68)*10]
	food_spawn = True

	#background
	Play_Surface.fill(lightyellow)
	
	#draw snake
	for pos in snack_body_length:
		pygame.draw.rect(Play_Surface, purple, pygame.Rect(pos[0],pos[1],10,10))
	
	pygame.draw.rect(Play_Surface, olive, pygame.Rect(food_position[0],food_position[1],10,10))

    #hit the boundary of playsurface => gameover setup
	if snake_position[0] >710 or snake_position[0]<0:
		gameover()
	if snake_position[1] >710 or snake_position[1]<0:
		gameover()
    
    #hit snake body => gameover
	for block in snack_body_length[1:]:
		if snake_position[0] == block [0] and snake_position[1] == block[1]:
			gameover()

	showscore()
	pygame.display.flip()
	fps_Controller.tick(20)
