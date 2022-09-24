# ESP32 Cam AR Object Identification
This project focuses on creating AR glasses with a transparent OLED display which can display information about what your looking at, like a heads up display. The glasses component is powered by an ESP32 Cam module, which takes pictures of what is in front of the user every second. These images are then sent to a remote server to be processed with OpenCV/cvlib, which uses the YOLOv3 model to identify an assortment of common household objects. The object information is then sent back to the ESP32 and displayed on an SSD1306 OLED. This concept can be adapted to creating assistance devices to help elderly citizens identify things or teach children what objects are.


## Examples of the object identification in action:
![Cat](images/cat.jpeg)
![Keyboard](images/keyboard.jpeg)
![Sink](images/sink.jpeg)
![Toilet](images/toilet.jpeg)

## esp32cvclien.ino
This program takes pictures every second and sends HTTP POST requests with images to the remote server. The server then replies with any identified objects, which are displayed on the OLED screen.

## imgproc.py
This program handles interfacing with the cvlib library and converts the recieved bytes from the client into a image to be processed by the model.

## server.py
This program implements contains the HTTP server that handles requests from the client and interfaces with the image processing module to find objects in images.

## BOM
- ESP32 Cam
- SSD1306 Transparent I2C OLED Display
- Power source for ESP32 and OLED (USB power bank or LiPo cell, with 3.3v voltage regulator, 2.1 amps is recomended to prevent brownouts)
- Computer capable of image processing to be used as server

## Setup 
1. Install the python libraries from requirements.txt in cvserver and run the following command (in the same directory as server.py) to download yolov3: `wget https://pjreddie.com/media/files/yolov3.weights`
2. Enter your computer's IP address in server.py
3. Enter your network details and the computer's IP in esp32cvclien.ino
4. Flash the ESP32 Cam with esp32cvclien.ino (use an FTDI adapter)
5. Connect SDA to pin 14 and SCL to pin 13 for the OLED display, then connect VCC (this may be 3.3v or 5v depending on the specifc display) and GND 
6. Connect the power supply to the ESP32 Cam / OLED
7. Run server.py, then power on the ESP32 Cam, which should connect (check the serial monitor for info on the connection status)
8. Point the camera at objects and their names should show up on the display!
