#!/usr/bin/env python
from wmutils.procesos import cmd_output

cmd_output(
      'xautolock -detectsleep -time 1 -locker \
      "i3lock-fancy" -notify 30 -notifier \
      "notify-send -u critic -t 10000 -- ' + "'Bloqueando en 30 segundos...'" + '"'
)
