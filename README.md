You'll wantc to edit the template file and the eject file for your printer, this is set up for an Ender 3 Pro with a custom firmware to turn on an external fan.
Also note that by default, the marlin firmware will time out while cooling after 20 minutes.


To loop `visor.gcode`:

```
python looper.py --loops 5 --template CE3-loop.template visor.gcode 
```


