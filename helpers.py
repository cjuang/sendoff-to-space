import feedparser
import urllib.parse

from flask import redirect, render_template, request, session, url_for
from functools import wraps

def satname(rocketsatname):
    """Takes in rocket and satellite name from SpaceflightNow website and returns only the satellite name"""
    
    # split the rocket and satellite name at the bullet
    names = rocketsatname.split('•')
    
    # remove spaces around satellite name
    namefull = names[1].strip()
    
    # return the satellite's name
    return namefull



# def lookup(satte):
#     """Looks up articles for a satellite."""
#     if satte in lookup.cache:
#         return lookup.cache[satte]
    
#     # get feed from Google
#     feed = feedparser.parse("http://news.google.com/news?geo={}&output=rss".format(urllib.parse.quote(satte, safe="")))

#     # cache results
#     lookup.cache[satte] = [{"link": item["link"], "title": item["title"]} for item in feed["items"]]

#     # return results
#     return lookup.cache[satte]
    
# # initialize cache
# lookup.cache = {}