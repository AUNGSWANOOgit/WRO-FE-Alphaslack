# Alphaslack  
**WRO 2025 Future Engineers**

## Team Members
- Jonathan Yeo Tze Ho  
- Aung Swan Oo  
- Xu Yunhe  

---

## Content
- [**t-photos**](./t-photos)  
  Team photos, including one official group picture and one fun photo of all members.  

- [**v-photos**](./v-photos)  
  Vehicle photos showing it from different perspectives.  

- [**video**](./video)  
  Contains a file with the link to the vehicle demonstration video.  

- [**schemes**](./schemes)  
  Diagrams that illustrate the structure and components of the vehicle and how they are connected.  

- [**src**](./src)  
  Source code that runs the vehicle.  

- [**models**](./models)  
  Files used to create physical parts and add-ons for the vehicle.  

---

## Introduction
This repository documents the development of our autonomous vehicle for the WRO 2025 Future Engineers category.  
It brings together all parts of the project, including team photos, vehicle design, control software, hardware diagrams, and supporting materials.  

The goal of this repository is to provide a clear overview of our work, show how the vehicle was designed and built, and make it easier to follow the process from concept to demonstration.  
It also serves as a reference for future improvements and as a record of our participation in the competition.  

---

<details>
  <summary><strong>1. Mobility</strong></summary>

The vehicle uses a **two-motor configuration**: one DC motor for propulsion and one DC motor for steering.  

- The propulsion motor drives the vehicle forward and backward.  
- The steering motor adjusts the wheel angle, forming an **Ackermann-style steering system**.  
- Both motors operate through **L298N motor drivers**, with speed and position regulated by **PWM signals** from the Raspberry Pi 5.  

A **PID control loop** regulates both propulsion and steering:  
- For the drive motor, PID maintains constant speed despite load changes or battery voltage drops.  
- For the steering motor, PID ensures the wheel angle is reached quickly and held steadily without overshoot or oscillation.  

**Trade-off:** Ackermann steering provides smooth, predictable motion and precise path tracking, but it requires a larger turning radius compared to differential drive. This reduces tight rotation ability but increases consistency during forward motion and cornering.  

</details>

---

<details>
  <summary><strong>2. Power</strong></summary>

We use a **dual power strategy** to isolate loads:  
- Raspberry Pi 5 + sensors powered by a **30W, 10,000 mAh USB-C power bank**  
- Drive and steering motors powered by a **Li-Po battery** through the L298N drivers  

**Protective components included:**  
- Resistors for GPIO protection  
- Voltage regulators for safe input levels to the Pi  
- Inline fuses and the Li-Po’s BMS to prevent shorts or over-discharge  

This separation ensures stable performance and prevents motor surges from resetting the Raspberry Pi.  

</details>

---

<details>
  <summary><strong>3. Sensing</strong></summary>

The sensing system integrates multiple devices for navigation:  
- **Logitech USB webcam** for line tracking, color recognition, and higher-level obstacle perception  
- **HC-SR04 ultrasonic sensor** for detecting obstacles directly ahead and providing short-range safety  
- **MPU6050 IMU** for measuring orientation and angular changes, used for tracking turns and stabilizing steering behavior  

</details>

---

<details>
  <summary><strong>4. Obstacle Management</strong></summary>

Obstacle detection uses a **two-layer system**:  
1. **Ultrasonic sensing** provides fast stop or slow responses when an object is detected within a threshold distance  
2. **Vision (camera)** detects markers, blocks, and course boundaries  

The avoidance strategy is **steer-around maneuvering**. When an obstacle is detected, the system reduces speed, adjusts steering to bypass the obstacle, and then re-centers to continue forward.  

- Current logic is **rule-based** for reliability  
- **Machine learning models** are being tested for adaptive decision-making  

</details>

---

<details>
  <summary><strong>5. Control and Computation</strong></summary>

The **Raspberry Pi 5 (8GB)** serves as the central controller. It handles:  
- Vision processing using the webcam  
- Sensor fusion from IMU and ultrasonic inputs  
- Control of the drive and steering motors via [**src**](./src)  

**Connections:**  
- USB → Webcam  
- I2C → MPU6050  
- GPIO → Ultrasonic trigger/echo  
- PWM GPIO → Motor control signals to the L298N  

The Pi runs tasks in parallel to guarantee responsive obstacle detection while processing camera input.  

</details>

---

<details>
  <summary><strong>6. Motivation</strong></summary>

The design choices are based on reliability, simplicity, and effective use of available parts.  

- **Frame and Motors:** LEGO is used for the frame and motors, providing a sturdy yet modular structure that is lightweight and easy to modify.  
- **Mobility:** An Ackermann-style steering system matches the layout of the LEGO chassis and provides smooth directional control through a dedicated steering motor. A separate drive motor handles propulsion, keeping the control system straightforward.  
- **Power:** A Li-Po battery powers the motors, while a USB power bank powers the Raspberry Pi 5. This prevents voltage fluctuations from affecting the controller.  
- **Motor Drivers:** L298N modules integrate easily with both DC motors and Raspberry Pi GPIO.  
- **Sensing:** The Logitech webcam, HC-SR04 ultrasonic sensor, and MPU6050 IMU provide a balance of vision, distance measurement, and orientation feedback.  

These decisions result in a system that combines the modularity of LEGO mechanics with the flexibility of external electronics. The design is simple, robust, and open to further improvement.  

</details>

---

## Development Status
This project is **still in development**. More detailed setup instructions will be added later, including:  
- Wiring diagrams  
- Python dependencies and installation  
- Script usage and workflow guides  

Future updates will expand this README with full documentation as the system evolves.  
