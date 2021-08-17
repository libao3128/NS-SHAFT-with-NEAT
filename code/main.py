import pygame
from pygame.locals import QUIT
import sys
import random
import time
import neat
import os
import visualize
import GameObject as Ob
import pickle
import numpy as np

node_name={0:'GoRight',1:'GoLeft',
               -1:'x',-2:'y',-3:'on_platform',-4:'life',-5:'closeXL',
               -6:'closeXR',-7:'closeY',-8:'ToRight',-9:'ToLeft',
               -10:'IsTram',-11:'IsNail',-12:'IsLR'}


def play():
    
    ground=Ob.buildground()

    running=True
    clock = pygame.time.Clock()
    cur_time=85
    last_time=0
    item=[]
    second=0
    floor=0
    

    nets=[]
    ge=[]
    Children=[]
    

    tot_num=len(Children)
    while running  :
        clock.tick(100)   
    
        for event in pygame.event.get():
            second+=1
            cur_time+=1
            if(second>250):
                second=0
                floor+=1

                

            keys=pygame.key.get_pressed()
            if event.type == QUIT:
                running = False
        

            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                        Children.append(Ob.Player(ground))
           
            #item,ground=Update_plateform(item,ground)
            ground=Ob.buildground(floor,len(Children))
           
            
                                                
                
                
                #if x==0:
                #    PrintP1State(P,ground)
            for P in Children:
                    if keys[pygame.K_LEFT]:
                        if not P.Update(item,'L'):
                            Children.remove( P)
                    elif  keys[pygame.K_RIGHT]:
                        if not P.Update(item,'R'):
                             Children.remove( P)
                    else:
                        if not P.Update(item,'N'):
                    
                            Children.remove( P)

            if(cur_time>85 ):
           
                
           
                rand=random.random()
                rand*=100
                if(rand<cur_time):
                    rand=random.randrange(0,100)
                    
                    
                    cur_time=0
                    if(rand>=40):
                        item.append(Ob.Normal(ground))
                    elif(rand>35):
                        item.append(Ob.Fake(ground))
                    elif(rand>25):
                        item.append(Ob.Nail(ground))
                    elif(rand>20):
                        item.append(Ob.Conveyor_left(ground))
                    elif(rand>15):
                        item.append(Ob.Conveyor_right(ground))
                    else:
                        item.append(Ob.Trampoline(ground))
                   
            for i in item:
                if not i.Update(Children):
                    item.remove(i)
    


        pygame.display.update()   
   
    if floor>Ob.max_floor:
        print(floor)
        print(Ob.max_floor)
        Ob.max_floor=floor
    pygame.display.update()
        
            

      

def PrintP1State(P1,window_surface):
    

    fontObj =pygame.font.SysFont('SimHei',35)
    text = fontObj.render('x: '+str(int(P1.x)), True, (255 ,193, 37))
    window_surface.blit(text, (0, 75))

    fontObj =pygame.font.SysFont('SimHei',35)
    text = fontObj.render('y: '+str(int(P1.y)), True, (255 ,193, 37))
    window_surface.blit(text, (0, 100))

    fontObj =pygame.font.SysFont('SimHei',35)
    text = fontObj.render('speed: '+str(int(P1.speed)), True, (255 ,193, 37))
    window_surface.blit(text, (0, 125))

    fontObj =pygame.font.SysFont('SimHei',35)
    text = fontObj.render('CloseX: '+str(int(P1.closeX)), True, (255 ,193, 37))
    window_surface.blit(text, (0, 150))

    fontObj =pygame.font.SysFont('SimHei',35)
    text = fontObj.render('CloseY: '+str(int(P1.closeY)), True, (255 ,193, 37))
    window_surface.blit(text, (0,175))

    pygame.draw.circle(P1.ground,(255, 255, 0),(P1.x+15,P1.y+20),20,2)

def evaluate(genomes,config):
   
    ground=Ob.buildground()

    running=True
    clock = pygame.time.Clock()
    cur_time=85
    last_time=0
    item=[]
    second=0
    floor=0
    

    nets=[]
    ge=[]
    Children=[]
    for genome_id, genome in genomes:
        genome.fitness = 0  # start with fitness level of 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        Children.append(Ob.Player(ground))
        ge.append(genome)

    tot_num=len(Children)
    while running and len(Children)>0:
        clock.tick(1000)   
    
        for event in pygame.event.get():
            second+=1
            cur_time+=1
            if(second>250):
                second=0
                floor+=1

                

            keys=pygame.key.get_pressed()
            if event.type == QUIT:
                running = False
        

        
           
            #item,ground=Update_plateform(item,ground)
            ground=Ob.buildground(floor,len(Children))
            rank=len(Children)
            for x,P in enumerate(Children):
                output = nets[Children.index(P)].activate((P.x,P.y, P.on_platform,P.life,
                                                           P.x-P.closeXL,P.x-P.closeXR,P.y-P.closeY,570-P.x,205-P.x,P.IsTram,P.IsNail,P.IsLR))
                                                
                if second%50==0:
                    ge[x].fitness+=P.life/10
                
                #if x==0:
                #    PrintP1State(P,ground)
                if output[0]>0.5:
                    alive,fit=P.Update(item,'R')
                elif output[1]>0.5:
                    alive,fit=P.Update(item,'L')
                else:
                    alive,fit=P.Update(item,'N')
                if not alive:
                    if floor>0:
                        ge[x].fitness+=fit
                        ge[x].fitness+=floor*10
                    Children.pop( x)
                    nets.pop(x)
                    ge.pop(x)

                else:
                    if not P.Update(item,'N'):
                        ge[x].fitness+=fit
                        Children.remove( P)

            if(cur_time>85 ):
           
                
           
                rand=random.random()
                rand*=100
                if(rand<cur_time):
                    rand=random.randrange(0,100)
                    
                    
                    cur_time=0
                    if(rand>=40):
                        item.append(Ob.Normal(ground))
                    elif(rand>35):
                        item.append(Ob.Fake(ground))
                    elif(rand>25):
                        item.append(Ob.Nail(ground))
                    elif(rand>20):
                        item.append(Ob.Conveyor_left(ground))
                    elif(rand>15):
                        item.append(Ob.Conveyor_right(ground))
                    else:
                        item.append(Ob.Trampoline(ground))
                   
            for i in item:
                if not i.Update(Children):
                    item.remove(i)
    


        pygame.display.update()   
   
    if floor>Ob.max_floor:
       
        Ob.max_floor=floor
    return floor
    pygame.display.update()
        

def run(config_path):
    global max_floor
    global node_name
    max_floor=0
    config=neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,
                              neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)
    p=neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    

    stats=neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(generation_interval=100))
  
    

    winner=p.run(evaluate,100)

    with open("winner.pkl", "wb") as f:
        pickle.dump(winner, f)
        f.close()

    visualize.draw_net(config, winner, True,node_names=node_name)
    #visualize.plot_stats(stats, ylog=False, view=True)
   # visualize.plot_species(stats, view=True)

    

    print('\nBest genome:\n{!s}'.format(winner))
    print('Max Floor:',Ob.max_floor)

def test():
    with open('winner.pkl', "rb") as f:
        genome = pickle.load(f)

    genomes = [(1, genome)]
    local_dir=os.path.dirname(__file__)
    config_path=os.path.join(local_dir,"config-feedforward")
    config=neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,
                              neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)
    test_type=input("Choose test_type:(1)singel test (2)Multiple test\n")
    if(test_type=='1'):
        y=1
        while y==1:
            evaluate(genomes,config)
            genomes = [(1, genome)]
            y=0
            while y!=1 and y!=2:
                y=int(input("play again?(1)yes (2)no"))
    elif test_type=='2':
        times=int(input("test for ? times"))
        floor=[]
        max=0
        for i in range(times):
            print("Generation ",i+1,"start.")
            floor.append(evaluate(genomes,config))
            print("Generation ",i+1,"finish.")
        floor=np.array(floor)
        print("generate for ",times, times)
        print("std:",np.std(floor, ddof=0))
        print("avg:",np.average(floor))
        print("max:",np.max(floor))

    
        

    

    

def Load_fit(filename,config_path):
    global max_floor
    global node_name
    max_floor=0

    generation_time=int(input("how many times you want to generate"))
    
    config=neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,
                              neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)
    p = neat.Checkpointer.restore_checkpoint(filename)
    #visualize.draw_net(config, winner, True,node_names=node_name)
    p.add_reporter(neat.StdOutReporter(True))
    

    stats=neat.StatisticsReporter()
    p.add_reporter(stats)
    

    p.add_reporter(neat.Checkpointer(generation_interval=50))
    

    

    winner=p.run(evaluate,generation_time)

    with open("winner.pkl", "wb") as f:
        pickle.dump(winner, f)
        f.close()

    visualize.draw_net(config, winner, True,node_names=node_name)
    #visualize.plot_stats(stats, ylog=False, view=True)
    #visualize.plot_species(stats, view=True)

    

    print('\nBest genome:\n{!s}'.format(winner))
    print('Max Floor:',max_floor)

if __name__=="__main__":
    option=input("Mode:(1)Play Game (2)Evaluate new fit (3) Load pretrain model (4) Load pretrain model and fit\n")
    #print(option)
    option=int(option)
    if option==1:
        print("play")
        print("Press 'Space' to generatea minion")
        print("Press 'Left' and 'Right' to control minion")
        play()
    elif option==2:
        os.environ["PATH"] += os.pathsep + '/bin/'
        local_dir=os.path.dirname(__file__)
        config_path=os.path.join(local_dir,"config-feedforward")
        run(config_path)
    elif option==3:
        
        test()
    elif option==4:
        os.environ["PATH"] += os.pathsep + '/bin/'
        local_dir=os.path.dirname(__file__)
        config_path=os.path.join(local_dir,"config-feedforward")
        version=input("Input your version(neat-checkpoint-+?) :")
        print(version)
        filename='neat-checkpoint-'+str(version)
        Load_fit(filename,config_path)
    else:
        print("wrong input")


        


