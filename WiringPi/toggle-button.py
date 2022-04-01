#!/usr/bin/env python3
with open('button', 'r+') as f:
   button_state = f.read().strip()
   f.seek(0)
   if button_state == 'unpressed':
       button_state = f.write('pressed')
       print(f'new state: pressed')
   if button_state == 'pressed':
       button_state = f.write('unpressed')
       print(f'new state: unpressed')
   f.truncate()

