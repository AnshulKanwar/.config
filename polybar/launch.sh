#!/bin/bash

killall -q polybar

while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

#polybar first &
#polybar second &
#polybar third &
#echo $! > ~/.config/polybar/scripts/schedule.pid 
#polybar fourth &
#polybar fifth &
polybar mybar &
echo $! > ~/.config/polybar/scripts/schedule.pid 

echo "Polybar launched..."
