def led1():
    import machine
    import utime
    pin = machine.Pin(2, machine.Pin.OUT)
    for i in range(5):
        pin.on()
        utime.sleep_ms(1000)
        pin.off()
        utime.sleep_ms(1000)
    pin.on()