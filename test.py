#!/usr/bin/env python3
import logging
import datetime

logging.basicConfig(filename = "test.log", level = logging.DEBUG)
logging.debug("Test" + str(datetime.datetime.now()))
