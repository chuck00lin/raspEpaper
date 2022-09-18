#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import subprocess
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

# -----------

try:
    logging.info("epd2in13_V2 Demo")
    
    epd = epd2in13_V2.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    # Drawing on the image
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    
    logging.info("1.Drawing on the image...")
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)

    # ---my info---
    draw.text((5,20), "--raspScreen is sleeping--", font = font20, fill =0) 

    epd.display(epd.getbuffer(image)) 
    logging.info("Goto Sleep...")
    time.sleep(2)         
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
