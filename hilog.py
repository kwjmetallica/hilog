#!/usr/bin/python

# ANSI color codes
# FYI: http://pueblo.sourceforge.net/doc/manual/ansi_color_codes.html 
style = {
    'reset'     :'[0m', # reset; clears all colors and styles (to white on black)
    'bold'      :'[1m', # bold on (see below)
    'italic'    :'[3m', #italics on
    'uline'     :'[4m', # underline on
    'inverse'   :'[7m', # inverse on; reverses foreground & background colors
    'strike'    :'[9m', # strikethrough on
    'unbold'    :'[22m', # bold off (see below)
    'unitalic'  :'[23m', # italics off
    'unuline'   :'[24m', # underline off
    'uninverse' :'[27m', # inverse off
    'unstrike'  :'[29m', # strikethrough off
}

fgColor = {
    'black'     :'[30m', # set foreground color to black
    'red'       :'[31m', # set foreground color to red
    'green'     :'[32m', # set foreground color to green
    'yellow'    :'[33m', # set foreground color to yellow
    'blue'      :'[34m', # set foreground color to blue
    'magenta'   :'[35m', # set foreground color to magenta (purple)
    'cyan'      :'[36m', # set foreground color to cyan
    'white'     :'[37m', # set foreground color to white
    'default'   :'[39m', # set foreground color to default (white)
}

bgColor = {
    'black'     :'[40m', # set background color to black
    'rec'       :'[41m', # set background color to red
    'green'     :'[42m', # set background color to green
    'yellow'    :'[43m', # set background color to yellow
    'blue'      :'[44m', # set background color to blue
    'magenta'   :'[45m', # set background color to magenta (purple)
    'cyan'      :'[46m', # set background color to cyan
    'white'     :'[47m', # set background color to white
    'default'   :'[49m', # set background color to default (black)
}

import sys

for line in sys.stdin:
    print "\x33[36m%s\x33[0m"%line.rstrip()
