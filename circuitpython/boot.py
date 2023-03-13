# This example is for a Circuit Playground,
# or any board with buttons that are connected to +V when pressed.
# désactive l'usb, le REPL et le midi sur la carte
# il faut un bouton connecté au + sur le GP4
# lorsque le bouton est appuyé, la carte fait apparaitre de device usb et l'interface de prog


import storage, usb_cdc
import board, digitalio

# On the Circuit Playground, pressing an on-board button
# connects the button to +V and GP4.
button = digitalio.DigitalInOut(board.GP11)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# Disable devices only if button is not pressed.
if not button.value:
  storage.disable_usb_drive()
  usb_midi.disable()
  usb_cdc.disable()
