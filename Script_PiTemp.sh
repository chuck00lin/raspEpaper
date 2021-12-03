#!/bin/bash
# Script: RpiTemp.sh
# Purpose: Display the ARM CPU and GPU temp 
# Author: Chuck00lin
# -------------------------------------------------------

# 
# vcgencmd command need to be activated
# need to chmod +x this.sh
#

cpuTemp=$(</sys/class/thermal/thermal_zone0/temp)

echo "$(date) @ $(hostname):"
echo "-------------------------------------------"
echo "GPU_temp => $(vcgencmd measure_temp | awk -F "=" '{print $2}')"
echo "CPU_temp => $((cpuTemp/1000))'C"
