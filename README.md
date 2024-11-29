# xmas-tree

  1. [About](#about)
  2. [Purpose](#purpose)

# About
This is a modified version of `randomsparkles.py` (renamed to `random_sparkles.py`) from the example folder in [ThePiHut/rgbxmastree](https://github.com/ThePiHut/rgbxmastree/tree/master). It adds the following functionalities:

  1. Adds the shebang `#!/usr/bin/python3` so the script can be run directly
  2. Initialises the pixels to green
  3. Adds a sleep(0.1) timer on each loop so as to not thrash the cpu
  4. On keyboard interrupts/SIGINT, turns the tree off and 'closes' the tree

In addition, there is a bash script `xmas-tree-kill.sh`, which will send a SIGINT to the tree to enforce a graceful shutdown.

There is also `tree-off.py`, a simple script to turn off a tree that for some reason is still switched on without any scripts running to control it.

# Purpose
I like automating stuff. I have a cron job that runs the python script on Dec 1st:
```
0 0 1 12 * /path/to/xmas-tree/random_sparkles.py #enable xmas tree lights
```

I have another that turns the tree off on Jan 6th:
```
0 0 6 1 * /usr/bin/killall -s SIGINT random_sparkles.py
```

There is another shell script `check-tree-on.sh` which is also meant to be used in a reboot macro in cron:
```
@reboot /path/to/check-tree-on.sh
```
This script checks if the date is Dec 1st or later, or Jan 5th or earlier. If so, it starts the `randomsparkles.py` script. This ensures the script is running after a reboot between these dates.

The script `xmas-tree-kill.sh` is provided mainly for completeness, even though I don't use it myself.

I haven't forked [ThePiHut/rgbxmastree](https://github.com/ThePiHut/rgbxmastree/tree/master) because I only edited the one file.
