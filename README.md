# Robot Fleet Simulation

A Python simulation of a multi-robot fleet (drone, ground, underwater) with battery management and mission execution using Object-Oriented Programming (OOP).

## Overview

This project simulates a small fleet of robots that carry out missions in different zones. Each robot type moves in its own way (flying, driving, or swimming), consumes battery while completing missions, and automatically returns to base to recharge when its battery runs low.

## Features

- **Base `Robot` class** with shared behavior: moving, tracking battery, reporting status, and performing missions
- **Specialized robot types** built with inheritance:
  - `DroneRobot` — flies to its destination at a set altitude
  - `GroundRobot` — drives to its destination
  - `UnderwaterRobot` — swims to its destination at a set depth
- **Battery management** — robots that fall below a low-battery threshold automatically return to base and recharge instead of starting a new mission
- **Mission system** — a `Mission` class defines a title, destination, and battery cost; missions are assigned randomly to robots in the fleet
- **Fleet simulation** — runs each robot in the fleet through a mission and prints its status afterward

## How It Works

1. A fleet of robots is created (one drone, one ground robot, one underwater robot), each starting with a different battery level
2. A set of missions is defined, each with its own destination and battery cost
3. For each robot in the fleet, a random mission is chosen and assigned
4. If the robot has enough battery, it moves to the mission's destination, completes the mission, and its battery decreases accordingly
5. If the robot's battery is too low, it returns to base and recharges instead of running the mission

## Running the Simulation

```bash
python main.py
```

## Example Concepts Demonstrated

- Object-Oriented Programming (classes, inheritance, method overriding)
- Encapsulation of robot state (battery, location)
- Simple simulation logic with randomized mission assignment

## Possible Improvements

- Add more robot types or mission types
- Track total distance traveled or missions completed per robot
- Add a graphical or web-based visualization of the fleet
- Log simulation results to a file
