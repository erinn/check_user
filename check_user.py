#!/usr/bin/env python

# Copyright 2016, Erinn Looney-Triggs <erinn.looneytriggs@gmail.com>
#
# License: AGPL Version 3 or later

import argparse
import logging
import pwd
import signal
import sys

__author__ = 'Erinn Looney-Triggs'
__credits__ = ['Erinn Looney-Triggs']
__license__ = 'AGPL 3.0'
__maintainer__ = 'Erinn Looney-Triggs'
__email__ = 'erinn.looneytriggs@gmail.com'
__version__ = '1.0'
__date__ = '2016-09-09'
__revised__ = '2016-09-09'
__status__ = 'Development'

# Nagios exit codes in English
UNKNOWN = 3
CRITICAL = 2
WARNING = 1
OK = 0


def get_user(username):
    """
    """

    try:
        user = pwd.getpwnam(username)
    except KeyError:
        user = None

    return user


def parse_exit(user_info, username):
    """
    """
    if user_info:
        print('User: "{0}" found. UID: {1}, GID: {2}, GECOS: {3}'
              .format(user_info.pw_name, user_info.pw_uid, user_info.pw_gid,
                      user_info.pw_gecos))
        sys.exit(OK)
    else:
        print('User: {0} not found!'.format(username))
        sys.exit(CRITICAL)


def sigalarm_handler(signum, frame):
    '''
    Handler for an alarm situation.
    '''

    print('{0} timed out after {1} seconds, '
          'signum:{2}, frame: {3}').format(sys.argv[0], options.timeout,
                                           signum, frame)

    sys.exit(CRITICAL)
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check for the existence of '
                                     'a given user name.')
    parser.add_argument('-t, --timeout', dest='timeout', action='store',
                        type=int, default=30,
                        help='Set the timeout for the program to run '
                        'Default: %(default)s seconds.')
    parser.add_argument('-u, --username', dest='username', action='store',
                        help='Specify the username to use. '
                        'Default: %(default)s')
    parser.add_argument('--version', action='version',
                        version='%(prog)s Version: {0}'.format(__version__))

    args = parser.parse_args()
    username = args.username

    signal.signal(signal.SIGALRM, sigalarm_handler)
    signal.alarm(args.timeout)

    user_info = get_user(username)
    parse_exit(user_info, username)

    signal.alarm(0)
