from config.gpio_config import GpioConfig
from service.door_lock_service import ModuleService

if __name__ == "__main__":

    try:
        while True:
            buttons = ModuleService.buttonModules
            for button in buttons:
                button.onClick()
    except KeyboardInterrupt:
        pass
    finally:
        GpioConfig.cleanup()

