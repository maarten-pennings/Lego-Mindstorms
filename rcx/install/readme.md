# Install 

This page describes installing an _IDE_, an integrated development environment for _RIS_, 
the LEGO Mindstorms Robotics Invention System, version 1.0 or 1.5. 
The goal is to install the IDE on a modern PC. 
Recall that RIS came out 25 years ago, in 1998, and I write this in 2023.

The first option is to use an Open Source IDE. That is relatively easy, because that still 
runs on modern PCs/OSes.

The second option is to use the original LEGO **IDE1.0**. 
That is harder; I used a virtual **Win98** machine for that. 
It is not really working for me: the serial connection is unreliable.

So, as third option I used a virtual **WinXP** machine with **RIS2.0**.
That works reliable. It even works with the serial IR tower.

A fourth option is to try bare metal GCC.

All these options have a common problem: gettig your application into the RCX 
(the programmable RIS brick). RIS comes with a so-called IR (infra red) tower,
which is the link from the PC to the RCX. 
The towers (from RIS1.0 or RIS1.5) need a DB9 serial connector on the PC,
which is absent on modern PCs. We will use a USB to DB9 converter cable.
I have not tried the RIS2.0 - that came with an USB IR tower.

Furthermopre, all options also require old software, which was typically distributed on CD-ROMs.
We have a look at how to rip these CD-ROMs.

 - [Introduction](#introduction)
 - [Historic wear](#historic-wear)
 - [Old software](#old-software)
 - [Old hardware](#old-hardware)
 - [Option 1: Open Source IDE](#option-1-open-source-ide)
 - [Option 2: LEGO IDE](#option-2-lego-ide)
 - [Option 3: Win XP](#option-3-win-xp)
 - [Option 4: GCC](#option-4-gcc)

Here is an [alternative](https://www.bartneck.de/2017/06/08/using-your-lego-mindstorms-rcx-on-a-modern-computer/) article.




## Introduction

The RCX (the smart brick in RIS) contains two memories: ROM and RAM.
The ROM contains a **bootloader**, which starts running when the RCX is powered.
The bootloader checks if there is a valid RAM image - with **(flex) firmware** -
and if so runs that. The flex firmware controls the display and buttons. 
If the user presses the _Run_ button, the flex firmware will run the 
**user application** (there are five slots, and the _Prgm_ button selects 
the slot/application to run). A second press on _Run_ stops the user application.

![System overview](images/system.svg)

Since the flex firmware (and the user application) are in RAM, removing the 
batteries causes the RAM to lose them (there is a large capacitor inside 
the RCX, so actually you have 60 seconds to replace the batteries without 
losing RAM content). An RCX with empty RAM is known by LEGO as an RCX in _boot mode_. 

![display boot mode](images/display-boot.png)

We can tell from the display if the RCX is in boot mode: it only shows 
the (running) man and the current slot (1 by default) to the right of the man. 
Once the flex firmware is loaded and the RCX is no longer in boot mode but
in _full function mode_, the display shows powered-on time (hours.minutes, 
begins with 00.00) left of the man.

![display full function](images/display.png)

When the RCX is in boot mode (no flex firmware, no user application), the 
bootloader runs a small **fixed firmware**. This firmware also allows the user to 
select a slot with the _Prgm_ key and run and stop that with the _Run_ key. 
This runs one of the 5 **fixed applications**.

  1. RCX beeps, next motors A and C are powered.
  
  2. Motors A and C are powered. While touch sensor 1 is pressed, A stops, while touch sensor 3 is pressed C stops.
  
  3. If light sensor on port 2 sees light, motors A and C are on, if it sees dark, they are off.
  
  4. Motors A and C are on for 3 seconds (robot moves), motor A is reversed for 3 seconds and then reversed again (robot turns ~ 360 degrees), finally both motors are reversed
  for 3 seconds (robot moves back). This is repeated 5 times.

  5. Motors A and C are powered, when touch sensor on port 1 is pressed: reverse for 1 second, turn, and forwards again.
     This is a drive until collision with backing up.

Also, in boot mode
 - The _View_ button is not working.
   I think the view application happens to be the sixth application, with a dedicated button (_View_) 
   to start and stop it. This application comes with the flex firmware. 
   I assume the view apllication is part of the flex firmware 
   and the not fixed firmware, because LEGO can now add other sensors/actuators
   to the eco system, and update the view application to support viewing them.
   
   The _View_ button needs the flex firmware, but also the sensor ports need to be 
   configured in a mode matching the attached senor (a user program could/should do that).
   
 - You can **not** upload user applications in boot mode.
 
 - But you can upload the flex firmware (takes several minutes) in boot mode.

See the [User guide RIS1.5](https://www.lego.com/cdn/product-assets/product.bi.core.pdf/4129418.pdf)
or the [Constructopedia RIS2.0](https://www.lego.com/cdn/product-assets/product.bi.core.pdf/4157492.pdf)
for official LEGO documentation on the RIS, the RCX and the firmware behavior.



## Historic wear

The cables did not survive the 25 years; the insulation crumbles.
This [video](https://www.youtube.com/watch?v=kXApTUbNzD0) has repair instructions.

![Crumbling cables](images/crumbling-cables.jpg)



## Old software

Depending on the option you chose, you need software from some old CD-ROM.
If not the Win98 installation files, then probably the LEGO IDE setup disk, 
and very likely the RCX (flex) firmware.

### CD-ROM
If you have a physical CD-ROM you need a CD or DVD drive.
But laptops and even desktop PCs no longer have that.

I have an [USB-to-IDE-adapter](https://www.aliexpress.com/item/1005005154651165.html).
It is normally used to connect a bare (IDE) harddisk to a PC via USB.
But I once rescued a DVD drive from an old desktop, and that also has an IDE connector.
So I used the USB-to-IDE-adapter to connect a bare DVD reader to my laptop.

![USB to IDE](images/USB-to-IDE.jpg)

This setup enabled me to read my old CD-ROMs.
For example I could copy the RCX firmware files from the LEGO RIS CD-ROM.

If you need more files, say _all_ because it is a setup CD-ROM,
I advise to convert ("rip") the entire disk to an ISO file. 

### ISO files

There are tools to read a CD-ROM and save its "image" as a single file.
This process is known as _ripping_, and the resulting file is called an _ISO_ file.
ISO files can be mounted in a Virtual machine, but also in Windows Explorer.

For ripping, I suggest [infrarecorder](http://infrarecorder.org/).
I installed it as a "portable application" (these leave no traces on your harddisc). 
Simply press Read Disc to start ripping to an ISO file.
   
![InfraRecorder](images/InfraRecorder.png)

### Download

Alternatively, you might download an ISO file from the net.
You never know if you get the real thing, and I wonder about the legal aspects.
But it is fast and easy. 

- For example, this [article](https://socket3.wordpress.com/2018/10/28/install-configure-windows-98-using-oracle-virtualbox/)
  has an Windows 98 Boot Disk ISO for download .

- I have an RIS 1.0 (9719) and RIS 1.5 (9747).
  They come with CD-ROMs, which contain firmware files; the (flex) firmware for the RCX.
  I have archieved these in this [repo](firmware). 
  Copies can also be found on, e.g., the 
  [pbricks](https://pbrick.info/rcx-firmware/index.html) site.

- I have not archieved the entire RIS CD-ROM.   
  Again you might download a LEGO ISO file from the net,
  ignoring safety and legal aspects, for example from [brickfactory](https://www.brickfactory.info/iso/)
  or [mediafire](https://www.mediafire.com/folder/ohsruj4zmjy9g).

### Mount ISO

If you do not have a CD-ROM, but you do have an ISO of it, you can mount it
with the Windows file explorer.

![Mount ISO](images/mount-iso.png)

Once the CD-ROM is mounted, you can browse it as any directory.
The screenshot below shows that I have an extra E: drive 
(the mounted LEGO RIS 1.0 CD-ROM), and that I find the firmware file
in `E:\FIRM\FIRM309.LGO`.

![Mount ISO](images/mount-iso-fw.png)



## Old hardware

There is one problem you likely have to tackle: connecting the LEGO infra red tower 
to your laptop. My IR towers are from mindstorms robotics invention 1.0 and 1.5. 
Both have a DB9 serial connector (male).

![DB9 connector](images/DB9.jpg)

I have no experience with the IR tower in mindstrorms robot invention 2.0.
It has a USB connector. I suspect it comes with a driver, and that driver is likely
for Windows 98, so useless for modern Windows or Linux.

The mindstrorms robotics invention sets come with a female-to-female serial cable.
I therefore decided to buy a USB-to-serial cable with a DB9 _male_ connector.
This means that my "laptop with the USB-to-serial cable" now has a DB9 male plug,
just like the old PCs, and I can use the LEGO serial cable to connect the IR tower.

![USB to DB9](images/USB-to-DB9.jpg)

Alternatively, you could buy a USB-to-serial _female_ cable, and skip the 
LEGO cable. Not only do I believe my solution is more generic, I also had a
mechanical consideration: I suspect female cables won't fit in the IR tower 
due to the side screws that are usually present.

![DB9 female](images/DB9-female.jpg)

I bought my cable from **ugreen**. The US website no longer lists it, but the 
[Indonesian](https://ugreen.co.id/product/ugreen-usb-to-db9-rs-232-adapter-cable/) or
[Pakistan](https://ugreen.com.pk/product/ugreen-20222-usb-to-db9-rs-232-adapter-cable-2m/)
websites are.
It is available via e.g. amazon. It has a Prolific chip (PL2303) which is plug-and-play
with Windons 10 (so no driver problems). I do have FTDI cables, but not with DB9
connector, and I was also worried about voltage levels. Maybe the ugreen has a 
MAX232 level shifter, anyhow this cable works for me.

![Device manager](images/device-manager.png)


## Option 1: Open Source IDE

The easiets way to program the RCX is using open source software.
That still runs on modern PCs/OSes.

My suggested approach is Bricx Command Center [BricxCC](https://bricxcc.sourceforge.net/).
The download [link](https://sourceforge.net/projects/bricxcc/files/bricxcc/)
gives access to latest version (`bricxcc_setup_3389.exe`), which is from 2011-03-15
so I do not expect updates (time of writing January 2023).

I installed BricxCC in `C:\programs\BricxCC` (still afraid of spaces in file paths);
and used "Typical" installation.

I plugged in the USB-to-DB9 cable, connected it with the LEGO serial cable
to the IR tower (which, of course, has a 9V battery), placed the IR tower in front of the RCX
(which, of course, has 6 times an AA battery), switched on the RCX (red _On-Off_ button),
and started BricxCC. The first pop-up is to find the RCX.

![Find the RCX](images/find-brick.png)

Make sure to select the correct COM port (see Device manager), and press OK.
If you get `No connection to programmable brick`, the USB-to-DB9 cable is not plugged-in 
(or has no driver), or it is not connected to the IR tower. If you get `Cannot find brick`, 
the RCX is not switched on, or not close enough (10cm). If all is fine, the green light in 
the IR tower lights up, confirming that BricxCC was successful in connecting to the tower.

The RCX is now likely in _boot mode_ (see Introduction, the RCX display 
does not show time left of the little man): we just placed batteries, so it contains no
firmware. **Warning:** as a result, most functions (tools) of BrickCC do _not_ work.
Running them typically causes a time-out (about 10sec) - and nothing happens.
It seems that only Tools > Diagnostics > Infrared Power seems to work somehow;
after waiting 10 seconds we can switch it to `Short` (and see the green LED on the tower
switched on for a short period).

![Diagnostics](images/diagnostics-ir-short.png)

Next step is to download the firmware. Select Tools > Download firmware, and browse 
to [`firm0332.lgo`](firm0332-RCX-education/firm0332.lgo). You will see the counter on 
the RCX display to run to 2494 (varies from firmware version to firmware version:
`firm0309.lgo` takes only 1638 steps - [video](https://www.youtube.com/shorts/t8wd-05d9GY)). 
This takes minutes. Note that flashing happens in blocks of 20 steps; I believe if 
such a block fails, it is retried, and finally aborted. This may happen if the distance
between tower and RCX does not match the distance settings (the switch at the bottom 
of the Tower, and configured in RCX, see above) or when there is too much ambient 
IR light (switch off lights in your room, close the curtains, put RCX and tower in a box).

![Download firmware](images/download-firmware.png)

To test if the firmware is downloaded successfully, connect a motor to port A, and 
start Tools > Direct control. Press Motors > A > forward. This should start the motor.

![Direct motor control](images/test-motor-a.png)

As a final test, we will write a Not Quite C program (NQC).
The default langauge of BricxCC is NXC, but I believe it is for the Lego second 
generation Mindstorms: NXT. So we set NQC as default.
Goto Edit > Preferences then in the Compiler tab and subtab Common check NQC:

![Set NQC as default](images/prefer-nqc.png)

First we "build the robot": motor on port C, and touch sensor on port 3.
Secondly, we write a program that will run the motor clock wise or anti clockwise
depending on whether the touch sensor is pressed.

Select File > New, paste this [code](test.nqc) and
save this somewhere with extension `nqc`. The extension supplied with _save_ is
important for the compiler. Only then Compile > Compile.

```C
task main()
{
  SetSensorType(SENSOR_3, SENSOR_TYPE_TOUCH);
  SetSensorMode(SENSOR_3, SENSOR_MODE_BOOL);
  SetPower(OUT_C,1);
  while( 1 )
  {
    if( SensorValue(2) )
      OnFwd(OUT_C);
    else
      OnRev(OUT_C);
  }

}
```

Next select Compile > Download (or press F6 or press the button with the "radio" icon). 
This will upload the compiled program to the slot shown on the ribbon.

![Download application](images/download-application.png)

Finally, on the RCX, select slot 1 with the _Prgm_ button and then 
start the uploaded program by pressing the _Run_ button.
The motor attached to port C should start running. A press on the touch
sensor on port 3 should make it run the other way.
Press _Run_ again to stop the program.


## Option 2: LEGO IDE

In this chapter we discuss running the LEGO RIS IDE in a Win98 virtual machine (on a Win10 host).

> **WARNING**
>
> The combination described in this chapter (VirtualBox, Windows98, RIS1.0 and a USB-to-serial cable) 
> results in a very unreliable serial connection to the IR tower. I can upload tiny programs
> but nothing a bit longer.

### Requirements

We need the following parts

 - A virtual machine, we will use VirtualBox, as a so-called hypervisor,
   it is available for [download](https://www.virtualbox.org/).
   
 - A Windows setup disc - with license key. 
   I used Win98SE with my license key, but probably Win95, Win98 and Windows ME also work.
   You might download a Windows ISO file from the net, ignoring safety and legal aspects, 
   for example this [article](https://socket3.wordpress.com/2018/10/28/install-configure-windows-98-using-oracle-virtualbox/)
   has an Windows 98 Boot Disk ISO for download .
   
 - A CD from the LEGO mindstorms robotics invention.
   You might download a LEGO ISO file from the net, ignoring safety and legal aspects, 
   for example from [brickfactory](https://www.brickfactory.info/iso/)
   or [mediafire](https://www.mediafire.com/folder/ohsruj4zmjy9g).

### Step 1 - Hypervisor

Download and install as hypervisor [VirtualBox](https://www.virtualbox.org/).
I have `VirtualBox-7.0.4-154605-Win.exe`.

### Step 2 - Create a virtual machine

We create a virtual Windows98SE for our LEGO IDE.
For a background see [this article](https://socket3.wordpress.com/2018/10/28/install-configure-windows-98-using-oracle-virtualbox/).
   
- Select New

  ![New VM](images/vm-1new.png) 
  
- Fill out the form for _Virtual machine Name_. 

  Use something with "Win98" in the _Name_, and VirtualBox will optimize the virtual machine for Windows 98 
  (see the last line with _Version_).
  Pick a _Folder_ that will store all VM related files (e.g. the virtual harddisk).
  Press _Next_.
  
  ![VM name](images/vm-2win98.png)
  
- The next screen is for _Hardware_. 
  64M and 1 CPU is typical for a PC with Win98.
  
  ![VM hardware](images/vm-3hardware.png)
  
- The next screen selects the _Virtual Hard disk_.
  Win98 needs between 100M and 300M bytes on the hard disk. 
  I picked 512MB (pre-allocated), don't overdo; Win98 has FAT, so 2G might cause problems.
  
  ![VM hardware](images/vm-4virtualhd.png)

### Step 3 - Install Win98SE

We now have a virtual PC, and we will install Windows 98.

- We mount the Window 98 disc in the secondary IDE drive of the virtual machine.
  
  ![Mount Win98 ISO](images/win-1mountdisc.png)  

  (I had several tries so you might see LegoWin98, V3Win98, Win98RIS, Win98RIS1.0 as VM names)     
  
- Start ("plug in the power") of the virtual machine.

  ![Start the VM](images/win-2start.png)
 
- Machines of that generation could boot from CD (older PCs only from floppy or harddisk). 
  The BIOS of the VM will ask
  if you want to boot from harddisc or CD-ROM, select the latter with the keyboard.
  
  **Warning** if you click the VM window (so that it gets focus for the keyboard input),
  the Win98 virtual machine "locks" your mouse pointer to that window.
  To release the mouse pointer for the host machine (the hypervisor) you must
  press the "secret key" **host key**. 
  It is listed in the lower right corner, by default it is the _right control key_.

  ![Boot from CD](images/win-3bootcd.png)

- The software from the CD is loaded, and it pops-up its main menu.
  Select "Start Windows 98 Setup from CD-ROM".
  
  ![Select Windows 98 Setup](images/win-4setup.png)

- Windows 98 Setup is now running from CD-ROM (white letters on blue for windows, no longer white on black for BIOS). 
  You need to confirm that you want to setup since it will wipe the harddisk (the virtual, still empty one in our case).
  So we confirm with ENTER.
  
  ![Confirm harddisk wipe](images/win-5wipehd.png)     

- Windows 98 Setup asks permission to partition ("Configure unallocated disk space")
  the (virtual Win98) harddisk.

  ![Boot from CD](images/win-6format.png)   

- Windows 98 Setup has now probably written the partition table to the master boot record (MBR) of the virtual harddisk.
  That requires a reboot so that the BIOS can register this. We get below information screen for that,
  but it is confusing: it assumes that we have a boot-floppy in A: and a setup cd in D:.
  However, we are more modern, we have a CD from which we boot, and we do not need the A floppy (fortunately).
  Anyhow, this is a clue that, after the reboot, we need to continue from the setup.

  ![Reboot after MBR](images/win-7reboot.png)   

- We need to continue Windows 98 Setup, so we boot (again) from the CD.

  ![Reboot after MBR](images/win-8bootcd2.png)

- This time, Setup will probably see that the MBR has some markings, and behave differently.
  
  After confirming Windows 98 Setup (again), it will format the harddisk. 
  This is done in a blink of the eye on our virtual machine.

  ![Format done](images/win-9install.png)
  
- Finally we get to the real Setup process.
  There are several screens, this is the first.
  
  ![Win98 1 screen](images/win-10setup1.png)

  After that several steps: (1) Continue, (2) Install on `C:\WINDOWS`, (3) use `Typical`, 
  (4) "Install the most common components", (5) enter some fancy `Computer Description` like `Win98RIS`,
  (6) "Establish your location" (I used United States), and (7) Start Copying Files.
  At the end of copying Setup will reboot. 
  
- This time, boot from **harddisk**, Win98 is installed now.

  (1) Enter some fancy Name and Company, (2) Accept the License Agreement, (3) Enter the License Key,
  and (4) Start Wizard, which will install drivers, and Windows will restart.
  
  ![Wizard](images/win-11wizard.png)
  
- Also now, boot from harddisk, Win98 is installed now.
  Some final driver installs, and then "Windows is now setting up"...
  
  It is probably wise to pick the correct Time Zone.
  
  ![Final items](images/win-12items.png)
  
  And again a restart.
  
- Also now, boot from harddisk (which contains Win98).
  I entered an empty password.
  
  ![Empty password](images/win-13nopw.png)
  
- And finally we have windows. We even have sound!

  ![Windows running](images/win-14installed.png)
  
  (I would suggest to uncheck this Welcome screen at the bottom left).
  
- This might be a good moment to eject the virtual (Windows 98 Setup) CD.

  ![Remove virtual CD](images/win-15unmount.png)
  
- It is possible to create a shortcut to a virtual machine.
  In the VurtualBox hypervisor, right-click on the VM and select
  "Create Shortcut on Desktop".

  ![Create shortcut to VM](images/win-15shortcut.png)
  
  If you want, you can add a [![RIS icon](images/RIS.ICO)](images/RIS.ICO):
  right-click the shortcut > Properties > tab Shortcut > button Change Icon.
 
### Step 4 - COM port

If we open the Device manager on the Win98 machine, we see that we do not have a COM port.
That makes sense, we have to configure the virtual machine to have a COM port.
To do that, we must first shutdown the virtual machine: press Start > Shutdown > OK.

- Make sure the COM port is available on the host machine.
  In my case, I plug in the Prolific USB-to-serial cable.
  And check its COM port assignment.

  ![Device manager on the host](images/serial-2hostdevice.png)
  
  On my machine COM7 is the port we need.

- In VirtualBox manager, select the virtual machine and click Settings and Serial Ports.

  ![VM manager for serial port](images/serial-1manager.png)

- We need to mount a COM port from the host into the virtual machine.
  The screen confused me quite a lot in the beginning.
  Each of the tabs allows you to mount a port, so at maximum we can mount 4 ports.
  On the tab itself, we select which port of the host to map and how it appears in the virtual machine.
  
  ![VM manager mapping serial port](images/serial-3mount.png)

  Note that we (1) enabled the first port mounting, (2) publish it as COM1 in the Win98 virtual machine,
  (3) configure the "source" as a host device, namely (4) COM7.
  
  The screenshot shows the tool tip help from Virtual box.
  
  Some source claim that instead of `COM7` we should use `COM7:`. I did not notice any difference.
  If the host port has a number above 9, use the long notation, e.g., `\\.\COM10`.
  

- Now we can start the Win98 VM again.
  We need to install a driver for the COM1 port.
  Note that a COM port is _not_ plug and play.
  So the "unknown" devices we find in the Device Manager (with a "?") are not our new COM port.
  
  Via Start > Settings > Control Panel > start Add New Hardware.
  
  ![Control Panel](images/serial-5controlpanel.png)

  
- On the first page of the Add New Hardware Wizard click Next. Click Next again to start searching.

  ![Not detected](images/serial-6notinlist.png)

  Only the plug&Play devices are found, so we select "No, the device isn't in the list".
  
- We let Windows search for the hardware.
  
  ![Not detected](images/serial-7Serach.png)

- Windows found the Serial Port (click Details if you want to check).

  ![Not detected](images/serial-8found.png)
  
- The wizard needs the driver, browse to `C:\WINDOWS\SYSTEM`, 
  where a driver happens to be copied from the CD-ROM.

  ![Not detected](images/serial-9path.png)

- Done. As a check, we open Device manager, for example by right-clicking on My Computer > Properties.
  It confirms we have COM1 driver installed.

  ![Not detected](images/serial-10installed.png)
  

### Step 5 - 256 colors

If we right-click the Win98 desktop and select Display Properties, tab Settings,
we cannot select the 256 colors mode. That is unfortunate, because the LEGO IDE needs that. 
We need a better driver for the virtual video card. Fortunately, there is one.

- Open Device manager, for example by right-clicking on My Computer > Properties

  ![Device manager](images/video-1devmngr.png)

- We want to update the video card driver. 
  So in section Display Adapters, select the Standard PCI Graphics Adapter (VGA),
  click Properties > Driver > Update driver, and we get the first page of the driver wizard.

  ![Update driver](images/video-2update.png)

  We click Next to get to the second page of the Wizard.
  
- The driver is not on our disc (CD nor harddisk) so we hand pick it.

  ![Hand pick video driver](images/video-3handpick.png)
  
- The list of matching hardware is empty, but we need to select "Show all hardware", so that we can select XGA.

  ![Hand pick video driver](images/video-4allhw.png)
  
  We will now install a custom driver, therefore we say "Have Disk..."
  
- We found a better video driver in this 
  [article](https://socket3.wordpress.com/2018/10/28/install-configure-windows-98-using-oracle-virtualbox/).
  The driver is an "VBEMP Universal VESA Video Driver", I have copied it into this 
  [repo](../driver/VBEMPWindows9xDrivers.iso).

  We mount this ISO on the Virtual Machine.
  
  ![Mount driver CD](images/video-5CD.png)

- Back in the Win98 VM, we browse to directory 032mb on this CD.

  ![Browse to driver](images/video-6path.png)
  
- Based on this `INF` file, the Select Device lists compatible hardware.
  First, again, check "Show all devices".

  ![Select device](images/video-7xga.png)

  Then select the XGA driver. Click OK.
  
- Ignore the warning.

  ![Ignore warning](images/video-8warn.png)
  
  Press Yes, Next, and Finish. WIndows restarts.
  
- On my machine, the reboot **fails**. 
  So I switched power off of the virtual machine, and then restarted it.

  **Recall** The Win98 virtual machine "locks" your mouse pointer to its window (which is now crashed).
  You need to release the mouse pointer by pressing the **host key**, by default it is the _right control key_.
  Then we can click the window close cross and get:

  ![Switch off](images/video-9off.png)
  
- Windows reboots (with a disk repair).
  We right click the background and select Properties, and open tab Settings.
  
  ![Higher viode settings](images/video-10hicol.png)

  Select 256 colors. I also selected a higher resolution 
  (but it must fit on my FHD screen of the host machine).

- Just to be sure I rebooted.
  A nice big screen, and persistent video settings.

  ![Higher video settings](images/video-11hivideo.png)

- Tip: the 256 color mode is requested by LEGO IDE.
  The resolution it needs is 640x480. If you pick a larger resolution,
  the LEGO IDE will just put a large border around its 640x480 area.
  What I prefer is to set the VM to 640x480, and use Win98 VM > View > Scaled mode
  then drag the VM window to nearly full screen in my host machine.

### Step 6 - Install LEGO IDE

Steps

- Start the Vitual Win98 machine. 
  Make sure the USB to Serial cable is plugged in, or you get an error.

- In the VM, make sure the video card uses the 256 colors mode.

- Mount the LEGO CD-ROM. Right click the disc in the virtual machine status bar,
  then either point to the physical CD-ROm driver or the ripped ISO.

  ![Mount CD-ROM](images/ris-1iso.png)
  
- This disc is typicaly "auto execute", if not open explorer, browse to
  the CD-ROM and start `AUTORUN.EXE`.
  
- The setup program runs, chose INSTALL.

- Follow the setup wizard (1) accept license, (2) accept install directory, (3) install
  maximum (our disk is large enough) components, (3) accept start location.

### Step 7 - Run LEGO IDE

- Start the Vitual Win98 machine.
  Make sure the USB to Serial cable is plugged in, or you get an error.

- Start the "Robotics Invention System".
  Make sure the LEGO CD-ROM (physical or ISO) is mounted,
  the application needs it (for videos, I guess).
  
- When you run the IDE, you have to "logon", i.e. select (enter) a user name.

- Every time a new user is enrolled, s/he must run the _Guide Mode_.
  This takes a long time because you need to execute 6 training missions.
  Here is a video of the [RIS2.0 training mission](https://www.youtube.com/watch?v=8yqhvVdOnM8).

  To bypass the the Guided Mode (enable all menus right away) hold down 
  the Control key and click the About button in the Main Menu.

- In the Main Menu > Getting Started > Setup Options, there are some
  interesting settings: which COM port to use, force firmware download, 
  which slots are locked, and some others.

  ![RIS settings](images/ris-settings.png)

- I wrote below simple program.

  ![RIS example code](images/ris-code2.png)
  
  But it is already too long to reliable send via the IR tower  to the RCX.


## Option 3: Win XP

Option 2, using virtual Win98 with RIS1.0, does not really work for me; I have problems
sending long files via the IR tower. RIS2.0 came out later, not 1998 but 2001, so I wanted to
try using virtual WinXP with RIS2.0. That has proven to be easier and more stable.

### Requirements

We need the following parts

 - Again we will use [VirtualBox](https://www.virtualbox.org/).
   
 - A Windows XP setup disc - with license key. 
   
 - RIS2.0 CD-ROM, I used `3804_Mindstorms_2.0_english` from 
   [brickfactory](https://www.brickfactory.info/iso/)
   (but [mediafire](https://www.mediafire.com/folder/ohsruj4zmjy9g) might alos work).

### Create a virtual machine

These steps are similare to the Win98 setup above, so check there if you are in doubt.

- We create a virtual machine in VirtualBox, making sure the `Version` is set to `Windows XP`.

  ![Create VM for WinXP](images/vmxp-1create1.png)

- Windows XP is later than Windows 98, so we picker a bigger machine: more RAM (256MB)

  ![256MB RAM in VM](images/vmxp-2create-ram.png)
  
  and bigger disk (4GB).

  ![2G HD in VM](images/vmxp-3create-hd.png]
  
- This time, I decided to map COM7 from the hypervisor (the serial port of the IR tower) 
  to COM1 in the virtual Windows XP right from the start (so that Windows Setup adds the correct driver).
  
  ![COM1 in VM](images/vmxp-4set-serial.png)

  What I forgot, but might be wise is to remove the virtual network card.
  I do not want my WinXP machine to be connected to the internet, but VirtualBox will do that.
  
- The final step is mouting the ISO (of the WinXP CD-ROM).

  ![WINXP ISO in VM](images/vmxp-5set-cd.png)

- Then we "turn on" (start) the virtual machine.
  It took me only 15 minutes to install WinXP:

  - Acknowledge setup (it wipes the harddisk, but our virtual haddisk is still empty)
  - Accept license (the legal stuff)
  - Partion and format the virtual harddisk
  - Setup starts installing Windows
    - Select regional options
    - Enter Name & Organization
    - Enter the **Product key**
    - Chose Computer name & admin credentials
    - Set the timezone
    - Typical settings
    - Network workgroup
  - The VM reboots and Windows starts running
    - Screen (resolution) settings
    - Welcome screen & music
    - Skip network
    - Not register
    - User's name
- I did some personal cleanup afterwards
  - I disabled the local Area Connection
  - Via "Add and remove software" I removed MSN
  - For Windows Messenger in Options I selected do not run

- I removed the WinXP ISO setup disc from the virtual machine.

This goes fast and easy. No unclear reboots, knew how to do the COM port, no screen resolution issue.
Also the funny mouse pointer capture, which happens in Win98,
seems to be absent in the virtual WinXP. It might be there is an extension pack for this.

Up to the next step, installing LEGO IDE. 

### Install LEGO IDE

Also this is fast and easy.
For me this IDE works fine, but on Philo's home we find a [patch](https://www.philohome.com/sdk25/sdk25.htm), maybe you need it.

- Insert the RIS2.0 ISO in the virtual CD-ROM player.
  If you do that while the virtual Windows XP machine is running, it performs an auto-play of the CD-ROM.

  ![Insert RIS CD-ROM](images/ris2.0-1install.png)

- Select `Install` and follow all steps. Click next several times.

- I selected Keep existing DirectX and Defaults for QuickTime.
  Setup will reboot your machine.

- Remove the ISO (CD-ROM) of the virtual WinXP.
  Unlike the RIS1.0 disc, it seems the RIS2.0 disc was completely copied to the (virtual) harddisk.
  

### Run LEGO IDE

- Start the Vitual WinXP machine (make sure the USB to Serial cable is plugged in).

- Start the "Robotics Invention System" and press "Run".

  ![IDE runs](images/ris2.0-2run.png)

- Follow the instructions to flash firmware.
  Remember to select serial (unless you have the USB IR tower).

  ![Select IR tower USB/serial](images/ris2.0-3tower.png)

- Then flashing of the RCX starts. Unlike Win98/RIS1.0, that now works.

  ![Flashing](images/ris2.0-4fw.png)

- Login with our name, the welcome video plays, and we get the login screen.
  After we select our name, we end-up on the home screen.

  ![Home screen](images/ris2.0-5home.png)

- I did some personal cleanup afterwards
  - I changed the shortcut from `C:\program Files\LEGO MINDSTORMS\RIS 2.0\LaunchRis2.exe` to
    `C:\program Files\LEGO MINDSTORMS\RIS 2.0\RIS2.exe`.
    You can skip the falling LEGO block animation (video) by pressing any key.
  - I configured the WinXP machine to start RIS automatically when the machine starts
    (drag the RIS shortcut to Start > All Programs > Startup).
  - In the VirtualBox Manager I created a shortcut of the WinXP machine on the desktop of my hypervisor.
  - I also changed the icon of that shortcut to [![RIS icon](images/RIS.ICO)](images/RIS.ICO).
  

- I wrote below simple program, more or less the same as for RIS1.0.
  Now it works fine.

  ![Example application](images/ris2.0-code.png)


## Option 4: GCC

Program RIS in GCC with [brickos](https://brickos.sourceforge.net/).


(end)
