
                                                                N-Body
                                            
Introduction:
        
        -In this excercise we'll simulate the trajectory of two masses in space and the forces that exert between them. We will increase the complexity of the exercises as well as the dimensions in which we will work.
    


Methodology:

        -First we import math and then we do the copyright
        -We start with the class "def_particle()" where we work with the particle and we define a constructor "_init_()" whitin the class
        -In the definition we do the function that will integrate the system by calculating the new position of "P." "def_integrate()".
        -After we do the method called "def_getPosition()"
        -We calculate the kinetic energy of a particle with the method "def_getkinecticEnergy()"
        -now we create the particle....."A = particle" in this class an object is being created and disappearing. Once created we add elements of speed, positioning and mass. After doing this we will give the initial conditions to our particles.
        -Then we will make prints integrating delta time "A.integrate(dt)" and we'll test in a cycle "for t in range (60)".In this step we have already programmed
        Newton's first law.
        -Now we measure the force exerted between two particles, including now Newton's second and third law.
        -We get the value of "r" (r is the distance between two particles) which is "r=√2"
        -We will calculate the distance r with the "def_computer()" method in "def_integrate()"
        -We calculate the vector "U" which is the direction so as not to obtain opposing forces using the method
 "def_computerU"
        -Now we define and add to particle two with its elements and do the test to see if it works for the two particles. We will calculate the distance between the two particles using the Pythagorean theorem.
        !!The result will be that the particle "A" is in a corner without moving and the particle "B" is in opposite motion!!
        -To solve this we will now integrate "A" with respect to "B" in a cycle.
        -Now we will add the method "A.setdt ()" (integration time ") where we will implement delta t and then define a method" def_setdt () "where abstraction with this method will be better done.
        -Then we make changes to our "def_integrate" method with respect to object "B".
        -The cycle serves to see the movement of the particles with the passage of the iterations.
        -Now we will see theoretically if our model is correct.
        -Now we try to integrate "B" with respect to "A" and the address changes and accelerates. Now we will graph, we will start by creating a subfigure that will return the figure and the axes. The graph at the beginning will be one dimension.
        -In the integrated graph with respect to "B" we can see that the result is not very good.
        -To be able to see the change of position with respect to time we can derive asking for finite differences or we can ask the program. Adding the method "def_getVelocity ()" (here we are in the first dimension). We will make a plot of the speed integrating "by hand", before that we keep our position in "X" and then we ask for the finite difference (time vs. distance), this in the first plot, in the second plot it will be time vs speed. So far we have already obtained the derivative and with this result we see that the speed increases as it approaches "A" because it falls into a gravitational potential.
        -Now we will include / see the acceleration in the first dimension, we will start it at 0 and we will seek to calculate the acceleration including it in the model integration cycle and change it in the second plot (time vs. acceleration). Our result will be that our particle will be made to a singularity.
        -Now we will pass the three-dimensional model where we will graph the particle in three dimensions.
        -
First we create a new figure and print point by point as the particles move. The results will be correct!
        -Now we will make the "A" (static) particle denser (with more mass) causing the accelerated movement to curve because it feels the force of the other particle.
        -
        -
        -
        -
        -
        -
        -
        -
Now we will do some tests 
        -What we will do now will be to make the two static particles 50 meters apart and then these particles will be supermassive and if we release them in space we will notice that they come together. If we weigh 1kg because the mass is so small, it will not move, if we do it at 100 kh, they will not move, if we separate them now at 5m we will notice that it starts to move and to see the complete movement we increase the iterations (1000) and we will notice that come together For another test we will return the mass to 10kg and return the iterations to 10, we will notice how the particles accelerate but do not come together (but it complies with what we want the acceleration to be).
        para resolver un error (del tiempo y la aceleracion) regresaremos la masa a 5e ^-3 e intentamos calcular a mano la fuerza y nos replantaremos algunas ecuaciones para debuguiar el programa.
        Solving the problems of magnitude of our G we will now change the measurements of our particles to MSG measurement and put the particles separated by 1 centimeter and with a mass of 10kg and then we will notice that they are already accelerating and at 1mm there is already interaction.
Now we will work over time using the variable lenTime
       -Now we spend everything in terms of time adding a variable to know how far to integrate, there we will configure the integration time (simulation time) and the steps.
       -Now we will add another particle and also make an arrangement so as not to have to add all the elements one by one.
       -the particle will be a millimeter above and the particles have no volume.
       -there are 3 particles that when you release them converge towards their center of mass of the system.
       -Now we will do the most complicated thing by adding speed again and we will notice a disturbance in the particles by diverting their trajectory and getting entangled.










