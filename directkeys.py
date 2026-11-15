
import time
from pynput.keyboard import Controller, Key

keyboard = Controller()

# Mac-compatible keyboard mappings
KEYS = {
    0x4D: Key.right,  # Accelerator
    0x4B: Key.left,   # Brake
    0x11: 'w',        # W key
}


def PressKey(hexKeyCode):
    key = KEYS.get(hexKeyCode)

    if key is not None:
        keyboard.press(key)


def ReleaseKey(hexKeyCode):
    key = KEYS.get(hexKeyCode)

    if key is not None:
        keyboard.release(key)


if __name__ == "__main__":
    print("Testing keyboard input...")
    print("Click the game window first.")
    print("Press Ctrl+C in the terminal to stop.")

    try:
        while True:
            PressKey(0x4D)
            time.sleep(1)

            ReleaseKey(0x4D)
            time.sleep(1)

    except KeyboardInterrupt:
        ReleaseKey(0x4D)
        ReleaseKey(0x4B)
        ReleaseKey(0x11)
        print("\nKeyboard test stopped.")

