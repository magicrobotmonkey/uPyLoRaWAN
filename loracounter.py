import time
import machine
from uPySensors.ssd1306_i2c import Display

def receive(lora):
    print("LoRa Receiver")
    display = Display()
    vcc = machine.ADC(machine.Pin(32))
    vcc.atten(machine.ADC.ATTN_11DB)

    current_packet = 0
    last_packet = 0
    while True:

        try:
            battery = vcc.read()
            if lora.receivedPacket():
                payload = lora.read_payload()
                current_packet = int(payload)
            if current_packet - last_packet == 1:
                msg = "OK ({0})   RSSI: {1}".format(current_packet, lora.packetRssi())
                lora.led_on()
            elif current_packet - last_packet > 1:
                msg = "PACKET GAP:  {0}-{1} RSSI: {2}".format(last_packet, current_packet, lora.packetRssi())
                lora.led_on(False)
            else:
                msg = "MISSING_PACKET:  {0}".format(last_packet)
                lora.led_on(False)
            msg = "{0}   battery: {1}".format(msg, battery)
            lora.println(msg)
            display.show_text_wrap(msg)
            print(msg)
            last_packet = current_packet
            lora.receive()

        except Exception as e:
            print(e)
        machine.sleep(2)

def sendabunch(lora):
    print(lora.getIrqFlags())
    i = 0
    while i < 10000:
        lora.println(str(i))
        print(i)
        i+=1

