from vpython import *
#GlowScript 2.8 vpython
 
print('Sun Moon Earth system')

def gforce(p1,p2):
       G = 1 
       r_vec = p1.pos-p2.pos
       r_mag = mag(r_vec)
       r_cap = r_vec/r_mag
       f_mag = G*p1.mass*p2.mass/r_mag**2
       f_vec = -f_mag*r_cap
       return f_vec


sun = sphere(pos=vector(0,0,0),radius= 10 ,color=color.yellow, mass = 20000, momentum=vector(0,0,0))
earth = sphere(pos=vector(100,0,0), color=color.blue, radius=1 , mass=200, make_trail=True, momentum= vector(0,2500,0))
moon = sphere(pos=vector(94,0,0),  radius =0.5, mass = 70, momentum=vector(0,700,0))

t=0
dt=0.005
while(True):
    rate(500)
    sun_gravity= gforce(sun,earth) + gforce(sun,moon)
    earth_gravity= gforce(earth,sun) + gforce(earth,moon)
    moon_gravity = gforce(moon,sun) +  gforce(moon,earth)

    sun.momentum= sun.momentum + sun_gravity*dt
    earth.momentum= earth.momentum + earth_gravity*dt
    moon.momentum= moon.momentum + moon_gravity*dt

    sun.pos = sun.pos + (sun.momentum/sun.mass)*dt
    earth.pos = earth.pos + (earth.momentum/earth.mass)*dt
    moon.pos = moon.pos + (moon.momentum/moon.mass)*dt
    t=t+dt
    
