#!/usr/bin/env python
import os

def parse_nautilus_environment():
    result = {
        'NAUTILUS_SCRIPT_SELECTED_FILE_PATHS' : [],
        'NAUTILUS_SCRIPT_SELECTED_URIS' : [],
        'NAUTILUS_SCRIPT_CURRENT_URI' : [],
        'NAUTILUS_SCRIPT_WINDOW_GEOMETRY' : []
    }
    for i in result.keys():
        if os.environ.has_key(i):
            result[i] = os.environ[i].split(':')
        else:
            result[i] = []
    return result
def open_terminal(result):
    os.system("/usr/bin/gnome-terminal --working-directory=%s" %result['NAUTILUS_SCRIPT_CURRENT_URI'][1][2:])

open_terminal(parse_nautilus_environment())
