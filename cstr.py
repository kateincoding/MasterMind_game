#!/usr/bin/python3
"""class cstr that inherists from str"""


class cstr(str):
    """a colored string class"""
    colors = {
        'black': '\u001b[30m', 'red': '\u001b[31m', 'green': '\u001b[32m',
        'yellow': '\u001b[33m', 'blue': '\u001b[34m', 'magenta': '\u001b[35m',
        'cyan': '\u001b[36m', 'white': '\u001b[37m',
        'reset': '\u001b[0m'
    }

    def color(self, value=None):
        """returns a colored string, works with str and int (from 0 to 255)"""
        if not value:
            return self
        else:
            colors = cstr.colors
            if type(value) is int:
                return "\u001b[38;5;{}m{}{}".format(value, self,
                                                    colors['reset'])
            if value not in colors:
                raise ValueError("Not a valid color")
            else:
                cl = colors[value]
                return "{}{}{}".format(cl, self, colors['reset'])

    def bright(self, value=None):
        """returns a bright colored string, only works with str"""
        if not value:
            return self
        else:
            colors = cstr.colors
            if value not in colors:
                raise ValueError("Not a valid color")
            else:
                cl = colors[value]
                return "{}{}{}".format(cl.replace('m', ';1m'), self,
                               colors['reset'])
