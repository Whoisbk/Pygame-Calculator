import pygame
import os
import button
import math
pygame.init()
pygame.font.init() 
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
WIN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Calculator")
FPS = 60

#COLORS
WHITE =(255,255,255)
BLACK = (0,0,0)
GRAY =(120,120,120)

width = 60
height = 60

#FONT
font_display = pygame.font.SysFont("Times New Roman",40)
font_buttons = pygame.font.SysFont("Times New Roman",30)

def draw_win():
    WIN.fill(GRAY)
    pygame.draw.line(WIN,BLACK,(0,90),(SCREEN_WIDTH,90),4)

#CALCULATE FACTORIAL
def get_factorial(num):  
    fact = 1
    for i in range(1,num+1):
        fact = fact *i

    return fact
#CALCULATE SQUAR ROOT
def get_sqrt(num):  
    num_sqrt = math.sqrt(num)
    return num_sqrt
    
#BUTTON INSTANCES
#NUMBERS
btn_0 = button.Button(WIN,50,200,"0",font_buttons)
btn_1 = button.Button(WIN,120,200,"1",font_buttons)
btn_2 = button.Button(WIN,190,200,"2",font_buttons)
btn_3 = button.Button(WIN,260,200,"3",font_buttons)
btn_4 = button.Button(WIN,330,200,"4",font_buttons)
btn_5 = button.Button(WIN,50,300,"5",font_buttons)
btn_6 = button.Button(WIN,120,300,"6",font_buttons)
btn_7 = button.Button(WIN,190,300,"7",font_buttons)
btn_8 = button.Button(WIN,260,300,"8",font_buttons)
btn_9 = button.Button(WIN,330,300,"9",font_buttons)
#SYMBOLS
btn_fact = button.Button(WIN,50,100,"Fact",font_buttons)
btn_sqrt = button.Button(WIN,120,100,"Sqrt",font_buttons)
btn_pow = button.Button(WIN,190,100,"Pow",font_buttons)
btn_diff = button.Button(WIN,430,200,"-",font_buttons)
btn_plus = button.Button(WIN,430,300,"+",font_buttons)
btn_equal = button.Button(WIN,430,400,"=",font_buttons)
btn_div = button.Button(WIN,330,400,"/",font_buttons)
btn_multi = button.Button(WIN,260,400,"X",font_buttons)
btn_close_bracket = button.Button(WIN,190,400,")",font_buttons)
btn_open_bracket = button.Button(WIN,120,400,"(",font_buttons)
btn_clear = button.Button(WIN,50,400,"C",font_buttons)

py_input = ""
py_sum = 0


#MAIN GAME LOOP
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)
    #TRY AND EXCEPT THAT LOOKS FOR SYNTAX ERROS
    try:
        draw_win()
        #BUTTON FUCTIONALITY
        if btn_fact.draw():
            py_sum = (get_factorial(int(py_input)))
        if btn_sqrt.draw():
            py_sum = (get_sqrt(int(py_input)))
        if btn_0.draw():
            py_input += "0"
        if btn_1.draw():
            py_input += "1"
        if btn_2.draw():
            py_input += "2"
        if btn_3.draw():
            py_input += "3"
        if btn_4.draw():
            py_input += "4"
        if btn_5.draw():
            py_input += "5"
        if btn_6.draw():
            py_input += "6"
        if btn_7.draw():
            py_input += "7"
        if btn_8.draw():
            py_input += "8"
        if btn_9.draw():
            py_input += "9"
        if btn_plus.draw():
            py_input += "+"
        if btn_diff.draw():
            py_input += "-"
        if btn_multi.draw():
            py_input += "*"
        if btn_div.draw():
            py_input += "/"
        if btn_pow.draw():
            py_input += "**"
        if btn_close_bracket.draw():
            py_input += ")"
        if btn_open_bracket.draw():
            py_input += "("
        if btn_equal.draw():
            py_sum = eval(py_input)
        #CLEARS INPUT 
        if btn_clear.draw():
            py_input =""
            py_sum = 0
        #DRAW TEXT SCREEN
        txt_input = font_display.render(f'{py_input}',True,WHITE)
        txt_sum = font_display.render(f'= {py_sum}',True,WHITE)
        WIN.blit(txt_input,(1,10))
        WIN.blit(txt_sum,(1,40))
    #Handle Errors
    except SyntaxError:
        py_sum = "Error"
    except ValueError:
        py_sum = "Invalid input"

    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
