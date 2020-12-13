# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:53:25 2020

@author: Romane Gajdos
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:01:04 2020

@author: Romane Gajdos
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:50:31 2020

@author: Romane Gajdos
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 09:19:58 2020

@author: Romane Gajdos
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:15:59 2020

@author: Romane Gajdos
"""

import numpy as np
import random as rd
import math 

#la fourmi mange une unité de grain de la cellule dans laquelle elle se trouve
#modèle simple : métabolisme = 1, identique pour toutes les fourmis

#complexification : chaque fourmi a une capacité de stockage 
#capacité de stockage représente le revenu gagné par un individu 
#on associe aléatoirement à chaque fourmi une capacité de stockage 
          
#modèle simple : toutes les fourmis ont la même vision
#la vision est constante et fixée au début de l'exécution
#les individus se déplacent en ligne et en colonne (pas en diagonale)
#un déplacement d'une case "coûte" un point de vision
            
 

#définition des fonctions
def maxligne (vision):
    
    #on crée la liste des indices j sur la ligne a 
    jpossibles = []
    for b in range(j-vision+1, j+vision):
        if b>=0 and b<taille :
           jpossibles.append(b) 
           
    #on élimine les cases trop éloignées
    if jpossibles != []:
        inter=[]
        for b in jpossibles :
            somme = abs(b - j) + abs(a - i)
            if somme > vision -1 :
              inter.append(b)                
        for t in inter:
            jpossibles.remove(t)
      
    #on élimine les cases qui sont occupées par d'autres fourmis
    if jpossibles != []:
        occupied = []
        for b in jpossibles:
            if table[a,b] != 0:
                occupied.append(b)
        if occupied !=[]:
            for k in occupied :
                jpossibles.remove(k)
            
    #on regarde quelles sont les quantités sur les cases qui restent
    quantite=[]
    for b in jpossibles:
        t = grain[a,b]
        quantite.append(t)
    #on prend le ou les max atteingnables de chaque ligne
    if jpossibles != []:
        miam = max(quantite)
        pasmax = []
        for b in jpossibles:
            if grain[a,b] < miam :
                pasmax.append(b)    
        if pasmax != []:
            for k in pasmax:
                jpossibles.remove(k) 

    #on prend le ou les max les plus proche
    if jpossibles != []:
        toofar = []
        distance = []
        for b in jpossibles :
            distance.append(abs(b-j) + abs(a-i))
        mindistance = min(distance)
        for k in range(len(distance)):
            if distance[k] > mindistance:
                toofar.append(jpossibles[k])
        if toofar != [] :      
            for k in toofar:
                jpossibles.remove(k)
            
    return(jpossibles)       


def maxcercle(vision,i,j,listemaxi,ligne):
    n=len(ligne)
    indicespossibles = []
    #on crée la liste contenant le nombre d'indices possibles
    for z in range(n):
        indicespossibles.append(z)

    miam = max(listemaxi)
    arraymaxi = np.array(listemaxi)
    pasmax = []
    #on ne garde que les max des max
    for s in indicespossibles:
        if arraymaxi[s] < miam :
            pasmax.append(s)    
    if pasmax != []:
        for k in pasmax:
            indicespossibles.remove(k) 
                     
    #on obtient une liste avec les max (tous égaux)
    #on veut trouver le plus proche    
    distance = []
    toofar = []
    for n in indicespossibles :
        somme = abs(listejmax[n] - j) + abs(ligne[n] - i)
        #print("somme=",somme)
        distance.append(somme)
    mindistance = min(distance)   
    for k in range(len(distance)):
        if distance[k] > mindistance :
            toofar.append(indicespossibles[k])
    if toofar != [] :      
        for k in toofar:
            indicespossibles.remove(k)                        
    return(indicespossibles)
  


def heredite(table,nbrfourmisdepart,cycle,p):
    nvgene = []
    #transmission des fourmis encore vivantes
    old = 0
    for i in range(taille):
        for j in range(taille):
            if table[i,j] > 0:
                old = old +1
                numfourm = table[i,j]
                k = indiv.index(numfourm)
                table[i,j] = 0
                info[3,k] = -1 #comme ça qu'on différencie mort de faim et mort naturelle
                info[0,k+nbrfourmisdepart] = numfourm + 1/10 #descendance numéro g de la fourmi numéro fournum
                info[1,k+nbrfourmisdepart] = rd.randint(0,10) #pas de transmission des capacités
                info[2,k+nbrfourmisdepart] = rd.choices([0,info[2,k]], [p,1-p])[0] #p proba de transmettre son stock
                nvgene.append(info[0,k+nbrfourmisdepart])
                
    #remplacement des fourmis mortes
    for y in range((cycle-1)*nbrfourmisdepart,(cycle)*nbrfourmisdepart-1):
        print(y)
        if info[3,y] > 0:
            info[0,y+nbrfourmisdepart] = (info[0,y][0]) + 1/10 #descendance numéro g de la fourmi numéro y
            info[1,y+nbrfourmisdepart] = rd.randint(0,10) #pas de transmission des capacités
            info[2,y+nbrfourmisdepart] = 0 #pas de transmission de stock
            nvgene.append(info[0,y+nbrfourmisdepart])  
    
    table = np.zeros((taille,taille))
    for n in nvgene:
        k = rd.randint(0,taille-1)
        l = rd.randint(0,taille-1)
        table[k,l] = n
    nbrzero=0
    for i in range(taille):
        for j in range(taille):
            if table[i,j] == 0:
                nbrzero = nbrzero +1
    nbrfourmisdepart = taille**2 - nbrzero
           
          
    return(info, table, old)

#Début des itérations 

#taille =  int(input("Quelle taille de map?")) 
#nbrindiv = math.inf 
#while nbrindiv > taille**2 : 
#    nbrindiv = int(input("Combien de fourmis voulez-vous?")) 
#vision = int(input("A quelle distance max voulez-vous que les fourmis se déplacent?"))
#iterations = int(input("Combien d'itérations voulez-vous?"))
#dureedevie = int(input("Quelle est la durée de vie d'une fourmi?"))   
#p = input("Quelle est la probabilité de transmettre sa richesse?")

taille =  10
nbrindiv = 10
vision = 3
iterations = 60
dureedevie = 10
p = 1/2

#On crée la matrice contenant les fourmis
#chaque fourmi est identifiée par un numéro 
table = np.zeros((taille,taille))
for n in range(1,nbrindiv+1):
    k = rd.randint(0,taille-1)
    l = rd.randint(0,taille-1)
    table[k,l]=n+1/10
nbrzero=0
for i in range(taille):
    for j in range(taille):
        if table[i,j] == 0:
            nbrzero = nbrzero +1
nbrfourmisdepart = taille**2 - nbrzero
print("il y a", nbrfourmisdepart, "fourmis au départ")
print("table=\n",table)


            
#on crée aléatoirement les quantités de grain dans chaque cellule de la map
grain = np.zeros((taille,taille),dtype=int)
for i in range (taille):
    for j in range (taille):
        k = rd.randint(0,10)
        grain[i,j] = k
print("grain=\n",grain)    
    



#on stocke les caractérstiques des fourmis dans une matrice
# première ligne = numéro de la fourmi
#deuxième ligne = capacité de stockage de la fourmi
#troisième ligne =  stock de la fourmi
#quatrième ligne = ordre de mort de la fourmi


info = np.zeros((4,nbrfourmisdepart*(int(iterations/dureedevie))))
z=0
for i in range (taille):
    for j in range (taille):
        if table[i,j] > 0:
            info[0,z]=table[i,j]
            info[1,z]=rd.randint(0,10)
            z = z + 1
print(info)
indiv = list(info[0,])




 
deaths = 0    
cycle = 1  
for n in range (1,iterations):
    
    if n == dureedevie*cycle +1:
        inter = heredite(table,nbrfourmisdepart,cycle,p)
        table = inter[1]
        info= inter[0]
        old = inter[2]
        indiv = list(info[0,])
        cycle = cycle + 1
        print("situation à l'issue du", cycle,"eme cycle\n",info)
        print(table)
        print("il y a",old,"morts de vieillesse à la fin du", cycle, "eme cycle")
        print("il y a", nbrfourmisdepart, "fourmis au départ du", cycle,"eme cycle")
        
      
    for i in range (taille):
       for j in range (taille):
           if table[i,j] > 0:
               identification = table[i,j]
               k = indiv.index(identification)
               jm = j
               im = i 
               ligne = []
               listemaxi = []
               listejmax=[]
               table[i,j]=0
               for a in range(i-vision+1,i+vision):
                  if a>=0 and a<taille:
                     ligne.append(a) #liste des indices des lignes
                     jpossibles = maxligne (vision) 
                     if jpossibles == []:
                         ligne.remove(a)
                     if jpossibles != []:
                         jma = rd.choice(jpossibles)
                         listejmax.append(jma) #liste des indices jmax du max de chaque ligne
                         maxi = grain[a,jma] #valeur du maxgrain de la ligne a
                         listemaxi.append(maxi) #liste des maxgrain de chaque ligne
               indicespossibles = maxcercle(vision,i,j,listemaxi, ligne)
               destination = rd.choice(indicespossibles)
               im = ligne[destination]
               jm = listejmax[destination]    
                    
  #la fourmi emporte ses caractéristiques avec elle
               table[im,jm]= -identification
               grain[im,jm] = grain[im,jm]-1 #la fourmi mange un grain
               #la fourmi stocke le maximum qu'elle peut en fonction de ces capacités et de la disponibilité 
               a = min(info[1,k], grain[im,jm]) 
               info[2,k] = info[2,k] + a
               grain[im,jm] = grain[im,jm] -a
               #la foumi consomme son stock si il n'y a plus de grain disponible
               if grain[im,jm] == -1:
                   grain[im,jm] = 0
                   info[2,k] = info[2,k] -1 
            #si la fourmi n'a plus de stock elle meurt
               if info[2,k] == -1 : 
                   deaths = deaths+1
                   info[2,k] = 0
                   info[3,k] = deaths
                   table[im,jm]=0

               
    for i in range (taille):
        for j in range (taille):
            table[i,j] = abs(table[i,j])
    
    
    nbrzero=0
    for i in range(taille):
        for j in range(taille):
            if table[i,j] == 0:
                nbrzero = nbrzero +1
    fourmis = taille**2 - nbrzero
    
    
    print("table=\n",table)
    print("grain=\n",grain)
    print("info=\n",info)
    print("il y a", nbrfourmisdepart, "fourmis au départ")
    print("Il y a", fourmis, "fourmis après", n, "itérations")
    print("Il y a", deaths, "morts (de faim) après", n, "itérations")
    
    
 
    




    



