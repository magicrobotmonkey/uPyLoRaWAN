import time
import machine
from uPySensors.ssd1306_i2c import Display
import esp32



class Wanderer:
    def __init__(self, lora):
        print("LoRa Wanderer")
        self.lora = lora
        self.display = Display()
        self.current_packet = 0
        lora.onReceive(self.listen)
        lora.onTimeout(self.timeout)

    def listen(self, lora, payload):
        msg = "OK! {} RSSI {}".format(self.current_packet, self.lora.packetRssi())
        print(msg)
        self.display.show_text_wrap(msg)
        time.sleep(10)
        lora.led_on()
        self.phone()
        

    def timeout(self, lora, payload):
        msg = "MISSING RESPONSE FOR PACKET {}".format(self.current_packet)
        print(msg)
        self.display.show_text_wrap(msg)
        time.sleep(5)
        lora.led_on(False)
        self.phone()

    def phone(self):
        message = []
        id = machine.unique_id()
        message.append('{:02x}{:02x}{:02x}{:02x}'.format(id[0], id[1], id[2], id[3]))
        message.append(str(esp32.hall_sensor()))
        message.append(str(esp32.raw_temperature()))
        message.append(str(self.current_packet))
        msg = "^".join(message)
        self.lora.println(msg)
        print(msg)
        self.lora.receive_single()
        # self.display.show_text_wrap(msg)
        self.current_packet += 1





