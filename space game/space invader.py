import pygame
import random
import math

#initilizing pygame
pygame.init()

# creating the game window
screen= pygame.display.set_mode((800, 600))

#background
background=pygame.image.load("galaxy.jpg")

#title and icon for the window
pygame.display.set_caption("Space Invaders")
icon= pygame.image.load("universe.png")
pygame.display.set_icon(icon)

#player spaceship
playerImg=pygame.image.load("ufo.png")
playerX=370
playerY=480
playerX_change=0

#enemy spaceship
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=5

for i in range (num_of_enemies):
	enemyImg.append(pygame.image.load("alien.png"))
	enemyX.append(random.randint(0,735))
	enemyY.append(random.randint(50,150))
	enemyX_change.append(0.2)
	enemyY_change.append(20)

#bullet
bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=0.2
bulletY_change=1.0
bullet_state= "ready"

#score
score_value=0
font =pygame.font.Font("freesansbold.ttf", 32)

textX=10
textY=10

#game over text
over_font =pygame.font.Font("freesansbold.ttf", 64)


def show_score(x,y):
	score=font.render("Score : "+ str(score_value), True, (255,255,255))
	screen.blit(score, (x, y))

def game_over_text():
	over_text=over_font.render("GAME OVER!", True, (255,255,255))
	screen.blit(over_text, (200, 250))

def player(x,y):
	screen.blit(playerImg, (x, y))

def enemy(x,y,i):
	screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
	global bullet_state
	bullet_state="fire"
	screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
	distance= math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
	if distance < 27:
		return True
	else :
		return False




#running the game window - 
#anything that happens while the game is running happens inside this loop 
running= True
while running:
	screen.fill((173,216,230))
	#background
	screen.blit(background,(0,0))

	for event in pygame.event.get():
		if event.type ==  pygame.QUIT:
			running= False

		#check for keystroke
		if event.type== pygame.KEYDOWN:
			#print("A Keystroke was pressed")
			if event.key== pygame.K_LEFT:
				playerX_change= -0.35
			if event.key== pygame.K_RIGHT:
				playerX_change= 0.35
			if event.key== pygame.K_SPACE:
				if bullet_state is "ready" :
					bulletX= playerX
					fire_bullet(playerX, bulletY)
				

				
		if event.type== pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key== pygame.K_RIGHT:
				playerX_change= 0

	playerX+=playerX_change
	if playerX<=0:
		playerX=0
	elif playerX>=736:
		playerX=736


	for i in range(num_of_enemies):
		#game over
		if enemyY[i]> 400:
			for j in range(num_of_enemies):
				enemyY[j]=2000
			game_over_text()
			break

		enemyX[i] +=enemyX_change[i]
		if enemyX[i] <=0:
			enemyX_change[i] =0.2
			enemyY[i] +=enemyY_change[i]
		elif enemyX[i]>=736:
			enemyX_change[i]=-0.2
			enemyY[i] +=enemyY_change[i]


		#collision
		collision=isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
		if collision:
			bulletY=480
			bullet_state="ready"
			score_value+= 1
			enemyX[i]=random.randint(0,735)
			enemyY[i]=random.randint(50,150)

		enemy(enemyX[i], enemyY[i], i)

	#bullet movement
	if bulletY <= 0 :
		bulletY=480
		bullet_state="ready"

	if bullet_state is "fire":
		fire_bullet(bulletX,bulletY)
		bulletY -= bulletY_change



	player(playerX, playerY)
	show_score(textX, textY)
	pygame.display.update()
    