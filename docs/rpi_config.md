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
sudo apt install git
```

Installer la synthese vocale **espeack-ng**
```
sudo apt install espeack-ng
```

Installer l'extension **mbrola** avec les voix française.
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
