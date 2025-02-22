# Création d'une list en python

fruit=["pomme","banane","annanas","papaye"];
print(fruit)

# ajout d'un element de ma liste
fruit.append("orange") #Ceci ajoute un element à la dernière position du tableau
print(fruit)
fruit.insert(2, "Goyave") #ceci ajout un element à un index preci exemple à l'indice 2
print(fruit) 

# Affichage d'un élement par indexation
print("**************les elemnts indexés********************")
print(fruit[0]) #affiche le premier élement du tableau
print(fruit[4])
print(fruit[-1]) # ceci permet d'afficher le tout dernier element de mon tableau

# Supprission d'un element du tableau
fruit.remove("orange") 
print(fruit)

# Parcourir le tableau

for fruits in fruit:
     print(fruits)