import math

velocity = 20
angle = 45
gravity = 9.81
vx = velocity * math.cos(math.radians(angle))
vy = velocity * math.sin(math.radians(angle))
print("Horizontal velocity:", vx)
print("Vertical velocity:", vy)
