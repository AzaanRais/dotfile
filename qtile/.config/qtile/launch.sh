#!/usr/bin/env bash

# polybar
killall -q polybar
echo "---" | tee -a /tmp/polybar_top.log
polybar top | tee -a /tmp/polybar_top.log & disown

# nitrogen
nitrogen --restore &

# picom compositor
picom &

# dunst notif daemon
dunst &