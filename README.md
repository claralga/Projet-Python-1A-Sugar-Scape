# Projet-Python-1A-Sugar-Scape
Sugar Scape 

Objectif : Simuler l’émergence et l'évolution des inégalités dans une population d'agents hétérogènes et autonomes

Modèle suivi : Le Sugarscape d’Epstein et Axtell. C’est un programme de modélisation des agents. Dans sa forme plus basique, des fourmis évoluent de manière autonome sur un plan 2D parsemé de ressources (les grains de sucre) qu’elles doivent consommer pour survivre.

2 propriétés élémentaires :

Autonomie des agents : ils évoluent comme bon leur semble, il n’y a pas d’autorité centrale
Hétérogénéité des agents : ils ne naissent pas égaux, ils ont des capacités de stockage différentes et la quantité de grains qu’ils ont à disposition varie en fonction de leur lieu de naissance sur le plan
D’autres hypothèses peuvent s’ajouter pour améliorer le modèle.

Notre modèle : En s’inspirant du modèle présenté par Epstein et Axtell, nous avons pas à pas créé un tableau générant aléatoirement des grains de sucre et un tableau (de mêmes dimensions) générant des fourmis capables de se déplacer dans un rayon qui nous appellerons leur vision. Leur but est de se déplacer sur la case (à l’intérieur de leur vision) contenant le maximum de sucre afin d’augmenter sa richesse. Chaque fourmi consomme 1 grain de sucre par déplacement (si possible). Une fourmi qui a une richesse nulle meurt (« de faim » nous dirons).

Nous avons ensuite ajouté des hypothèses :

Chaque fourmi a une capacité de stockage. Quand elle est sur une case, elle consomme 1 grain et stocke le reste selon sa capacité et ce qu’il reste sur la case. Si une fourmi n’a plus la possibilité de consommer un grain sur la map, elle consomme son stock. Quand la fourmi n’a plus de grain à disposition (ni sur la map ni dans son stock) elle meurt.
On crée des générations en introduisant une durée de vie (égale pour toutes les fourmis) inférieure au nombre d’itérations.
Il y a une transmission à chaque génération : la fourmi morte de vieillesse se régénère en un nouvel individu, à qui on attribue la capacité de stockage de son ancêtre avec la proba c ou une capacité de stockage aléatoire avec une probabilité 1-c. Le nouvel individu reçoit avec une probabilité s une part p du stock de grain dont disposait son ancêtre à sa mort, et ne reçoit rien avec une probabilité 1-s. Les nouvelles fourmis sont placées au hasard sur la map.
Il y a une régénération du grain : à chaque génération, chaque case croit de t unités avec une probabilité v.
Il y a une forme de « rente » pour les fourmis les plus riches (ie ayant un stock de grain très important) : à chaque itération, les fourmis appartenant au 9ème décile touchent une rente correspondant 2% de leur richesse.
Ainsi, notre code est paramétré d'une certaine manière mais il est possible de changer ces paramètres au début de la 3e partie "Simulations et tests", afin d'observer différents résultats.

Nos outils : Etant tous les trois d’anciens «prépa éco », nous avons préféré utiliser les outils les plus simples de la programmation Python. Ainsi si nous avons songé à utiliser la programmation orientée objet, cela allait nous prendre du temps d’apprentissage alors que nous avions déjà une ébauche fonctionnelle utilisant des matrices, des boucles et des fonctions. Nous avons donc continué avec ces outils pour la construction de notre simulation.

Représentation graphique des résultats : Le premier résultat graphique que nous avons modélisé est un gif animé présentant le déplacement des fourmis à chaque itération (représentées par un point rouge) sur une heatmap de la map de grain qui s’actualise à chaque itération en fonction de ce que les fourmis consomment. Si ce premier résultat était très visuel et nous permettait de voir l’évolution « en direct » de notre modèle, il n’était que peu exploitable pour l’analyse des inégalités (qui était notre but initial). Nous avons donc représenté des courbes de Lorenz à partir des richesses (stock) des fourmis à l’issue de chaque génération. Nous avons également implémenté un calcul de l’indice de Gini de notre population de fourmis à chaque itération. Enfin, nous avons représenté l’évolution du rapport interdécile (D9/D1) et exprimé la part de la richesse totale détenue par les 20% les plus riches.

Résultats obtenus :

Avec des paramètres intermédiaires (on transmet l’intégralité de sa richesse avec une proba ¾ et on transmet ses capacités avec une proba ¾) on observe un accroissement des inégalités intergénérationnelles mais diminution des inégalités à l’intérieur d’une génération. Les inégalités se transmettent et se creusent : l’indice de Gini s’accroit à chaque nouvelle génération (processus cumulatif). L’indice de Gini diminue légèrement à l’intérieur d’une même génération car les ressources sont abondantes donc chaque individu stocke le maximum de ses capacités à chaque itération et on observe donc un plafonnement des inégalités.
