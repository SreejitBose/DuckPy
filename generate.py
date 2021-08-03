import os
import sys

if(len(sys.argv)<2):
    print("provide I/P file")
    exit(0)

if os.path.isfile('code.py'):
    os.system('rm code.py')
out=open("code.py","a")
out.write("import time\nimport board\nimport digitalio\nimport usb_hid\nfrom adafruit_hid.keyboard import Keyboard\nfrom adafruit_hid.keyboard_layout_us import KeyboardLayoutUS\nfrom adafruit_hid.keycode import Keycode\n\nkeyboard = Keyboard(usb_hid.devices)\nkeyboard_layout = KeyboardLayoutUS(keyboard)\n\nled = digitalio.DigitalInOut(board.LED)\nled.direction = digitalio.Direction.OUTPUT\n\n")
inp=open(sys.argv[1],"r")
prev=None

keys={'ENTER':'ENTER','CTRL':'CONTROL','SHIFT':'SHIFT','ALT':'ALT','GUI':'GUI','UP':'UP_ARROW','UPARROW':'UP_ARROW','DOWN':'DOWN_ARROW','DOWNARROW':'DOWN_ARROW','LEFT':'LEFT_ARROW','LEFTARROW':'LEFT_ARROW','RIGHT':'RIGHT_ARROW','RIGHTARROW':'RIGHT_ARROW','DELETE':'DELETE','PAGEUP':'PAGE_UP','PAGEDOWN':'PAGE_DOWN','HOME':'HOME','ESC':'ESCAPE','ESCAPE':'ESCAPE','INSERT':'INSERT','TAB':'TAB','END':'END','CAPSLOCK':'CAPS_LOCK','F1':'F1','F2':'F2','F3':'F3','F4':'F4','F5':'F5','F6':'F6','F7':'F7','F8':'F8','F9':'F9','F10':'F10','F11':'F11','F12':'F12','SPACE':'SPACE','NUMLOCK':'KEYPAD_NUMLOCK','PRINTSCREEN':'PRINT_SCREEN'}
for line in inp:
    s=line[:-1]
    l=s.split()
    if (l[0]=='REPEAT'):
        for i in range(int(l[1])):
            out.write(prev)
    elif (l[0]=='DELAY'):
        fl=float(l[1])
        fl=str(fl/10)
        temp="time.sleep("+fl+")\n"
        prev=temp
        out.write(temp)
    elif (l[0]=='REM'):
        temp="#"+l[1]
        for i in range(2,len(l)):
            temp=temp+" "+l[i]
        temp=temp+"\n"
        prev=temp
        out.write(temp)
    elif (l[0]=='STRING'):
        temp="keyboard_layout.write(\""+l[1]
        for i in range(2,len(l)):
            temp=temp+" "+l[i]
        temp=temp+"\")\n"
        prev=temp
        out.write(temp)
    elif (l[0]=='BLINK'):
        temp=None
        if(len(l)==1):
            temp="led.value=True\ntime.sleep(.5)\nled.value=False\ntime.sleep(.5)\n"
        else:
            fl=float(l[1])
            fl=str(fl/10)
            temp="led.value=True\ntime.sleep("+fl+")\nled.value=False\ntime.sleep("+fl+")\n"
        prev=temp
        out.write(temp)
    elif (l[0] in keys):
        temp="keyboard.send(Keycode."+keys[l[0]]
        for i in range(1,len(l)):
            if(l[i] in keys):
                temp=temp+",Keycode."+keys[l[i]]
            else:
                temp=temp+",Keycode."+l[i].upper()
        temp=temp+")\n"
        prev=temp
        out.write(temp)
    else:
        print("command not found--"+l[0])
        inp.close()
        out.close()
        exit(0)
inp.close()
out.close()
