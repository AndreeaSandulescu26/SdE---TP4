Biblioteque = dict({
    "Miguel de Cervantes": "Don Quixote",
    "Gustave Flaubert": "Madame Bovary",
    "Fyodor Dostoyevsky": "Crime and Punishment"
})

val = ""

while(val != "exit"):
    val = input("Entrez un auteur ")
    livres = Biblioteque.get(val)
    if livres != None:
        print(livres)
    else: 
        print("Auteur n'est pas trouve!")