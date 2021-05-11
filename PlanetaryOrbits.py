import math
from turtle import *

G = 6.67e-11

AU = (149.6e6 * 1000)
SCALE = 250 / AU

class Body(Turtle):

    name = 'Body'
    mass = None
    vx = vy = 0.0
    px = py = 0.0

    def attraction(self, other):

        if self is other:
            raise ValueError("Attraction of object %r to itself requested" %  self.name)

        sx, sy = self.px, self.py
        ox, oy = other.px, other.py

        dx = (ox - sx)
        dy = (oy - sy)
        d = math.sqrt(dx**2 + dy**2)

        if d == 0:
            raise ValueError("Collision between objects %r and %r" %(self.name, other.name))

        F = G * self.mass * other.mass / (d**2)

        theta = math.atan2(dy, dx)
        Fx = math.cos(theta) * F
        Fy = math.sin(theta) * F
        return Fx, Fy

def update_info(step, bodies):
    print('Step #{}'.format(step))
    for body in bodies:
        s = '{:<8}  Pos.={:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f}'.format(
            body.name, body.px/AU, body.py/AU, body.vx, body.vy)
        print(s)
    print()

def loop(bodies):
    timestep = 24 * 3600

    for body in bodies:
        body.penup()
        body.hideturtle()

    step = 1
    while True:
        update_info(step, bodies)
        step += 1

        force = {}
        for body in bodies:
            total_fx = total_fy = 0.0
            for other in bodies:
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                total_fx += fx
                total_fy += fy

            force[body] = (total_fx, total_fy)

        for body in bodies:
            fx, fy = force[body]
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep

            # Update positions
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px*SCALE, body.py*SCALE)
            body.dot(3)

def main():
    sun = Body()
    sun.name = 'Sun'
    sun.mass = 1.9882 * 10 ** 30
    sun.pencolor('yellow')

    earth = Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10 ** 24
    earth.px = -1 * AU
    earth.vy = 29.783 * 1000
    earth.pencolor('blue')

    loop([sun, earth])

if __name__ == '__main__':
        main()
    










        
