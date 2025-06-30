## Configuration du Raspberry PI
### Création de l'image système

Avec l'outil [Raspberry Pi Imager](https://www.raspberrypi.com/software/) installer la dernière version de **Raspberry PI OS** en version **lite** sur une carte SD.

vous devez activer une installation personnalisée avec les options suivantes

* Nom d'hote **subwaymap**
* creation d'un utilisateur **tactilmap** avec un mot de passe.
* activation de **ssh**.

```{note}
Pour terminer l'installation, vous aurez besoin de vous connecter au Raspberry PI par le réseau. De manière générale nous réalisons cette opération en connectant un cable ethernet, si vous souhaitez connecter le raspberry pi en wifi, vous devez configurer le wifi avant l'installation
```

Une fois toute les options configurées, vous pouvez lancer la création de l'image sur la carte SD.

### Installation du système

* Connecter la carte shapeless_rp2040_40keys sur le Raspberry Pi avec un cable micro USB.
* Connecter le Raspberry Pi au réseau ethernet si besoin
* Brancher le cable USB micro d'alimentation du Raspberry PI
* Brancher la sortie audio du Raspberry PI sur un système audio avec un cable jack.

Une fois le Raspberry PI démarrer, connecter vous au Raspberry PI en ouvrant une console et en utilisant la commande :
```
ssh tactilmap@subwaymap.local
```
le Raspberry PI vous demande alors le mot de passe associé au compte **tactilmap**. Le mot de passe a été configuré au moment de la création de l'image du système.

ensuite a l'aide de l'outil **raspi_config** étendre la partition à l'ensemble de la carte SD et redémarrer le raspberry PI.
```
sudo raspi_config
```

Le Raspbery PI est désormais prêt pour l'installation des logiciels necessaires pour l'utilisation avec la carte tactile.

### Installation des logiciels

Connecter vous au Raspberry PI :
```
ssh tactilmap@subwaymap.local
```

Installer les logiciels avec les commandes :
```
sudo apt update
sudo apt upgrade
sudo apt install git nano
```

Installer la synthese vocale **espeack-ng**
```
sudo apt install espeack-ng
```

Installer l'extension **mbrola** avec les voix françaises.
```
mkdir contrib
cd contrib
wget https://raspberry-pi.fr/download/espeak/mbrola3.0.1h_armhf.deb -O mbrola.deb
sudo dpkg -i mbrola.deb
sudo apt install mbrola-fr1 mbrola-fr2 mbrola-fr3 mbrola-fr4
```

Vous pouvez ensuite tester la synthèse vocale à l'aide des commandes:
```
espeak-ng -v mb-fr1 "Bonjour tout le monde"
espeak-ng -v mb-fr4 "Bonjour tout le monde"
```

### Installation du logiciel speakerkeyboard

le logiciel [speakerkeyboard](https://github.com/crocsg/speakerkeyboard) permet de déclencher la lecture d'un message en synthèse vocale lors de l'appuie sur une touche du clavier. En utilisant la carte **shapeless_rp2040_40keys** il est possible de simuler l'appuie sur une touche d'un clavier en appuyant sur un des boutons de la carte tactile.

```
cd /home/tactilmap
git clone https://github.com/crocsg/speakerkeyboard.git
cd speakerkeyboard
python -m venv venv
source ./venv/bin/activate
pip install -r requirement.txt
```

Le logiciel est utilisable uniquement en mode **root** dans la mesure ou nous utilisons le module python **keyboard** pour intercepter les évenements clavier.

Pour lancer le logiciel
```
sudo bash
source ./venv/bin/activate
python kspeaker.py
```

### Configurer les noms des stations

Pour réaliser la configuration, les boutons de la carte tactile doivent êtrent branchés sur la carte **shapeless_rp2040_40keys** et la carte **shapeless_rp2040_40keys** doit être relié en usb sur le Raspberry PI.

Lancer le logiciel
```
sudo bash
source ./venv/bin/activate
python kspeaker.py
```

Lors de l'appuie sur un bouton de la carte tactile, le logiciel affiche le **code clavier**, le texte associé. Si un texte est associé à la touche, la synthèse vocale se déclenche et lit le texte en audio.

Pour configurer un message, arreter le logiciel avec `CTR-C`, vous devez ensuite éditer le fichier **kspeaker.json** pour entrer le **code clavier** et le texte associé dans la section **messages**.

Le fichier **configuration.json** pour la carte tactile du métro de Rennes est donné ici a titre d'exemple.
```
{
    "device": "",
    "speed": 100,
    "volume": 40,
    "voice": "mb-fr4",
    "sync":0,
    "messages": {
	"49":"J.F Kénnédy, ligne A",
	"5" :"Villejean Université, ligne A",
	"2" :"Pontchaillou, ligne A",
	"4" :"Anatole France, ligne A",
	"6" :"Sainte Anne, ligne A et B",
	"50":"République, ligne A",
	"7" :"Charles de Gaulles, ligne A",
	"3" :"Gares, ligne A et B",
	"45":"Jacques Cartier, ligne A",
	"44":"Clémenceau, ligne A",
	"46":"Henri Fréville, ligne A",
	"47":"Italie, ligne A",
	"38":"Triangle, ligne A",
	"48":"Le Blaune, ligne A",
	"37":"La poterie, ligne A",
	
	"20":"Saint Jacques Gaité, ligne B",
	"17":"La Courrouze, ligne B",
	"19":"Mabilais, ligne B",
	"22":"Saint Germain, ligne B",
	"24":"Jules Ferry, ligne B",
	"23":"Gros Chêne, ligne B",
	"25":"Joliot Curie  Chateaubriand, ligne B",
	"32":"Beaulieu université, ligne B",
	"9" :"Césson Via Silva, ligne B",
	"10":"Atalante, ligne B",
	"33":"Cleunay, ligne B",
	"31":"Colombier, ligne B",
	"34":"Les Gayeulles, ligne B"
    }
}
```
Vous pouvez remarquer que certain nom on été modifié pour mieux correspondre à la phonétique francaise et permettre une meilleur compréhension de la synthèse vocale. Notamment **Kennedy** a été transformé en **Kénnédy**, **Le Blosne** a été transfomé en **Le Blaune**.

