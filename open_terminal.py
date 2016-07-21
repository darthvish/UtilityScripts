#!/usr/bin/env python
import os
import logging

#logging.basicConfig(level=logging.DEBUG, filename="logs.data", filemode="w")
#logger = logging.getLogger(__name__)

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
	path = result['NAUTILUS_SCRIPT_CURRENT_URI'][1][2:]
	path = path.replace("%20", " ")
	#logger.debug(path)
	#os.system("zenity --info --text '%s'"%path)
	os.system("/usr/bin/gnome-terminal --working-directory='%s'" %path)

open_terminal(parse_nautilus_environment())
