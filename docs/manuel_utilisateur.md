# Introduction
OpenStreetTangible est une démonstration de ce qu'il est possible de réaliser en terme de plan de transports en communs accessible à l'aide du logiciel OpenStreetTouch, d'une BrailleRAP et de divers outils de fabrication numérique.

C'est un plan de métro tactile et parlant de la ville de Rennes qui est destiné aux personnes déficientes visuelles.  

Ce prototype , réalisé  avec le  programme  [OpenStreetTouch] (https://github.com/braillerap/OpenStreetTouch/releases) et l’embosseuse braille opensource [Braillerap] (https://github.com/braillerap) , est une preuve de concept qui peut être déclinée pour n’importe quelle autre ville dans le monde.

Il associe un plan en relief du métro avec des boutons pour chaque station permettant de vocaliser leur nom. Il est complété par des étiquettes en braille pour chacune d’elle, en surimpression du nom écrit de manière contrastée et en gros caractère.


Le  programme OpenStreetTouch permet non seulement d’extraire des plans de ville  mais aussi d’en extraire les données de transport (bus/car, tramway, métro, train, train interurbain, monorail, ferry, funiculaire) depuis OpenStreetMap, fonction que nous utilisons ici.

Les fichiers numériques ainsi récupérés permettent de produire des objets physiques avec des machines à commande numérique que l’on trouve notamment dans les fablabs.

Les personnes déficientes visuelles s’appuient principalement sur le toucher et la synthèse vocale pour compenser le sens de la vision. Elles peuvent alors se faire des représentations mentales de leur environnement et faciliter leur locomotion.

Compte tenu du panel très large que représente la déficience visuelle entre une vision totalement inexistante et une vue altérée, ainsi que les sensibilités et capacités de chacun que ce soit pour lire le braille ou préférer une information vocalisée, il nous a semblé pertinent de multiplier l’accessibilité en proposant 3 possibilités pour accéder à  l’information (synthèse vocale, écriture en gros caractère, et écriture en braille). 


En répondant aux exigences des uns et des autres à travers un seul objet, ce type de plan pourrait parfaitement avoir sa place dans une station de métro ou un centre de locomotion pour déficients visuels.

Il est composé d’un panneau de bois de 80 x 60 cm sur lequel les deux lignes du métro de Rennes , découpées à la laser,  y sont collées. L’une se caractérise par un toucher rugueux spécifique au papier de verre tandis que l’autre est très lisse grâce au PMMA,  elles sont ainsi immédiatement dissociables au toucher. Une légende en bas à gauche du plan est également présente afin d’identifier chacune des deux lignes. 



Chaque station est représentée par un bouton que l’on peut cliquer pour vocaliser son nom.  Une étiquette est aussi associé à chacune d’elle avec son nom écrit en braille en surimpression du nom écrit en noir et gros caractère.

Pour l'impression des étiquettes, nous avons utilisé la police *Luciole*, spécialement crée pour les mal voyants. Cette police est disponible ici [https://www.luciole-vision.com](https://www.luciole-vision.com). La police *Luciole* est disponible sous licence libre CC BY 4.0.


Le matériau utilisé pour les étiquettes sont des feuilles transparentes pour impression laser. La transparence permet d'imprimer les étiquettes en contraste élevé. Ces feuilles fonctionnent correctement pour l'embossage Braille avec la BrailleRAP.


L’écriture braille ne permet pas de modifier la taille des caractères puisqu’il est indispensable de respecter un écart standard entre les points qui composent chaque caractère afin de rester lisible. C’est une contrainte majeure dans la mesure où le braille prend nécessairement une place importante et écarte d’emblée la réalisation de petits formats si l’on souhaite avoir l’ensemble de l’information sur un même support.


