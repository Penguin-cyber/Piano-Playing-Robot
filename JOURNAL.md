---
title: Anthropomorphic, Piano-Playing Robot
author: MengYang Yu
description: A robot that plays the piano using an anthropomorphic robotic hand.
created_at: 2025-06-08
---
# June 8: Started designing the forearm

Today, I worked on drafting ideas for what the entire arm system might look like. This was done on a separate Google Doc: https://docs.google.com/document/d/1JBX58aGr_KxgK6paylfiLBcvCcq8-dvwz1_QLYsHlvY/edit?usp=sharing in the "Arm Decisions" Tab. The primary concern was on how the hand would access the keys in various ranges on the piano. Ultimately, I settled on doing a rail system, due to its simplicity. 

Otherwise, I began CADing the forearm in SolidWorks. I have general ideas for the servo motors and a concept in mind of what it may end up looking like. I am still figuring out where to place the ESP32 and the corresponding control boards for the serial communication. 

For packaging purposes, I may have to design a PCB that combines six serial ports in parallel, just so I don’t have to use the boards that come with the servos, which are pretty space inefficient since they only combine two ports.

![image](https://github.com/user-attachments/assets/7a6dc6b0-0b42-465f-9717-187fc9a0de47)


**Total time spent: 2h**

# June 10: Started designing the PCB

Today, I worked on a custom PCB to connect the six serial bus ports in parallel. I have used KiCAD before, but I'm a little rusty, so a lot of the time spent was trying to relearn the basics of KiCAD. I created the project, drew the schematic, and started working on the PCB layout. In previous projects, I would accidentally make the PCB too large; accordingly, I chose to focus on space this time to ensure that the board would not be too expensive, and that it would actually be more space efficient than the boards that come with the servos. For mounting purposes, I added some holes where M2 bolts can go.

![image](https://github.com/user-attachments/assets/e3d0eafd-50e9-4686-8e96-c5a1c3f2da38)


**Total time spent: 3:30h**
