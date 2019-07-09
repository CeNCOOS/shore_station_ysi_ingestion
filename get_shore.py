#
# Simple code to read shore station files
# rely on a config file to know the columns names and units
#
import csv
from csv import writer, reader
from pylab import date2num
# code to be written
from configread import configread
import numpy as np
import logging
def get_shore(station):
    #station='Monterey'
    #station='Trinidad'
    '''
    Get shore station data for a given station
    Uses configread to get the data columns and how many there are
    station_parameters.txt file needs to be \t (tab) seperated and correct
    for this to work.
    Returns a list of the data where data[0][:] is the first line fo the data file
    data[0][0] is the first line, first column
    It returns an empty list if file contains no data
    Actual return is [cfg, data] since we may want the cfg info if we have data.
    '''
    cfg=configread(station)
    if len(cfg)==0:
        logging.warning('Bailing, failure to read config file for station '+station)
        #print("Bailing failure reading config file for station "+station)
        data=[]
        return [cfg,data]
    # path to file
    try:
    	# windows code for the moment
        fn='z:/incoming/Fred/'+station+'.csv'
        # code to change to for Linux
        #fn='/ftp/incoming/Fred/'+station+'.csv'
        datafile=open(fn,'r')
        s=datafile.readlines()
        # can we tell if s is empty at this point?
        # remove header line
        s.pop(0)
        ns=len(s)
        lcount=0
        if ns > 0:
            # define empty data array
            # this only works for numbers not strings...
            #data=np.zeros([ns,cfg[0]])
            data=[]
            for line in s:
                line=line.rstrip('\n')
                line=line.split(',')
                data.append(line)
        #        for vnum in range(0,cfg[0]):
        #            data[lcount][vnum]=line[vnum]
        #        ++lcount
        else:
            logging.warning('There appears to be no data in the file for station '+station)
            #print("There appears to be no data in the file for station "+station)
            data=[]
        datafile.close()
    except:
        logging.warning('Failure! Could not read data file for station '+station)
        #print("Failure reading data file for station "+station)
        data=[]
        # try to close data file if it is open
        try:
            datafile.close()
        except:
            pass
    return [cfg,data]
