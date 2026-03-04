import pygame
import sys
import os

pygame.init()

tela = pygame.display.set_mode((1450, 750))
pygame.display.set_caption("teste de pygame no python!")

font = pygame.font.SysFont("8-Bit-Madness", 50)
text = font.render("jogo 100% peak", True, (0, 0, 255))
text1 = font.render("tenho potencial pra ser dev?", True, (255, 0, 0))
text2 = font.render("jogo = bom", True, (255, 0, 0))
text3 = font.render("fps = 480", True, (255, 0, 0))
text4 = font.render("graficos = ultra realista", True, (255, 0, 0))
text5 = font.render("Hackers = False", True, (255, 0, 0))
text6 = font.render("Femboys = True", True, (255, 0, 0))

picbase = os.path.dirname(__file__)
picpath = os.path.join(picbase, "luispic.png")
pic = pygame.image.load(picpath)
pic = pygame.transform.scale(pic, (300, 400))
botao = pygame.Rect(400, 100, 200, 200)

textoshow = False
startime = 0

rodando = True
while rodando :
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            rodando = False
    
        if event.type == pygame.MOUSEBUTTONDOWN :
            if botao.collidepoint(mousepos) :
                textoshow = True
                startime = pygame.time.get_ticks()

    tela.fill((0, 200, 60))       
    pygame.draw.rect(tela, (0, 0, 0), botao) 
    tela.blit(text, (400, 50)) 

    if textoshow :
        rntime = pygame.time.get_ticks()
        if rntime - startime > 15000 :
            textoshow = False

    if textoshow :
        tela.blit(text1, (200, 200))
        tela.blit(text2, (200, 250))
        tela.blit(text3, (200, 300))
        tela.blit(text4, (200, 350))
        tela.blit(text5, (200, 400))
        tela.blit(text6, (200, 450))
        tela.blit(pic, (700, 100))


    pygame.display.flip()
    
pygame.quit()
sys.exit()