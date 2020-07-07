import serial
#import time
import pyautogui
import os
#import subprocess
from os import path
a=0
os.system('say "Welcome to smart application"')
def functions(value):
    if(value=='500006'):
        a=1
    #Music
    if(value=='501006'):
        os.system('say "Music Playing"')
        os.system("music_start")
        while True:    
            ser = serial.Serial("/dev/tty.HC-05-SPPDev")
            ser.flushInput()
            ser_bytes = ser.readline()
            decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            c=str(decoded_bytes)
            print(c)
            if(c=='500006'):
                continue
            if(c == '501006'):
                os.system('say "Volume Up"')
                os.system("vup")
            if(c == '500106'):
                os.system('say "Volume Down"')
                os.system("vless")
            if(c == '510006'):
                os.system('say "Next Song"')
                os.system("music_next")
            if(c == '511006'):
                os.system("music_prev")
            if(c == '511106'):
                os.system('say "Closing music"')
                os.system("music_quit")
                break
                

    #Weather
    if(value=='510006'):
        os.system('say "Opening Siri"')
        os.system('v7')
        os.system('open -a "Siri"')
        while True:
            ser = serial.Serial("/dev/tty.HC-05-SPPDev")
            ser.flushInput()
            ser_bytes = ser.readline()
            decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            c=str(decoded_bytes)
            if(c=='500006'):
                continue
            if(c=='501006'):
                pyautogui.hotkey('fn','space')
            if(c=='510006'):
                os.system('say "Say Bye to close Siri"')
                break
             
    #Mail
    if(value=='511006'):
        os.system('say "Opening your Mail"')
        os.system('open -a "Mail"')
        #time.sleep(3)
        while True:
            ser = serial.Serial("/dev/tty.HC-05-SPPDev")
            ser.flushInput()
            ser_bytes = ser.readline()
            decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            c=str(decoded_bytes)
            if(c=='500006'):
                continue
            if(c=='510006'):
                pyautogui.moveTo(131,255)
            if(c=='501006'):
                pyautogui.moveTo(845,249)
            if(c=='511006'):
                pyautogui.press('down')
                os.system('say "Moving Down"')
            if(c=='501106'):
                pyautogui.press('up')
                os.system('say "Moving Up"')
            if(c=='500106'):
                pyautogui.scroll(-5)
                os.system('say "Scrolling down"')
            if(c=='510106'):
                pyautogui.scroll(5)
                os.system('say "Scrolling Up"')
            if(c=='511106'):
                os.system('pkill "Mail"')
                os.system('say "Closing Mail Application"')
                break
    #News
    if(value=='501106'):
        os.system('say "Opening latest News"')
        os.system('open -a "feedly"')
        pyautogui.moveTo(883,371)
        while True:
            ser = serial.Serial("/dev/tty.HC-05-SPPDev")
            ser.flushInput()
            ser_bytes = ser.readline()
            decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            c=str(decoded_bytes)
            if(c=='500006'):
                continue
            if(c=='501006'):
                pyautogui.scroll(-10)
                os.system('say "Scrolling Down"')
            if(c=='511006'):
                pyautogui.scroll(10)
                os.system('say "Scrolling Up"')
            if(c=='511106'):
                os.system('pkill "feedly"')
                os.system('say "Closing News"')
                break



    #Twitter       
    if(value=='500106'):
        os.system('say "Opening Twitter"')
        os.system('open -a "Twitter"')
        pyautogui.moveTo(523,201)
        pyautogui.hotkey('command','1')
        while True:
            ser = serial.Serial("/dev/tty.HC-05-SPPDev")
            ser.flushInput()
            ser_bytes = ser.readline()
            decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            c=str(decoded_bytes)
            if(c=='500006'):
                continue
            if(c=='501006'):
                pyautogui.press('down')
                os.system('say "Next post"')
            if(c=='500106'):
                pyautogui.hotkey('command','l')
                os.system('say "Liked"')
            if(c=='511006'):
                pyautogui.press('up')
                os.system('say "Previous post"')
            if(c=='511106'):
                os.system('pkill "Twitter"')
                os.system('say "Closing Twitter"')
                break

    #2048 game
    if(value=='511106'):
        os.system('say "Opening 2048 Game"')
        os.system('open -a "2048 Game"' )
        while True:
            ser = serial.Serial("/dev/tty.HC-05-SPPDev")
            ser.flushInput()
            ser_bytes = ser.readline()
            decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            c=str(decoded_bytes)
            if(c=='500006'):
                continue
            if(c=='501006'):
                pyautogui.press('a')
                os.system('say "Left"')
            if(c=='511006'):
                pyautogui.press('d')
                os.system('say "Right"')
            if(c=='510006'):
                pyautogui.press('w')
                os.system('say "Up"')
            if(c=='500106'):
                pyautogui.press('s')
                os.system('say "Down"')
            if(c=='501106'):
                pyautogui.press('r')
                os.system('say "New game"')
            if(c=='511106'):
                #os.system('wmctrl -c "Firefox"')
                os.system('pkill "2048 Game"')
                os.system('say "Closing 2048 Game"')
                break

                

while True:
    ser = serial.Serial("/dev/tty.HC-05-SPPDev")
    ser.flushInput()
    ser_bytes = ser.readline()
    decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    c=str(decoded_bytes)
    print(c)
    functions(c)

