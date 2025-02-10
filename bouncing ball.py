import pygame


pygame.init()


screen_width = 800
screen_height = 600


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Basics")

background_color = 'mintcream'

running = True
circ_x,circ_y=450,500

circx,circy=45,50

speed_x,speed_y=4,4

speedx,speedy=4.5,4.5


radius=15

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    circ_x -= speed_x
    circ_y -= speed_y

    if circ_x + radius >screen_width or circ_x - radius <0:
        speed_x =- speed_x

    if circ_y + radius >screen_height or circ_y - radius <0:
        speed_y =- speed_y



    circx -= speedx
    circy -= speedy

    if circx + radius > screen_width or circx - radius < 0:
        speedx = - speedx

    if circy + radius > screen_height or circy - radius < 0:
        speedy = - speedy

        
    screen.fill(background_color)

    pygame.draw.circle(screen,'steelblue4',(circ_x,circ_y),15)
    pygame.draw.circle(screen,'forestgreen',(circx,circy),15)


    pygame.display.flip()
    pygame.time.delay(10)
