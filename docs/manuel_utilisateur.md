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


Le matériau utilisé pour les étiquettes est du Rhodoïde qui permet de conserver la transparence et l’esthétique de l’ensemble tout en permettant un contraste élevé. 


L’écriture braille ne permet pas de modifier la taille des caractères puisqu’il est indispensable de respecter un écart standard entre les points qui composent chaque caractère afin de rester lisible. C’est une contrainte majeure dans la mesure où le braille prend nécessairement une place importante et écarte d’emblée la réalisation de petits formats si l’on souhaite avoir l’ensemble de l’information sur un même support.


# Étapes de fabrication pas à pas

# Partie logicielle : Open Street Touch & Inkscape

## 1-Extraction des données de lignes de transport avec OpenStreetTouch
* Installer OpenStreetTouch et suivre le tutoriel associé pour extraire les données de transports qui vous intéressent.
 (https://openstreettouch.readthedocs.io/fr/latest/manuel_utilisateur.html) 

 Attention à bien cocher l’option « Polygones pour tracés de lignes », pour avoir deux traits comme contour de ligne et pas un seul !!

![Vue de l’interface OpenStreetTouch avec l’option « polygones pour tracés de lignes » cochée](/IMG/OSM_vue_export_svg.png)

* Extraire l’ensemble des lignes de transport souhaitées sur un seul SVG afin de graver les contours de l’ensemble du plan pour venir ensuite y coller chaque ligne. 

* Extraire ensuite les lignes une à une dans un SVG séparé. On a alors un SVG pour chacune des lignes ce qui permettra de les découper sur des matériaux distincts. 
