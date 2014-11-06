#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: github_languages
#   date: 2014-11-06
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""

import sys
import operator
from collections import defaultdict

import requests

def get_repositories(user):
    """ Retreive a list of a user's repositories """
    url = "https://api.github.com/users/{user}/repos".format(user=user)
    response = requests.get(url)
    return response.json()

def main():
    """ Main function """
    repositories = get_repositories(sys.argv[1])
    print repositories

if __name__ == "__main__":
    main()

