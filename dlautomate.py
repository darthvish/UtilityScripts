import psutil  # this module retrieve process, network information
import time # this module is used to sleep for give time
import os # used for system call to bash commands

def start_download():
  """starts download

  This function start downloading by starting downloading program.
  """
  NAME = 'deluge &' # command to be run in next statement
  os.system(NAME) # run bash command # used to start downloading program in background

def stop_download():
  """stops download

  This function stop downloading by killing desired pid of downloading program.
  """
  print 'stop download mode' # debug statement
  NAME = 'deluge'
  for x in psutil.process_iter(): # psutil.process_iter() returns process generator for all running process and their pid's
    if NAME in x.name:  
      os.system('kill %d'%(x.pid)) # it kills downloading programming if conditions holds true
      break


def monitor_normal_mode():
  """monitor in normal mode

  this method works in normal mode and it checks given condition for 
  a period and then as per it deductions it returns a interger 0 or 1
  which decide what step will occur next.
  """
  TIME = 30                       # monitor time in seconds # cycles during one iteration of method
  NAMES = ['chrome', 'banshee']   # program names used during monitoring
  speeds = []                     # list to hold internet speed values during given time
  for x in range(TIME):             # loop iterates for given period of time in TIME variable
    speeds.append(get_dl_speed()) # get internet speed and append that to list
  status = get_process_status(NAMES) # status to check whether some predefined running or not
  print speeds # debug statement
  print status # debug statement
  count = 0                         # variable which decides what will do in next iteration
  if status == False:               # status get by checking that whether some program running or not  # if status is False
    for x in speeds:              # checks all internet speeds are zero or not # if zero it means that user is doing nothing on pc
      if x == 0:
        count = 0             # count = 0 means that we are moving to downloading_mode
      else:
        count = 1             # count = 1 means that status is false # but somebody using internet like update manager
  else:
    count = 1

  print "cycle complete"   # debug statement
  if count == 0:                   # count = 1 means start downloading 
    start_download()
    return 1
  else:
    return 0                    # count = 0 keep monitoring 

def monitor_download_mode():
  """monitor_download_mode

  this method monitors user defined criteria when downloading is running.
  it checks for some user-defined programs.
  if any program running then it goes in monitor_normal_mode
  """
  print 'download monitor cycle' # debug statement
  TIME = 30                                        # running time of program
  NAMES = ['gnome-terminal','chrome', 'banshee']   # user-defined programs to monitor
  count = 0
  for x in range(TIME):
    status = get_process_status(NAMES)
    if status == True:
      count = 1
      break
    else:
      time.sleep(1)
  if count == 1:
    stop_download()
    return 0
  else:
    return 1

def get_process_status(names):
  """get_process_status

  it check status of user defined program are running or not
  """
  for x in psutil.process_iter():
    for name in names:
      if name in x.name:
        return True # one of the user defined program is running
  return False # no user defined program is running
  

def get_dl_speed():
  """returns downloading speed

  returns downloading speed by computing speed during period of 1 second
  """
  value1 = psutil.network_io_counters(pernic=True)['wlan0'][1] # first value of total received data by wlan
  time.sleep(1)                                                # sleeps for a second
  value2 = psutil.network_io_counters(pernic=True)['wlan0'][1] # second value of total received data by wlan
  speed = (value2 - value1) / 1000 # by using difference of these values we find out speed in a second
  return speed

def schedule_program():
  """This is funciton is will be utilized later
  """
  print 'Enter minutes:->',
  user_input = int(raw_input())
  minutes = user_input * 60
  print 'sleeping for %s minutes' %minutes
  time.sleep(minutes)
  print 'start working'


flag = 0
os.system('clear')
print '<<<------------Hi--------------->>>'
while True:
  print flag
  if flag == 0:
    flag = monitor_normal_mode()
  elif flag == 1:
    flag = monitor_download_mode()
  
