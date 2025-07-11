---
Title: Anthropomorphic, Piano-Playing Robot
Author: MengYang Yu
Description: A robot that plays the piano using an anthropomorphic robotic hand.
Created_at: 2025-06-08
Total_Time: 63 hours
---
# June 8: Started designing the forearm

Today, I worked on drafting ideas for what the entire arm system might look like. This was done on a separate Google Doc: https://docs.google.com/document/d/1JBX58aGr_KxgK6paylfiLBcvCcq8-dvwz1_QLYsHlvY/edit?usp=sharing in the "Arm Decisions" Tab. The primary concern was on how the hand would access the keys in various ranges on the piano. Ultimately, I settled on doing a rail system, due to its simplicity. 

Otherwise, I began CADing the forearm in SolidWorks. I have general ideas for the servo motors and a concept in mind of what it may end up looking like. I am still figuring out where to place the ESP32 and the corresponding control boards for the serial communication. 

For packaging purposes, I may have to design a PCB that combines six serial ports in parallel, just so I don’t have to use the boards that come with the servos, which are pretty space inefficient since they only combine two ports.

![image](https://github.com/user-attachments/assets/7a6dc6b0-0b42-465f-9717-187fc9a0de47)

**Time spent: 2h**

# June 10: Started designing the PCB

Today, I worked on a custom PCB to connect the six serial bus ports in parallel. I have used KiCAD before, but I'm a little rusty, so a lot of the time spent was trying to relearn the basics of KiCAD. I created the project, drew the schematic, and started working on the PCB layout. In previous projects, I would accidentally make the PCB too large; accordingly, I chose to focus on space this time to ensure that the board would not be too expensive, and that it would actually be more space efficient than the boards that come with the servos. For mounting purposes, I added some holes where M2 bolts can go.

![image](https://github.com/user-attachments/assets/e3d0eafd-50e9-4686-8e96-c5a1c3f2da38)

**Time spent: 1:30h**

# June 11: Finished the PCB & further planning for arm

Today, I worked on finishing the PCB. Again, I aimed to optimize the size of the board, since that was the primary motivation for designing it in the first place. I managed to get the board down to 11mm x 49.5mm, which, in my opinion, is a good size. After finishing up everything (which took a while because I was relearning some more KiCad stuff), I started drafting ideas for how to actuate the pivot. I came to the conclusion that the pivot should be a dead axle which has a tooth profile on the outside. This way I can drive it with precision, and this would work especially well since the range of motion is rather limited, ~45 degrees.

![image](https://github.com/user-attachments/assets/a733877f-92f3-4093-b2b5-5310a6aac6b0)
![image](https://github.com/user-attachments/assets/b75618a9-2299-4cc6-899a-4085b383db84)

**Time spent: 2:30h**

# June 16: Finished drafting the profiles of the arm & started designing the pulley

Today, I worked on the profiles of the arm. I have the layout complete now, and all that is left is to actually make the parts for the arm. I will add mounting holes onto the outside flange and I may change the height of the arm. I also started designing a ratcheting pulley, which would be incredibly useful. I have the general design for it finished, and simply need to start cadding it. Again, all of the logic and main decision-making is outlined in my document on the Google Drive. The majority of the time was spent on drafting and thinking, and not so much on actual cad.

![image](https://github.com/user-attachments/assets/5bc5c8be-2253-42c0-af8d-14ed29e630b2)


**Time spent: 2h**

# June 17: Cadding pulley

Today, I worked on cadding the pulley. I mapped out the mastermodel for the pulley, and all that is left is to extrude the pieces. I have already extruded and made the bottom piece, only the top remains. After this is done, I will extrude parts on the arm to create the arm. Most of the time spent today was on figuring out the precise placement of features within the pulley. This was primarily deciding on tolerances and clearances, as well as figuring out what the ratchet profile should look like.

![image](https://github.com/user-attachments/assets/58b6c786-c8f6-425c-b363-1e2d353472fd)
![image](https://github.com/user-attachments/assets/dfc3b863-40b9-4c94-be74-ac69d5588341)

**Time spent: 2h**

# June 18: Cadding pulley cont. and tendons

Today, I finished cadding the pulley by extruding the top half and creating the assembly. After finishing, I pulled those dimensions into the main mastermodel for the forearm, defining the desired height of the arm to encase the pulleys. After doing so, I created a block for the servo with the pulley, to help me map out the tendons. The tendons were then routed, with the supporting structure created. I will work on extruding the parts of the arm, and putting finishing touches on the design. There were no major design decisions made today, just simple tolerancing and clearances.

![image](https://github.com/user-attachments/assets/daf9244f-99cc-4e74-882c-78f26a99c083)
![image](https://github.com/user-attachments/assets/c45f7803-0b67-432a-b778-371ad756b947)
![image](https://github.com/user-attachments/assets/f0b4ae17-304e-4f24-8d18-2a1e55686434)

**Time spent: 5h**

# June 19: Cadding forearm

Today, I extruded the parts of the arm and refined a bit of the design. Naturally, as things are extruded and designed, small adjustments are made where things don't work exactly as envisioned. For example, I tweeked the general shape of the forearm such that the holes for the PTFE lined up correctly. The tendons' paths were updated to ensure that the holes pierced the correct sections. The assembly for the forearm will be completed next.

![image](https://github.com/user-attachments/assets/30cd9d10-9a5f-4f10-b101-21f32eea93c1)
![image](https://github.com/user-attachments/assets/9e60b94c-6ba1-4113-84b0-da294ade1f9f)

**Time spent: 4h**

# June 20: Creating forearm assembly and main assembly

Today, I created the assemblies for the forearm and the main assembly. This was primarily to set up the calculations I will do tomorrow to determine the reduction necessary in my gearbox. I also created a PLA material in SolidWorks to better match real life, so my math is more accurate. 

![image](https://github.com/user-attachments/assets/2045e586-b537-4750-b41b-75421f2c29b5)
![image](https://github.com/user-attachments/assets/b7e1df36-3af1-4300-9128-98d04e1513bc)

**Time spent: 2h**

# June 21: Designing the pivot gearbox

Today, I created the ratios for the pivot gearbox

After running some calculations based on SolidWorks’s data, I was able to calculate the torque required to pivot the arm. The calculations are shown below. Notably, I included a safety factor (x2) to ensure that nothing breaks–I would rather have a slower arm than an arm that cannot pivot. This is possible because the pivot is not required to have an extensive range of motion; so long as it operates within its range of motion at a reasonable speed, it will suffice.

Ultimately, I decided on a two-stage gearbox: 18T:54T (1:3) stage and an 18T:60T (3:10) stage. The relatively similar reductions ensure that the gears experience wear equally and that the packaging is optimized (since the gears are of similar sizes).

After adding a 20DP 60T gear to the arm (at 100% infill), the mass increased, and the center of mass (COM) distance from the pivot decreased. Ultimately, the new required torque stayed within the safety tolerance I had set.

Based on my experience, I ensured that I used the rated torque and moving torque of the servo motor. This will mitigate any substantial wear or damage to the servos.

![image](https://github.com/user-attachments/assets/d7bdec46-d9c0-402f-808c-132af56269cd)

**Time spent: 4h**

# June 23: Base arm and linear slide actuation

Today, I looked at how I might actuate the lateral movement of the arm and generally how the base of the arm might look. I think I will go with a linear slide in tandem with a pulley system. This is documented on my document, but essentially it involves a spool on a servo that is connected to two sets of string. Both strings will have enough length to span the linear slide, and when the servo turns in one direction, the strings will spool or despool correspondingly, pulling the chassis to the respective ends of the slide. I will flesh this out further after adding the arm, since a gearbox may need to be included depending on the torque required.

![image](https://github.com/user-attachments/assets/0d2ac032-7442-441c-a735-2611c325f0c5)

**Time spent: 4h**

# June 24: Gearbox and base arm cad

Today, sketched out what the gearbox may look like. I made sure to include areas for bearings and mounting since it's pretty easy to forget those. I also ensured that there was no interference between stages.

Another thing I tackled was the general layout of the control boards. namely the FE-URT-1 and NANO ESP32 boards that will be used.

Furthermore, I dealt with holes for wiring, which I may update to include areas for zipties, since the wires may be passing through the gearbox. The last thing I want is to have the wires stuck on the gears and just destroyed, so I may just do that. Most of the work today was just on cadding and specifying areas.

An area I struggled with was the gearbox. Since I decided on using dead axles for the gearbox, I would need to put the gears on bearings; however, this would cause an interference problem with the gears. Hence I decided to include spacers and widen the base of the arm to match the new spacing.

![image](https://github.com/user-attachments/assets/83c557e4-c3fa-4e2e-90d5-28a397aac3e5)

**Time spent: 6h**

# June 27: Power considerations and base arm changes

Today, I started thinking more about the power.

According to my current configuration, the power consumption will resemble this.

![image](https://github.com/user-attachments/assets/6130eeae-1c71-4cd2-a479-792cf7534bdb)

All of the data for the table was collected from datasheets. The current ratings of the servo motors were specified in terms of the rated current, as the torque calculations were based on the rated torque.

Since the total typical current is expected to be 6700 mA–6400 mA for the servos alone, I will add FE-URT-1. This is because the screw terminals on the FE-URT-1 have a maximum current rating of 6A. Hence, I will separate the SCS0009 servos and the SCS15 servos into two different FE-URT-1 boards. These will be powered by the same power source in parallel and connect to the Nano ESP32 board’s RX and TX in parallel.

Since some RC cars are commonly powered by the cumulative voltage range (6 - 7.4V), I will be using a 2S LiPo battery. These batteries are rated at 7.4 volts and are rechargeable, making them compatible with my purposes. Ideally, the battery would last for about an hour, meaning it would need a capacity of about 6700mAh. Moreover, it would be able to safely and continuously discharge 18 600 mA (18.6 A).

As such, the battery I have chosen is Zeee 2S 5200mAh Lipo Battery 7.4V 50C. Its capacity is approximately 46 minutes (at the rated current), and it can supply a maximum of 260 A, well above the peak current of the circuit.

These changes were reflected in the base arm sketches.

![image](https://github.com/user-attachments/assets/3c58090d-ac61-4cb1-b024-2e45e7616bbc)

**Time spent: 3h**

# June 29: Extrusion and changes

Today, I started extruding parts of the base arm, which will help me when determining the strength of my linear slide.

As I was extruding, many problems came to light. For example, I realized that I had not really thought about the mounting of the various boards and motors. Hence, a lot of time was spent on figuring that out.

![image](https://github.com/user-attachments/assets/e3ee0cc9-45ed-4039-9aff-520b6284cc15)
![image](https://github.com/user-attachments/assets/f034157e-77c9-438d-b68b-a618eb9b5020)

While extruding the gears, I realized that it would be almost impossible to 3D-print, meaning I had to redesign the gear so that it would be easily printed. To fix it, I had to reconsider the ordering of the gears, and ultimately settled on an assymetrical design, with the gear stages distinct and separate, as opposed to a "sandwich." 

Another thing I had to figure out was how to incorporate a bearing on the side with the smaller gear, which on its own would be unable to hold a bearing. Hence, I designed an extra spacer section that would be able to house the bearing, ensuring greater stability for the gear.

![image](https://github.com/user-attachments/assets/21057cfb-4e72-44c5-9c67-25bd9f380814)

**Time spent: 7h**

# July 3: Finishing assembly and updating main assembly

I worked on the assembly, making sure that I have the mass of the entire system before deciding on the rail and actuation of the rail. I created custom parts in Solidworks to ensure that all the masses are accurate, like the FE-URT-1 control board, or the LiPo battery. 

![image](https://github.com/user-attachments/assets/f5439228-a48e-4f49-9bf9-48397cdf952a)
![image](https://github.com/user-attachments/assets/150652b0-f3b7-4b65-b0e5-23d09ff753ec)

I also made the 60T gear a separate part that can be attached by bolts. This way, the forearm’s printing will be far easier and stronger.

![image](https://github.com/user-attachments/assets/d29890eb-82d7-4963-b1b3-2b2fc7260f04)

**Time spent: 6h**

# July 4: Determining slide and pulley size

For my purposes, I will be purchasing a linear slide from igus. This is because they provide a CAD file for the linear slide I chose, which will be incredibly useful. Moreover, their slides are easily configurable according to my requirements using their digital configuration tool: https://drylin-linear-guide-expert.igus.tools/requirements?l=en&c=CA.

While my initial requirements involved being able to play keys within a range of two octaves, igus does not sell a linear slide of that length (330mm). Hence, I will opt instead for a linear slide that enables the system to play half of the keys on the keyboard; in other words, the length of the slide should be ~612.85mm. This value will be rounded down to 501mm (the minimum rail length), since the hand itself is wide enough to enable the system to play all the keys on the piano.

![image](https://github.com/user-attachments/assets/44440fe0-1928-426f-93f8-e26423668c72)

All of these calculations are under the assumption that an octave is approximately 165mm (which is standard for pianos).

Under the assumption that drylin® W pillow block WJ200QM-01s will be used, which have a coefficient of friction of about 0.05. With the system’s mass being 3713.42g, which will be rounded up to 8000g (approximately twice the original value), the friction force will be approximately 4N. 

![image](https://github.com/user-attachments/assets/7347afd4-bd95-4cdb-89f6-023af0cef8f8)

Hence, with a pulley of OD 3cm, the system will reach an acceleration of approximately 3.75 ms^-2, which will be more than adequate. High acceleration is essential for this project, so I will try to keep the pulley OD as small as possible to increase the acceleration of the system.

**Time spent: 4h**

# July 7: Linear slide CAD, creating double pulley

Today I worked on the above. I added the rail and bearings into the CAD, as well as the corresponding mounting holes for the arm. With this, I created the double pulley that I will use for actuating the linear slide.

![image](https://github.com/user-attachments/assets/7eccecf6-77c3-4d74-ac19-8107d4e78950)
![image](https://github.com/user-attachments/assets/fc4a882c-0d70-43e3-95d0-4019251c223d)

I also updated the hand CAD to utilize the board I had created, simplifying wiring.

![image](https://github.com/user-attachments/assets/72aa1c15-549b-4b5d-8217-fd8881c3c3bd)

Furthermore, I began thinking about how to design the mounting blocks for which the pulleys will hold onto. This will be a challenge since there is only one mounting hole for these end blocks, so I will have to come up with a design that is somehow rather rigid in spite of that.

**Time spent: 5h**

# July 8: Linear slide end blocks

Today, I created the end blocks on the linear slide that the pulley can attach to. I made sure that the shafts were ratcheted, meaning that I could tension the pulleys freely. This ensures that there is the correct amount of slack in the strings. Now I am done with the blocks, I am done with all of the parts.

![image](https://github.com/user-attachments/assets/f6dca29b-4c14-4517-bfa3-c9f7565c4668)

A concern that may arise is tipping. Since the center of mass of the system is not directly above the rail (which is the system's contact point to the ground), there is a chance that the entire arm might tip over. While I find that this is unlikely, given the proximity of the COM to the rail, it is still possible. However, a simple solution may be implemented, wherein I simply tweek the design of the linear slide blocks to house weights, moving the COM closer to the rail and decreasing the likelihood of it tipping.

**Time spent: 3h**
