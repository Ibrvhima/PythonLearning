# Creation d'un dictionnaire
dictionnaire = {"id": "001", "nom": "Diallo", "prenom": "Ibrahim", "age": 22}
print(dictionnaire)

# acceder à la valeur d'une clé specifique
print(dictionnaire["id"])
print(dictionnaire["nom"])

# modifier la valeur d'une clé
dictionnaire["age"] = 23
print(dictionnaire["age"])

# ajout d'une propiete
dictionnaire["profession"] = "developpeur"
print(dictionnaire)

# Supprimer une proprieté
del dictionnaire["prenom"]
print(dictionnaire)

# parcourir un dictonnair
for cle, val in dictionnaire.items():
     print(cle, ":" ,val)
