# Fullstack python : du bare-metal (ARM) au web

## Objectif

 * réalisation d'un capteur IoT => un thermomètre connecté avec visualisation sur une page web
 * ne sera codé qu'en python (et un peu de HTML)
 * intéret pédagogique seulement, pas pour l'utilisation de l'objet, on peut faire mieux, moins cher...
 * technologies mises en place :
   ** micropython => récupération d'une température et envoie par port série
   ** lecture d'un port série en python en arrière plan
   ** création d'un mini serveur web avec Flask
   ** création de figure en HTML avec plotly en mode hors ligne

## Technologies

### Micropython

 * réécriture de l'interpréteur python 3.4 pour tourner sur un microcontroleur (ARM ou PIC)
 * permet d'avoir un shell python sur un µC, très pratique pour les tests et le développement
 * problèmes de contrôle fin des performances et de l'empreinte mémoire
 * pour plus d'infos :

## Port série

 * vieux protocole de communication où les données sont envoyés en... série (contrairement au port parallèle)
 * full duplex (les données peuvent être envoyés et reçues en même temps)
 * plutôt facile à utiliser
 * très utilisé encore de nos jours (avec des adaptateurs USB/RS232) pour communiquer avec plein d'objets IoT

## Flask

 * framework web léger permettant de faire du développement d'application web rapidement

## Matplotlib / plotly

 * matplotlib : bibliothèque de plot la plus répendue en python
 * plotly : permet de rendre des plots matplotlib de façon intéractive sur navigateur

## Place au code

4 étapes indépendantes :
 * coder le termomètre
 * lire les infos sur le port série
 * générer un graphique au format HTML avec plotly
 * faire le serveur


## Une bonne approche

 La solution mise en place est intéressante pour du prototypage :
  * facile à mettre en oeuvre
  * problème d'intéraction (on doit recharger la page car on n'a pas de JS pour le faire)
  * on ne garde pas les informations
  * quid de l'intérêt du proto ?

Une meilleure approche :
 * une fois que l'on a validé l'intérêt du prototype, il ne faut pas se limiter dans les choix technique
 * même si ce n'est pas notre spécialité, on peut chosir d'utiliser du javascript
   * soit pour recharger le div automatiquement avec jquery (#old)
   * soit en décidant d'utiliser un framework de représentation graphique en JS (d3.js, highcharts.js, *.js, ...) et en exposant une API avec Flask
   * pourquoi ne pas avoir la FULL JS EXPERIENCE avec Vue.js ou React.js ou
  * on peut (doit!) stocker les infos dans une base de donnée pour la persistance
 * pour le dispositif en lui même, on peu se demander l'intérêt d'avoir un STM32 qui communique par port série avec un ordinateur
   * on peut utiliser autre chose en codant en C / C++, ce ne sont pas les microcontroleurs qui manquent
   * on peut utiliser un protocole de communication sans fil (plus long)
   * le nerf de la guerre est la gestion de la batterie et de la communication

## Conclusion

 * Matthieu + Python <3
 * Python peut servir autre chose qu'aux scripts simples (mais ça vous le saviez déjà)
 * Python est intéressant pour le prototypage en IoT et en web (peut-être même plus que Node)
 * A retenir : tour d'horizon de l'écosystème, n'utiliser ce code que comme inspiration et pas en production

Shameless plug : iotary


# Conda install

conda create -n fullstack_iot
activate fullstack_iot
conda install -n fullstack_iot jupyter
conda install -n fullstack_iot flask pyserial plotly matplotlib