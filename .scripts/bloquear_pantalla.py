#!/usr/bin/env python

from subprocess import Popen, DEVNULL, PIPE

mensaje = '"' + "notify-send -u critic -t 10000 -- 'Bloqueando en 30 segundos...'" + '"'

xautolock = [
      'xautolock', '-detectsleep',
      '-time', '30', '-locker', '"i3lock-fancy"',
      '-notify', '30',
      '-notifier', mensaje
  ]

Popen(xautolock)

