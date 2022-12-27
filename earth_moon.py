from vpython import *

ME = 5.97237e24  # mass of earth in kg
MM = 7.34767309e22  # mass of moon in kg
RE = 6.3781e6  # radius of earth in m
RM = 1.7374e6  # radius of moon in m
REM4500 = 2.421e7  # distance between earth and moon in m in 4500ma
YEAR = 3600*24*365  # total number of second per year
G = 6.6743e-11*((YEAR*1000000)**2)  # gravitational constant in (m^3)(kg^-1)(one million year^-2)
drift_rate = 20.8e-2 * 1000000  # drifting rate of moon in m per million year
freq = 100  # animation rate

earth = sphere(pos=vector(0,0,0), radius=2*RE, texture=textures.earth)
moon = sphere(pos=earth.pos+vector(REM4500,0,0), radius=2*RM, make_trail=False)
point_mass1 = sphere(pos=vector(REM4500*cos(pi/3), REM4500*sin(pi/3), 0), radius=1e6, color=color.red)
time_label = label(xoffset=180, yoffset=-160, line=False)
point_mass1.mass = 1000 # mass of point mass
point_mass1.v = sqrt(G*ME/REM4500)*vector(-cos(pi/6),sin(pi/6),0)
d_em = REM4500  # distance between earth and moon


t = 4500  # simulation starts at 4500 million years ago
dt = 10/freq  # 10 million year every sec



# 1sec is equivalent to 10 million year in the simulation
while t >= 3500:
    rate(freq)
    moon.speed = sqrt(G*ME/d_em)/1000000
    moon.angspeed = moon.speed/d_em
    # moon.force = -G*ME*MM*norm(moon.pos)/(d_em**2)

    # update position of the moon
    moon.pos = moon.pos + moon.speed*dt*vector(cos(moon.angspeed*dt), sin(moon.angspeed*dt), 0)
    # point_mass.pos = vector(distance*cos(pi/3), distance*sin(pi/3), 0)

    # update position of point mass
    point_mass1.a = G*(MM*norm(moon.pos - point_mass1.pos)/(mag(moon.pos - point_mass1.pos)**2) + ME*norm(earth.pos - point_mass1.pos)/(mag(earth.pos - point_mass1.pos)**2))
    point_mass1.v = point_mass1.v + point_mass1.a * dt
    # point_mass1.pos = point_mass1.pos + point_mass1.v * dt

    # update time and camera perspective
    time_label.text = f"Time: {int(t)}ma"
    scene.append_to_caption(f"Time: {t}ma   Distance: {d_em}m\n")
    scene.up = rotate(moon.pos, pi/2, axis=vector(0,0,1))
    t = t-dt
    d_em = d_em + drift_rate*dt

##https://www.youtube.com/watch?v=froU7lSU7IU
# 1sec is equivalent to 100 million year in the simulation
# while True:
#     rate(freq)
#     distance = distance + drift_rate*dt
#     moon.speed = sqrt(G*ME/distance)
#     r = moon.pos - earth.pos
#     F = -G*ME*MM*norm(r)/distance**2
#
#     # update momentum
#     moon.p = moon.p + F*dt
#
#     # update position using the final momentum of the specified time interval
#     moon.pos = moon.pos + moon.p*dt/MM
#     scene.up = rotate(r, pi/2, axis=vector(0,0,1))
#     #scene.append_to_caption("Hello\n")