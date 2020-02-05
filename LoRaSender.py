from time import sleep
from uPySensors.ssd1306_i2c import Display

display = Display()
def handle(lora, payload):
    print(payload)
    display.show_text_wrap(payload)
        
def send(lora):
    counter = 0
    print("LoRa Sender")

    lora.onReceive(handle)

    while True:
        lora.sleep()
        payload = '{0}'.format(counter)
        print("Sending packet: {}".format(payload))
        display.show_text_wrap("{0} RSSI: {1}".format(payload, lora.packetRssi()))
        lora.println(payload)
        lora.receive()

        counter += 1
        sleep(2)
