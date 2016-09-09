#!/usr/bin/env python

# Copyright 2016, Erinn Looney-Triggs <erinn.looneytriggs@gmail.com>
#
# License: AGPL Version 3 or later

import argparse
import logging
import pwd

__author__ = 'Erinn Looney-Triggs'
__credits__ = ['Erinn Looney-Triggs']
__license__ = 'AGPL 3.0'
__maintainer__ = 'Erinn Looney-Triggs'
__email__ = 'erinn.looneytriggs@gmail.com'
__version__ = '1.0'
__date__ = '2016-09-09'
__revised__ = '2016-09-09'
__status__ = 'Development'

def get_user(username):
    '''
    '''

    user = pwd.getpwnam(username)

    return user
