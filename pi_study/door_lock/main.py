from door_lock.config.gpio_config import GpioConfig
from door_lock.service.door_lock_service import ModuleService, DoorLockService

if __name__ == "__main__":
    GpioConfig.setMode()
    DoorLockService.setModule()
    print(ModuleService.getLedMoules())
    print(ModuleService.getButtonMoules())

    try:
        buttons = ModuleService.getButtonMoules()
        print(buttons)
        while True:
            for button in buttons:
                button.onClick()
    except KeyboardInterrupt:
        pass
    finally:
        GpioConfig.cleanup()

