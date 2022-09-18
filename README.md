# Show some info on Epaper

### Hardware 
- 2.13inch waveshare 
- piZero 1.1 -w

## Dependency
---
https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_Manual#Users_Guides_of_Raspberry_Pi
---
- python3

Install BCM2835 libraries:
```
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.71.tar.gz
tar zxvf bcm2835-1.71.tar.gz
cd bcm2835-1.71/
sudo ./configure && sudo make && sudo make check && sudo make install
```

Install WiringPi libraries:
```
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v # Run gpio -v and version 2.52 will appear
```

## How to

### turn into service
- put .service file to `/etc/systemd/system`
- `sudo systemctl daemon-reload`
- `sudo systemctl enable run-after-boot.service`
- `sudo systemctl enable run-before-shutdown.service`

check with `sudo systemctl status run-after-boot.service`
