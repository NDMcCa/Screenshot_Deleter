# Screenshot_Deleter
A Python script that deletes all files in the 'Screenshots' folder on Windows.

As described in the source code, this script deletes all files in the 'Screenshots' folder on Windows. 
Included is both the source code and the 'compiled' .exe (compiled with pyinstaller).

Modern Windows begs users to enable OneDrive so this script is configured to work on systems with or without OneDrive enabled (handled by the 'try/except' block).
If you take a lot of screenshots on your system but want to periodically clear the folder, this is for you.

Useful for students who take screenshots of lecture slides and paste them in their notes.
When compiled as an .exe, you can schedule it to run in Windows Task Scheduler.

More/better functionality may be added in the future if I come by any inspiration to expand this idea.
