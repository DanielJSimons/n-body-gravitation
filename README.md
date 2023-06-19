# n_body_sim

I wanted to break away from the typical data analysis & science libraries that I am used to and expand my knowledge base into basic simulation and visualisation tools such as Pygame. 
This provided me the foundations for visualising the simulations that I implemented using Euler integration, a first order numerical procedure for solving ODEs. With Pygame being less relevent in the data science world, this was an interesting exercise in algorithm design and implementation of mathematical principles.

This project also enabled me to learn further about optimizing my code. Originally this simulation could only handle approximately 20 bodies before slowing down. With some easy rewriting of code for generating sprites and interactions between bodies I was able to get this running with up to around 100 bodies simultaneously without too much trouble.

---

I've attempted to add some resemblance to unlikely and unstable star systems that could be found throughout the universe with each star corresponding to one of the main spectral types of stars. Colour, relative mass and size are all in proportion to their respective star type although scaled distance between stars is very off.

Red (Type M) - Examples of this star are the famous Betelgeuse, the 7th brightest start in our sky.

Yellow (Type G) - Examples of this star are our Sun and is set as the reference for mass and size for the other two stars in this system.

White / Light Blue (Type A) - Examples of this star are Sirius. This is the brightest star in our sky by far and almost double that of the second brightest.
