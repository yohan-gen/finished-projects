import pygame
import math, sys, os

pygame.init()

tela = pygame.display.set_mode((1450, 750))             #tamanho da tela
pygame.display.set_caption("teste de pygame no python")  #texto do jogo


chbase = os.path.dirname(__file__)
chpath = os.path.join(chbase, "choosescreen.png")
chosescreen = pygame.image.load(chpath)                 # tela inicial
chosescreen = pygame.transform.scale(chosescreen, (1450, 750))
botao = pygame.Rect(577, 110, 385, 125)                     #botao de ir para escolha de personagem


strtbase = os.path.dirname(__file__)
strtpath = os.path.join(strtbase, "startscreen.png")
startscreen = pygame.image.load(strtpath)               #escolher personagem
startscreen = pygame.transform.scale(startscreen, (1450, 750))
startbutton = pygame.Rect(510, 30, 408, 118)
startsurface = pygame.Surface((408, 118), pygame.SRCALPHA)
startsurface.fill((0, 0, 0, 105))                       #botao de ready transparencia

picbase = os.path.dirname(__file__)
picpath = os.path.join(picbase, "lima.png")     # lima
pic = pygame.image.load(picpath)
pic = pygame.transform.scale(pic, (170, 87))
limabutton = pygame.Rect(352, 613, 311, 90)     #botao de escolher lima

luisbase = os.path.dirname(__file__)
luispath = os.path.join(luisbase, "luis.png")
luis = pygame.image.load(luispath)              # luis
luispic = pygame.transform.scale(luis, (150, 100)) 
luisbutton = pygame.Rect(766, 613, 311, 90)     #botao de escolher luis

enemybase = os.path.dirname(__file__)
enemypath = os.path.join(enemybase, "scp.png")      #scp
enemypic = pygame.image.load(enemypath)
enemypic = pygame.transform.scale(enemypic, (180, 120))

scpbase = os.path.dirname(__file__)
scppath = os.path.join(scpbase, "scproom.png")
scproom = pygame.image.load(scppath)                #sala scp
scproom = pygame.transform.scale(scproom, (1450, 750))

clock = pygame.time.Clock()


teclas = pygame.key.get_pressed()

lima, luis = False, False
monster = False
char = False
character = False
choose = True                           #outras coisas sla oq sla isso
x, y = 50, 50
rodando = True
luissurface = pygame.Surface((311, 90), pygame.SRCALPHA)
luissurface.fill((10, 10, 10, 135))
    
limasurface = pygame.Surface((311, 90), pygame.SRCALPHA)
limasurface.fill((20, 20, 20, 135))

xg, yg = 165, 605
xl, yl = 1200, 605
x, y = 615, 120

startvidaG = 170            #alguns outros valores
startvidaL = 150
hitCD = 500
lasthitL = 0                
lasthitG = 0

players = []
while rodando : 

    clock.tick(45)
    mousepos = pygame.mouse.get_pos()           #sempre pega a posição do mouse
    teclas = pygame.key.get_pressed()           
    
    
    for event in pygame.event.get() :

        if event.type == pygame.QUIT :
            rodando = False

        
        if event.type == pygame.MOUSEBUTTONDOWN :       # se clicar choose vai para escolha de personagem
            if botao.collidepoint(mousepos) :
                choose = False
                character = True

            if character :
                if limabutton.collidepoint(mousepos) :
                    lima = True  # clica botao escolha personagem
                    char = True
                if luisbutton.collidepoint(mousepos) :
                    luis = True
                    char = True


            if char and startbutton.collidepoint(mousepos) : # se clicar ele inicia o jogo
                character = False
                monster = True

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] :
        yg -= 8
    if teclas[pygame.K_a] :
        xg -= 8                     #teclas do lima
    if teclas[pygame.K_s] :
        yg += 8
    if teclas[pygame.K_d] :
        xg += 8
                                    
    if teclas[pygame.K_UP] :
        yl -= 6                         #teclas do luis
    if teclas[pygame.K_LEFT] :
        xl -= 6
    if teclas[pygame.K_DOWN] :
        yl += 6
    if teclas[pygame.K_RIGHT] :
        xl += 6

    monspeed = 9

    Pluis = pygame.Rect(xl, yl, 150, 100)           #quadrado do luis para calcular se encostou no monstro
    Pgab = pygame.Rect(xg, yg, 170, 87)             #quadrado do lima para calcular se encostou no monstro
    evil = pygame.Rect(x, y, 180, 120)                 #quadrado do monstro

        
    if choose :
        tela.blit(chosescreen, (0, 0)) # se nao clicar pra escolher personagem, ficara na imagem inicial
        
    else :
        tela.blit(startscreen, (0,0))
        if startbutton.collidepoint(mousepos) :
            tela.blit(startsurface, (510, 30))    # se clicar vai pra escolha de personagem

    if luis :
        tela.blit(luissurface, (766, 613))
    if lima :
        tela.blit(limasurface, (352, 613))      #se for escolhido o personagem do lima ou luis, botao respectivo de escolher ficara meio cinza
    
    if character == False and char == True:
        tela.blit(scproom, (0,0))           #assim que clicar ready, jogo inicia, mas apenas se personagem ja tiver sido escolhido


    if lima == True and character == False : # se lima for escolhido e clicado ready = inicia jogo com lima
        tela.blit(pic, (xg, yg))
        pygame.draw.rect(tela, (255,0,0), (xg,yg,startvidaG,20))

    if luis == True and character == False : # se luis for escolhido e clicado ready = inicia jogo com luis
        tela.blit(luispic, (xl, yl))         # se os dois forem escolhidos, inicia jogo com os dois
        pygame.draw.rect(tela, (255,0,0), (xl,yl,startvidaL,20))

    if (lima or luis) and monster  :        # se either luis or lima forem escolhidos e clicado ready = monstro aparece
        tela.blit(enemypic, (x, y))

        alvos = []
        if luis :
            alvos.append((xl, yl))
        if lima :
            alvos.append((xg, yg))                      # se luis ou lima estiverem no jogo : os considera alvo do monstro
        
        if len(alvos) > 0 :
            alvo = min(alvos, key=lambda pos:(pos[0]-x)**2 + (pos[1] - y)**2)       # se distancia do(s) alvos for maior que 0, calcula qual personagem esta mais perto
            huntx, hunty = alvo                                                      

        dx, dy = huntx - x, hunty - y
        dist = math.sqrt(dx**2 + dy**2)         #ultilizando matematica(teorema de pitagoras para calcular a posição)
        if dist != 0:                           #sempre calcula a distancia do lima/luis em relação ao monstro
            xm = dx / monspeed
            ym = dy / monspeed
        if dist != 0:
            dx /= dist
            dy /= dist
            x += dx * monspeed
            y += dy * monspeed

    Lcurrenthit = pygame.time.get_ticks()
    Gcurrenthit = pygame.time.get_ticks()


    if evil.colliderect(Pluis) :
        x -= dx * monspeed
        y -= dy * monspeed
        if Lcurrenthit - lasthitL > hitCD :   #se luis encostar no bixo perde 15 de vida a cada 500 MS
            startvidaL -= 15                #se vida de luis chegar a 0 ele morre/desaparece
            lasthitL = Lcurrenthit

    if startvidaL <= 0 :
        luis = False   
        if lima == False :
            rodando = False
            
    if evil.colliderect(Pgab) :
        x -= dx * monspeed
        y -= dy * monspeed     
        if Gcurrenthit - lasthitG > hitCD :   #se lima encostar no bixo perde 20 de vida a cada 500 MS
            startvidaG -= 20                #se vida de lima chegar a 0 lima morre/desaparece
            lasthitG = Gcurrenthit  
    if startvidaG <= 0 :
        lima = False 
        if luis == False :
            rodando = False

                                                                                                                                                                                                                        

    pygame.display.flip()
        
pygame.quit()
sys.exit()

# 200+ LINHAS DE CODIGOO!!!!1!!1!1!