#!/usr/bin/env python3
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
import time


class LCD16x2(CharLCD):
    def __init__(self):
        super().__init__(
            pins_data=[25, 24, 23, 18],
            numbering_mode=GPIO.BCM,
            pin_rw=None,
            pin_rs=7,
            pin_e=8,
            cols=16,
            rows=2
        )

    def nettoyer(self):
        self.clear()
        self.write_string("Merci et\n\rAu revoir !")
        time.sleep(2)
        self.close(clear=True)
