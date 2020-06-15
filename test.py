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
parser.add_option('--input', dest="input", help="input name; default is first one from config", default="1")
parser.add_option('--output', dest="output", help="output filename to save data", default=None)
parser.add_option('--time', dest="time", help="runtime in seconds", default="10")

options, args = parser.parse_args()

tswipe = timeswipe.TimeSwipe()

json_file = open(options.config)
data = json.load(json_file)
item = data[options.input]
runtime = int ( options.time )
output = None
if options.output:
    sys.stdout = open(options.output, "w")

tswipe.SetMode(item["MODE"]);
offs = item["SENSOR_OFFSET"]
tswipe.SetSensorOffsets(offs[0], offs[1], offs[2], offs[3]);
gain = item["SENSOR_GAIN"]
tswipe.SetSensorGains(gain[0], gain[1], gain[2], gain[3]);
trans = item["SENSOR_TRANSMISSION"]
tswipe.SetSensorTransmissions(trans[0], trans[1], trans[2], trans[3]);
tswipe.SetBurstSize(24000);
tswipe.SetSampleRate(24000);
#tswipe.TraceSPI(True);

def signal_handler(sig, frame):
    tswipe.Stop()
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def on_event(ev):
    print("event: ", ev);

tswipe.onEvent(on_event);

count = 0
def process(data, errors):
    global count
    if errors:
        print_err("errors: ", errors)
    count = count + data.DataSize();
    for i in range(data.DataSize()):
        #print('\t'.join([str(data.sensor(j)[i]) for j in range(data.SensorsSize())]))
        pass

if tswipe.Start(process):
    time.sleep(runtime)
    print("count: ", count)
else:
    print("start failed")

