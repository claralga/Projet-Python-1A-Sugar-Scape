# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:13:34 2020

@author: Romane Gajdos
"""



import numpy as np
import random as rd
import matplotlib.pyplot as plt



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
  


#matrices de stockage pour les graphismes:
liste=list()
listefourmis=list() 
richesses=list() 

#Début des itérations 

#taille =  int(input("Quelle taille de map?")) 
#nbrindiv = math.inf 
#while nbrindiv > taille**2 : 
    #nbrindiv = int(input("Combien de fourmis voulez-vous?")) 
#vision = int(input("A quelle distance max voulez-vous que les fourmis se déplacent?"))
#iterations = int(input("Combien d'itérations voulez-vous?"))
#dureedevie = int(input("Quelle est la durée de vie d'une fourmi?"))   

            
taille =  100
nbrindiv = 10
vision = 10
iterations = 30


#On crée la matrice contenant les fourmis
#chaque fourmi est identifiée par un numéro 
table = np.zeros((taille,taille),dtype=int)
for n in range(1,nbrindiv+1):
    k = rd.randint(0,taille-1)
    l = rd.randint(0,taille-1)
    while table[k,l] != 0 :
            k = rd.randint(0,taille-1)
            l = rd.randint(0,taille-1)
    table[k,l]=n
nbrzero=0
for i in range(taille):
    for j in range(taille):
        if table[i,j] == 0:
            nbrzero = nbrzero +1
nbrfourmisdepart = taille**2 - nbrzero
print("il y a", nbrfourmisdepart, "fourmis au départ")
#print("table=\n",table)


            
#on crée aléatoirement les quantités de grain dans chaque cellule de la map
grain = np.zeros((taille,taille),dtype=int)
for i in range (taille):
    for j in range (taille):
        k = rd.randint(0,10)
        grain[i,j] = k
#print("grain=\n",grain)    
    



#on stocke les caractérstiques des fourmis dans une matrice
# première ligne = numéro de la fourmi
#deuxième ligne = capacité de stockage de la fourmi
#troisième ligne =  stock de la fourmi
#quatrième ligne = ordre de mort de la fourmi


info = np.zeros((5,nbrfourmisdepart),dtype=int)
z=0
for i in range (taille):
    for j in range (taille):
        if table[i,j] > 0:
            info[0,z] = 1
            info[1,z]=table[i,j]
            info[2,z]=rd.randint(0,10)
            z = z + 1
indiv = list(info[1,])


#début des itérations:
 
deaths = 0      

for n in range (1,iterations+1):
    
    sumgrain = 0
    for i in range(taille):
        for j in range(taille):
            sumgrain = sumgrain + grain[i,j]
    if sumgrain == 0 : 
        print("Il n'y a plus de grain")
    if sumgrain != 0 : 
                
          
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
                   a = min(info[2,k], grain[im,jm]) 
                   info[3,k] = info[3,k] + a
                   grain[im,jm] = grain[im,jm] -a
                   #la foumi consomme son stock si il n'y a plus de grain disponible
                   if grain[im,jm] == -1:
                       grain[im,jm] = 0
                       info[3,k] = info[3,k] -1 
                #si la fourmi n'a plus de stock elle meurt
                   if info[3,k] == -1 : 
                       deaths = deaths+1
                       #info[3,k] = 0
                       info[4,k] = deaths
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
        
       
                        
        #on stocke les matrices grain afin d'enregistrer les images ensuite
        a=np.array(grain)
        liste.append(a)
        
       
                    
        #on exagere le numero de chaque fourmi afin que sa couleur ressorte 
        #bien sur les graphiques 
        for i in range (taille):
            for j in range (taille):
                if table[i,j] !=0:
                    table[i,j]= table[i,j]+100
                        
        #on stocke les matrices fourmi afin d'enregistrer les images ensuite
        b=np.array(table)
        listefourmis.append(b)
        
        #on "renomme"les fourmis (=on supprime l'exagération)
        for i in range (taille):
            for j in range (taille):
                if table[i,j] !=0:
                    table[i,j]=table[i,j]-100
        
        #Pour lorenz, on stocke la 3e ligne de info
        richesses.append(np.array(info[3]))
        
      #  print("table=\n",table)
       # print("grain=\n",grain)
        #print("info=\n",info)
        print("il y a", nbrfourmisdepart, "fourmis au départ")
        print("Il y a", fourmis, "fourmis après", n, "itérations")
        print("Il y a", deaths, "morts (de faim) après", n, "itérations")



#graphismes
        
plt.pcolormesh(liste[0],cmap ='Greys',alpha=0.25)
plt.pcolormesh(listefourmis[0],cmap='Reds',alpha=0.75)
plt.savefig('grain1.png')
plt.pcolormesh(liste[int(iterations/10)],cmap ='Greys',alpha=0.25)
plt.pcolormesh(listefourmis[int(iterations/10)],cmap='Reds',alpha=0.75)
plt.savefig('grain2.png')
plt.pcolormesh(liste[int(2*iterations/10)],cmap ='Greys', alpha=0.25)
plt.pcolormesh(listefourmis[int(2*iterations/10)],cmap='Reds',alpha=0.75)
plt.savefig('grain3.png')
plt.pcolormesh(liste[int(3*iterations/10)],cmap ='Greys', alpha=0.25)
plt.pcolormesh(listefourmis[int(4*iterations/10)],cmap='Reds',alpha=0.75)
plt.savefig('grain4.png')
plt.pcolormesh(liste[8],cmap ='Greys',alpha=0.25)
plt.pcolormesh(listefourmis[int(5*iterations/10)],cmap='Reds',alpha=0.75)
plt.savefig('grain5.png')
plt.pcolormesh(liste[int(6*iterations/10)],cmap ='Greys',alpha=0.25)
plt.pcolormesh(listefourmis[int(6*iterations/10)],cmap='Reds',alpha=0.75)
plt.savefig('grain6.png')
plt.pcolormesh(liste[int(7*iterations/10)],cmap ='Greys',alpha=0.25)
plt.pcolormesh(listefourmis[int(7*iterations/10)],cmap='Reds',alpha=0.75)
plt.savefig('grain7.png')
plt.pcolormesh(liste[int(8*iterations/10)],cmap ='Greys',alpha=0.25)
plt.pcolormesh(listefourmis[int(8*iterations/10)],cmap='Reds',alpha=0.75)
plt.savefig('grain8.png')
plt.pcolormesh(liste[int(9*iterations/10)],cmap ='Greys',alpha=0.25)
plt.pcolormesh(listefourmis[int(9*iterations/10)],cmap='Reds',alpha=0.75)
plt.savefig('grain9.png')

import imageio
images = []
filenames=['grain1.png','grain2.png','grain3.png','grain4.png','grain5.png','grain6.png','grain7.png','grain8.png','grain9.png']
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images)



#Lorenz et Gini


plt.clf()
k = 0
n = len(richesses[k])
lorenz = np.cumsum(np.sort(richesses[k])) / richesses[k].sum()
lorenz = np.append([0],lorenz) 
xaxis = np.linspace(0-1/n,1+1/n,n+1) 
plt.plot(xaxis,lorenz,drawstyle='steps-post')
plt.savefig('lorenz1.png')

plt.clf()
k = int(iterations/2)
n = len(richesses[k])
lorenz = np.cumsum(np.sort(richesses[k])) / richesses[k].sum()
lorenz = np.append([0],lorenz) 
xaxis = np.linspace(0-1/n,1+1/n,n+1) 
plt.plot(xaxis,lorenz,drawstyle='steps-post')
plt.savefig('lorenz2.png')

plt.clf()
k = int((3/4)*iterations)
n = len(richesses[k])
lorenz = np.cumsum(np.sort(richesses[k])) / richesses[k].sum()
lorenz = np.append([0],lorenz) 
xaxis = np.linspace(0-1/n,1+1/n,n+1) 
plt.plot(xaxis,lorenz,drawstyle='steps-post')
plt.savefig('lorenz3.png')

plt.clf()
k = iterations-1
n = len(richesses[k])
lorenz = np.cumsum(np.sort(richesses[k])) / richesses[k].sum()
lorenz = np.append([0],lorenz) 
xaxis = np.linspace(0-1/n,1+1/n,n+1) 
plt.plot(xaxis,lorenz,drawstyle='steps-post')
plt.savefig('lorenz4.png')







