# code base: ©2018 Kattni Rembor for Adafruit Industries
#
# complete code @mrbbp 2303
#
# SPDX-License-Identifier: MIT

import time
# lib de l'encodeur rotatif
import rotaryio
# gestion de la config de la carte
import board
# gestion des IO num.
import digitalio
# gestion de l'usb_HID (transformer la carte en device HID)
import usb_hid

# import lib des raccourcis clavier
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode_mac_fr import Keycode
# import lib de la led onboard
import neopixel

boutonEncodeur = digitalio.DigitalInOut(board.GP4)
boutonEncodeur.direction = digitalio.Direction.INPUT
boutonEncodeur.pull = digitalio.Pull.UP

boutonRouge = digitalio.DigitalInOut(board.GP7)
boutonRouge.direction = digitalio.Direction.INPUT
boutonRouge.pull = digitalio.Pull.UP

boutonJaune = digitalio.DigitalInOut(board.GP6)
boutonJaune.direction = digitalio.Direction.INPUT
boutonJaune.pull = digitalio.Pull.UP

boutonVert = digitalio.DigitalInOut(board.GP5)
boutonVert.direction = digitalio.Direction.INPUT
boutonVert.pull = digitalio.Pull.UP

boutonData = digitalio.DigitalInOut(board.GP12)
boutonData.direction = digitalio.Direction.INPUT
boutonData.pull = digitalio.Pull.DOWN

# gestion de la led

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
# éteint la led
led.brightness = 0

# déclaration de l'encodeur
encoder = rotaryio.IncrementalEncoder(board.GP2, board.GP3)

# déclaration du clavier
keyboard = Keyboard(usb_hid.devices)

# état des boutons
boutonEncodeur_state = None
boutonRouge_state = None
boutonVert_state = None
boutonJaune_state = None
last_position = encoder.position


while True:
    current_position = encoder.position
    position_change = current_position - last_position
    if boutonData.value:
        if position_change > 0:
            keyboard.press(Keycode.RIGHT_ARROW)
            led.brightness = .3
            led[0] = (255, 0, 0)
            time.sleep(.04)
            keyboard.release(Keycode.RIGHT_ARROW)
            led.brightness = 0
            print("->", current_position)
        elif position_change < 0:
            keyboard.press(Keycode.LEFT_ARROW)
            led.brightness = .3
            led[0] = (0, 0, 255)
            time.sleep(.04)
            keyboard.release_all()
            led.brightness = 0
            print("<-", current_position)
        last_position = current_position
        if not boutonEncodeur.value and boutonEncodeur_state is None:
            boutonEncodeur_state = "pressed"
        if boutonEncodeur.value and boutonEncodeur_state == "pressed":
            print("boutonEncodeur pressed.")
            # led allumée verte
            led.brightness = .3
            led[0] = (0, 255, 0)
            # envoie le HID
            keyboard.press(Keycode.ENTER)
            keyboard.release_all()
            boutonEncodeur_state = None
            # 1/25 sec et éteint la led
            time.sleep(0.04)
            led.brightness = 0
        if not boutonJaune.value and boutonJaune_state is None:
            boutonJaune_state = "pressed"
        if not boutonVert.value and boutonVert_state is None:
            boutonVert_state = "pressed"
        if not boutonRouge.value and boutonRouge_state is None:
            boutonRouge_state = "pressed"
        if boutonVert.value and boutonVert_state == "pressed":
            print("boutonVert pressed.")
            # led allumée verte
            led.brightness = .3
            led[0] = (0, 255, 0)
            # envoie le HID
            keyboard.press(Keycode.ENTER)
            keyboard.release_all()
            boutonVert_state = None
            # 1/25 sec et éteint la led
            time.sleep(0.04)
            led.brightness = 0
        if boutonJaune.value and boutonJaune_state == "pressed":
            print("boutonJaune pressed.")
            # led allumée jaune
            led.brightness = .3
            led[0] = (255, 255, 0)
            # envoie le HID
            keyboard.press(Keycode.SPACEBAR)
            keyboard.release_all()
            boutonJaune_state = None
            # 1/25 sec et éteint la led
            time.sleep(0.04)
            led.brightness = 0
        if boutonRouge.value and boutonRouge_state == "pressed":
            print("boutonRouge pressed.")
            # led allumée rouge
            led.brightness = .3
            led[0] = (255, 0, 0)
            # envoie le HID (B)
            # keyboard.press(0x05) touche B
            keyboard.press(Keycode.BACKSPACE)
            keyboard.release_all()
            boutonRouge_state = None
            # 1/25 sec et éteint la led
            time.sleep(0.04)
            led.brightness = 0
