# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 21:01:16 2021

@author: Léa
"""

'''
from itertools import combinations
from itertools import permutations
from itertools import product
from collections import Counter

        
        
li =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
test = product(li,repeat=8)

def fact(n):
    fac =1
    while(n>1):
        fac=fac*n
        n=n-1
    return fac
    

compteur =0
for i in test:
    if sum(i)==100:
        compteur =compteur +1
        
        tes = Counter(i)
        denom=1
        for j in tes:
            #print(tes[j])
            denom = fact(test[j])*denom
        compteur = compteur +fact(8)/denom
        
print(compteur)
'''
import numpy as np
class ant:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.previousx=x
        self.previousy=y
    
    def update_position_adjacente(self,length_tab):
        possiblemoves=[]
        if self.x>0:
            possiblemoves.append([-1,0])
        if self.y>0:
            possiblemoves.append([0,-1])
        if self.x<length_tab-1:
            possiblemoves.append([1,0])
        if self.y<length_tab-1:
            possiblemoves.append([0,1])

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
        if self.y<length_tab-1:
            possiblemoves.append([0,1])
        if self.x>0 and self.y>0:
            possiblemoves.append([-1,-1])
        if self.y>0 and self.x<length_tab-1:
            possiblemoves.append([1,-1])
        if self.y<length_tab-1 and self.x>0 :
            possiblemoves.append([-1,1])
        if self.y<length_tab-1 and self.x<length_tab-1:
            possiblemoves.append([1,1])
        aleatorymove = (int) (np.random.random() * len(possiblemoves))
        newposition = possiblemoves[aleatorymove]
        self.x = self.x+ newposition[0]
        self.y = self.y+newposition[1]

    def update_previousmove_notallowed(self,length_tab):
        possiblemoves=[]
        if self.x>0 and (self.x-1!=self.previousx or self.y!=self.previousy):
            possiblemoves.append([-1,0])
        if self.y>0 and (self.x!=self.previousx or self.y-1!=self.previousy):
            possiblemoves.append([0,-1])
        if self.x<length_tab-1 and (self.x+1!=self.previousx or self.y!=self.previousy):
            possiblemoves.append([1,0])
        if self.y<length_tab-1 and (self.x!=self.previousx or self.y+1!=self.previousy):
            possiblemoves.append([0,1])
        if self.x>0 and self.y>0 and (self.x-1!=self.previousx or self.y-1!=self.previousy):
            possiblemoves.append([-1,-1])
        if self.y>0 and self.x<length_tab-1 and (self.x+1!=self.previousx or self.y-1!=self.previousy):
            possiblemoves.append([1,-1])
        if self.y<length_tab-1 and self.x>0 and (self.x-1!=self.previousx or self.y+1!=self.previousy):
            possiblemoves.append([-1,1])
        if self.y<length_tab-1 and self.x<length_tab-1 and (self.x+1!=self.previousx or self.y+1!=self.previousy):
            possiblemoves.append([1,1])
        aleatorymove = (int) (np.random.random() * len(possiblemoves))
        newposition = possiblemoves[aleatorymove]
        self.previousx =self.x
        self.previousy = self.y
        self.x = self.x+ newposition[0]
        self.y = self.y+newposition[1]
    
    def ants_same_cell(self,ant2):
        indicator = True
        if self.x==ant2.x and self.y==ant2.y:
            indicator = False
        return indicator
    
    
#diagmove =0 allow only adjacente, diagmove =1 move possible in diagonale, diagmove =2 move possible in diag and goind back to previous move is not allowed
def antGameStart(number_simulation=10000,length_tab=8,secondForAMove=10,diagmove=0):
    compteur_time =0
    compteur_mean_time =0
    ant1 = ant(0,0)
    ant2 = ant(length_tab-1,length_tab-1)
    for i in range(0,number_simulation):
        while(ant1.ants_same_cell(ant2)):
            if diagmove == 0:
                ant1.update_position_adjacente(length_tab)
                ant2.update_position_adjacente(length_tab)
                compteur_time = compteur_time+1
            else:
                if diagmove ==1:
                    ant1.update_position_adjacenteAndDiagonale(length_tab)
                    ant2.update_position_adjacenteAndDiagonale(length_tab)
                    compteur_time = compteur_time+1
                else :
                    ant1.update_previousmove_notallowed(length_tab)
                    ant2.update_previousmove_notallowed(length_tab)
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
print("Adjacente moves only")
antGameStart(number_simulation,length_tab,secondForAMove,0)
#With diag moves
print("Diagnale moves allowed")
antGameStart(number_simulation,length_tab,secondForAMove,1)
print("Diagnale moves allowed")
antGameStart(number_simulation,length_tab,secondForAMove,2)
 
"""
Average step :  82.655527  average step sec :  826.5552700000001
Average step :  94.484044  average step sec :  944.84044
"""
    
    
    
"""
Two ants start in opposite corners of a regular chessboard. Every 10 seconds, they move from the center of the square they're on to the center of an adjacent square.
How long until they both land on the same square? How long until their paths cross (Ant A moving from square K to L and Ant B moving from square L to K)?
What happens if we allow the ants to move diagonally? What happens if we restrict ants from moving to their immediately previous square?
"""
