# Thermal-detection
Thermal detection in preparation for a separate project

The main conceit of this project is to detect humans using a thermal camera without using any deep-learning techniques. This is due to the fact that this will later be built on to create a remote sensing drone, due to the nature of drones computation will be limited, and the computation will have to be done in real time.


The data used for this project comes from 
http://vcipl-okstate.org/pbvs/bench/Data/03/download.html

The results from this project are promising, it was completed over the course of a day and a half, and i got decent detection working using mostly filters. 

I had issues tracking the centre of mass of humans, as I was using the changes between photos.

Next time I'll try to use a light neural network to detect the presence of humans


