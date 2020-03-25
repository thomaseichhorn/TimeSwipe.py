#!/usr/bin/python3
import timeswipe
import time
import json
import sys
import signal

def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

import optparse

parser = optparse.OptionParser()

parser.add_option('--config', dest="config", help="config file name", default="config.json")
parser.add_option('--input', dest="input", help="input name; default is first one from config", default="NORM")
parser.add_option('--output', dest="output", help="output filename to save data", default=None)

options, args = parser.parse_args()

tswipe = timeswipe.TimeSwipe()

json_file = open(options.config)
data = json.load(json_file)
item = data[options.input]
output = None
if options.output:
    sys.stdout = open(options.output, "w")

# old style
#tswipe.SetBridge(item["U_BRIDGE"]);
#tswipe.SetSensorOffsets(item["SENSOR_OFFSET"]);
#tswipe.SetSensorGains(item["SENSOR_GAIN"]);
#tswipe.SetSensorTransmissions(item["SENSOR_TRANSMISSION"]);

#new style
tswipe.Init(item["U_BRIDGE"], item["SENSOR_OFFSET"], item["SENSOR_GAIN"], item["SENSOR_TRANSMISSION"]);

def signal_handler(sig, frame):
    tswipe.Stop()
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

count = 0
def process(data, errors):
    #print("process")
    global count
    if errors:
        print_err("errors: ", errors)
    for i in range(data.DataSize()):
        count = count + 1
        #print('\t'.join([str(data.sensor(j)[i]) for j in range(data.SensorsSize())]))

if tswipe.Start(process):
    time.sleep(10)
    print("count: ", count)
else:
    print("start failed")

