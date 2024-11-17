#This is a simple Particle Simulation with 3 balls jumping around in a window. Plz check that you have pygame installed on your system.

# all the necessary imports 
import pygame
import random
from math import *
from Particle_Class import ParticleRound


#init pygame to work
pygame.init()
#Creating the screen
Screen_Height = 600
Screen_Width = 800
Screen = pygame.display.set_mode((Screen_Width,Screen_Height))




#Class for the Round Particles
class ParticleRound():
    def __init__(self, radius, colour, speed_x, speed_y, position_x, postition_y):
        self.radius = radius
        self.colour = colour
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.position_x = position_x
        self.position_y = postition_y

    def draw_to_screen(self, Screen):
        pygame.draw.circle(Screen, self.colour, (self.position_x, self.position_y), self.radius)

    def movement(self, border_right, border_down):
        #overall movement on the axes
        self.position_x += self.speed_x
        self.position_y += self.speed_y

        #movement collision with the borders
        if self.position_x <= 0 or self.position_x + self.radius >= border_right:
            self.speed_x *= -1
        if self.position_y <= 0 or self.position_y + self.radius >= border_down:
            self.speed_y *= -1




#Here we create some balls 
kreis = ParticleRound(20, (255,0,0), 0.1, 0.1, 50, 50)
kreis2 = ParticleRound(10,(0,0,250), -0.2, 0.3, 700, 50)
kreis3 = ParticleRound(10,(0,0,255),-0.3,0.1, 750, 550)



#The loop for the game
run = True
while run == True:
    #make the screen black so its a fresh canvas
    Screen.fill((0,0,0))
    #looking for all events and if the x is clicked exit the simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #draw the balls to the screen
    kreis.draw_to_screen(Screen)
    kreis2.draw_to_screen(Screen)
    kreis3.draw_to_screen(Screen)

    #make the balls move inside the borders
    kreis.movement(Screen_Width,Screen_Height)
    kreis2.movement(Screen_Width,Screen_Height)
    kreis3.movement(Screen_Width,Screen_Height)

    pygame.display.update()

pygame.quit
