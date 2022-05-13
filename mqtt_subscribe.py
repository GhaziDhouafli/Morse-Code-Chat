import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")), file=open("output.txt", "a"))


mqttBroker = "www.mqtt-dashboard.com"
client = mqtt.Client("MorseCode3")
client.connect(mqttBroker)
client.subscribe("MorseCode")
client.on_message = on_message
client.loop_forever()

