#!/usr/bin/bash
d=`date +%m%d`
t=false
if [ "$d" -ge "1201" ]; then
    t=true
elif [ "$d" -le "0105" ]; then
    t=true
fi
if [ "$t" = true ]; then
    /home/pi/xmas-tree/randomsparkles.py &
fi
