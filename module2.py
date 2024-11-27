from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)

def on_release(key):
    if key==Key.esc:
        print(keys)
        return False
    
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()