#!/home/jacques/venv_bt/bin/python3
import RPi.GPIO as GPIO
from bluezero import peripheral, adapter

# Configuration GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

LED_SERVICE_UUID = '0000cafe-0000-1000-8000-00805f9b34fb'
LED_CHAR_UUID = '0000feed-0000-1000-8000-00805f9b34fb'

def led_write(value, options):
    print(f"Valeur reçue == {value}")
    if value == b'\x01':
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("🔴 LED allumée")
    elif value == b'\x00' :
        GPIO.output(LED_PIN, GPIO.LOW)
        print("⚫ LED éteinte")
    else:
        print(f"Valeur inattendue : {value}")

def main():
    
    adapter_addr = list(adapter.Adapter.available())[0].address
    print(f"Adresse == {adapter_addr}")
    led_server = peripheral.Peripheral(adapter_addr, local_name='LED Server')
    print(f"led_server1 == {led_server}")
    led_server.add_service(srv_id=1, uuid=LED_SERVICE_UUID, primary=True)
    led_server.add_characteristic(srv_id=1, chr_id=1,
                                  uuid=LED_CHAR_UUID,
                                  value=[], notifying=False,
                                  flags=['write'],
                                  write_callback=led_write)
    print(f"led_server2 == {led_server}")
    
    # Le service et la caractéristique sont maintenant enregistrés

    print("🔵 Serveur GATT BLE prêt. Ctrl+C pour quitter.")
    
    try:
        led_server.publish()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("🛑 Arrêt propre du serveur.")

if __name__ == '__main__':
    main()
