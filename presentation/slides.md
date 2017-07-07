## Fullstack python

<hr/>
<div style="margin-bottom: 2em;"></div>

Matthieu Falce -- MF Consulting

<div style="margin-bottom: 1em;"></div>

Meetup Lille.py

06 juillet 2017


# Objectifs

##

 * réaliser un capteur IoT (internet of things)
 * uniquement en Python (et un peu de HTML)
    * accès aux données
    * traitement
    * affichage

<div style="margin-bottom: 3em;"></div>

Intérêt pédagogique seulement...

# Technologies

## Gros plan

<div style="margin-bottom: 3em;"></div>

* micropython => récupération d'une température et envoie par port série
* lecture d'un port série en python en arrière plan
* création d'un mini serveur web avec Flask
* création de figures en HTML avec plotly en mode hors ligne


## MicroPython

<div style="margin-bottom: 3em;"></div>

 * python 3.4 sur microcontroleur (ARM ou PIC)
 * shell python sur un µC (tests et le développement)
 * (problèmes de performances et empreinte mémoire)
 * pour plus d'infos :
    * [Site officiel](https://micropython.org/)
    * [Github du projet](https://github.com/micropython/micropython)


## Port série

<div style="margin-bottom: 3em;"></div>

 * protocole RS232
 * full duplex
 * plutôt facile à utiliser
 * très utilisé encore de nos jours dans l'IoT


## Flask

<div style="margin-bottom: 2em;"></div>

 * framework web léger
 * création facile d'appli WEB


## Charting
<div style="margin-bottom: 3em;"></div>

 * [matplotlib](https://matplotlib.org/) : la plus répandue en python
 * [plotly](https://plot.ly/) : rendu interactif de figures sur navigateur


# Place au code

##

* code micropython
* lire les infos sur le port série
* générer un graphique au format HTML avec plotly
* faire le serveur
* tout intégrer

##

<img src="demo.jpg" style="width: 45%; height: 45%"/>


# Et alors ?

## Prototypage

 * facile à mettre en oeuvre
 * problème d'intéraction
 * pas de persistance


## Mieux faire

<div style="margin-bottom: 2em;"></div>

* pas de limites dans les choix technique
* javascript !
    * recharger le div avec jquery (#old)
    * chart en JS + API avec Flask
    * FULL JS EXPERIENCE (Vue.js)
* bdd / persistance

## Mieux faire

<div style="margin-bottom: 1em;"></div>

* intérêt du STM32 vu l'utilisation
    * C / C++ et n'importe quel µC
    * gestion de la batterie et de la communication
* communication sans fil

# Conclusion

##

Python :

 * autre chose que scripts simples
 * proto IoT et en web (plus simple que Node ?)

<hr>

<img src="biohazard.png"/>

Inspiration / découverte / pas en production


## Shameless plug

 * [iotary](https://github.com/Kayoku/iotari/) => système de capteur sans fils
 * si vous avez des projets n'hésitez pas à me contacter (consulting@falce.net)

## Merci

<img src="axolot.png" style="width: 45%; height: 45%"/>
