import numpy as np
class ant:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
        
    def update_position_adjacente(self,length_tab):
        possiblemoves=[]
        if self.x>0:
            possiblemoves.append([-1,0])
        if self.y>0:
            possiblemoves.append([0,-1])
        if self.x<length_tab-1:
            possiblemoves.append([1,0])
        if self.y>length_tab-1:
            possiblemoves.append([1,0])

        aleatorymove = (int) (np.random.random() * len(possiblemoves))
        newposition = possiblemoves[aleatorymove]
        self.x = self.x+ newposition[0]
        self.y = self.y+newposition[1]
        
    def update_position_adjacenteAndDiagonale(self,length_tab):
        possiblemoves=[]
        if self.x>0:
            possiblemoves.append([-1,0])
        if self.y>0:
            possiblemoves.append([0,-1])
        if self.x<length_tab-1:
            possiblemoves.append([1,0])
        if self.y>length_tab-1:
            possiblemoves.append([1,0])
        if self.x>0 and self.y>0:
            possiblemoves.append([-1,-1])
        if self.y>0 and self.x<length_tab-1:
            possiblemoves.append([1,-1])
        if self.y<length_tab-1 and self.x>0 :
            possiblemoves.append([-1,1])
        if self.y>length_tab-1 and self.x<length_tab-1:
            possiblemoves.append([1,1])
        aleatorymove = (int) (np.random.random() * len(possiblemoves))
        newposition = possiblemoves[aleatorymove]
        self.x = self.x+ newposition[0]
        self.y = self.y+newposition[1]
    
    def ants_same_cell(self,ant2):
        indicator = True
        if self.x==ant2.x and self.y==ant2.y:
            indicator = False
        return indicator
    
    

def antGameStart(number_simulation=10000,length_tab=8,secondForAMove=10,diagmove=False):
    compteur_time =0
    compteur_mean_time =0
    ant1 = ant(0,0)
    ant2 = ant(length_tab-1,length_tab-1)
    for i in range(0,number_simulation):
        while(ant1.ants_same_cell(ant2)):
            if diagmove == False:
                ant1.update_position_adjacente(length_tab)
                ant2.update_position_adjacente(length_tab)
                compteur_time = compteur_time+1
            else:
                ant1.update_position_adjacenteAndDiagonale(length_tab)
                ant2.update_position_adjacenteAndDiagonale(length_tab)
                compteur_time = compteur_time+1
                
        compteur_mean_time =compteur_mean_time+compteur_time
        compteur_time=0
        ant1 = ant(0,0)
        ant2 = ant(length_tab-1,length_tab-1)
        
    meanProba=compteur_mean_time/number_simulation
    meanProbaSec =    secondForAMove*meanProba     
    print("Average step : ",meanProba," average step sec : ",meanProbaSec)


number_simulation =1000000    
secondForAMove=10
length_tab=8
antGameStart(number_simulation,length_tab,secondForAMove)
#With diag moves
antGameStart(number_simulation,length_tab,secondForAMove,True)
 
"""
Average step :  25.788792  average steps sec :  257.88792
Average step :  35.459197  average steps sec :  354.59197000000006
"""
