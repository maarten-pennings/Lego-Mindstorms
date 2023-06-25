# Firmware
2023 June 25

See instructions on [pybricksdev](https://github.com/pybricks/pybricksdev/blob/master/README_dfu.rst).

## Steps 
 - I created a virtual Python Environment  
   `c:\Programs\Python\python.exe -m venv env`
 - I activated it  
   `env\Scripts\activate.bat`
 - and installed the pybricks development tools  
   `pip install pybricksdev`
 - I put the brick in DFU mode
    - Hub is off and disconnected (no USB cable)
    - Press and hold the Bluetooth button on the hub.
    - Connect the USB cable.
    - Wait for the Bluetooth light to start blinking pink-green-blue-off.
    - Release the Bluetooth button.
 - I ran backup command  
   `pybricksdev dfu backup /path/to/original/firmware.bin`
 - I renamed it to the versions shown in the Mindstorms app:  
   `firmware3.2.36(1.5.6.0).bin`

(end)
