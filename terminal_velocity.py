#We begin by initialising the constants. rho is the density of water in kgm^-3 and c_d is the drag coefficient of a sphere. As this is only meant as an approximation, values have only been written to 2 or 3 significant figures
g = 9.81
rho = 997
pi = 3.14
c_d = 0.47
#We initialise the variables. h is vertical displacement, t is time, v is velocity and dt is the time increment (we vary dt as some ball bearings must fall significantly further than others).
h = 0
t = 0
v = 0
dt = 0.001
#Here we define a function called height_finder which uses a while loop to find an approximation of the height the sphere would fall before reaching terminal velocity.
def height_finder(v, h, t, ball_number, v_t, m, rho_s, d):
  #We define A (the projected area of the sphere) for each ball bearing.  
  A = (pi*(d**2))/4
  #The while loop repeats until the velocity computed is greater than the terminal velocity
  
  while v < v_t:
    #We define all the forces acting on the sphere and define the acceleration at any point in the motion. We multiply this by the change in time to give the change in velocity and add this to the velocity. Similarly we increase the height by the distance travelled in that time and increment the time. This loops until v < v_t.
    F = (pi/6)*(d**3)*(rho_s)*g - (pi/6)*(d**3)*rho*g - (rho*(v**2)*c_d*A)/2
    a = F/m
    v = v + a*dt
    h = h + v*dt
    #We print a statement to give the value of the height of water that the ball bearing must pass through to reach terminal velocity
  print('Ball number', str(ball_number), 'approximately falls a height of', str(round(h, 2)) + 'm')

height_finder(v, h, t, 1, 4.73, 0.0635, 7777.52, 0.024983)
height_finder(v, h, t, 2, 3.03, 0.01668, 7780.37, 0.015998)
height_finder(v, h, t, 3, 3.03, 0.01644, 7833.24, 0.015885)
height_finder(v, h, t, 4, 2.46, 0.00894, 7784.14, 0.012993)
height_finder(v, h, t, 5, 1.20, 0.00104, 7794.12, 0.006340)
height_finder(v, h, t, 6, 1.20, 0.00104, 7757.35, 0.006350)
height_finder(v, h, t, 7, 0.91, 0.00044, 7826.19, 0.004753)
height_finder(v, h, t, 8, 0.57, 0.00011, 7780.91, 0.003)
