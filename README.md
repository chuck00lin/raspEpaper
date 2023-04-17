# Show some info on Epaper V1.0

## Function

boot
- show its wifi ESSID 
- show its wifi ipV4 for connection
- show if your servers are alive or not

```
how to add:
[[<Name>],[<host>],[<port>]]
```

shutdown
- bye bye message

## Hardware 
- 2.13inch waveshare 
- piZero 1.1 -w

## Dependency
- python3

- Install BCM2835 libraries:
```
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.71.tar.gz
tar zxvf bcm2835-1.71.tar.gz
cd bcm2835-1.71/
sudo ./configure && sudo make && sudo make check && sudo make install
```

- Install WiringPi libraries:
```
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v # Run gpio -v and version 2.52 will appear
```
---
source: https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_Manual#Users_Guides_of_Raspberry_Pi

## How to

### turn into service
- put .service file to `/etc/systemd/system`
- `sudo systemctl daemon-reload`
- `sudo systemctl enable run-after-boot.service`
- `sudo systemctl enable run-before-shutdown.service`

check with `sudo systemctl status run-after-boot.service`

run every 15 min
- `*/n * * * * /usr/bin/systemctl restart run-after-boot.service`

<iframe width="528" height="327" seamless frameborder="0" scrolling="no" src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQdiZn-NqW4VvyLJ-RAKwh9HhANekt004b3i-dT2l6Ly_CN6iuJLaV504J_-LrCC5t-BCwR8d__46l_/pubchart?oid=1943139083&amp;format=image"></iframe>
