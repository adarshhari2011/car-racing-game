import pygame
import random

pygame.init()
car=pygame.image.load("image/RED_CAR.png")
tree=pygame.image.load("image/tree.png")
font_score=pygame.font.Font("fonts/Montserrat-VariableFont_wght.ttf",20 )
font_score.set_bold(True)
# font_score.set_italic(True)
tree = pygame.transform.scale(tree , ( 50 , 50))
player_car = pygame.transform.scale(car , ( 40 , 80))
enemy_car1 = pygame.image.load("image/ORANGE_CAR.png")
orange_car = pygame.transform.scale(enemy_car1 , ( 40 , 80))
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Player():
    def __init__(self):
        self.x = 620
        self.score = 0
        self.y = 620
        self.width = 25
        self.height = 50
        self.speed = 4
        self.color 
        self.alive = True 

class Enemy():
    def __init__(self):
        self.x = random.randint(420,825)
        self.y = random.randint(100,150)
        self.width = 25
        self.height = 50
        self.speed = 4
        self.color = "grey"
        self.image_color = random.choice(['orange'])
    def movement(self, *otherEnemy):
        self.y += self.speed
        if self.y >= 720:
            self.y = random.randint(-150 , 0)
            self.x = random.randint(420,825)
            self.color = "grey"
        
            for other in otherEnemy : 
                if abs( self.y - other.y ) < 50 and abs( self.x - other.x )  < 50  :
                    self.y = random.randint(-150 , 0)
                    self.x = random.randint(420,825)
                    continue
                else:
                    return
    def collision(self,Player):
            if ( self.x + self.width > Player.x and self.x < Player.x + Player.width ):
                if ( self.y + self.height > Player.y ) :
                    print("CAR CRASHED GAME END") 
                    self.y = 700
                    Player.alive = "false"
    def image_finder(self):
        if self.image_color == 'orange':
            screen.blit(orange_car , (self.x , self.y))

class Tree():
    def __init__(self):
        self.side = "left"
        self.x = random.randint(0,420) 
        self.y = random.randint(100,150)
        self.width = 50
        self.height = 50

        self.speed = 2
        self.color = "lightgreen"
    def move(self):
        self.y += self.speed
        if self.y >= 720:
            self.y = random.randint(-150 , 0)
            self.side = random.choice(["right" , "left"])
            self.random_amount=random.choice([50,-50])
            if ( self.side == "left") : 
                self.random_amount=random.choice([55,-55])
                self.x = (random.randint(0,360)+self.random_amount)
            else : 
                self.random_amount=random.choice([55,-55])
                self.x = (random.randint(820,1280)+self.random_amount)
    def image(self):
        screen.blit(tree ,[self.x , self.y] )
car = Player()
tree1 = Tree()
tree2 = Tree()
tree3 = Tree()
tree4 = Tree()
tree5 = Tree()
enemy_1 = Enemy()
enemy_2 = Enemy()
enemy_3 = Enemy()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("grey")
    enemy_1.collision(car)
    enemy_2.collision(car)
    enemy_3.collision(car)

    pygame.draw.rect(screen , car.color , [car.x , car.y , car.width , car.height])
    screen.blit(player_car , (car.x , car.y))
    pygame.draw.rect(screen , enemy_1.color , [enemy_1.x , enemy_1.y , enemy_1.width , enemy_1.height])
    pygame.draw.rect(screen , enemy_2.color , [enemy_2.x , enemy_2.y , enemy_2.width , enemy_2.height])
    pygame.draw.rect(screen , enemy_3.color , [enemy_3.x , enemy_3.y , enemy_3.width , enemy_3.height])
    print(car.score)
    car.score +=1
    carscore = car.score
    car_str=str(carscore)
    text_surface = font_score.render(car_str , True , "black")

    enemy_1.image_finder()
    enemy_2.image_finder()
    enemy_3.image_finder()
    
    pygame.draw.rect(screen, 'lightgreen',[0,0,420,1000])
    pygame.draw.rect(screen, 'lightgreen',[850,0,1000,1000])

    pygame.draw.rect(screen , tree1.color , [tree1.x , tree1.y , tree1.width , tree1.height])
    tree1.move()
    screen.blit(tree ,[tree1.x , tree1.y , tree1.width , tree1.height] )
    tree1.image()
    pygame.draw.rect(screen , tree2.color , [tree2.x , tree2.y , tree2.width , tree2.height])
    tree2.move()
    screen.blit(tree ,[tree2.x , tree2.y , tree2.width , tree2.height] )
    tree2.image()
    pygame.draw.rect(screen , tree3.color , [tree3.x , tree3.y , tree3.width , tree3.height])
    tree3.move()
    screen.blit(tree ,[tree3.x , tree3.y , tree3.width , tree3.height] )
    tree3.image()
    pygame.draw.rect(screen , tree4.color , [tree4.x , tree4.y , tree4.width , tree4.height])
    tree4.move()
    screen.blit(tree ,[tree4.x , tree4.y , tree4.width , tree4.height] )
    tree4.image()
    pygame.draw.rect(screen , tree5.color , [tree5.x , tree5.y , tree5.width , tree5.height])
    tree5.move()
    screen.blit(tree ,[tree5.x , tree5.y , tree5.width , tree5.height] )
    tree5.image()
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and car.x >420:
        car.x -=  car.speed
    if keys[pygame.K_d] and car.x < 824:
        car.x +=  car.speed

    if car.alive == True : 
        enemy_1.movement(enemy_2,enemy_3)
        enemy_2.movement(enemy_1,enemy_3)
        enemy_3.movement(enemy_1 , enemy_2)
    elif car.alive == "false":
        break
    screen.blit(text_surface , [100,100,500,100])


    pygame.display.flip()

    clock.tick(120)

pygame.quit()