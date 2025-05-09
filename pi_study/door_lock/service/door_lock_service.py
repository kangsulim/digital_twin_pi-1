from time import sleep

import RPi.GPIO as gpio
from door_lock.constant.password import PASSWORD
from door_lock.module.led import Led
from door_lock.module.button import Button, ButtonEvent
from time import sleep

class ModuleService:
    ledModules = []
    buttonModules = []

    @classmethod
    def addLedModule(cls, led:Led):
        cls.ledModules.append(led)

    @classmethod
    def addButtonModule(cls, button:Button):
        cls.ledModules.append(button)

class DoorLockService:

    currentInputPassword = ""

    @classmethod
    def getPassword(cls):
        return PASSWORD

    @classmethod
    def setModule(cls):
        led1 = Led(16, "RED")
        led2 = Led(20, "YELLOW")
        led3 = Led(21, "GREEN")
        ModuleService.addLedModule(led1)
        ModuleService.addLedModule(led2)
        ModuleService.addLedModule(led3)

        button1 = Button(13, "1")
        cls.setLedOnAndOffButtonEvent(button1, led1)
        button2 = Button(19, "2")
        cls.setLedOnAndOffButtonEvent(button2, led2)
        button3 = Button(26, "3")
        cls.setLedOnAndOffButtonEvent(button3, led3)

        ModuleService.addButtonModule(button1)
        ModuleService.addButtonModule(button2)
        ModuleService.addButtonModule(button3)

    @classmethod
    def setLedOnAndOffButtonEvent(cls, button, led):
        def handleButtonOnClick():
            if button.currentState == gpio.HIGH:
                led.ledOn()
            else:
                led.ledOff()
            if len(cls.currentInputPassword) < 3:
                cls.currentInputPassword += button.value
            else:
                cls.checkPassword()
                cls.currentInputPassword = ""

        buttonEvent = ButtonEvent(handleButtonOnClick)
        button.setButtonEvent(buttonEvent)

    @classmethod
    def checkPassword(cls):
        if cls.getPassword() == DoorLockService.currentInputPassword:
            for _ in range(3):
                for ledModule in ModuleService.ledModules:
                    ledModule.blink(1, 0.5)
        else:
            for _ in range(3):
                for ledModule in ModuleService.ledModules:
                    ledModule.onLed()
                sleep(0.5)
                for ledModule in ModuleService.ledModules:
                    ledModule.onOff()
                sleep(0.5)
