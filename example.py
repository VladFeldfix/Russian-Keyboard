import keyboard

keys = {
    'q':'Й',
    'w':'Ц'
    }

def redo(x):
    press = keys[x]
    keyboard.press('BACKSPACE')
    keyboard.write(press)

while True:
    if keyboard.is_pressed('q'):
        redo('q')
    
    if keyboard.is_pressed('w'):
        redo('w')