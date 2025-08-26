# sensor_test.py
# Test ultrasonic distance and MPU6050 orientation


import time
import smbus2
import RPi.GPIO as GPIO

# Ultrasonic pins
TRIG = 5
ECHO = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# MPU6050 setup
bus = smbus2.SMBus(1)
MPU_ADDR = 0x68
bus.write_byte_data(MPU_ADDR, 0x6B, 0)  # Wake MPU6050

def read_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    start = time.time()
    stop = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()

    duration = stop - start
    distance = duration * 17150
    return round(distance, 2)

def read_accel_x():
    high = bus.read_byte_data(MPU_ADDR, 0x3B)
    low = bus.read_byte_data(MPU_ADDR, 0x3C)
    value = (high << 8) + low
    if value > 32768:
        value -= 65536
    return value / 16384.0

if __name__ == "__main__":
    try:
        while True:
            dist = read_distance()
            accel_x = read_accel_x()
            print(f"Distance: {dist} cm | Accel-X: {accel_x:.2f} g")
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()
