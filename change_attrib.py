import sys
import os
import win32api
import win32com


def change_file_attribute(filename):
    if sys.platform.startswith("win"):
        if not win32api.GetFileAttributes(filename) and win32com.FILE_ATTRIBUTE_SYSTEM:
            os.system("attrib +s +i +h {}".format(filename))