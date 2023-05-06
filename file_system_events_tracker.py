import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print('Hey, {event.src_path} has been created')
    
    def on_deleted(self,event):
        print('Oops! Someone deleted {event.scr_path}!')

    def on_modified(self, event):
        print('Hey there, {event.src_path} has been modified')

    def on_moved(self,event):
        print('Someone moved {event.scr_path} to {event.dest_path}')


try:
    while True:
        time.sleep(2)
        print('running...')
except KeyboardInterrupt:
    print('stopped')
    observer.stop()

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt

while True:
    time.sleep(2)
    print("running...")






