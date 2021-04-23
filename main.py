import pygame
from pygame.locals import*
import sys
import os

def draw_text(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

def main(sr):
	pygame.init()
	win=pygame.display.set_mode((1000,900),0,32)
	global srno
	srno=sr
	class Girl(pygame.sprite.Sprite):
		run=[pygame.image.load(os.path.join('image','Run ('+str(x)+').png')).convert_alpha() for x in range(1,9)]
		for x in range(0,8):
			run[x]=pygame.transform.scale(run[x],(118,100))
			run[x].set_colorkey((255,255,255))
		left=[pygame.image.load(os.path.join('image','Run ('+str(x)+').png')).convert_alpha() for x in range(1,9)]
		for x in range(0,8):
			left[x]=pygame.transform.scale(pygame.transform.flip(run[x],True,False),(118,100))
			left[x].set_colorkey((255,255,255))
		#walk=[pygame.image.load(os.path.join('image','Walk ('+str(x)+')')) for x in range(0,8)]
		shoot=[pygame.image.load(os.path.join('image','Shoot ('+str(x)+').png')).convert_alpha() for x in range(1,4)]
		dead=[pygame.image.load(os.path.join('image','Dead ('+str(x)+').png')).convert_alpha() for x in range(1,11)]
		idle=[pygame.image.load(os.path.join('image','Idle ('+str(x)+').png')).convert_alpha() for x in range(1,11)]
		for x in range(0,10):
			idle[x]=pygame.transform.scale(idle[x],(100,100))
		melee=[pygame.image.load(os.path.join('image','Melee ('+str(x)+').png')).convert_alpha() for x in range(1,8)]


		def __init__(self,x,y):
			super().__init__()
			self.x=x
			self.y=y
			self.slidecount=0
			self.runcount=0
			self.idlec=0
			self.rect=self.run[0].get_rect()
			self.rect.height-=10
			self.rect.center=(self.x,self.y)
			self.rect.width=90
			

		def draw(self,win):
			#pygame.draw.rect(win, (255, 0, 0),(self.rect.x-true_scroll[0],self.rect.y-true_scroll[1],90,100))
			keys=pygame.key.get_pressed()
			if keys[K_RIGHT]:
				self.runcount+=1
				if self.runcount//2>=8:
					self.runcount=0
				win.blit(self.run[self.runcount//2],(self.rect.x-true_scroll[0],self.rect.y-true_scroll[1]))
			elif keys[K_LEFT]:
				self.runcount+=1
				if self.runcount//2>=8:
					self.runcount=0
				win.blit(self.left[self.runcount//2],(self.rect.x-true_scroll[0],self.rect.y-true_scroll[1]))
			else:
				self.runcount=0
				self.idlec+=1
				if self.idlec//2>=10:
					self.idlec=0
				win.blit(self.idle[self.idlec//2],(self.rect.x-true_scroll[0],self.rect.y-true_scroll[1]))



	class Map:
		door=pygame.image.load("game assets/door.png").convert_alpha()
		def __init__(self,map):
			file=open(map+".txt")
			data=file.readlines()
			self.over=[0,0]
			map=[]
			level=[]
			for i in data:
				map=[]
				for j in i:
					if j=="0" or j=="1" or j=="2" or j=="3":
						map.append(j)
				level.append(map)
			self.level=level
			self.width=30
			self.block=[]
			self.arect=self.door.get_rect()
			
		
		def draw(self,win):
			x,y=2*self.width,0
			BLACK=(0,0,0)
			CYAN=(0,255,255)
			pygame.draw.rect(win,(7,80,75),pygame.Rect(0,540,1000,900))
			for background_object in background_objects:
				obj_rect = pygame.Rect(background_object[1][0]+500-scroll[0]*background_object[0],background_object[1][1]+600-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
				if background_object[0] == 0.5:
					pygame.draw.rect(win,(14,222,150),obj_rect)
				else:
					pygame.draw.rect(win,(9,91,85),obj_rect)
			for background_object in background_objects:
				obj_rect = pygame.Rect(background_object[1][0]+900-scroll[0]*background_object[0],background_object[1][1]+600-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
				if background_object[0] == 0.5:
					pygame.draw.rect(win,(14,222,150),obj_rect)
				else:
					pygame.draw.rect(win,(9,91,85),obj_rect)
			for background_object in background_objects:
				obj_rect = pygame.Rect(background_object[1][0]-scroll[0]*background_object[0],background_object[1][1]+600-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
				if background_object[0] == 0.5:
					pygame.draw.rect(win,(14,222,150),obj_rect)
				else:
					pygame.draw.rect(win,(9,91,85),obj_rect)
			
			for i in self.level:
				x=2*self.width
				y+=self.width
				for j in i:
					if j=="0":
						x+=self.width
					if j=="1":
						self.block.append(Block(win,x,y,BLACK,self.width))
						x+=self.width
					if j=="2":
						self.arect.center=(x,y)
						win.blit(self.door,(self.arect.x-scroll[0],self.arect.y-scroll[1]))
						x+=self.width
						
					if j=="3":
						self.block.append(Block(win,x,y,CYAN,self.width))
						x+=self.width

	class Block(pygame.sprite.Sprite):
		tile=pygame.image.load("game assets/tiles.png").convert()
		tile2=pygame.image.load("game assets/tile2.png").convert_alpha()
		def __init__(self,win,x,y,color,width):
			super().__init__()
			self.x=x
			self.y=y
			self.width=width
			self.color=color
			self.rect=pygame.Rect((self.x,self.y,self.width,self.width))
			self.tile.set_colorkey((146,244,255))
			self.tile=pygame.transform.scale(self.tile,(self.width,self.width))
			self.tile2=pygame.transform.scale(self.tile2,(self.width,self.width))
			if self.color==(0,0,0):
				win.blit(self.tile,(self.rect.x-scroll[0],self.rect.y-scroll[1]))
			else:
				win.blit(self.tile2,(self.rect.x-scroll[0],self.rect.y-scroll[1]))
			


	def move(girl, movement):
		collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
		girl.rect.x += movement[0]
		hit_list = pygame.sprite.spritecollide(girl, group,False)
		for tile in hit_list:
			if movement[0] > 0:
				girl.rect.right = tile.rect.left
				collision_types['right'] = True
			elif movement[0] < 0:
				girl.rect.left = tile.rect.right
				collision_types['left'] = True
		girl.rect.y += movement[1]
		hit_list = pygame.sprite.spritecollide(girl, group,False)
		for tile in hit_list:
			if movement[1] > 0:
				girl.rect.bottom = tile.rect.top
				collision_types['bottom'] = True
			elif movement[1] < 0:
				girl.rect.top = tile.rect.bottom
				collision_types['top'] = True
		return girl.rect, collision_types

	def movement(girl):
		global air_timer,moving_left,moving_right,player_y_momentum
		player_movement = [0, 0]
		if moving_right:
			player_movement[0] += 10
		if moving_left:
			player_movement[0] -= 10
		player_movement[1] += player_y_momentum
		player_y_momentum += 3
		if player_y_momentum > 15:
			player_y_momentum = 15

		girl.rect, collisions = move(girl, player_movement)
		if collisions['bottom']:
			player_y_momentum = 0
			air_timer = 0
		else:
			air_timer += 1
		
		keys=pygame.key.get_pressed()
		if keys[K_RIGHT]:
			moving_right=True
		else:
			moving_right=False

		if keys[K_UP]:
			if air_timer < 6:
				player_y_momentum = -28

		if keys[K_LEFT]:
			moving_left=True
		else:
			moving_left=False


	def redrawwin():
		global srno
		win.fill((146,244,255))
		map.draw(win) 
		girl.draw(win)
		movement(girl)
		if girl.rect.colliderect(map.arect):
			font = pygame.font.SysFont(None, 50)
			img = font.render('YOU WON!! CONGRATZ', True, (0,0,0))
			rectangle=img.get_rect()
			rectangle.center=(500,450)
			win.blit(img, rectangle)
			pygame.display.update()
			pygame.time.delay(1000)
			srno+=1
			if srno<7:
				main(srno)
		pygame.display.update()

	global scroll,true_scroll,g,player_y_momentum,girl,map,moving_right,moving_left,air_timer
	g=[]
	background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,100,400]],[0.5,[300,80,120,400]]]
	scroll=[0,0]
	true_scroll=[0,0]
	
	map=Map("level"+str(sr))
	map.draw(win) 
	girl=Girl(200,800-20)
	for b in map.block:
		g.append(b)
	group=pygame.sprite.Group(g)
	player_y_momentum = 0
	moving_right = False
	moving_left = False
	air_timer = 0
	moving_right = False
	moving_left = False
	clock=pygame.time.Clock()
	while True:
		true_scroll[0]+=(girl.rect.x-true_scroll[0]-500)/20
		true_scroll[1]+=(girl.rect.y-true_scroll[1]-450)/20
		scroll=true_scroll.copy()
		scroll[0]=int(true_scroll[0])
		scroll[1]=int(true_scroll[1])
		
		clock.tick(50)
		redrawwin()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				quit()

def options():
	running = True
	while running:
		win.fill((0,0,0))

		draw_text('options', font, (255, 255, 255), win, 20, 20)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
		
		pygame.display.update()
		clock.tick(60)

def animate(itext):
	text = ''
	string=itext.split(" ")
	for i in range(len(string)):
		win.fill((255,255,255))
		text += string[i]+" "
		text_surface = font.render(text, True, (0,0,0))
		text_rect = text_surface.get_rect()
		text_rect.center = (W/2, H/2)
		win.blit(text_surface, text_rect)
		pygame.display.update()
		pygame.time.wait(1000)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False


def gameopening():
	animate("Get ready")
	animate("Go!!!")
	sr=1
	main(sr)
	
	
def redrawWin():
		win.blit(bg,(bgX,0))
		win.blit(bg,(bgX2,0))
		win.blit(img,button_1)
		win.blit(img2,button_2)
		win.blit(font.render("Adventure To Jungle", 0, (0, 176, 80)), (10, 60))
		pygame.display.update() 

pygame.init()
run=True
W,H = 900, 260
win = pygame.display.set_mode((W,H))
bg =pygame.image.load(os.path.join('game assets','background.jpg')).convert()
H=bg.get_height()
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('escape of adventurous girl')
font = pygame.font.SysFont(None, 40)
img = font.render("PLAY", True, (0,0,0))
img2= font.render("OPTIONS", True, (0,0,0))
button_1 = img.get_rect()
button_2 = img2.get_rect()
button_1.center=(W/2,300)
button_2.center=(W/2,400)

font=pygame.font.Font("Soul_Calibur.ttf",144)
bgX = 0
bgX2 = bg.get_width()

bgs=5
clock=pygame.time.Clock()
click = False
while run:
		redrawWin()
		bgX-=bgs
		bgX2-=bgs

		mx, my = pygame.mouse.get_pos()

		if button_1.collidepoint((mx, my)):
				if click:
						gameopening()
		if button_2.collidepoint((mx, my)):
				if click:
						options()
		

		if bgX < bg.get_width() * -1: 
				bgX = bg.get_width()
		
		if bgX2 < bg.get_width() * -1:
				bgX2 = bg.get_width()
		for event in pygame.event.get():
				if event.type==pygame.QUIT:
						pygame.quit()
						quit()
				if event.type == MOUSEBUTTONDOWN:
						if event.button == 1:
							click = True
		clock.tick(20)