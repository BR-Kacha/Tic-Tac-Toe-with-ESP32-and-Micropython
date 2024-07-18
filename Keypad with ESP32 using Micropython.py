# Matrix Keypad
# NerdCave - https://www.youtube.com/channel/UCxxs1zIA4cDEBZAHIJ80NVg - Subscribe if you found this helpful.
# Github - https://github.com/Guitarman9119

from machine import Pin
import time

# Create a map between keypad buttons and characters
matrix_keys = [['1', '2', '3'],
               ['4', '5', '6'],
               ['7', '8', '9'],
               ['*', '0', '#']]

# PINs according to schematic - Change the pins to match with your connections
keypad_rows = [27, 26, 25, 33]
keypad_columns = [13, 12, 14]

# Create two empty lists to set up pins ( Rows output and columns input )
col_pins = []
row_pins = []

# Loop to assign GPIO pins and setup input and outputs
for x in range(0,4):
    row_pins.append(Pin(keypad_rows[x], Pin.OUT))
    row_pins[x].value(1)
for y in range(0,3):
    col_pins.append(Pin(keypad_columns[y], Pin.IN, Pin.PULL_DOWN))
    col_pins[y].value(0)
    
##############################Scan keys ####################
    
print("Please enter a key from the keypad")
    
def scankeys():  
    for row in range(4):
        for col in range(3):
            row_pins[row].on()
            key = None
            
            if col_pins[col].value() == 1:
                print("You have pressed:", matrix_keys[row][col])
                key_press = matrix_keys[row][col]
                time.sleep(0.3)
                    
        row_pins[row].off()

while True:
    scankeys()
