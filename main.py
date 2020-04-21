import pygame
from network import network

sock = network()
sock.connect_to_server()

pygame.init()
clock = pygame.time.Clock()
size = (width, height) = (800, 450)
screen = pygame.display.set_mode(size)
done = False
player_pos = [int(width/2), int(height/2)]
background_pos = [0, 0]

#images
background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, (background.get_rect().size[0]*4, background.get_rect().size[1]*4))
player = {}
for direction in ['up', 'down', 'left', 'right']:
	player[direction] = {}
	player[direction]['stop'] = pygame.image.load('images/player-'+direction+'-stop.png')
	player[direction]['run'] = []
	for i in range(10):
		player[direction]['run'].append(pygame.image.load('images/player-'+direction+'-run1.png'))
	for i in range(10):
		player[direction]['run'].append(pygame.image.load('images/player-'+direction+'-run2.png'))

player_img = player['down']['stop']

speed = 2
animation_counter = 0
direction = 'down'

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				done = True
	keys = pygame.key.get_pressed()
	is_moving = False
	if keys[pygame.K_UP]:
		direction = 'up'
		is_moving = True
		if player_pos[1] != int(height/2) or background_pos[1] == 0:
			if player_pos[1] != 0:
				player_img = player['up']['run'][animation_counter]
				player_pos[1] -= speed
		else:
			player_img = player['up']['run'][animation_counter]
			background_pos[1] += speed
	if keys[pygame.K_DOWN]:
		direction = 'down'
		is_moving = True
		if player_pos[1] != int(height/2) or background_pos[1] == height-background.get_rect().size[1]:
			if player_pos[1] != height-50:
				player_img = player['down']['run'][animation_counter]
				player_pos[1] += speed
		else:
			player_img = player['down']['run'][animation_counter]
			background_pos[1] -= speed
	if keys[pygame.K_LEFT]:
		direction = 'left'
		is_moving = True
		if player_pos[0] != int(width/2) or background_pos[0] == 0:
			if player_pos[0] != 0:
				player_img = player['left']['run'][animation_counter]
				player_pos[0] -= speed
		else:
			player_img = player['left']['run'][animation_counter]
			background_pos[0] += speed
	if keys[pygame.K_RIGHT]:
		direction = 'right'
		is_moving = True
		if player_pos[0] != int(width/2) or background_pos[0] == width-background.get_rect().size[0]:
			if player_pos[0] != width-50:
				player_img = player['right']['run'][animation_counter]
				player_pos[0] += speed
		else:
			player_img = player['right']['run'][animation_counter]
			background_pos[0] -= speed

	if not is_moving:
		player_img = player[direction]['stop']

	screen.fill((255,255,255))

	screen.blit(background, background_pos)
	screen.blit(player_img, player_pos)

	pygame.display.flip()
	animation_counter += 1
	if animation_counter == 20:
		animation_counter = 0
	clock.tick(60)