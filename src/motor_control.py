# motor_control.py
# Basic motor control for propulsion and steering using L298N drivers

import RPi.GPIO as GPIO
import time

# Pin definitions (example setup)
MOTOR_DRIVE_IN1 = 17
MOTOR_DRIVE_IN2 = 27
MOTOR_STEER_IN1 = 22
MOTOR_STEER_IN2 = 23
PWM_DRIVE = 18
PWM_STEER = 24

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([MOTOR_DRIVE_IN1, MOTOR_DRIVE_IN2, MOTOR_STEER_IN1, MOTOR_STEER_IN2], GPIO.OUT)
GPIO.setup([PWM_DRIVE, PWM_STEER], GPIO.OUT)

pwm_drive = GPIO.PWM(PWM_DRIVE, 100)  # 100 Hz
pwm_steer = GPIO.PWM(PWM_STEER, 100)
pwm_drive.start(0)
pwm_steer.start(0)

def drive_forward(speed=50):
    GPIO.output(MOTOR_DRIVE_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_DRIVE_IN2, GPIO.LOW)
    pwm_drive.ChangeDutyCycle(speed)

def drive_backward(speed=50):
    GPIO.output(MOTOR_DRIVE_IN1, GPIO.LOW)
    GPIO.output(MOTOR_DRIVE_IN2, GPIO.HIGH)
    pwm_drive.ChangeDutyCycle(speed)

def stop_drive():
    GPIO.output(MOTOR_DRIVE_IN1, GPIO.LOW)
    GPIO.output(MOTOR_DRIVE_IN2, GPIO.LOW)
    pwm_drive.ChangeDutyCycle(0)

def steer_left(angle=50):
    GPIO.output(MOTOR_STEER_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_STEER_IN2, GPIO.LOW)
    pwm_steer.ChangeDutyCycle(angle)

def steer_right(angle=50):
    GPIO.output(MOTOR_STEER_IN1, GPIO.LOW)
    GPIO.output(MOTOR_STEER_IN2, GPIO.HIGH)
    pwm_steer.ChangeDutyCycle(angle)

def center_steer():
    GPIO.output(MOTOR_STEER_IN1, GPIO.LOW)
    GPIO.output(MOTOR_STEER_IN2, GPIO.LOW)
    pwm_steer.ChangeDutyCycle(0)

if __name__ == "__main__":
    try:
        drive_forward(60)
        time.sleep(2)
        stop_drive()
        steer_left(40)
        time.sleep(1)
        center_steer()
    finally:
        pwm_drive.stop()
        pwm_steer.stop()
        GPIO.cleanup()
