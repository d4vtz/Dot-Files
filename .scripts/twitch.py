#!/usr/bin/env python

from subprocess import PIPE, Popen
from sys import argv

CANAL = 'https://twitch.tv/' + argv[1]
CALIDAD = 'best'

streamlink = [
    'streamlink',
    CANAL,
    CALIDAD
    ]

chat = [
    'midori',
    '--app='+ CANAL + '/chat?popout='
    ]

Popen(streamlink, stdout=PIPE)
