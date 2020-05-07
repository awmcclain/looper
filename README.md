Based on the excellent technique here (watch this first): https://www.youtube.com/watch?v=cuSGl17JGNA&fbclid=IwAR1Lbx3q-mOagbZ_tSOdqCvAEEZd4ESIZ4YAUtiyh_xqdda6N71b7wYlluk

You'll want to edit the template file and the eject file for your printer, this is set up for an Ender 3 Pro with a custom firmware to turn on an external fan.


To loop `visor.gcode`:

```
python looper.py --loops 5 --template CE3-loop.template visor.gcode 
```


Also note that by default, marlin firmware will time out (and stop waiting) when bed cooling if the bed doesn't change temperature for 1 minute. You can override that by adding
```
#define MIN_COOLING_SLOPE_TIME_BED 1200 // (seconds) Timeout if bed temperature can't be reached
```
to `Configuration.h` in the firmware.
