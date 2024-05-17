import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "/Users/srivatsav/Downloads/PRO-C118-Student-Boilerplate-Code-main”

class FileSystemEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print({"hey, {event.src_path} has been created"})

    def on_deleted(self, event):
        print({"oops someone deleted {event.src_path}"})   


try :
    while true:
        time.sleep(2)
        print('running')
except KeyboardInterrupt:
    print('stopped')
    observer.stop()

