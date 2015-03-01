import pygame

pygame.init()

Display_width = 800
Display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((Display_width,Display_height))
pygame.display.set_caption('Hero')
clock = pygame.time.Clock()

heroImg = pygame.image.load('em_hero.png')
heroImg = pygame.transform.scale(heroImg, (66,77))

def hero(x,y):
    gameDisplay.blit(heroImg,(x,y))
    


def game_loop():

    x = (Display_width * 0.2)
    y = (Display_height * 0.2)

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

            if x > Display_width or x < 0:
                gameExit = True
            elif y > Display_height or y < 0:
                gameExit = True


        x += x_change
        y += y_change
        
        gameDisplay.fill(white)
        hero(x,y)

  

        pygame.display.flip()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

    
    
    




