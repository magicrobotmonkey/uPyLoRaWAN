#import LoRaDuplexCallback
#from  loracounter import receive
#from LoRaSender import send, handle
#import LoRaReceiver
from phonehome import Wanderer
import config_lora
from sx127x import SX127x
from controller_esp32 import ESP32Controller


controller = ESP32Controller()
lora = controller.add_transceiver(SX127x(name = 'LoRa'),
                                  pin_id_ss = ESP32Controller.PIN_ID_FOR_LORA_SS,
                                  pin_id_RxDone = ESP32Controller.PIN_ID_FOR_LORA_DIO0,
                                  pin_id_RxTimeout = ESP32Controller.PIN_ID_FOR_LORA_DIO1)


wanderer = Wanderer(lora)
wanderer.phone()
