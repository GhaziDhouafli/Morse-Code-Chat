from playsound import playsound
import time
import os

def play_morse_code(message):
    for c in message:
        if c == ".":
            playsound(r"C:\\Users\\ASUS\\Desktop\\low-beep.mp3")
            time.sleep(0.5)
        elif c == "-":
            playsound(r"C:\\Users\\ASUS\\Desktop\\high-beep.mp3")
            time.sleep(0.5)
        else:
            time.sleep(5)

while True:
    if os.stat("output.txt").st_size != 0:
        break
time.sleep(5)
f = open("output.txt", 'r')
data = f.readlines()
msg=data[1][:-2]
print(msg)
play_morse_code(msg)
f.truncate(0)