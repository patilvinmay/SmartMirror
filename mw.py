#! python3
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        point="X= "+str(x)+"    Y= "+str(y)
        print(point)
except KeyboardInterrupt:
    print('\n')
