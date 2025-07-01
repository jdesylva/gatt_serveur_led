# Serveur GATT pour LED

Ce dépôt contient un script Python qui expose un service Bluetooth Low Energy (GATT) permettant de contrôler une LED connectée à un Raspberry Pi.

## Prérequis
- Python 3
- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)
- [bluezero](https://github.com/ukBaz/bluezero)
- Un Raspberry Pi compatible Bluetooth avec une LED connectée sur la broche GPIO 17

Installez les dépendances Python avec :

**pip install -r requirements.txt**

### Utilisation
Lancez le script avec les privilèges administrateur pour accéder au GPIO et à la pile Bluetooth :

**sudo python3 gatt_serveur_led.py**
Le serveur enregistre un service personnalisé (0000cafe-0000-1000-8000-00805f9b34fb) avec une caractéristique en écriture seulement (0000feed-0000-1000-8000-00805f9b34fb).
Écrire 0x01 allume la LED et 0x00 l’éteint. Il a été testé avec l’application mobile nRF Connect. Utiliser le type de donnée "octet" (byte) avec la valeur b'\x01'

Appuyez sur Ctrl+C pour arrêter le serveur ; le script nettoiera l’état du GPIO lors de la sortie.
