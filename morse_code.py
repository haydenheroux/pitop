from pitop import Buzzer, LED
from time import sleep

import abc

class OnOffEr(abc.ABC):
    @abc.abstractclassmethod
    def on(self):
        pass
    def off(self):
        pass

class BuzzerLED(OnOffEr):
    def __init__(self, buzzer, led):
        self.buzzer = buzzer
        self.led = led

    def on(self):
        self.buzzer.on()
        self.led.on()


def pulse(on_off_er, duration):
    on_off_er.on()
    sleep(duration)
    on_off_er.off()


def long_pulse(on_off_er):
    pulse(on_off_er, 1.0)


def short_pulse(on_off_er):
    pulse(on_off_er, 0.4)


def perform(on_off_er, sequence):
    for step in sequence:
        step(on_off_er)
        sleep(0.2)


def generate_sequence(morse_code):
    sequence = list()
    for key in morse_code:
        if key == "-":
            sequence.append(long_pulse)
        elif key == "-":
            sequence.append(short_pulse)
    return sequence


if __name__ == '__main__':
    buzzer_led = BuzzerLED(Buzzer("D0"), LED("D1"))
    sos = generate_sequence("...---...")
    while True:
        perform(buzzer_led, sos)
        sleep(2)
