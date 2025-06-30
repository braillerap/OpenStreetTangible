## Configuration du Raspberry PI
### Création de l'image système

Avec l'outil [Raspberry Pi Imager](https://www.raspberrypi.com/software/) installer la dernière version de **Raspberry PI OS** en version **lite** sur une carte SD.

vous devez activer une installation personnalisée avec les options suivantes

* creation d'un utilisateur **tactilmap**.
* activation de **ssh**.

```{note}
Pour terminer l'installation, vous aurez besoin de vous connecter au Raspberry PI par le réseau. De manière générale nous réalisons cette opération en connectant un cable ethernet, si vous souhaitez connecter le raspberry pi en wifi, vous devez configurer le wifi avant l'installation
```

Une fois toute les options configurées, vous pouvez lancer la création de l'image sur la carte SD.

### Installation du système

