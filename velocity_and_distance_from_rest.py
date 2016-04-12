import sys
import argparse
import math

heavenly_body = {'mercury' : 3.7,
                 'venus' : 8.87,
                 'earth' : 9.8,
				 'mars' : 3.71,
				 'jupiter' : 24.79,
				 'saturn' : 10.44,
				 'uranus' : 8.87,
				 'neptune' : 11.15,
                 'moon' : 1.624
}

#Set the argument parser and command line arguments
parser = argparse.ArgumentParser(description="Produce ")
parser.add_argument('-t', dest='max_time', action='store', type=int, help='the amount of time given in seconds')
parser.add_argument('-s', dest='sample_time', action='store', type=float, help='the amount of time to sample in seconds')
parser.add_argument('-b', dest='body', action='store', help='heavenly body')

args = parser.parse_args()

#Check and act on the arguments
if args.max_time == None or args.max_time == 0 or args.body == None or len(args.body) == 0 or args.sample_time == None or args.sample_time == 0:
    print("Please give values for max and sample time above zero and the name of the heavenly body")
    sys.exit()
else:
    current_time = 0
    print( args.max_time)
    while current_time <= args.max_time:
	    print "Time:",current_time,"sec"
	    print "Velocity:",heavenly_body[args.body]*current_time,"m/s/s", " Distance:",0.5*(heavenly_body[args.body]*math.pow(current_time,2)),"m"
	    current_time = current_time + args.sample_time
    sys.exit("Complete")