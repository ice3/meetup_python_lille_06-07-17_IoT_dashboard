# Présentation fullstack python

Une présentation avec live coding permettant de montrer l'utilisation de diverse bibliothèques permettant de :
 * faire un prototype de capteur connecté (IoT)
 * faire des dashboard web en python et HTML

# Détail du dépôt :

 * dossier `code` avec le code complet de la démo
 * dossier `live coding minimal` avec le squelette de code et des fichiers à compléter au fur et à mesure
 * dossier `presentation` avec le markdown et le HTML de la présentation


# Mise à jour de la présentation :

J'utilise `pandoc` pour générer la présentation en `reveal.js` à partir d'un fichier `markdown`

    sudo apt-get install pandoc

Dans le dossier `presentation`

    make all  # pour télécharger reveal.js, faire des renomages et compiler le markdown

Dans un autre shell on peut lancer cette commande pour recompiler la présentation chaque seconde (make ne fait rien si le fichier `slides.md` est intouché depuis la dernière compilation) :

    watch -n 1 make index.html


# Dépendances :

## Logiciel

On peut utiliser `conda` ou `pip` pour installer les dépendances

    conda create -n fullstack_iot
    activate fullstack_iot
    conda install -n fullstack_iot jupyter
    conda install -n fullstack_iot flask pyserial plotly matplotlib

---------------

Pour micropython, il suffit de copier le contenu du dossier `code/micropython` sur la carte pour que ça fonctionne



## Matériel

 * Carte électronique avec micropython (un arduino peut faire l'affaire, mais il se programme en C/C++)
 * Un capteur de température, j'utilise le DTH22