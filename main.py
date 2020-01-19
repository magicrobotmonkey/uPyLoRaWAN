#import LoRaDuplexCallback
#from  loracounter import receive
#from LoRaSender import send, handle
#import LoRaReceiver
#from phonehome import Wanderer
import config_lora
from sx127x import SX127x
from controller_esp32 import ESP32Controller


controller = ESP32Controller()
lora = controller.add_transceiver(SX127x(name = 'LoRa'),
                                  pin_id_ss = ESP32Controller.PIN_ID_FOR_LORA_SS,
                                  pin_id_RxDone = ESP32Controller.PIN_ID_FOR_LORA_DIO0,
                                  pin_id_RxTimeout = ESP32Controller.PIN_ID_FOR_LORA_DIO1)


#wanderer = Wanderer(lora)
#wanderer.phone()

#loracounter.receive(lora)



#LoRaDuplexCallback.duplexCallback(lora)
#LoRaPingPong.ping_pong(lora)
#LoRaSender.send(lora)
#LoRaReceiver.receive(lora)

last_packet = 0
def handle(lora, payload):
    global last_packet
    lora.println("received")
    print(payload)
    try:
        current_packet = int(str(payload.decode()).split(" ")[-1])
    except Exception as e:
        print(e)
        current_packet = 800813
    if current_packet != last_packet + 1:
        print("miss at {} - {}".format(last_packet, current_packet))
    last_packet = current_packet
    lora.receive()

def timeout(lora, payload):
    print("timeout")

lora.onReceive(handle)
lora.onTimeout(timeout)
lora.receive()
