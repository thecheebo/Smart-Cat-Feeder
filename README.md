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
[Usage](#usage)   
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


  
