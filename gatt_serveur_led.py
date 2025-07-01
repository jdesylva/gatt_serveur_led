#!/home/jacques/venv_bt/bin/python3
import RPi.GPIO as GPIO
from gi.repository import GLib
from bluezero import localGATT

# Configuration GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

class LEDService(localGATT.Service):
    def __init__(self):
        super().__init__(
            service_id=0,
            uuid='0000cafe-0000-1000-8000-00805f9b34fb',
            primary=True
        )

    def ajouter_caracteristique_led(self):
        led_char = localGATT.Characteristic(
            service=self,
            uuid='0000feed-0000-1000-8000-00805f9b34fb',
            characteristic_id=0,
            flags=['write'],
            notifying=False,
            value=[],
            write_callback=self.led_write
        )
        self.add_characteristic(led_char)

    def led_write(self, value, options):
        if value == [1]:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("🔴 LED allumée")
        elif value == [0]:
            GPIO.output(LED_PIN, GPIO.LOW)
            print("⚫ LED éteinte")
        else:
            print(f"Valeur inattendue : {value}")

def main():
    led_service = LEDService()
    app = localGATT.Application([led_service])
    app.start()

    # Maintenant que D-Bus a initialisé le service, on ajoute la caractéristique
    led_service.ajouter_caracteristique_led()

    print("🔵 Serveur GATT BLE prêt. Ctrl+C pour quitter.")
    try:
        GLib.MainLoop().run()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("🛑 Arrêt propre du serveur.")

if __name__ == '__main__':
    main()
