import argparse, re, os
from jinja2 import Template

parser = argparse.ArgumentParser()
parser.add_argument('target')
parser.add_argument('--loops', type=int, default=2)
parser.add_argument('--template', type=str)
parser.add_argument('--output', type=str)
parser.add_argument('--eject', type=str, default="eject.gcode")

args = parser.parse_args()

if args.output == None:
    filenameparts = os.path.splitext(args.target)
    args.output = "{0}-loop{1}x{2}".format(filenameparts[0], args.loops, filenameparts[1])

# load the template

f = open(args.template, "r")
template = Template(f.read())
f.close()

# lazy enum
MODE_BED_TEMP = 0
MODE_NOZZLE_TEMP = 1
MODE_FINDING_START = 2
MODE_FINDING_END = 3
MODE_COMPLETE = 4
mode = MODE_BED_TEMP

# read in the gcode
bedtemp = 55
nozzletemp = 220
print "Reading target " + args.target

f = open(args.target, "r")

bed_re = re.compile(r"M140 S(\d+)")
nozzle_re = re.compile(r"M104 S(\d+)")
start_re = re.compile(r"^;MESH") # A line like `;MESH:Object 1` starts the object
end_re = re.compile(r"^G90") # A line like `G90 ;Absolute positionning` ends the object

object_gcode = ""
for line in f:
    if mode == MODE_BED_TEMP:
        match = bed_re.search(line)
        if match:
            bedtemp = match.group(1)
            print "Bed temp is " + bedtemp
            mode = MODE_NOZZLE_TEMP
    if mode == MODE_NOZZLE_TEMP:
        match = nozzle_re.search(line)
        if match:
            nozzletemp = match.group(1)
            print "Nozzle temp is " + nozzletemp
            mode = MODE_FINDING_START
    if mode == MODE_FINDING_START:
        match = start_re.search(line)
        if match:
            mode = MODE_FINDING_END
    if mode == MODE_FINDING_END:
        match = end_re.search(line)
        if match:
            mode = MODE_COMPLETE
        else:
            # Keep adding lines until we reach the end
            object_gcode += line
    if mode >= MODE_COMPLETE:
        break
f.close()

# read in the eject code
f = open(args.eject, "r")
eject_gcode = f.read()
f.close()


# combine the templates
output = template.render(bedtemp=bedtemp, nozzletemp=nozzletemp, loops=args.loops, object_gcode=object_gcode, eject_gcode=eject_gcode)

f = open(args.output, "w")
f.write(output)
f.close()

print "Wrote looped gcode to " + args.output
