from machine import Pin
from machine import PWM
import time

count_bar = None

led_red = PWM(Pin(19))
led_green = PWM(Pin(23))
led_blue = PWM(Pin(18))

led_red.duty_u16(0)
led_green.duty_u16(0)
led_blue.duty_u16(0)

def rgb_color(red_value, green_value, blue_value):
    if red_value < 0:
        red_value = 0
    if red_value > 100:
        red_value = 100

    led_red.duty_u16(red_value * 65535 // 100)

    if green_value < 0:
        green_value = 0
    if green_value > 100:
        green_value = 100

    led_green.duty_u16(green_value * 65535 // 100)

    if blue_value < 0:
        blue_value = 0
    if blue_value > 100:
        blue_value = 100

    led_blue.duty_u16(blue_value * 65535 // 100)

button = Pin(27, Pin.IN, Pin.PULL_UP)

led_25   = Pin(13, Pin.OUT)
led_50   = Pin(4, Pin.OUT)
led_75   = Pin(16, Pin.OUT)
led_100  = Pin(17, Pin.OUT)

led_25.off()
led_50.off()
led_75.off()
led_100.off()


#Author: 'Marcos Paulo Pazzinatto'
#Description: 'Button RGB LED'

rgb_color(0, 0, 0)
while True:
  if (button.value()) == False:
    count_bar = (count_bar if isinstance(count_bar, int) else 0) + 1
    if contador_barra > 4:
      contador_barra = 0
    while (button.value()) == False:
      pass
  if contador_barra == 0:
    led_25.off()
    led_50.off()
    led_75.off()
    led_100.off()
  elif contador_barra == 1:
    led_25.on()
    led_50.off()
    led_75.off()
    led_100.off()
  elif contador_barra == 2:
    led_25.on()
    led_50.on()
    led_75.off()
    led_100.off()
  elif contador_barra == 3:
    led_25.on()
    led_50.on()
    led_75.on()
    led_100.off()
  else:
    led_25.on()
    led_50.on()
    led_75.on()
    led_100.on()
  time.sleep(0.05)

