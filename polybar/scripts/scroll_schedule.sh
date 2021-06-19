#!/bin/bash

# see man zscroll for documentation of the following parameters
zscroll -l 80 \
        -p "                   " \
        --delay 0.2 \
        --update-check true "$HOME/.config/polybar/scripts/schedule.py" &

wait
