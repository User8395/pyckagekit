"""
Pyckagekitd: The Packagekit daemon rewritten in Python
"""

import logger
import platform
from os import system

install, remove, update, upgrade, search = ""

"""
If distro uses dnf (Fedora, RHEL, CentOS?)
"""
def dnf():
    install = "dnf install"
    remove = "dnf remove"
    update = "dnf update --refresh"
    upgrade = "dnf upgrade"
    search = "dnf search"
