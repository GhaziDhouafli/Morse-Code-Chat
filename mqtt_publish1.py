import paho.mqtt.client as mqtt
import time

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ': '.......'}

mqttBroker = "www.mqtt-dashboard.com"
client = mqtt.Client("MorseCode1")
client.connect(mqttBroker)


message=input("Enter Your message:")
MCmessage= " ".join(MORSE_CODE_DICT[c] for c in message.upper())
client.publish("MorseCode", MCmessage)
print("Just published " + str(message) + " to Topic MorseCode")
time.sleep(3)

