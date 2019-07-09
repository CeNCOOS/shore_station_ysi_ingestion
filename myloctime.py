#
#
import pytz
from pytz import timezone
from datetime import datetime, timedelta
import dateutil
#from shore_modules import pretty_date
from pylab import date2num
#from shore_modules import findAge
def myloctime(stationtime):
    '''
    Code to create various flavors of time for output.
    Input is time of the form '2019-07-02 21:50:00'
    Output is...
    '''
    # should we put a try section in to find out if this fails?
    utc=pytz.utc
    pacific=timezone('US/Pacific')
    fmt='%Y-%m-%d %H:%M:%S %Z%z'
    pytz1970UTC=datetime(1970,1,1,0,0,0,tzinfo=utc)
    pytzNowUTC=datetime.utcnow().replace(tzinfo=utc)
    #
    pytzUTC=[dateutil.parser.parse(s) for s in stationtime]
    pytzUTC=[utc.localize(s) for s in pytzUTC]
    pytzL=[s.astimezone(pacific) for s in pytzUTC]
    pyL=[s.replace(tzinfo=pacific) for s in pytzL]
    tmptimeval=[s.strftime('%m/%d/%y %I:%M %p') for s in pyL]
    # convert to seconds since Jan 01 01 00 00 00 GMT
    diff1970UTC=[s-pytz1970UTC for s in pytzUTC]
    ss1970UTC=[(s.days*24*60*60)+s.seconds for s in diff1970UTC]
    # convert to Javascript timestap in local time (for highcharts)
    diff1970L=[s-pytz1970UTC for s in pytzL]
    diffNow1970=pytzNowUTC-pytz1970UTC
    js_diffNow1970=((diffNow1970.days*24*60*60)+diffNow1970.seconds)*1000
    # milliseconds since 1970
    jsL=[((s.days*24*60*60)+s.seconds)*1000 for s in diff1970L]
    diffNowUTC=[pytzNowUTC-s for s in pytzUTC]
    # check how old the data is...
    timeflag=[]
    for i in range(len(diffNowUTC)):
        if diffNowUTC[i].days > 7:
            timeflag.append(7)
        elif diffNowUTC[i].days > 1:
            timeflag.append(1)
        else:
            timeflag.append(0)
    # make Pretty time
    prettytimeL=[pretty_date(s) for s in diffNowUTC]
    pydatenumUTC=date2num(pytzUTC)
    
    timeInfo=tmptimeval,pyL,pytzL,pytzUTC,pydatenumUTC,ss1970UTC,jsL,js_diffNow1970,prettytimeL
    return timeInfo,timeflag
def pretty_date(diff):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """

    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0: return ''
    if day_diff == 0:
        if second_diff < 10: return "just now"
        if second_diff < 60: return str(second_diff) + " seconds ago"
        if second_diff < 120: return  "a minute ago"
        if second_diff < 3600: return str( second_diff / 60 ) + " minutes ago"
        if second_diff < 7200: return "an hour ago"
        if second_diff < 86400: return str( second_diff / 3600 ) + " hours ago"
    if day_diff == 1: return "Yesterday"
    if day_diff < 7: return str(day_diff) + " days ago"
    if day_diff < 31: return str(day_diff/7) + " weeks ago"
    if day_diff < 365: return str(day_diff/30) + " months ago" 
    return str(day_diff/365) + " years ago"    
