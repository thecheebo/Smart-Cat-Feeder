#  Smart Cat Feeder

This is a walkthrough of a raspberry-pi powered, motion sensing, AI-trained, cat-detecting, publisher/subscriber broker (MQTT), app-enabled cat feeder I built for my cat Basil (pictured below). 

<p align="center">
  <img src="https://i.imgur.com/fXNZdzI.jpg" alt="Basil" width=42% height=42%></img>
  <h4 align="center">Basil</h4>
</p>

A 1.5 minute demonstration of Basil and I using it. <a href="https://youtu.be/Y3K3dwvThA8">Here is a link of me using it. </a>This solo project was completed for CS 498 Internet of Things during my Fall 2020 semester at University of Illinois Urbana-Champaign.



## Table of Contents  
[Materials](#materials)  
[Installation](#installation)  
[Motion Sensing](#motion) <br>
[Google's Object Detection API](#detection)<br>
[Servo's](#servo)<br>
[Usage](#usage)   <br>
[Credits](#credits) <br>
[License](#license) 

## Materials

* [Dremel: $60](https://www.amazon.com/Dremel-3000-1-24-Attachment-Accessories/dp/B005JRJE56/ref=sr_1_8?dchild=1&keywords=dremel&qid=1630520111&sr=8-8)
* [Raspberry Pi 4 Model B 4gb: $55](https://www.adafruit.com/product/4296)
* [Raspberry Pi Camera Module 2: $30](https://www.raspberrypi.org/products/camera-module-v2/)
* [Motion Sensor: $8](https://www.amazon.com/HiLetgo-HC-SR501-Infrared-Sensor-Arduino/dp/B07KZW86YR/ref=sr_1_5?dchild=1&keywords=raspberry+pi+motion+sensor&qid=1630521087&sr=8-5)
* [Servo MG995/MG996R: $10](https://www.amazon.com/Digital-Steering-Control-Helicopter-Airplane/dp/B08TWZNZC8/ref=sr_1_8?dchild=1&keywords=MG996R&qid=1630522971&s=industrial&sr=1-8)
* [Power Supply 3A: $7](https://www.amazon.com/Power-Supply-Adapter-Switch-Raspberry/dp/B07TSDJSQH/ref=sr_1_8?dchild=1&keywords=3a+power+supply+adapter+raspberry+pi&qid=1630198961&sr=8-8)
* [Double Cat Feeder Bowls: $9](https://www.amazon.com/UPSKY-Double-Premium-Stainless-Modeling/dp/B07LF1JLZ6/ref=sr_1_5?dchild=1&keywords=double+cat+feeder+bowl+eyes&qid=1630521009&sr=8-5)
* [Any Power Drill]
* [Pringles Can]
* [25 ounce or larger can]
* [Zip ties or super glue]
* [Eye Protection] ** DO NOT IGNORE **

<p align="center">
  <img src="https://i.imgur.com/eWU46YJ.jpg" alt="Sparks flying" width=50% height=50%>
</p>

*Warning* Sparks flying while cutting metal. Please be sure to wear eye Protection


## Installation

<ol>
<li>Get both your pringles can and soup can and remove the paper wrapping from the soup can. You can use wrapping paper on your pringles to make it look nicer at the end but thats optional.
  </li>
<p align="center">
  <img src="https://i.imgur.com/T2DxYku.jpg" alt="Cans" width=40% height=40%>
</p>

<li>Get a sharpie and mark the bottom of both cans like this:</li>
<p align="center">
  <img src="https://i.imgur.com/qM7iksl.jpg" alt="Soup Can" width=40% height=40%>
   <img src="https://i.imgur.com/PZrSutT.jpg" alt="Pringles Can" width=40% height=40%>
</p>
  
<li>Get out a .5 inch spade bit from your drill bit set, and WEAR YOUR EYE PROTECTION</li>
<p align="center">
  <img src="https://i.imgur.com/xCzJe0y.jpg" alt=".5 inch spade bit" width=40% height=40%>
</p>
   
  <li>It should look like this afterwards</li>
<p align="center">
  <img src="https://i.imgur.com/oTw5e34.jpg" alt="Can with hole in it" width=30% height=30%>
</p>
  
  <li>Time to break out the dremel. Keep your eye pro on. If you havnt used it before, watch some youtube videos please. <a href="https://photos.app.goo.gl/gx8oZPCbP9pxyYsP8">Here is a link of me using it.</a></li>
<p align="center">
  <img src="https://i.imgur.com/f16LW5v.jpg" alt="Dremel" width=30% height=30%>
</p>
    <li>Make sure to cut a hole in the back for the raspberry pi power cable, 4 holes for the servo, and an opening for the food to dispense. Insert zip ties to attach MG995 servo.</li>
<p align="center">
  <img src="https://i.imgur.com/3NrEfJe.jpg" alt="Can" width=25% height=25%>
  <img src="https://i.imgur.com/1u4yxFE.jpg" alt="Can" width=25% height=25%>
  <img src="https://i.imgur.com/E65ZPac.jpg" alt="Can" width=25% height=25%>
  <img src="https://i.imgur.com/2wjBCXr.jpg" alt="Can" width=25% height=25%>
</p>
<li>This step is optional but I wrapped my can with cute kitty wrapping paper, although dont get one that is glittery like my wife bought for me.</li>
<p align="center">
  <img src="https://i.imgur.com/VGxeo9c.jpg" alt="Can" width=33% height=33%>
  <img src="https://i.imgur.com/EETPAkK.jpg" alt="Can" width=33% height=33%>
</p>
  <li>We'll come back to installing the pi/camera/motion sensor/servo after you've tested it all out.</li>
</ol>

## Motion

The purpose of the motion sensor is to activate the object detection algorithm. It's compute heavy and activates the camera. We don't want to always be running the camera, so a more low-powered approach is using a simple motion sensor for when Basil (cat) walks in front of the cat feeder, and only then it will start the object detection api.

Attach your motion sensor like this:
<br>
![image](https://i.imgur.com/AMcoCBn.png)

Here is a good tutorial if you are having difficulty but it is pretty self exaplanatory. 
https://projects.raspberrypi.org/en/projects/parent-detector/1


<p align="center">
  <img src="https://i.imgur.com/jaRkhX7.jpg" alt="Installed in the back" width=50% height=50%>
  <h4 align="center">This is the camera and the sensor in the back.</h4>
</p>


<p align="center">
  <img src="https://i.imgur.com/PmcHlVR.jpg?1" alt="Installed in the front" width=50% height=50%>
  <h4 align="center">Here is the sensor on the top and the camera in the middle.</h4>
</p>


## Dectection

Install the rapberry camera pi. There are a few tutorials on how to do so, so there is no need to repeat their great work:
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera

After you have installed the camera and tests that it has worked. Please check out TensorFlow's object detection API that was designed and specialized for Raspberry Pi.
The AI model has been trained to detect 100 or so items. You can check out the list and instructions on the link.

https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi


## Servo

## Usage



## Credits

https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi

https://www.youtube.com/watch?v=dqr-AT5HvyM


## License

MIT License

Copyright (c) 2021 Albert Yeh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
  
