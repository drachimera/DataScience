"""Simple Utility to make graphics behave in scripts/atom."""
import os
import psutil


def getParentName():
    """."""
    parentID = getParentID()
    return psutil.Process(parentID).name()


def getParentID():
    """."""
    return psutil.Process(os.getpid()).ppid()

# print(getParentName())
if(getParentName() == "Atom Helper"):
    # aperently the following needs to be run manually! GRRR!
    %matplotlib inline
