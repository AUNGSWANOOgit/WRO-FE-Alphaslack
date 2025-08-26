# Example of a PID loop controlling motor speed with L298N

import RPi.GPIO as GPIO
import time

# Pin definitions (example)
MOTOR_DRIVE_IN1 = 17
MOTOR_DRIVE_IN2 = 27
PWM_DRIVE = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup([MOTOR_DRIVE_IN1, MOTOR_DRIVE_IN2], GPIO.OUT)
GPIO.setup(PWM_DRIVE, GPIO.OUT)

pwm_drive = GPIO.PWM(PWM_DRIVE, 100)  # 100 Hz
pwm_drive.start(0)

# PID constants (tune for your vehicle)
Kp = 1.2
Ki = 0.5
Kd = 0.1

target_speed = 50.0   # desired speed (arbitrary units, e.g., cm/s or encoder ticks/s)
integral = 0.0
last_error = 0.0

def drive_forward(duty):
    GPIO.output(MOTOR_DRIVE_IN1, GPIO.HIGH)
    GPIO.output(MOTOR_DRIVE_IN2, GPIO.LOW)
    pwm_drive.ChangeDutyCycle(duty)

def stop_drive():
    GPIO.output(MOTOR_DRIVE_IN1, GPIO.LOW)
    GPIO.output(MOTOR_DRIVE_IN2, GPIO.LOW)
    pwm_drive.ChangeDutyCycle(0)

# --- Simulated speed feedback (replace with encoder readings) ---
def get_speed_feedback(duty):
    # crude simulation: higher duty cycle = higher speed with some noise
    return duty * 0.8 + (2 - time.time() % 4)

# --- PID loop ---
try:
    duty = 0
    while True:
        measured_speed = get_speed_feedback(duty)
        error = target_speed - measured_speed

        global integral, last_error
        integral += error
        derivative = error - last_error

        output = Kp * error + Ki * integral + Kd * derivative

        duty = max(0, min(100, duty + output))  # constrain between 0–100
        drive_forward(duty)

        print(f"Target: {target_speed:.2f}, Measured: {measured_speed:.2f}, Duty: {duty:.2f}")

        last_error = error
        time.sleep(0.1)

except KeyboardInterrupt:
    stop_drive()
    pwm_drive.stop()
    GPIO.cleanup()
