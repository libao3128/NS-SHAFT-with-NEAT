import pygame
import random

max_floor=0
wall=pygame.image.load('./assets/wall.png')
ceiling=pygame.image.load('./assets/ceiling.png')
normal=pygame.image.load('./assets/normal.png')
nail=pygame.image.load('./assets/nails.png')

conveyor_left=[]
conveyor_left.append(pygame.image.load('./assets/conveyor_left1.png'))
conveyor_left.append(pygame.image.load('./assets/conveyor_left2.png'))
conveyor_left.append(pygame.image.load('./assets/conveyor_left3.png'))
conveyor_left.append(pygame.image.load('./assets/conveyor_left4.png'))

conveyor_right=[]
conveyor_right.append(pygame.image.load('./assets/conveyor_right1.png'))
conveyor_right.append(pygame.image.load('./assets/conveyor_right2.png'))
conveyor_right.append(pygame.image.load('./assets/conveyor_right3.png'))
conveyor_right.append(pygame.image.load('./assets/conveyor_right4.png'))

trampoline=[]
trampoline.append(pygame.image.load('./assets/trampoline1.png'))
trampoline.append(pygame.image.load('./assets/trampoline2.png'))
trampoline.append(pygame.image.load('./assets/trampoline3.png'))
trampoline.append(pygame.image.load('./assets/trampoline4.png'))
trampoline.append(pygame.image.load('./assets/trampoline5.png'))
trampoline.append(pygame.image.load('./assets/trampoline6.png'))

fake=[]
fake.append(pygame.image.load('./assets/fake1.png'))
fake.append(pygame.image.load('./assets/fake2.png'))
fake.append(pygame.image.load('./assets/fake3.png'))
fake.append(pygame.image.load('./assets/fake4.png'))
fake.append(pygame.image.load('./assets/fake5.png'))
fake.append(pygame.image.load('./assets/fake6.png'))

player={'normal':[],'dead':[]}
player['normal'].append(pygame.image.load('./assets/player_normal.png'))
player['dead'].append(pygame.image.load('./assets/player_dead.png'))

Type={'nor':0,'nail':1,'left':2,'right':3,'tram':4,'Fake':5}

def buildground(floor=0,player=0):
    pygame.init()
    
    window_surface = pygame.display.set_mode((800, 600))
    window_surface.fill((0, 0, 0))
    
    global wall
    global ceiling
    global max_floor

    wall.convert()
    window_surface.blit(wall,(190,10))
    window_surface.blit(wall,(190,400))
    window_surface.blit(wall,(605,10))
    window_surface.blit(wall,(605,400))

    fontObj =pygame.font.SysFont('SimHei',35)
    text = fontObj.render('Floor: '+str(floor), True, (255 ,193, 37))
    window_surface.blit(text, (0, 0))
    text = fontObj.render('Player: '+str(player), True, (255 ,193, 37))
    window_surface.blit(text, (0, 25))
    text = fontObj.render('MaxFloor: '+str(max_floor), True, (255 ,193, 37))
    window_surface.blit(text, (0, 50))

    ceiling.convert()
    
    window_surface.blit(ceiling,(205,10))
    
    return window_surface
class Normal:
    def __init__(self, ground):
        global normal
        self.ground=ground
        self.type='nor'

        self.platform=normal
        self.x=random.randint(220,500)
        self.y=600
        self.Generate()
        
    def Generate(self):
        self.platform.convert()
        self.ground.blit(self.platform,(self.x,self.y))
    def Update(self,Player):
        self.y=self.y-1
        if self.y<30:
            return False
        self.ground.blit(self.platform,  (self.x,self.y))
        return True
class Nail:
    def __init__(self, ground):
        global normal
        self.ground=ground
        self.type='nail'

        self.platform=nail
        self.x=random.randint(220,500)
        self.y=600
        self.Generate()
        
    def Generate(self):
        self.platform.convert()
        self.ground.blit(self.platform,(self.x,self.y))
    def Update(self,Player):
        self.y=self.y-1
        if self.y<30:
            return False
        self.ground.blit(self.platform,  (self.x,self.y))
        return True
class Conveyor_left:
    def __init__(self, ground):
        global normal
        self.ground=ground
        self.type='left'

        self.platform=conveyor_left
        self.cnt=0
        self.x=random.randint(220,500)
        self.y=600
        self.Generate()
        
    def Generate(self):
        for i in self.platform:
            i.convert()
        self.ground.blit(self.platform[3],(self.x,self.y))
    def Update(self,Player):
        self.y=self.y-1
        if self.y<30:
            return False
        self.ground.blit(self.platform[int(self.cnt)],  (self.x,self.y))
        self.cnt-=0.25
        if(self.cnt<0):
            self.cnt=len(self.platform)-1
        return True

class Conveyor_right:
    def __init__(self, ground):
        global normal
        self.ground=ground
        self.type='right'

        self.platform=conveyor_right
        self.cnt=0
        self.x=random.randint(220,500)
        self.y=600
        self.Generate()
        
    def Generate(self):
        for i in self.platform:
            i.convert()
        self.ground.blit(self.platform[3],(self.x,self.y))
    def Update(self,Player):
        self.y=self.y-1
        if self.y<30:
            return False
        self.ground.blit(self.platform[int(self.cnt)],  (self.x,self.y))
        self.cnt-=0.25
        if(self.cnt<0):
            self.cnt=len(self.platform)-1
        return True

class Trampoline:
    def __init__(self, ground):
        global normal
        self.ground=ground
        self.type='tram'

        self.platform=trampoline
        self.cnt=0
        self.x=random.randint(220,500)
        self.y=600
        self.Generate()
        
    def Generate(self):
        for i in self.platform:
            i.convert()
        self.ground.blit(self.platform[3],(self.x,self.y))
    def Update(self,Player):
        self.y=self.y-1
        if self.y<30:
            return False
        self.ground.blit(self.platform[0],  (self.x,self.y))
        
      
        return True

class Fake:
    def __init__(self, ground):
       
        self.ground=ground
        self.type='Fake'

        self.platform=fake
        self.state=0
        self.turn=False
        self.cnt=0
        self.x=random.randint(220,500)
        self.y=600
        self.Generate()
        
    def Generate(self):
        for i in self.platform:
            i.convert()
        self.ground.blit(self.platform[3],(self.x,self.y))
    def Update(self,player):
        for P in player:
             if self.y-30>=P.y and self.y-35<=P.y and self.x-20<=P.x and self.x+100>=P.x:
                 self.turn=True
        self.y=self.y-1
        if self.y<30:
            return False
        if self.turn:
            self.ground.blit(self.platform[int(self.state/8)],  (self.x,self.y))
            self.state+=1
            if self.state>=len(self.platform)*8:
                self.state=0
                self.turn=False
        else :
            self.ground.blit(self.platform[0],  (self.x,self.y))
        
      
        return True


class Player:
    def __init__(self, ground):
        
        self.ground=ground
        

        self.state=player
        self.cnt=0
        self.x=400
        self.y=30
        self.speed=2
        self.Generate()
        self.life=10
        self.on_platform=False
        self.plat_form=None

        self.closeY=0
        self.closeXL=0
        self.closeXR=0
        self.closeTp=-1
        self.IsTram=False
        self.IsNail=False
        self.IsLR=0
        self.IsFake=False


        self.secondY=0
        self.secondXL=0
        self.secondXR=0
        self.secondTp=-1


    def Generate(self):
        
        self.ground.blit(self.state['normal'][0],(self.x,self.y))

    def ClosestPlatform(self,item):
        have_play_form=False
        for x,i in enumerate(item):
            if i.y-25>self.y:
                self.closeY=i.y
                self.closeXL=i.x-20
                self.closeXR=i.x+85
                self.closeTp=Type[i.type]
                if i.type=='Fake':
                    self.IsFake=True
                else:
                    self.IsFake=False
                if i.type=='tram':
                    self.IsTram=True
                else:
                    self.IsTram=False
                if i.type=='nail':
                    self.IsNail=True
                else:
                    self.IsNail=False
                if i.type=='right':
                    self.IsLR=1
                elif i.type=='left':
                    self.IsLR=-1
                else:
                    self.IsLR=0
                have_play_form=True
                if x+1<len(item):
                    self.secondY=item[x+1].y
                    self.secondXL=item[x+1].x-20
                    self.secondXR=item[x+1].x+85
                    self.secondTp=Type[item[x+1].type]
                else:
                    self.secondY=0
                    self.secondXL=0
                    self.secondXR=0
                    self.secondTp=-1
                break
        if not have_play_form:
            self.closeY=0
            self.closeXL=0
            self.closeXR=0
            self.closeTp=-1
    def Update(self,item,keys):
        fit=0
        if(self.y>=600):
                return False,fit
        if(self.life<=0):
            self.y=self.y+5
            self.ground.blit(self.state['dead'][0],  (self.x,self.y))
            
            return True,fit

        if(keys=='R'):
            self.x=self.x+1.5
            
        if(keys=='L'):
            self.x=self.x-1.5

        if(self.x<205):
            self.x=205
        if(self.x>570):
            self.x=570
       
        plat_form=False
        for i in item:
            if i.y-30>=self.y and i.y-35<=self.y and i.x-23<=self.x and i.x+85>=self.x:
                if i.type=='Fake' and i.state>=6 :
                    if i.turn:
                        continue
                if(self.on_platform==False and self.plat_form!=i):
                   
                    if(i.type=='nail'):
                        self.life-=4
                        fit-=3
                        self.plat_form=i
                    elif i.type!='tram' :
                        self.life=self.life+1
                        self.plat_form=i
                        
                    if(self.life>10):
                        self.life=10
                plat_form=True
                self.speed=0
                self.y=i.y-35
                if(i.type=='left'):
                    self.x=self.x-1
                if(i.type=='right'):
                    self.x=self.x+1
                if(i.type=='tram'):
                    self.speed=-5
                
        
        self.on_platform=plat_form
        
        if(self.speed<=2 and not self.on_platform):
            self.speed=self.speed+0.15
        self.y=self.y+self.speed
        if self.y<30:
            self.y=self.y+20
            self.speed=1
            self.life-=4
            fit-=3
        for i in range(self.life):
            if self.life>6:
                color=(0,255,0)
            elif self.life>3:
                color=(255, 255, 0)
            else:
                color=(	255, 0 ,0)
        
            pygame.draw.rect(self.ground,color,[self.x-4+i*4,self.y-10,2,5],1)
        self.ClosestPlatform(item)
        self.ground.blit(self.state['normal'][0],  (self.x,self.y))
        pygame.draw.circle(self.ground,(255, 255, 0),((self.closeXL+self.closeXR)/2,self.closeY),20,0)
        
      
        return True,fit
