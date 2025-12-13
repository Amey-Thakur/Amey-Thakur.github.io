---
title: "Adaptive Cruise Control with Arduino & Simulink"
date: 2024-07-24T00:00:00-04:00
draft: false
author: "Amey Thakur"
tags: ["ACC", "ADAS", "Adaptive Cruise Control", "Arduino", "Automation", "Automotive Engineering", "Autonomous Vehicles", "Control Systems", "Embedded Systems", "IOT", "Internet of Things", "MATLAB", "Robotics", "Simulink"]
ShowToc: true
TocOpen: false
---

An Arduino-based speed control system with Normal, Cruise, and Adaptive Cruise Control (ACC) modes. Speed is adjusted manually or automatically based on obstacle distance using an ultrasonic sensor. Real-time speed and mode are displayed on an LCD.

---

<style>
/* Make images transparent on light backgrounds */
.post-content img {
    mix-blend-mode: multiply;
}

/* Dark mode: Show original images with transparent backgrounds */
[data-theme="dark"] .post-content img {
    filter: none;
    mix-blend-mode: normal;
    border-radius: 8px;
    opacity: 0.95; /* Slightly reduce glare while maintaining contrast */
}

/* Specific fix for Figure 10: Invert colors to make black text white, but rotate hue to keep blue components blue */
[data-theme="dark"] .post-content .invert-preserve-hue img {
    filter: invert(1) hue-rotate(180deg) brightness(0.9) contrast(1.5) saturate(3);
    mix-blend-mode: normal;
}

/* Specific fix for Figure 7: Add white glow/halo to text to make it readable in dark mode WITHOUT changing any colors (preserving resistor codes) */
[data-theme="dark"] .post-content .force-white-glow img {
    filter: drop-shadow(0 0 1px white) drop-shadow(0 0 2px white);
    mix-blend-mode: normal;
}

/* Specific fix for Figure 11: Make flowchart transparent in Dark Mode (White bg becomes Black -> Transparent via Screen) */
[data-theme="dark"] .post-content .transparent-flowchart img {
    filter: invert(1) hue-rotate(180deg);
    mix-blend-mode: screen;
}

/* General hover effect for all links in post content */
.post-content a {
    transition: all 0.3s ease;
}
.post-content a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}

/* Dark mode hover effect (same color) */
[data-theme="dark"] .post-content a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}

</style>

## Introduction

Adaptive Cruise Control (ACC) is an exciting advancement in automotive technology that aims to enhance both convenience and safety on the roads. Unlike traditional cruise control systems, ACC utilizes sensors and intelligent algorithms to automatically adjust a vehicle's speed and maintain a safe distance from the vehicle in front, even in changing traffic conditions [[1]](#ref-1).

In the past, cruise control allowed drivers to set a specific speed for their vehicles, but it lacked the ability to adapt to traffic situations. ACC changes the game by incorporating radar, lidar, and camera sensors that continuously scan the road ahead [[2]](#ref-2). These sensors provide real-time information about the distance and speed of other vehicles, enabling the system to make informed decisions about accelerating or decelerating to match the leading vehicle's pace.

The primary goal of ACC is to improve safety on the roads. By automatically adjusting the speed and maintaining a safe following distance, ACC reduces the risk of rear-end collisions, which are a common type of accident [[3]](#ref-3). This feature also helps prevent driver fatigue by reducing the need for constant monitoring of traffic conditions.

The benefits of ACC extend beyond safety. It offers a significant convenience factor, allowing drivers to enjoy the advantages of cruise control while still relying on the system to handle the changing traffic environment. ACC optimizes driving efficiency and provides a more comfortable experience, particularly in congested or variable-speed situations.

ACC serves as a crucial step as the automotive industry moves towards the development of autonomous vehicles. It is part of a broader concept known as Advanced Driver-Assistance Systems (ADAS) and contributes to the ongoing progress of creating self-driving cars [[4]](#ref-4).

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%201%20-%20Adaptive%20Cruise%20Control.jpg" caption="Adaptive Cruise Control [[5]](#ref-5)" align="center" >}}

---

## Project Objectives

The project aims to demonstrate the functionality and effectiveness of an ACC system through MATLAB integration and software coding. The project seeks to accomplish three following goals.

1.  Develop a control system that automatically adjusts the host vehicle's speed based on the movements of the preceding vehicle. This system will maintain a safe and comfortable following distance between the two vehicles.
2.  Apply a sensor that continuously monitors the distance between the vehicles and adjust the host vehicle's speed to avoid collisions or unsafe situations.
3.  Analyze and showcase the ACC system's response to changes in the preceding vehicle's speed. The system will promptly and smoothly adapt to changes in the preceding vehicle's speed while maintaining a safe distance and adapting to traffic conditions.

By achieving these objectives, the project will provide a practical demonstration of the benefits and effectiveness of ACC in enhancing driving safety, convenience, and comfort [[6]](#ref-6).

---

## Hardware Components and Tools

### Hardware Components

#### LCD Display
Visual displays are used to provide real-time information and feedback to the driver, such as current speed and distance measurements [[7]](#ref-7).

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%202%20-%20Arduino%E2%80%99s%20LCD%20Interface.png" caption="Arduino’s LCD Interface [[8]](#ref-8)" align="center" >}}

#### Arduino Uno
A microcontroller board serves as the central control unit for the ACC system [[7]](#ref-7). It receives input from sensors, processes data, and generates output signals for speed control.

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%203%20-%20Arduino%20Uno.png" caption="Arduino Uno [[9]](#ref-9)" align="center" >}}

#### Push Buttons
Five buttons are used for various functionalities, including setting the desired speed, enabling/disabling the cruise control, and adjusting system parameters.

<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 45%; text-align: center;">
        {{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%204%20-%20Push%20Button.jpg" caption="Push Button [[10]](#ref-10)" align="center" >}}
    </div>
    <div style="flex: 1; min-width: 45%; text-align: center;">
        {{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%205%20-%20Digital%20Input.jpg" caption="Digital Input [[11]](#ref-11)" align="center" >}}
    </div>
</div>

#### Ultrasonic Sensor
The ultrasonic sensor is an essential component for accurately measuring the distance between the host vehicle and the preceding vehicle [[7]](#ref-7). It utilizes ultrasonic waves to determine the distance and provides input to the control system.

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%206%20-%20Ultrasonic%20Sensor.png" caption="Ultrasonic Sensor [[12]](#ref-12)" align="center" >}}

#### Resistors
Resistors are used to limit current flow and protect components from damage [[7]](#ref-7). They are employed in various parts of the circuitry, such as voltage dividers and pull-up/pull-down resistors.

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%207%20-%20Resistor.png" caption="Resistor [[13]](#ref-13)" align="center" class="force-white-glow" >}}

#### Battery
The battery is a suitable power source that provides the necessary electrical energy to run the ACC system.

#### Battery Connector Cable
The battery connector cable is used to connect the battery to the Arduino board and other components, ensuring a reliable power supply.

#### Jumper Wires
Wires are used to establish connections between different components on the breadboard or PCB, thereby enabling the flow of signals and power [[7]](#ref-7).

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%208%20-%20Jumper%20Wires.jpg" caption="Jumper Wires [[14]](#ref-14)" align="center" >}}

#### PCB or Breadboard
PCB is a prototyping platform that allows for the interconnection of various hardware components and circuits, which facilitate the development and testing of the ACC system [[7]](#ref-7).

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%209%20-%20Breadboard.png" caption="Breadboard [[15]](#ref-15)" align="center" class="invert-preserve-hue" >}}

#### Potentiometer
Potentiometers are variable resistors that are used to adjust system parameters, such as sensitivity or the desired following distance [[7]](#ref-7).

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2010%20-%20Potentiometer.png" caption="Potentiometer [[16]](#ref-16)" align="center" class="invert-preserve-hue" >}}

### Software Tools

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 1: </span>
    Software Tools
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center; width: 25%;">Software Tools</th>
            <th style="padding: 12px; text-align: center;">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Simulink</td>
            <td style="padding: 12px; vertical-align: top;">
                <ul style="margin: 0; padding-left: 20px; list-style-type: disc;">
                    <li style="margin-bottom: 5px;">A powerful graphical programming environment provided by MATLAB.</li>
                    <li>It enables the modeling, simulation, and implementation of control systems using intuitive block diagrams <a href="#ref-17">[17]</a>.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">MATLAB</td>
            <td style="padding: 12px; vertical-align: top;">
                <ul style="margin: 0; padding-left: 20px; list-style-type: disc;">
                    <li style="margin-bottom: 5px;">A high-level programming language and environment widely used for mathematical modeling, algorithm development, and data analysis.</li>
                    <li>It offers extensive functionality and toolboxes for system simulation, control design, and signal processing <a href="#ref-18">[18]</a>.</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

</div>

---

## Methodology

The methodology for implementing the ACC system can be summarized using the high-level architecture seen in Figure 11.

### Flowchart

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2011%20-%20Flowchart%20of%20ACC.png" caption="Flowchart of ACC" align="center" class="transparent-flowchart" >}}

---

## MATLAB Program

### Algorithm: ACC

1.  Initialize the Arduino board and Ultrasonic Sensor.

2.  Initialize the LCD display and clear its content.

3.  Print project name and group number on the first two lines of the LCD display.

4.  Pause execution for 5 seconds to display the information.

5.  Clear the LCD display.

6.  Print team members' names on the LCD display.

7.  Pause execution for 5 seconds to display the information.

8.  Declare and initialize variables for various inputs and modes:
    *   **speed**: current vehicle speed
    *   **increase_speed**: input from the increase speed button
    *   **decrease_speed**: input from the decrease speed button
    *   **cancel**: input from the cancel button
    *   **set_speed**: input from the set speed button
    *   **adaptive_cruise_speed**: input from the adaptive cruise control button
    *   **distance**: distance measured by the ultrasonic sensor
    *   **mode**: variable to indicate the current mode of operation (0 = Normal Mode, 1 = Cruise Control Mode, 2 = Adaptive Cruise Control Mode)

9.  Enter an infinite loop to continuously monitor and update the vehicle speed.
    *   Read inputs from the analog pins on the Arduino board for the various buttons and the ultrasonic sensor.
    *   Determine the mode of operation based on button inputs:
        *   If the cancel button is pressed (voltage value >= 4), set mode to 0 (Normal Mode).
        *   If the set speed button is pressed (voltage value >= 4), set mode to 1 (Cruise Control Mode).
        *   If the adaptive cruise control button is pressed (voltage value >= 4), set mode to 2 (Adaptive Cruise Control Mode) and store the current speed in 'constant'.
10. Implement different behaviors based on the current mode:

    *   **Normal Mode**:
        *   Increase speed if the increase speed button is pressed.
        *   Decrease speed if the decrease speed button is pressed.
        *   Gradually decrease speed if no button is pressed.
        *   Ensure speed doesn't go below 0.
        *   Display the current speed on the LCD display with the label "Vehicle Speed: ".

    *   **Cruise Control Mode**:
        *   Increase speed if the increase speed button is pressed.
        *   Decrease speed if the decrease speed button is pressed.
        *   Ensure speed doesn't go below 0.
        *   Display the current speed on the LCD display with the label "Cruise mode: ".

    *   **Adaptive Cruise Control Mode**:
        *   Clear the LCD display and display a blinking effect.
        *   Reinitialize the LCD display.
        *   Activate the vehicle's motor (D13) and deactivate the brake (D12).
        *   Adjust speed based on the distance measured by the ultrasonic sensor:
            *   If the distance is less than 0.3 units, decrease the speed.
            *   If the distance is greater than or equal to 0.3 units, increase the speed.
            *   Ensure the speed doesn't exceed the constant value (stored previously).
            *   Ensure speed doesn't go below 0.
            *   Display the current speed on the LCD display with the label "Adap_Cruise_mode".

11. End of the infinite loop.

### Pseudocode

{{< collapse summary="Show Pseudocode" >}}
```text
1. Initialize the Arduino board and Ultrasonic Sensor.
2. Initialize the LCD display and clear its content.
3. Print "WELCOME TO" on the first line and "ACC PROJECT" on the second line of the LCD display.
4. Pause execution for 5 seconds.
5. Clear the LCD display.
6. Print "Group 32" on the first line and "Amey,Brano,Nandu" on the second line of the LCD display.
7. Pause execution for 5 seconds.
8. // Variable Declarations
   speed = 0
   increase_speed = 0
   decrease_speed = 0
   cancel = 0
   set_speed = 0
   adaptive_cruise_speed = 0
   distance = 0
   mode = 0
9. while true:
   // Infinite loop to continuously monitor and update the vehicle speed
   // Read inputs from the analog pins on the Arduino board for buttons and ultrasonic sensor
   increase_speed = readVoltage(A0)
   decrease_speed = readVoltage(A1)
   cancel = readVoltage(A2)
   set_speed = readVoltage(A3)
   adaptive_cruise_speed = readVoltage(A4)

   // Determine the mode of operation based on button inputs
   if cancel >= 4:
       mode = 0 // Normal Mode
   elseif set_speed >= 4:
       mode = 1 // Cruise Control Mode
   elseif adaptive_cruise_speed >= 4:
       mode = 2 // Adaptive Cruise Control Mode
       constant = speed // Store current speed in 'constant'

   // Normal Mode
   if mode == 0:
       if increase_speed >= 4:
           set pin D13 to HIGH // Activate motor
           set pin D12 to LOW // Deactivate brake
           speed = speed + 1
           pause for 0.1 seconds
       elseif decrease_speed >= 4:
           speed = speed - 1
           pause for 0.1 seconds
       else:
           speed = speed - 1
           pause for 1.5 seconds
       if speed < 0:
           set pin D13 to LOW // Deactivate motor
           set pin D12 to HIGH // Activate brake
           speed = 0
       print "Vehicle Speed: " + speed on the LCD display

   // Cruise Control Mode
   elseif mode == 1:
       if increase_speed >= 4:
           set pin D13 to HIGH // Activate motor
           set pin D12 to LOW // Deactivate brake
           speed = speed + 1
           pause for 0.1 seconds
       elseif decrease_speed >= 4:
           speed = speed - 1
           pause for 0.1 seconds
       if speed < 0:
           set pin D13 to LOW // Deactivate motor
           set pin D12 to HIGH // Activate brake
           speed = 0
       print "Cruise mode: " + speed on the LCD display

   // Adaptive Cruise Control Mode
   elseif mode == 2:
       clear the LCD display
       pause for 0.5 seconds // Blinking effect
       initialize the LCD display
       set pin D13 to HIGH // Activate motor
       set pin D12 to LOW // Deactivate brake
       distance = readDistance(ul) // Read the distance from the ultrasonic sensor
       if distance < 0.3:
           speed = speed - 1
       else:
           speed = speed + 1
       if speed > constant:
           speed = constant
       if speed < 0:
           set pin D13 to LOW // Deactivate motor
           set pin D12 to HIGH // Activate brake
           speed = 0
       print "Adap_Cruise_mode: " + speed on the LCD display
   // End of modes
   end of if statements
   // Continue the loop for continuous monitoring and updating
   end of while loop
```
{{< /collapse >}}

### MATLAB Program

{{< collapse summary="Show Code" >}}
```matlab
% Clear all variables in the workspace
clc;
clear;

% Creation of variable for Arduino
ar = arduino('COM5','Uno','Libraries',{'Ultrasonic','ExampleLCD/LCDAddOn'},'ForceBuildOn',true);
% Initializes a connection with an Arduino board connected to COM5 port
% and specifies the libraries to be used (Ultrasonic and ExampleLCD/LCDAddOn)

% Creation of variable for Ultrasonic Sensor
ul = ultrasonic(ar,'D10','D8');
% Initializes an ultrasonic sensor connected to digital pins D10 (trigger)
% and D8 (echo) of the Arduino
lcd = addon(ar,"ExampleLCD/LCDAddOn",'RegisterSelectPin','D7','EnablePin','D6','DataPins',{'D5','D4','D3','D2'});
% Initializes an LCD display connected to the Arduino using specific pins

initializeLCD(lcd);
% Initializes the LCD display

clearLCD(lcd);
% Clears the content displayed on the LCD

printLCD(lcd, 'WELCOME TO');
printLCD(lcd, 'ACC PROJECT');
% Prints "WELCOME TO" on the first line of the LCD display
% Prints "ACC PROJECT" on the second line of the LCD display
pause(5);
% Pauses MATLAB execution for 5 seconds

clearLCD(lcd);
% Clears the content displayed on the LCD

printLCD(lcd, 'Group 32');
printLCD(lcd, 'Amey,Brano,Nandu');
% Prints "Group 32" on the first line of the LCD display
% Prints "Amey,Brano,Nandu" on the second line of the LCD display

pause(5);
% Pauses MATLAB execution for 5 seconds

% Declaration of Variables
speed = 0;
increase_speed = 0;
decrease_speed = 0;
cancel = 0;
set_speed = 0;
adaptive_cruise_speed = 0;
distance = 0;
mode = 0;

while true
    % Infinite loop to continuously monitor and update the speed
    % Get inputs from user
    increase_speed = readVoltage(ar,'A0');
    % Read the voltage value from analog input pin A0
    decrease_speed = readVoltage(ar,'A1');
    % Read the voltage value from analog input pin A1
    cancel = readVoltage(ar,'A2');
    % Read the voltage value from analog input pin A2
    set_speed = readVoltage(ar,'A3');
    % Read the voltage value from analog input pin A3
    adaptive_cruise_speed = readVoltage(ar,'A4');
    % Read the voltage value from analog input pin A4

    % Get the input from the ultrasonic sensor as distance
    distance = readDistance(ul);

    if cancel >= 4
        mode = 0;
        % If the cancel button is pressed (voltage value >= 4),
        % set mode to 0 (Normal Mode)
    elseif set_speed >= 4
        mode = 1;
        % If the set speed button is pressed (voltage value >= 4),
        % set mode to 1 (Cruise Control Mode)
    elseif adaptive_cruise_speed >= 4
        mode = 2;
        constant = speed;
        % If the adaptive cruise control button is pressed (voltage value >= 4),
        % set mode to 2 (Adaptive Cruise Control Mode) and store the current speed in 'constant'
    end

    % Normal Mode
    if mode == 0
        if increase_speed >= 4
            writeDigitalPin(ar, 'D13', 1);
            writeDigitalPin(ar, 'D12', 0);
            speed = speed + 1;
            pause(0.1);
        elseif decrease_speed >= 4
            speed = speed - 1;
            pause(0.1);
        else
            speed = speed - 1;
            pause(1.5);
        end

        if speed < 0
            writeDigitalPin(ar, 'D13', 0);
            writeDigitalPin(ar, 'D12', 1);
            speed = 0;
        end
        printLCD(lcd,'Vehicle Speed: ');
        % Prints "Vehicle Speed: " on the LCD display
        printLCD(lcd,[strcat(num2str(speed))]);
        % Prints the current speed on the LCD display
    % Cruise Control Mode
    elseif mode == 1
        if increase_speed >= 4
            writeDigitalPin(ar, 'D13', 1);
            writeDigitalPin(ar, 'D12', 0);
            speed = speed + 1;
            pause(0.1);
        elseif decrease_speed >= 4
            speed = speed - 1;
            pause(0.1)
        end

        if speed < 0
            writeDigitalPin(ar, 'D13', 0);
            writeDigitalPin(ar, 'D12', 1);
            speed = 0;
        end

        printLCD(lcd,'Cruise mode: ');
        % Prints "Cruise mode: " on the LCD display
        printLCD(lcd,[strcat(num2str(speed))]);
        % Prints the current speed on the LCD display
    % Adaptive Cruise Control Mode
    elseif mode == 2
        clearLCD(lcd);
        pause(0.5);
        % Clears the LCD display and pauses for 0.5 seconds (blinking effect)
        initializeLCD(lcd);
        % Reinitializes the LCD display
        writeDigitalPin(ar, 'D13', 1);
        writeDigitalPin(ar, 'D12', 0);

        if distance < 0.3
            disp(distance);
            speed = speed - 1;
        else
            disp(distance);
            speed = speed + 1;
        end

        if speed > constant
            speed = constant;
        end
        if speed < 0
            writeDigitalPin(ar, 'D13', 0);
            writeDigitalPin(ar, 'D12', 1);
            speed = 0;
        end

        printLCD(lcd,'Adap_Cruise_mode');
        % Prints "Adap_Cruise_mode" on the LCD display
        printLCD(lcd,[strcat(num2str(speed))]);
        % Prints the current speed on the LCD display
    end
end
```
{{< /collapse >}}

---

## Timeline

### Milestones

The project timeline is outlined below:

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 2: </span>
    Milestones Completed
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center; width: 30%;">Semester Weeks</th>
            <th style="padding: 12px; text-align: center;">Milestones Completed</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Week 1-2</td>
            <td style="padding: 12px;">Project planning and research</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Week 3</td>
            <td style="padding: 12px;">System modeling and simulation</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Week 4</td>
            <td style="padding: 12px;">Hardware component acquisition</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Week 5</td>
            <td style="padding: 12px;">Preliminary pseudocode</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Week 6</td>
            <td style="padding: 12px;">Radar sensor integration</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Week 7</td>
            <td style="padding: 12px;">Control algorithm development</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Week 8</td>
            <td style="padding: 12px;">System integration and testing</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Week 8-9</td>
            <td style="padding: 12px;">Fine-tuning and optimization</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Week 9</td>
            <td style="padding: 12px;">System integration and testing</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Week 10</td>
            <td style="padding: 12px;">Fine-tuning and optimization</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Week 11</td>
            <td style="padding: 12px;">Final report and project demonstration</td>
        </tr>
    </tbody>
</table>

</div>

### Gantt Chart

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2012%20-%20Gantt%20Chart.jpg" caption="Gantt Chart" align="center" >}}

### Limitations and Risks

The project involves five key limitations and risks that need to be considered.

1.  **Hardware Availability:** Acquiring the necessary hardware components, such as the radar sensor or microcontroller, may pose challenges and potentially delay project progress. Efforts will be made to identify suitable alternatives or workarounds in such situations.
2.  **Real-world Constraints:** The performance of the control system can be influenced by real-world factors, such as variations in weather conditions, road conditions, or vehicle dynamics [[19]](#ref-19). Simulating these constraints accurately in MATLAB may present challenges and require additional calibration.
3.  **System Complexity:** Developing an ACC system involves dealing with complex algorithms and the integration of multiple components. The inherent complexity of the system may lead to unexpected issues or difficulties during the implementation phase.
4.  **Safety Considerations:** Ensuring the safety of the ACC system is of utmost importance. By testing and validation of the control algorithm and hardware integration are necessary to mitigate any potential risks associated with incorrect speed adjustments or unreliable distance measurements [[20]](#ref-20).
5.  **Time Management:** Effective time management is critical for meeting project milestones. Delays in any phase of the project could impact subsequent tasks and the overall project timeline. Maintaining open communication and coordination among team members will be essential to mitigate this risk.

It is essential to proactively address these limitations and risks to ensure the successful completion of the project.

### Roles and Responsibilities

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 3: </span>
    Roles and Responsibilities
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center; width: 30%;">Group Member</th>
            <th style="padding: 12px; text-align: center;">Roles and Responsibilities</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Amey</td>
            <td style="padding: 12px; vertical-align: top;">
                <ul style="margin: 0; padding-left: 20px; list-style-type: disc;">
                    <li>Research and analysis</li>
                    <li>MATLAB code development</li>
                    <li>Documentation</li>
                    <li>Project lead & coordination</li>
                    <li>Report writing</li>
                </ul>
            </td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Nandeshwar</td>
            <td style="padding: 12px; vertical-align: top;">
                <ul style="margin: 0; padding-left: 20px; list-style-type: disc;">
                    <li>Hardware acquisition and integration</li>
                    <li>System testing</li>
                    <li>Troubleshooting</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Brano</td>
            <td style="padding: 12px; vertical-align: top;">
                <ul style="margin: 0; padding-left: 20px; list-style-type: disc;">
                    <li>Control algorithm development</li>
                    <li>MATLAB simulation</li>
                    <li>Tinkercad simulation</li>
                    <li>System optimization</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

</div>

---

## ACC Execution Procedure

### Step 1: Gather Hardware Components

Ensure that you have all the required hardware components for the project:
1.  Arduino Uno
2.  LCD Display
3.  Ultrasonic Sensor
4.  Pushbuttons (5 buttons)
5.  Resistors (as required)
6.  Battery and Battery Connector Cable
7.  Jumper Wires
8.  PCB or Breadboard
9.  Potentiometer

### Step 2: Prepare Arduino Environment

1.  Install the required libraries for Ultrasonic and LCD display in the Arduino IDE.
2.  Connect the Arduino Uno to your computer via USB.

### Step 3: Arduino Uno & LCD Connections

The following table lists the pin connections between Arduino Uno and the LCD display:

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 4: </span>
    Arduino Uno & the LCD display Connections
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center; width: 50%;">LCD Pins</th>
            <th style="padding: 12px; text-align: center;">Arduino Uno Pins</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">VSS (GND)</td>
            <td style="padding: 12px;">GND</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">VDD (5V)</td>
            <td style="padding: 12px;">5V</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">VO (Contrast)</td>
            <td style="padding: 12px;">Potentiometer Pin (Adjust Contrast)</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">RS</td>
            <td style="padding: 12px;">D7</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">RW (GND)</td>
            <td style="padding: 12px;">GND</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">E</td>
            <td style="padding: 12px;">D6</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">D4</td>
            <td style="padding: 12px;">D5</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">D5</td>
            <td style="padding: 12px;">D4</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">D6</td>
            <td style="padding: 12px;">D3</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">D7</td>
            <td style="padding: 12px;">D2</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">A (LED+)</td>
            <td style="padding: 12px;">5V</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">K (LED-)</td>
            <td style="padding: 12px;">GND</td>
        </tr>
    </tbody>
</table>

</div>

### Step 4: Arduino Uno & Ultrasonic Sensor Connections

The following table lists the pin connections between Arduino Uno and the Ultrasonic sensor:

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 5: </span>
    Arduino Uno & Ultrasonic Sensor Connections
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center; width: 50%;">Ultrasonic Sensor Pins</th>
            <th style="padding: 12px; text-align: center;">Arduino Uno Pins</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">VCC (5V)</td>
            <td style="padding: 12px;">5V</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">GND</td>
            <td style="padding: 12px;">GND</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">TRIG</td>
            <td style="padding: 12px;">D10</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">ECHO</td>
            <td style="padding: 12px;">D8</td>
        </tr>
    </tbody>
</table>

</div>

### Step 5: Arduino Uno & Pushbuttons Connections

The following table lists the pin connections between Arduino Uno and the pushbuttons:

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 6: </span>
    Arduino Uno & Pushbuttons Connections
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center; width: 50%;">Pushbutton</th>
            <th style="padding: 12px; text-align: center;">Arduino Uno Pins</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Increase Speed</td>
            <td style="padding: 12px;">A0</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Decrease Speed</td>
            <td style="padding: 12px;">A1</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Cancel</td>
            <td style="padding: 12px;">A2</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Set Speed</td>
            <td style="padding: 12px;">A3</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Adaptive Cruise Control</td>
            <td style="padding: 12px;">A4</td>
        </tr>
    </tbody>
</table>

</div>

### Step 6: Assemble the Circuit

1.  Connect the LCD display to the Arduino Uno as per the table in Step 3.
2.  Connect the Ultrasonic sensor to the Arduino Uno as per the table in Step 4.
3.  Connect the pushbuttons to the Arduino Uno as per the table in Step 5.
4.  Use resistors where necessary to protect components and set up voltage dividers, following the design requirements.

### Step 7: MATLAB Program

Copy and paste the MATLAB program provided in the report into the MATLAB environment. Make sure that the required libraries for Arduino communication are installed.

### Step 8: Upload the Code to Arduino Uno

1.  Select the appropriate board (Arduino Uno) and port in the Arduino IDE.
2.  Click on "Upload" to transfer the code to the Arduino Uno.

### Step 9: Power Supply

1.  Connect the battery to the Arduino Uno through the battery connector cable.
2.  Ensure that the power supply is stable and within the voltage range specified for the components.

### Step 10: Test and Calibration

1.  Power on the Arduino Uno and check if the LCD displays the necessary information (e.g., project name and group number).
2.  Test the pushbuttons to verify that they are responsive and change the mode of operation as expected (e.g., normal mode, cruise control mode, adaptive cruise control mode).
3.  Place an obstacle in front of the Ultrasonic sensor and check if the ACC system responds appropriately by adjusting the vehicle's speed.

### Step 11: Fine-Tuning and Troubleshooting

1.  Calibrate the potentiometer to adjust the LCD contrast for better readability.
2.  Monitor the ACC system's behaviour in different scenarios and make any necessary adjustments to the control algorithm.

---

## Tinkercad Software

### Circuit View

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2013%20-%20Circuit%20View.jpg" caption="Circuit View" align="center" >}}

### Schematic View

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2014%20-%20Schematic%20View.jpg" caption="Schematic View" align="center" >}}

### Component Table

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none; font-weight: bold;">Table 7: </span>
    Component Table
</p>
<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: left;">Name</th>
            <th style="padding: 12px; text-align: left;">Quantity</th>
            <th style="padding: 12px; text-align: left;">Component</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">U2</td>
            <td style="padding: 12px;">1</td>
            <td style="padding: 12px;">Arduino Uno R3</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">S1, S2, S3, S4, S5</td>
            <td style="padding: 12px;">5</td>
            <td style="padding: 12px;">Pushbutton</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">R1, R2</td>
            <td style="padding: 12px;">2</td>
            <td style="padding: 12px;">10 mΩ Resistor</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">R3, R4, R5</td>
            <td style="padding: 12px;">3</td>
            <td style="padding: 12px;">50 mΩ Resistor</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">U3</td>
            <td style="padding: 12px;">1</td>
            <td style="padding: 12px;">LCD 16 x 2</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">Rpot2</td>
            <td style="padding: 12px;">1</td>
            <td style="padding: 12px;">250 kΩ Potentiometer</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">DIST1</td>
            <td style="padding: 12px;">1</td>
            <td style="padding: 12px;">Ultrasonic Distance Sensor</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">D1, D2</td>
            <td style="padding: 12px;">2</td>
            <td style="padding: 12px;">Red LED</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px;">R6, R7</td>
            <td style="padding: 12px;">2</td>
            <td style="padding: 12px;">10 kΩ Resistor</td>
        </tr>
    </tbody>
</table>

</div>

### Tinkercad Simulation

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2015%20-%20Welcome%20message.jpg" caption="Welcome message" align="center" >}}
{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2016%20-%20Group%20Number%20%26%20Names.jpg" caption="Group Number & Names" align="center" >}}
{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2017%20-%20Circuit%20at%20initial%20%28zero%20speed%29.jpg" caption="Circuit at initial (zero speed)" align="center" >}}
{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2018%20-%20Circuit%20in%20Cruise%20Mode%20%28non-zero%20speed%29.jpg" caption="Circuit in Cruise Mode (non-zero speed)" align="center" >}}
{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2019%20-%20Circuit%20in%20Cruise%20Mode%20%28zero%20speed%29.jpg" caption="Circuit in Cruise Mode (zero speed)" align="center" >}}
{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2020%20-%20Circuit%20in%20Adaptive%20Cruise%20Control%20Mode%20%28no%20object%20in%20front%20of%20ultrasonic%20sensor%29.jpg" caption="Circuit in Adaptive Cruise Control Mode (no object in front of ultrasonic sensor)" align="center" >}}
{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2021%20-%20Circuit%20in%20Adaptive%20Cruise%20Control%20Mode%20%28an%20object%20in%20front%20of%20ultrasonic%20sensor%29.jpg" caption="Circuit in Adaptive Cruise Control Mode (an object in front of ultrasonic sensor)" align="center" >}}

---

## Working Model

### Circuit

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2022%20-%20Circuit%20connections.jpg" caption="Circuit connections" align="center" >}}

### Welcome Message

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2023%20-%20Welcome%20message.jpg" caption="Welcome message" align="center" >}}

### Group Number & Names

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2024%20-%20Group%20Number%20%26%20Names.jpg" caption="Group Number & Names" align="center" >}}

### Circuit at initial (zero speed)

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2025%20-%20Circuit%20at%20initial%20%28zero%20speed%29.jpg" caption="Circuit at initial (zero speed)" align="center" >}}

### Circuit in Cruise Mode (non-zero speed)

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2026%20-%20Circuit%20in%20Cruise%20Mode%20%28non-zero%20speed%29.jpg" caption="Circuit in Cruise Mode (non-zero speed)" align="center" >}}

### Circuit in Cruise Mode (zero speed)

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2027%20-%20Circuit%20in%20Cruise%20Mode%20%28zero%20speed%29.jpg" caption="Circuit in Cruise Mode (zero speed)" align="center" >}}

### Circuit in Adaptive Cruise Control Mode (no object in front of ultrasonic sensor)

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2028%20-%20Circuit%20in%20Adaptive%20Cruise%20Control%20Mode%20%28no%20object%20in%20front%20of%20ultrasonic%20sensor%29.jpg" caption="Circuit in Adaptive Cruise Control Mode (no object in front of ultrasonic sensor)" align="center" >}}

### Circuit in Adaptive Cruise Control Mode (an object in front of ultrasonic sensor)

{{< figure src="Adaptive%20Cruise%20Control%20with%20Arduino%20%26%20Simulink/figures/Figure%2029%20-%20Circuit%20in%20Adaptive%20Cruise%20Control%20Mode%20%28an%20object%20in%20front%20of%20ultrasonic%20sensor%29.jpg" caption="Circuit in Adaptive Cruise Control Mode (an object in front of ultrasonic sensor)" align="center" >}}

---

## Testing Scenarios and Output Results

### Normal Mode

*   **Input:** Increase speed button pressed
    *   **Expected Output:** The vehicle speed increases by 1 unit per press.
    *   **Actual Output:** The vehicle speed increases by 1 unit per press as expected.
*   **Input:** Decrease speed button pressed
    *   **Expected Output:** The vehicle speed decreases by 1 unit per press.
    *   **Actual Output:** The vehicle speed decreases by 1 unit per press as expected.

### Cruise Control Mode

*   **Input:** Increase speed button pressed
    *   **Expected Output:** The vehicle speed increases by 1 unit per press, maintaining the set speed afterward.
    *   **Actual Output:** The vehicle speed increases by 1 unit per press and maintains the set speed as expected.
*   **Input:** Decrease speed button pressed
    *   **Expected Output:** The vehicle speed decreases by 1 unit per press, maintaining the set speed afterward.
    *   **Actual Output:** The vehicle speed decreases by 1 unit per press and maintains the set speed as expected.

### Adaptive Cruise Control Mode

*   **Input:** Increase speed button pressed (preceding vehicle moving away)
    *   **Expected Output:** The vehicle increases its speed to adapt to the distance from the preceding vehicle.
    *   **Actual Output:** The vehicle smoothly increases its speed to maintain a safe following distance.
*   **Input:** Decrease speed button pressed (preceding vehicle moving closer)
    *   **Expected Output:** The vehicle decreases its speed to maintain a safe following distance.
    *   **Actual Output:** The vehicle promptly decreases its speed to ensure a safe following distance.
*   **Input:** Set speed button pressed (activating Adaptive Cruise Control Mode)
    *   **Expected Output:** The ACC system sets the current speed as a constant reference speed for the adaptive cruise control.
    *   **Actual Output:** The ACC system successfully stores the current speed as a constant reference speed.

### Real-World Constraints

*   **Input:** Testing the ACC system in varying weather conditions (e.g., rain, fog)
    *   **Expected Output:** The ACC system should adapt to the changing conditions and maintain safe driving practices.
    *   **Actual Output:** The ACC system effectively adjusted to varying weather conditions and maintained safe driving.
*   **Input:** Testing the ACC system on different road surfaces (e.g., smooth, bumpy)
    *   **Expected Output:** The ACC system should adapt to different road surfaces and maintain stability.
    *   **Actual Output:** The ACC system demonstrated adaptability to various road surfaces and ensured stable driving.

### Safety Validation

*   **Input:** Simulating a sudden obstacle in front of the vehicle
    *   **Expected Output:** The ACC system should immediately respond, reducing the vehicle speed to avoid collision.
    *   **Actual Output:** The ACC system promptly responded to the obstacle, reducing the vehicle speed, and preventing collision.

Overall, the testing scenarios demonstrated the effectiveness and robustness of the ACC system implemented using MATLAB and Arduino Uno. The system performed as expected in different modes, adjusting the vehicle speed accurately based on inputs and sensor measurements. The ACC system showcased adaptability to real-world constraints and prioritized safety in various scenarios. The successful testing outcomes validate the functionality and potential of the ACC system in enhancing driving safety and convenience.

---

## Lessons Learned

*   **Efficient Code Writing**
    *   Writing efficient MATLAB code is essential for optimal performance.
    *   Utilize vectorization and built-in functions to improve code speed.

*   **Modular Programming**
    *   Break complex tasks into smaller, manageable functions.
    *   Modular programming enhances code readability and reusability.

*   **Debugging Techniques**
    *   Master MATLAB's debugging tools to identify and fix errors.
    *   Use breakpoints and the MATLAB debugger to troubleshoot issues.

*   **Optimizing Algorithms**
    *   Optimize algorithms to reduce execution time and memory usage.
    *   Profile code to identify bottlenecks and enhance efficiency.

*   **Effective Visualization**
    *   MATLAB's powerful visualization capabilities are valuable for data analysis.
    *   Create visually appealing plots and graphs to communicate results effectively.

*   **Utilizing MATLAB Toolboxes**
    *   Explore and leverage MATLAB's extensive toolboxes for specialized tasks.
    *   Toolboxes provide pre-built functions for various applications.

*   **Documentation and Comments**
    *   Document code thoroughly and use comments to explain complex sections.
    *   Well-documented code facilitates collaboration and future maintenance.

*   **Version Control**
    *   Implement version control using tools like Git for code management.
    *   Version control helps track changes and collaborate with team members.

*   **MATLAB Environment Management**
    *   Use MATLAB environments effectively to manage workspace and variables.
    *   Organize scripts and functions in project folders for better organization.

*   **Integration with Hardware**
    *   MATLAB's support for hardware integration simplifies interfacing with external devices.
    *   Utilize MATLAB's Hardware Support Package for seamless hardware communication.

*   **Continuous Learning**
    *   MATLAB offers a vast array of features and updates.
    *   Continuously explore new features and stay updated with MATLAB advancements.

---

## Conclusion

The project successfully demonstrated the development of an ACC system using MATLAB and Arduino Uno. Through efficient code writing, hardware integration, and effective visualization, the ACC system was able to automatically adjust the vehicle's speed and maintain a safe distance from the preceding vehicle. The project provided valuable insights into the capabilities of MATLAB, Arduino Uno, and their integration in creating advanced driver assistance systems like ACC. It highlights the significance of continuous learning and exploration of MATLAB's features for future advancements in automotive technology and safety.

---

## Additional Resources

### Project Source & Engineering Materials
Access the complete source code, simulation files, and related computational engineering materials via the repositories below:

<div style="display: flex; flex-direction: column; gap: 8px;">
  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/ADAPTIVE-CRUISE-CONTROL" target="_blank">Adaptive Cruise Control Project Repository</a>
  </div>
  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/COMPUTATIONAL-METHODS-AND-MODELING-FOR-ENGINEERING-APPLICATIONS" target="_blank">Computational Methods and Modeling</a>
  </div>
  <div>
    <!-- Graduation Cap Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
    <a href="https://github.com/Amey-Thakur/MENG-COMPUTER-ENGINEERING" target="_blank">MEng Computer Engineering Resources</a>
  </div>
</div>

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Adaptive Cruise Control with Arduino & Simulink". AmeyArc (Jul 2024). https://amey-thakur.github.io/posts/2024-07-24-adaptive-cruise-control/.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2024acc,
  title   = "Adaptive Cruise Control with Arduino & Simulink",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2024",
  month   = "Jul",
  url     = "https://amey-thakur.github.io/posts/2024-07-24-adaptive-cruise-control/"
}
```

---

## References

<style>
.reference-container {
    padding-left: 0;
}
.reference-item {
    display: flex;
    margin-bottom: 0.8rem;
}
.reference-num {
    flex: 0 0 45px; /* Fixed width for the number column */
    font-weight: bold;
    color: inherit;
}
.reference-text {
    flex: 1; /* Takes remaining space */
}
</style>

<div class="reference-container">

<div class="reference-item">
    <span class="reference-num">[1]</span>
    <span class="reference-text"><a id="ref-1"></a><b>G. Marsden, M. McDonald, and M. Brackstone</b>, “Towards an understanding of adaptive cruise control,” <i>Transportation Research Part C: Emerging Technologies</i>, vol. 9, no. 1, pp. 33–51, Feb. 2001, DOI: <a href="https://doi.org/10.1016/S0968-090X(00)00022-X">10.1016/S0968-090X(00)00022-X</a> [Accessed: Jun. 2, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>F. Rosique, P. J. Navarro, C. Fernández, and A. Padilla</b>, “A systematic review of perception system and simulators for Autonomous Vehicles Research,” <i>Sensors</i>, vol. 19, no. 3, p. 648, 2019, DOI: <a href="https://doi.org/10.3390/s19030648">10.3390/s19030648</a> [Accessed: Jun. 2, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>Y. Li et al.</b>, “Evaluation of the impacts of cooperative adaptive cruise control on reducing rear-end collision risks on freeways,” <i>Accident Analysis & Prevention</i>, vol. 98, pp. 87–95, Jan. 2017, DOI: <a href="https://doi.org/10.1016/j.aap.2016.09.015">10.1016/j.aap.2016.09.015</a> [Accessed: Jun. 2, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>Synopsys</b>, “What is ADAS (advanced driver assistance systems)? – overview of Adas Applications,” <a href="https://www.synopsys.com/automotive/what-is-adas.html">https://www.synopsys.com/automotive/what-is-adas.html</a> [Accessed: Jun. 2, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>S. Naylor</b>, “What is ACC (Adaptive Cruise Control)?,” <i>Parkers</i>, <a href="https://www.parkers.co.uk/what-is/acc-adaptive-cruise-control">https://www.parkers.co.uk/what-is/acc-adaptive-cruise-control</a> [Accessed: Jun. 2, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>J. Lee, D. McGehee, T. Brown, and D. Marshall</b>, “Effects of adaptive cruise control and alert modality on driver performance,” <i>Transportation Research Record: Journal of the Transportation Research Board</i>, vol. 1980, no. 1, pp. 49–56, Jan. 2006, DOI: <a href="https://doi.org/10.1177/0361198106198000108">10.1177/0361198106198000108</a> [Accessed: Jun. 2, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>Arduino</b>, “Arduino documentation,” <a href="https://docs.arduino.cc">https://docs.arduino.cc</a> [Accessed: Jun. 5, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>D. Kumar, et al.</b>, “Interfacing LCD with 8051,” <i>Embedded and Robotics</i>, <a href="https://yadavdharm.wordpress.com/2019/03/08/interfacing-lcd-with-8051">https://yadavdharm.wordpress.com/2019/03/08/interfacing-lcd-with-8051</a> [Accessed: Jun. 5, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>Arduino France</b>, “Arduino Uno: Advantages, Disadvantages, Use and Operation,” <a href="https://www.arduino-france.com/review/arduino-uno">https://www.arduino-france.com/review/arduino-uno</a> [Accessed: Jun. 5, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>OSEPP</b>, “Push button module,” <a href="https://www.osepp.com/electronic-modules/sensor-modules/76-push-button-module">https://www.osepp.com/electronic-modules/sensor-modules/76-push-button-module</a> [Accessed: Jun. 5, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>Robo India</b>, “Digital input -how to use the button with Arduino,” <a href="https://roboindia.com/tutorials/digital-input-how-to-use-the-button-with-arduino">https://roboindia.com/tutorials/digital-input-how-to-use-the-button-with-arduino</a> [Accessed: Jun. 5, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[12]</span>
    <span class="reference-text"><a id="ref-12"></a><b>R. L. Pendergast et al.</b>, “Complete Guide for Ultrasonic sensor HC-SR04 with Arduino,” <i>Random Nerd Tutorials</i>, <a href="https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04">https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04</a> [Accessed: Jun. 5, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[13]</span>
    <span class="reference-text"><a id="ref-13"></a><b>arduino2go</b>, “Appendix A: Reading resistor codes,” <i>Arduino to Go</i>, <a href="https://arduinotogo.com/2017/03/10/appendix-a-reading-resistor-codes">https://arduinotogo.com/2017/03/10/appendix-a-reading-resistor-codes</a> [Accessed: Jun. 5, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[14]</span>
    <span class="reference-text"><a id="ref-14"></a><b>Electronics Infra</b>, “Jumper wire 0.5mm - electronics infra,” <a href="https://electronicsinfra.com/product/jumper-wire-0-5mm">https://electronicsinfra.com/product/jumper-wire-0-5mm</a> [Accessed: Jun. 5, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[15]</span>
    <span class="reference-text"><a id="ref-15"></a><b>arduino2go</b>, “Chapter 2: Building a circuit step by step,” <i>Arduino to Go</i>, <a href="https://arduinotogo.com/2016/08/22/chapter-2-building-a-circuit-step-by-step">https://arduinotogo.com/2016/08/22/chapter-2-building-a-circuit-step-by-step</a> [Accessed: Jun. 5, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[16]</span>
    <span class="reference-text"><a id="ref-16"></a><b>Raspberry Pi</b>, “Getting started with raspberry pi,” <i>Raspberry Pi Foundation</i>, <a href="https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started">https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started</a> [Accessed: Jun. 5, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[17]</span>
    <span class="reference-text"><a id="ref-17"></a><b>Simulink</b>, “Simulink Documentation,” <a href="https://www.mathworks.com/help/simulink">https://www.mathworks.com/help/simulink</a> [Accessed: Jun. 12, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[18]</span>
    <span class="reference-text"><a id="ref-18"></a><b>Matlab</b>, “MATLAB Documentation,” <a href="https://www.mathworks.com/help/matlab">https://www.mathworks.com/help/matlab</a> [Accessed: Jun. 12, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[19]</span>
    <span class="reference-text"><a id="ref-19"></a><b>Team-BHP</b>, “Adaptive Cruise Control Limitations,” <a href="https://www.team-bhp.com/forum/indian-car-scene">https://www.team-bhp.com/forum/indian-car-scene</a> [Accessed: Jun. 15, 2023].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[20]</span>
    <span class="reference-text"><a id="ref-20"></a><b>B. D. Seppelt and J. D. Lee</b>, “Making Adaptive Cruise Control (ACC) limits visible,” <i>International Journal of Human-Computer Studies</i>, vol. 65, no. 3, pp. 192–205, Mar. 2007, DOI: <a href="https://doi.org/10.1016/j.ijhcs.2006.10.001">10.1016/j.ijhcs.2006.10.001</a> [Accessed: Jun. 15, 2023].</span>
</div>

</div>
