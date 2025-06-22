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

# June 11: Finished the PCB & further planning for arm

Today, I worked on finishing the PCB. Again, I aimed to optimize the size of the board, since that was the primary motivation for designing it in the first place. I managed to get the board down to 11mm x 49.5mm, which, in my opinion, is a good size. After finishing up everything (which took a while because I was relearning some more KiCad stuff), I started drafting ideas for how to actuate the pivot. I came to the conclusion that the pivot should be a dead axle which has a tooth profile on the outside. This way I can drive it with precision, and this would work especially well since the range of motion is rather limited, ~45 degrees.

![image](https://github.com/user-attachments/assets/a733877f-92f3-4093-b2b5-5310a6aac6b0)
![image](https://github.com/user-attachments/assets/b75618a9-2299-4cc6-899a-4085b383db84)

**Total time spent: 6h**

# June 16: Finished drafting the profiles of the arm & started designing the pulley

Today, I worked on the profiles of the arm. I have the layout complete now, and all that is left is to actually make the parts for the arm. I will add mounting holes onto the outside flange and I may change the height of the arm. I also started designing a ratcheting pulley, which would be incredibly useful. I have the general design for it finished, and simply need to start cadding it. Again, all of the logic and main decision-making is outlined in my document on the Google Drive. The majority of the time was spent on drafting and thinking, and not so much on actual cad.

![image](https://github.com/user-attachments/assets/5bc5c8be-2253-42c0-af8d-14ed29e630b2)


**Total time spent: 8h**

# June 17: Cadding pulley

Today, I worked on cadding the pulley. I mapped out the mastermodel for the pulley, and all that is left is to extrude the pieces. I have already extruded and made the bottom piece, only the top remains. After this is done, I will extrude parts on the arm to create the arm. Most of the time spent today was on figuring out the precise placement of features within the pulley. This was primarily deciding on tolerances and clearances, as well as figuring out what the ratchet profile should look like.

![image](https://github.com/user-attachments/assets/58b6c786-c8f6-425c-b363-1e2d353472fd)
![image](https://github.com/user-attachments/assets/dfc3b863-40b9-4c94-be74-ac69d5588341)

**Total time spent: 10h**

# June 18: Cadding pulley cont. and tendons

Today, I finished cadding the pulley by extruding the top half and creating the assembly. After finishing, I pulled those dimensions into the main mastermodel for the forearm, defining the desired height of the arm to encase the pulleys. After doing so, I created a block for the servo with the pulley, to help me map out the tendons. The tendons were then routed, with the supporting structure created. I will work on extruding the parts of the arm, and putting finishing touches on the design. There were no major design decisions made today, just simple tolerancing and clearances.

![image](https://github.com/user-attachments/assets/daf9244f-99cc-4e74-882c-78f26a99c083)
![image](https://github.com/user-attachments/assets/c45f7803-0b67-432a-b778-371ad756b947)
![image](https://github.com/user-attachments/assets/f0b4ae17-304e-4f24-8d18-2a1e55686434)

**Total time spent: 15h**

# June 19: Cadding forearm

Today, I extruded the parts of the arm and refined a bit of the design. Naturally, as things are extruded and designed, small adjustments are made where things don't work exactly as envisioned. For example, I tweeked the general shape of the forearm such that the holes for the PTFE lined up correctly. The tendons' paths were updated to ensure that the holes pierced the correct sections. The assembly for the forearm will be completed next.

![image](https://github.com/user-attachments/assets/30cd9d10-9a5f-4f10-b101-21f32eea93c1)
![image](https://github.com/user-attachments/assets/9e60b94c-6ba1-4113-84b0-da294ade1f9f)

**Total time spent: 19h**

# June 19: Creating forearm assembly and main assembly

Today, I created the assemblies for the forearm and the main assembly. This was primarily to set up the calculations I will do tomorrow to determine the reduction necessary in my gearbox. I also created a PLA material in SolidWorks to better match real life, so my math is more accurate. 

![image](https://github.com/user-attachments/assets/2045e586-b537-4750-b41b-75421f2c29b5)
![image](https://github.com/user-attachments/assets/b7e1df36-3af1-4300-9128-98d04e1513bc)

**Total time spent: 21h**

# June 19: Creating forearm assembly and main assembly

Today, I created the ratios for the pivot gearbox

After running some calculations based on SolidWorks’s data, I was able to calculate the torque required to pivot the arm. The calculations are shown below. Notably, I included a safety factor (x2) to ensure that nothing breaks–I would rather have a slower arm than an arm that cannot pivot. This is possible because the pivot is not required to have an extensive range of motion; so long as it operates within its range of motion at a reasonable speed, it will suffice.

As a note, I created my own custom PLA material in SolidWorks to ensure greater mass accuracy. Although it should be noted that the 3D prints will not be 100% infill, meaning that the mass given by SolidWorks will serve as an overestimate, which helps ensure that the gearbox will be more than adequately prepared to handle the torques.

Ultimately, I decided on a two-stage gearbox: 18T:54T (1:3) stage and an 18T:60T (3:10) stage. The relatively similar reductions ensure that the gears experience wear equally and that the packaging is optimized (since the gears are of similar sizes).

After adding a 20DP 60T gear to the arm (at 100% infill), the mass increased, and the center of mass (COM) distance from the pivot decreased. Ultimately, the new required torque stayed within the safety tolerance I had set.

Based on my experience, I ensured that I used the rated torque and moving torque of the servo motor. This will mitigate any substantial wear or damage to the servos.

![image](https://github.com/user-attachments/assets/d7bdec46-d9c0-402f-808c-132af56269cd)

**Total time spent: 25h**
