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


### 2- Transformation des fichiers
Les SVG peuvent être modifiés avec des logiciels vectoriels comme Inkscape (logiciel libre et gratuit).

* Ouvrir le svg de l'ensemble des lignes avec Inkscape et passer en mode "vue des contours"

  Vue>Mode d’affichage>Contours ou en anglais View>Display mode>Outline 
  
  Si vous avez bien coché l'otion "Polygones pour tracés" lors de l'export vous devriez avoir les contours de lignes visibles comme sur cette image.
  
  ![Vue de l’interface OpenStreetTouch avec l’option « polygones pour tracés de lignes » cochée](/IMG/Export_option_polygone_traces_lignes_active.png)
  
  Si vous avez une image avec un seul trait représentant la ligne de métro comme sur l'image ci-dessous, recommencer l'export dans OpenStreetTouch
  
  ![Vue de l’export SVG avec l’option « polygones pour tracés de lignes » qui n'est pas cochée](/IMG/Export_option_polygone_traces_inactive.png)
  
 
* Mettre le SVG à l’échelle du plan choisi (redimensionner le document à la taille souhaitée)

  Fichier>propriétés du document ou en anglais File>document properties>Display
  
  Ajuster la taille du document aux dimensions souhaitées (ici 800 x600 mm)
  
  Sélectionner ensuite l'ensemble des lignes (CTL+A) et agrandir à la taille souhaitée pour s'ajuster au format du document
  
  
* Découper chacune des lignes au niveau des croisement et /ou au niveau des stations de correspondance (afin de ne conserver qu’une réprésentation de station (cercle) quelque soit le nombre de lignes qui s’arrête à cette station).
* Simplifier ou décaler les lignes quand elles se touchent pour faciliter la lisibilité
* Redessiner les stations en fin de ligne pour les remplacer par des cercles si vous le jugez nécessaire
* Faire un cercle plus grand pour chacune des stations de correspondance
* Ajuster la taille des cercle de chaque station et ajouter un cercle interne à chaque station pour faire une découpe qui correspond à la taille du bouton que vous avez choisi. Pour notre exemple, les cercles externes font Xmm et les cercles internes Xmm

