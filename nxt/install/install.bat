@echo off
REM From https://www.reddit.com/r/mindstorms/comments/fn2vdh/fix_nxtg_software_on_x64_windows_10/
REM 1) Download the last version (v2.0f6) of the software from the lego mindstorms website.
REM 2) Unzip the archive
REM 3) Copy this batch file inside the base folder, where "setup.exe" is located
REM 4) Run this batch

if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit)
echo Pieced together using the info on this blog:
echo.
echo https://social.technet.microsoft.com/Forums/en-US/d1df912f-e47f-4295-be77-f2d0897a69f5/nxt-lego-mindstorm-20-deployment-doesnt-work?forum=configmanagerapps
echo.
cd /D "%~dp0"
echo Installing NXT-G software...
msiexec /i "products\lego_retail_neutral\nxt_lego_ms\mindstorms.msi" ADDLOCAL="LEGO.LEGO.20000" ALLUSERS="1" /qn
echo Installing NXT-G English language pack...
msiexec /i "products\lego_retail_english\lego_eng\mindstormseng.msi" ADDLOCAL="EngLEGO.LEGO.20001.ENG" ALLUSERS="1" /qn
echo Installing NXT Fantom Driver (x64)...
msiexec /i "products\lego_nxt_driver_64\nxt_d02\legomindstormsnxtdriver64.msi" ALLUSERS="1" /qn
echo Everything installed!
pause
