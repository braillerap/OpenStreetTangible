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

Une fois le Raspberry PI démarrer, connecter vous au Raspberry PI en ouvrant une console et en utilisant la commande :
```
ssh tactilmap@subwaymap.local
```
le Raspberry PI vous demande alors le mot de passe associé au compte **tactilmap**. Le mot de passe a été configuré au moment de la création de l'image du système.
