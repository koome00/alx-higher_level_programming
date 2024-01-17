#!/usr/bin/python3
'''
Module 1: Reddit API querying
'''


import json
from requests import post, get


def number_of_subscribers(subreddit):
    """
    returns number of subscribers of a channel
    """
    
