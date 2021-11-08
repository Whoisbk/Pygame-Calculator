import pygame 
import os
from pygame import mixer
pygame.mixer.init()

#button class
class Button():
	#COLORS
	click_sfx = pygame.mixer.Sound(os.path.join("Assets","click.mp3"))
	click_sfx.set_volume(0.2)
	button_color = (0,0,0)
	hover_color = (255,255,255)
	click_color = (255,255,255)
	text_color = (255,255,255)
	def __init__(self, surface, x, y,text,font):
		self.x = x
		self.y = y
		self.clicked = False
		self.surface = surface
		self.width = 60
		self.height = 70
		self.text = text
		self.font = font

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()
		#button rect
		button_rect = pygame.Rect(self.x,self.y ,self.width,self.height)

		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			#Hover Effect
			pygame.draw.rect(self.surface,self.hover_color,button_rect,5)
			#if button is clicked draw an outline on the button
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True
				self.click_sfx.play()
				pygame.draw.rect(self.surface,self.click_color,button_rect,5)
			elif pygame.mouse.get_pressed()[0] == 0:
					self.clicked = False
		#DRAW buttons
		pygame.draw.rect(self.surface,self.button_color,button_rect)
		
		#draw text
		txt = self.font.render(self.text,True,self.text_color)
		self.surface.blit(txt,(self.x + (self.width//2 - txt.get_width()//2),(self.y + (self.height/2- txt.get_height()//2))))

		return action