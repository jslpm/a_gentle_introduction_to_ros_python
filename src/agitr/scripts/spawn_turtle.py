#!/usr/bin/env python3

# This program spawns a new turtlesim turtle by calling
# the appropriate service.
import rospy
import math
from turtlesim.srv import Spawn

rospy.init_node("spawn_turtle")

# Create a client object for the spawn service.
# This needs to know the data type of the service and its name.
spawnClient = rospy.ServiceProxy("spawn", Spawn)

# Create the request and response objects.
x = 2
y = 3
theta = math.pi / 2
name = "Leo"
resp = None

# Actually call the service. This won't return
# until the service is complete.
resp = spawnClient(x, y, theta, name)

if resp is not None:
	rospy.loginfo(f"Spawned a turtle named {resp.name}.")
else:
	rospy.logerror("Failed to spawn.")

