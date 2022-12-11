import sys
import signal
import time
import pyautogui


def exit_s(signum, frame):
    print('exit')
    sys.exit()

def main():
    try:
        pyautogui.click(1000, 600)
    for i in range(500):
        print(i)
        pyautogui.press('z')
        time.sleep(1.5)
        pyautogui.press('down')
        time.sleep(1.5)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_s)                                
    signal.signal(signal.SIGTERM, exit_s)
    main()