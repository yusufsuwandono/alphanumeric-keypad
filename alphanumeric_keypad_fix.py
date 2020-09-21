#code by yusuf suwandono
#follow me in instagram : @yusuf_swnd


import RPi.GPIO as GPIO
import time
import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

x = 0
y= 0
HIGH=1
LOW=0


pesan=""
alphanumeric="1!@.,:?ABCDEFGHIJKLMNOPRSTUVWXY* #"

KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

pin_baris      = [18,23,24,25]
pin_kolom     = [4,17,22,21]

def keypad():
        
    for j in range(len(pin_kolom)):
        GPIO.setup(pin_kolom[j], GPIO.OUT)
        GPIO.output(pin_kolom[j], GPIO.LOW)
        
    for i in range(len(pin_baris)):
        GPIO.setup(pin_baris[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    rowVal = -1
    for i in range(len(pin_baris)):
        tmpRead = GPIO.input(pin_baris[i])
        if tmpRead == 0:
            rowVal = i
                
    if rowVal <0 or rowVal >3:
        return
        
    for j in range(len(pin_kolom)):
            GPIO.setup(pin_kolom[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
    GPIO.setup(pin_baris[rowVal], GPIO.OUT)
    GPIO.output(pin_baris[rowVal], GPIO.HIGH)

    colVal = -1
    for j in range(len(pin_kolom)):
        tmpRead = GPIO.input(pin_kolom[j])
        if tmpRead == 1:
            colVal=j
                
    if colVal <0 or colVal > 3:
        return

    ch11 = KEYPAD[rowVal][colVal]
    time.sleep (0.1)
    return ch11
   

def abjad(Key, index, maksimum_index):
    ch=0
    ch=index
    Char=''
    count=0
    global pesan
    global x
    global y
    global key1
    global passEnter
    while count<20:
        key1=keypad()
        if key1== Key:
            Char=alphanumeric[ch]
            print (Char)
            ch=ch+1
            if ch>maksimum_index:
                ch=index
            count=0
        count=count+1
        time.sleep(0.1)
    pesan+= Char
    print (pesan)
    mylcd.lcd_display_string(pesan,1,0)
    x=x+1
    if x>15:
        x=0 
        y=1

def alphanumeric_keypad():
    pesan=""
    while 1:
        key1=0
        count=0
        key1=keypad()
        if key1 == '1':
            index=0
            maksimum_index=6
            Key='1'
            abjad(Key, index, maksimum_index)
            
        elif key1 == '2':
            index=7
            maksimum_index=9
            Key='2'
            abjad(Key, index, maksimum_index)
            
        elif key1 == '3':
            index=10
            maksimum_index=12
            Key='3'
            abjad(Key, index, maksimum_index)
            
        elif key1 == '4':
            index=13
            maksimum_index=15
            Key='4'
            abjad(Key, index, maksimum_index)

        elif key1 == '5':
            index=16
            maksimum_index=18
            Key='5'
            abjad(Key, index, maksimum_index)

        elif key1 == '6':
            index=19
            maksimum_index=21
            Key='6'
            abjad(Key, index, maksimum_index)

        elif key1 == '7':
            index=22
            maksimum_index=24
            Key='7'
            abjad(Key, index, maksimum_index)

        elif key1 == '8':
            index=25
            maksimum_index=27
            Key='8'
            abjad(Key, index, maksimum_index)

        elif key1 == '9':
            index=28
            maksimum_index=30
            Key='9'
            abjad(Key, index, maksimum_index)


        elif key1 == '*':
            index=31
            maksimum_index=31
            Key='*'
            abjad(Key, index, maksimum_index)


        elif key1 == '0':
            index=32
            maksimum_index=32
            Key='0'
            abjad(Key, index, maksimum_index)

        elif key1 == '#':
            index=33
            maksimum_index=33
            Key='#'
            abjad(Key, index, maksimum_index)


        elif key1== 'D':
            return

alphanumeric_keypad()

