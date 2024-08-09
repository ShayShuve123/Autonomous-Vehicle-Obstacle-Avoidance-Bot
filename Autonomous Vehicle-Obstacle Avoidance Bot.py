distance = 0
distance = maqueenPlusV2.read_ultrasonic(DigitalPin.P13, DigitalPin.P14)

def on_forever():
    global distance
    maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
        maqueenPlusV2.MyEnumDir.FORWARD,
        100)
    distance = maqueenPlusV2.read_ultrasonic(DigitalPin.P13, DigitalPin.P14)
    if distance <= 25:
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.LEFT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            0)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.RIGHT_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            100)
        basic.pause(800)
        maqueenPlusV2.control_motor(maqueenPlusV2.MyEnumMotor.ALL_MOTOR,
            maqueenPlusV2.MyEnumDir.FORWARD,
            100)
basic.forever(on_forever)