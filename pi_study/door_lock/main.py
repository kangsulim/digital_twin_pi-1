from config.gpio_config import GpioConfig
from service.door_lock_service import ModuleService, DoorLockService

if __name__ == "__main__":
    DoorLockService.setModule()

    try:
        while True:
            buttons = ModuleService.buttonModules
            for button in buttons:
                button.onClick()
    except KeyboardInterrupt:
        pass
    finally:
        GpioConfig.cleanup()

