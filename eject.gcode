M300 P200 ; beep 
M0;

M140 S30 ; set the bed to 30C
G28; home (for standalone)
M117 Resetting position...
G90 ; absolute positioning
G0 Z15 ; printhead up
;G0 X0 Y234 Z15 ; printhead in corner


G0 Z6 X120 Y225
M106; fan blast
M42 P46 S1; turn on external fan
;M140 S0 ; Turn-off bed
;G4 S6000 ; wait for 20 minutes
M190 R30 ; wait for bed to cool to 30C
M117 Cooling part...
M140 S0 ; Turn-off bed
G4 S300 ; wait for 5 minutes just in case

M300 P200 ; beep 
M0;
;M300 P200 ; beep 
M42 P46 S0; turn off external fan
M106 S0 ;fan off

M117 Ejecting part...
G0 Z15 ; printhead up
G0 X120 Y235 F8000 ; move x
G0 Z4 ; lower z
G0 Y0 F6000 ;  eject (slower)
G0 Z15 ; raise z
G28 Y ; home y in case we jammed

G0 Y235 F8000; second pass
G0 Z4 ; lower z
G0 Y0 F8000 ; eject
G0 Z15 ;raise z

G28 Y; home y again

M117 Returning to corner...
G0 X0 Y234 Z15 F8000
M107 
M140 S0

M117 Eject complete!