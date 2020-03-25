#!/usr/bin/python3
import timeswipe
import optparse

parser = optparse.OptionParser()

parser.add_option('--command', dest="command", help="one of: start stop get", default="get")
parser.add_option('--num', dest="num", help="output number - 0 or 1", default=0)
parser.add_option('--freq', dest="freq", help="frequency", default=1)
parser.add_option('--high', dest="high", help="high level signal", default=4095)
parser.add_option('--low', dest="low", help="low level signal", default=0)
parser.add_option('--repeats', dest="repeats", help="number of generation to repeat", default=0)
parser.add_option('--duty', dest="duty", help="duty", default=0.5)

options, args = parser.parse_args()

tswipe = timeswipe.TimeSwipe()

if options.command == "start":
    print("exec command:", options.command, "num: ", options.num, "freq:", options.freq, "high:", options.high, "low:", options.low, "repeats:", options.repeats, "duty:", options.duty)
    if not tswipe.StartPWM(int(options.num), int(options.freq), int(options.high), int(options.low), int(options.repeats), float(options.duty)):
        ret = tswipe.GetPWM(int(options.num))
        if ret[1]:
            print("start failed: already started")
        else:
            print("start failed")
    else:
        print("start succeded")
elif options.command == "stop":
    print("exec command:", options.command, "num: ", options.num)
    if not tswipe.StopPWM(int(options.num)):
        ret = tswipe.GetPWM(int(options.num))
        if not ret[1]:
            print("stop failed: already stopped")
        else:
            print("stop failed")
    else:
        print("stop succeded")
elif options.command == "get":
    print("exec command:", options.command, "num: ", options.num)
    (ret, active, freq, high, low, repeats, duty) = tswipe.GetPWM(int(options.num))
    if not ret:
        print("get failed")
    elif not active:
        print(options.command, "num: ", options.num, "active:", active)
    else:
        print(options.command, "num: ", options.num, "active:", active, "freq:", freq, "high:", high, "low:", low, "repeats:", repeats, "duty:", duty)
else:
    print("wrong command: ", options.command)

