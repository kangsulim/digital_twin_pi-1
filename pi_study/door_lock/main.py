from config.gpio_config import GpioConfig
from service.door_lock_service import ModuleService, DoorLockService

if __name__ == "__main__":
    GpioConfig.setMode()
    DoorLockService.setModule()

    try:
        buttons = ModuleService.buttonModules
        print(buttons)
        while True:
            for button in buttons:
                button.onClick()
    except KeyboardInterrupt:
        pass
    finally:
        GpioConfig.cleanup()

