"""Simple robot controller."""

from controller import Robot
import sys
import math

# Define the target motor position in radians.
# comprimento = angulo * raio
# angulo = comprimento / raio
target = 0.250/0.021
# Get pointer to the robot.
robot = Robot()

# Print the program output on the console
print("Move the motors of the Thymio II to position " + str(target) + ".")

# Set the target position of the left and right wheels motors.
robot.getDevice("motor.left").setPosition(target)
robot.getDevice("motor.right").setPosition(target)

# Run the simulation for 10 seconds
robot.step(10000)

# This is the simplest controller that works for this competition
# If you want to experiment with more complex functions, you can read the programming guide here:
# https://www.cyberbotics.com/doc/guide/controller-programming?tab-language=python
# or the Robot() documentation here:
# https://cyberbotics.com/doc/reference/robot?tab-language=python
