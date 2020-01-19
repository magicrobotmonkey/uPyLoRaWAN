import time
import machine
from uPySensors.ssd1306_i2c import Display



class Wanderer:
    def __init__(self, lora):
        print("LoRa Wanderer")
        self.lora = lora
        self.display = Display()
        self.current_packet = 0
        lora.onReceive(self.listen)
        lora.onTimeout(self.timeout)

    def listen(self, lora, payload):
        msg = "OK!! {}    RSSI {}".format(str(payload), self.lora.packetRssi())
        print(msg)
        self.display.show_text_wrap(msg)
        time.sleep(5)
        lora.led_on()
        self.phone()
        

    def timeout(self, lora, payload):
        msg = "MISSING RESPONSE FOR PACKET {}".format(self.current_packet)
        print(msg)
        self.display.show_text_wrap(msg)
        time.sleep(1)
        lora.led_on(False)
        self.phone()

    def phone(self):
        msg = "PHONING ATTEMPT NUMBER {}".format(self.current_packet)
        self.lora.println(msg)
        print(msg)
        self.lora.receive_single()
        # self.display.show_text_wrap(msg)
        self.current_packet += 1





