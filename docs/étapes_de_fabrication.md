# Étapes de fabrication

## Partie logicielle : Open Street Touch & Inkscape

### 1-Extraction des données de lignes de transport avec OpenStreetTouch
* Installer OpenStreetTouch et suivre le tutoriel associé pour extraire les données de transports qui vous intéressent.
 (https://openstreettouch.readthedocs.io/fr/latest/manuel_utilisateur.html) 

 Attention à bien cocher l’option « Polygones pour tracés de lignes », pour avoir deux traits comme contour de ligne et pas un seul !!

![Vue de l’interface OpenStreetTouch avec l’option « polygones pour tracés de lignes » cochée](/IMG/OSM_vue_export_svg.png)

* Extraire l’ensemble des lignes de transport souhaitées sur un seul SVG afin de graver les contours de l’ensemble du plan pour venir ensuite y coller chaque ligne. 

* Extraire ensuite les lignes une à une dans un SVG séparé. On a alors un SVG pour chacune des lignes ce qui permettra de les découper sur des matériaux distincts. 

* Extraire également le nom des stations pour chacune des lignes avec le bouton "Enregistrer les stations en TXT"

* ''TO DO : Ajouter ICI les fichiers source issus de l'extraction''


### 2- Transformation des fichiers avec Inkscape
Les SVG peuvent être modifiés avec des logiciels vectoriels comme Inkscape (logiciel libre et gratuit).


#### 2-1 Vérification des fichiers

* Ouvrir le svg de l'ensemble des lignes avec Inkscape et passer en mode "vue des contours"

  Vue>Mode d’affichage>Contours ou en anglais View>Display mode>Outline 
  
  Si vous avez bien coché l'otion "Polygones pour tracés" lors de l'export vous devriez avoir les contours de lignes visibles comme sur cette image.
  
  ![Vue de l’interface OpenStreetTouch avec l’option « polygones pour tracés de lignes » cochée](/IMG/Export_option_polygone_traces_lignes_active.png)
  
  Si vous avez une image avec un seul trait représentant la ligne de métro comme sur l'image ci-dessous, recommencer l'export dans OpenStreetTouch
  
  ![Vue de l’export SVG avec l’option « polygones pour tracés de lignes » qui n'est pas cochée](/IMG/Export_option_polygone_traces_inactive.png)
  


#### 2-2 Mise à l'échelle du plan
* Mettre le SVG à l’échelle du plan choisi (redimensionner le document à la taille souhaitée)

  Fichier>propriétés du document ou en anglais File>document properties>Display
  
  Ajuster la taille du document aux dimensions souhaitées (ici 800 x600 mm)
  
  Sélectionner ensuite l'ensemble des lignes (CTL+A) et agrandir à la taille souhaitée pour s'ajuster au format du document
  
#### 2-3 Préparation des fichiers pour la découpe laser
* Découper chacune des lignes au niveau des croisement et /ou au niveau des stations de correspondance (afin de ne conserver qu’une réprésentation de station (cercle) quelque soit le nombre de lignes qui s’arrête à cette station). ''' (TO DO : A décrire techniquement avec Inkscape)'''
* Simplifier ou décaler les lignes quand elles se touchent pour faciliter la lisibilité
* Redessiner les stations en fin de ligne pour les remplacer par des cercles si vous le jugez nécessaire
* Faire un cercle plus grand pour chacune des stations de correspondance
* Ajuster la taille des cercle de chaque station et ajouter un cercle interne à chaque station pour faire une découpe qui correspond à la taille du bouton que vous avez choisi. Pour notre exemple, les cercles externes font Xmm et les cercles internes Xmm
* '' TO DO : Ajouter ICI les fichiers source transformés''

## Fabrication du plan de métro à partir des fichiers retravaillés

### Fichiers sources extraits d’open street map et retravaillés dans Inkscape
- l'ensemble du plan de métro retravaillé (les deux lignes : ligne A et ligne B) sur un seul fichier (à graver)
- les deux lignes de métro sur des fichiers séparés : les deux lignes redécoupées en plusieurs parties sur les jonctions de stations de correspondance
- les deux stations de correspondance :
- les deux légendes : 
- le fichier avec les noms des stations écrit en 24 points police Arial black ou Luciole : 


### Fichier 3D à imprimer
Imprimer en PLA :

* le fichier 3D qui sert à faire sortir le câble pour alimenter le prototype
* Le passe cable 


**Machines et outils**
* Braillerap
* découpe laser
* imprimante laser à jet d’encre. (Attention à utiliser une photocopieuse laser sinon le rhodoïde risque de casser la machine!)
* perceuse 
* fer à souder
* multimètre
* serre joints ou grosses pinces


**Consommables**

**Partie design**
* étain
* colle cyano pour coller plexi sur bois
* colle à bois
* papier de verre (grammage 80)
* PMMA blanc 5mm
* 2 plaques de contreplaqué de peuplier de 5mm d'épaisseur de 80 cm x 60cm 
* contreplaqué de peuplier 3mm pour découpe d’une ligne de métro (format adapté à la taille de la découpeuse laser) et légende
* 1 tasseau de 53,5cm (3x5cm)
* 1 tasseau de 41cm
* 2 tasseaux de 80 cm (3x5cm)
* Feuilles de rhodoïde pour imprimer les étiquettes brailles
* 8 x inserts M6 x23mm (chevilles laitons pour tige filetée diam 6mm)
* 8 x Vis M6
* bombe de peinture noire
* bombe de peinture rouge




**Circuit électronique**

* une raspberry pi (version?)
* carte clavier
* cable USB (type?)
* X nb de boutons vissables (ref?)
* fil pour connecter les boutons à la raspi (deux couleurs différentes, pour dissocier chaque ligne)
* connecteurs (?)
* ampli speaker (REF?)
* prise mini jack audio
* connecteurs



### Préparation des éléments pour la découpe laser

**Plan d'ensemble**


Importer le fichier global retravaillé  représentant les deux lignes de métro, sur le logiciel de la découpe laser. 

Créer deux calques pour travailler sur le fichier. L’un sert pour graver le contour des lignes servant de référence pour le collage, et l’autre sert à découper les cercles des stations.

Graver le contour de l’ensemble du plan des deux lignes de métros sur la grande plaque de 80 x60cm avec le SVG correspondant, et couper les cercles internes (stations, légendes) prévus pour y insérer les boutons. 

 ![Plan avec traçage des contours des deux lignes de métro sur la plaque de peuplier 80cm x60cm ](/IMG/gravure_et_percage_plan_global_laser.jpg)


**Découpe des lignes de transport**

Découper ensuite chaque ligne de métro redécoupée en plusieurs parties numériquement (dans Inkscape) (cf:transformation des fichiers) sur  leur matériau respectif (Peuplier 3mm et PMMA blanc 3mm). Préférer la ligne la plus courte ou la plus simple pour le matériau bois/papier de verre puisqu’elle nécessite plus de travail. Pour notre cas, nous choisissons la ligne A. (JF Kennedy-Poterie)

Ne pas enlever le plastique protecteur du PMMA lors de la découpe.


To do : ajouter photos 


Découper ensuite le papier de verre à la découpe laser avec les fichiers de la ligne A qui a déjà été  découpé sur le peuplier 3 mm


**Découpe des stations de correspondance et des légendes**

Découper les stations de correspondance qui ont un cercle externe légèrement agrandi dans du peuplier 5mm. ***(ajouter diamètre)***

Découper également la légende pour les deux lignes. (une avec le papier de verre collé sur le bois et l’autre en PMMA)




**Collage du papier de verre sur la ligne A**

Coller la ligne découpée dans le papier de verre sur sa ligne correspondante en bois (ligne A) avec la colle à bois



### Peinture

Peindre à la bombe de couleur noire la ligne en papier de verre.

Peindre à la bombe rouge les deux stations de correspondances



### Préparation du chassis du plan

* Mettre le plan 80 X60 face gravée contre une table (propre !).

* Placer les tasseaux découpés à la bonne taille sur le cadre de la plaque. Dessiner au crayon à papier leur contour pour bien avoir le repère au moment du collage

* Coller les tasseaux avec la colle à bois et les maintenir en place avec des pinces ou des serre-joints. Pour ne pas faire de marquage ou déformer les tasseaux avec les pinces et étaux, ajouter des plaue de protection entre le tasseau et la pince de serrage.
Procéder en plusieurs étapes si nécessaire en laissant sécher un minimum avant d'enlever les pinces et les serre-joints.


![Collage tasseaux](/IMG/collage_tasseaux.jpg)

![Finalisation collage tasseaux](/IMG/finalisation_collage_tasseaux.jpg)


* Percer 8 trous pour ajouter les inserts (1 à chaque coin et 1 entre chaque extrémité)

 ![Plan global gravé et percé monté sur chassis avec inserts ajoutés pour le refermer par dessous](/IMG/plan_global_grave_et_perce_monte_sur_chassis_avec_inserts.jpg)
 


### Collage des lignes de métro

* Coller les deux lignes de métro découpées à la laser sur le plan

* Coller ensuite chacune des lignes en vous repérant à la gravure. Utiliser la colle à bois pour la ligne A en peuplier et la colle cyano pour la ligne B en PMMA (enlever la protection sur la face qui sera collée juste avant d’appliquer la colle . 

* Coller ensuite les cercles correspondant aux stations de correspondance ici peintes à la bombe de peinture rouge.

### Assemblage et collage des deux lignes et des deux stations de correspondance sur le plan
- Avec la colle cyano, coller la ligne B en PMMA. 
- Avec la colle à bois coller la ligne A préparée avec le papier de verre peint en noir


### Préparation des étiquettes

#### Préparation du fichier
Préparer le fichier contenant l’ensemble du nom des stations  avec les consignes suivantes :
- redimensionner la taille de la police sur 24 pts
- Changer la police sur Arial black ou Luciole (TO DO: dire quelle police on a choisi)
- Remettre en page les noms de manière à ce qu’ils ne soient pas coupés.
- Laisser un espace entre chaque ligne. (TO DO: de combien?)


TO DO : mettre le fichier exemple sur lequel nous avons travaillés.


#### Impression des noms sur les étiquettes
Une fois prêt , imprimer en noir avec l’imprimante laser le fichier sur du papier Rhoidoïde (papier plastique transparent généralement utilisé pour les rétroprojecteurs. Prévoir de les faire en double ou triple au cas où il y ait des ratés ...

Effectuer la configuration des marges avant de faire l’impression des caractères en noir sur l’imprimante laser. (TO DO: Préciser quelle marge et quels réglages ont été fait fait pour l'impression)

Attention il ne faut pas faire les impressions sur une imprimante qui n’est pas laser au risque d’endommager la machine !! Il est impératif de le faire sur une imprimante laser. 

#### Impression brailles
Une fois les noms imprimés sur le rhodoïde , préparer l’impression en braille avec les consignes suivante : 

- Dans le logiciel AccessBrailleRap, ajuster les marges de manière à ce que le braille se cale sur le nom imprimé en noir. Cette étape est un peu délicate et nécessite des ajustements en faisant des tests préalables.
Pour notre cas, nous avons cette configuration (TO DO : impression écran de la config ou explications sur la manip pour le calage)

- Quand le calage est satisfaisant, on peut alors lancer l’embossage avec la machine braillerap sur les rhodoïdes préparés.

#### Découpe des étiquettes
- Découper ensuite les étiquettes ligne par ligne de préférence à l’aide d’un massicot sinon cutter ou ciseaux.
- Finaliser la découpe pour les séparer verticalement à l’aide d’un cutter ou de ciseaux en laissant toujours la même marge en début de mot et à la fin si possible


![Etiquette imprimée en caractère noir avec surimpression braille ](/IMG/etiquette_braille1_Clemenceau.jpg)


## Montage du circuit électronique
### Préparation des boutons
- Étamer les boutons
- Mesurer la longueur de fil nécessaire entre chaque emplacement de bouton (trous des stations) jusqu'à l'emplacement de la carte clavier . Enlever la longueur de fil des fils des connecteurs pour avoir la bonne longueur. Prévoir quelqus cm de plus
- Souder le fil intermédiaire (rallonge) entre le connecteur et le bouton comme sur cette photo.
- Préparer l'ensemble des boutons pour une ligne pour commencer en s'assurant d'avoir la même couleur de fil pour tous les boutons de cette ligne. On prendra une autre couleur pour la 2 e ligne.



### Montage des boutons sur le plan
- Insérer la rondelle sur le bouton pour qu'elle se trouve sous la plaque . Insérer ensuite le bouton avec sa rondelle par dessous et le fixer à la main (sans clé pour commencer)
- Procéder ainsi pour tous les botuons de l'ensemble de la ligne

### Connecter les connecteurs de chaque bouton à la carte clavier
- Positionner de manière provisoire la carte clavier dans l'espace libre et assurez-vous que les connecteurs de chaque boutons puissent l'atteindre 
- Connecter les connecteurs des boutons si possible dans l'ordre es stations de la ligne

### Plan fritzing du schéma électronique
Alimentation 12V => régulateur de tension 5V (?, quelle ref ?) => Raspi (version?)
Raspi USB vers Clavier (ref) =>connecteurs boutons (Type câble?)
Sortie audio raspi vers Ampli (ref?) (Type câble ?)
Alimentation 12V (ampérage?)  => Ampli=>Speaker

### Montage sur l'envers de la plaque du plan de métro





