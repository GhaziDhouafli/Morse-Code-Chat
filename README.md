# Morse-Code-Chat
Morse code is a character-encoding scheme that allows operators to send messages using a series of electrical pulses represented as short or long pulses, dots, and dashes.
A-mqtt-publish1.py:
	This Python file represents our publisher, here we have a client named “MorseCode1” whom will connect to the broker www.mqtt-dashboard.com and this client will publish an encrypted message with the morse code to the topic “MorseCode”.
B-mqtt-subscribe.py:
	This python file represents our subscriber, here we have a client named “MorseCode3” whom will connect to the broker www.mqtt-dashboard.com and this client will try to receive every encrypted message from the topic “MorseCode”.
After  it receives it, the subscriber will then add the encrypted message to the output.txt and keeps on listening for another message to come.
C-MorseCoding.py:
	This python file will wait for the message to be written in the output.txt file. After that it will loop each character written in the file and it will choose the right beep based on the it. If it’s a “.” Then we will hear a low-beep, if it’s a “-“ then we will hear a high beep.
