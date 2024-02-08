
# Thermal Detection

This project focuses on the detection of humans using a thermal camera without employing deep-learning techniques. The initiative is driven by the ambition to integrate this technology into a remote sensing drone, where computational resources are limited and processing must occur in real-time.

## Data Source

The thermal imagery data used in this project is obtained from the [OSU Thermal Pedestrian Database](http://vcipl-okstate.org/pbvs/bench/Data/03/download.html), which provides a comprehensive set of thermal images for developing and testing detection algorithms.

## Overview

The project employs basic image processing filters to detect humans in thermal images. This strategy is designed to ensure the system remains computationally light to facilitate its deployment on drones, where processing power is constrained.

### Achievements

- Successfully developed a human detection system using straightforward filtering techniques in just a day and a half.
- Demonstrated promising results that serve as a solid foundation for future improvements.

### Challenges

- Experienced difficulty in accurately tracking the center of mass of humans due to the reliance on changes between sequential images.

### Future Directions

- Intend to investigate the application of lightweight neural networks to improve the accuracy of human detection while maintaining minimal computational requirements.

## Getting Started

To run this project, use the following command:

./run.bat


I've not made a bash or command script for this program, but you could just copy the commands within the run.bat onto whatever terminal you have. 
