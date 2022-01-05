# Cours 03

## 08:00

Il faut comprendre les mécanismes d'acceptation d'un projet (avoir une vue d'ensemble de ce qui gravite autour du projet) lorsqu'on cherche à obtenir un financement (ou autre).

## 10:00

On a des systèmes de plus en plus compliqués (spatial, etc...) et ce qui permet de les réaliser est l'ingénierie systèmes. L'ingénierie systèmes a d'abord été mise en oeuvre pour le spatial et le militaire puis le reste

le principe de l'ingénierie systèmes est de faire une décomposition d'un système global (voyage vers la lune par exemple). Il existe plusieurs façons de décomposer : 

- Séparation par physique (électrique, mécanique, etc...)
- Séparation par fonction (Lanceur, pas de tir, atmosphère, lune, etc...)

## 33:00

Travailler par itérations pour comprendre les besoins et les problèmes du projet. Par exemple faire une esquisse d'un projet pour obtenir un feedback des clients, puis rendre le projet plus concret etc...

## 42:00

Lorsqu'on commence un projet on doit :

1) Avoir une idée, comme un problème à résoudre ou un objectif (très importante)
2) S'informer sur le sujet (auprès du client ou faire de la recherche)
   1) Dans le cas d'un client : Poser des questions et/ou se mettre à sa place. Itération Client->démarche->solution (IPPD : Integrated produt & process developpement)
   2) Structurer le système afin de mieux identifier les solutions

## 1:08:00

Le ConOps est extrêmement puissant, il permet notamment de :

- Bien décrire ce qu'on veut faire et ce qui est attendu
- Utilisations du projet (intégration dans son environnement)
- Rechercher des points qui auraient peut-être été ignorés autrement

Il doit être réalisé au début du projet

le ConOps est un schéma qui représente toutes les étapes d'un projet. Par exemple, ça peut être un graph de l'état d'une fusée en fonction du temps (avec un axe non-linéaire pour le temps afin de compacter un peu les informations)

On va chercher à avoir une indépendance de la solution

- fonction operationnelle : l'action qui permet au système complet de remplir sa tâche
- fonction contrainte : sécurité, coût, etc...
- fonction constitutive : liées aux objets (planer pour un planeur, treuiller pour un treuil)
- métrique de performance : mesure qui permet d'évaluer la capacité du système à remplir sa tâche, mais aussi d'autres métriques comme le confort, le bruit, amélioration de la sécurité, etc...