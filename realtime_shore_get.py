from get_shore import get_shore
from configread import configread
from myloctime import myloctime
from writestationlast import writestationlast
from writestationlastj import writestationlastj
from csv_for_highcharts import csv_for_highcharts
import logging
#from push_to_webserver import push_to_webserver
import pdb
# Test code to try and break code and eventually be the driver
# okay need to rename this file to something meaning full
# also need to make it a loop through the stations
# need config files generated
# final piece is the push to skyrocket
#mystation=['IndianIsland']
mystation=['Humboldt','IndianIsland','Trinidad','Monterey','SantaCruzWharfFred']
lat=['40.7775','40.81503','41.055','36.60513','36.9603']
lon=['-124.19652','-124.15754','-124.14703','-121.88935','-122.0203']
for station in mystation:
##    station='Monterey'
##    lat='36.60513'
##    lon='-121.88935'
    # need to find the number in the list
    index=mystation.index(station)
    #pdb.set_trace()
    [cfg,data]=get_shore(station)
# This assumes date is column 1 and time is column 2 (column 0 is something else)
    stationtime=[]

    lv=len(data)
    if lv > 0:
        for i in range(lv):
            tmp=data[i][1]+' '+data[i][2]
            stationtime.append(tmp)
        # get timeInfo for output
        timeInfo,timeflag=myloctime(stationtime)
        # if cfg or data are empty we don't want to write data
        if station=='SantaCruzWharfFred':
            station='SantaCruzWharf'
        # path='/home/flbahr/shore/data/realtime/'+station+'/'
        path='c:/shore_data/'
        success=writestationlast(station,cfg,data,path,timeInfo)
        if success==-1:
            logging.warning('Failed to write latest csv file for '+station)
            #print("Failed to write latest csv file for "+station)
        # write latest json file
        success=writestationlastj(station,cfg,data,path,timeInfo,lat[index],lon[index],timeflag)
        if success==-1:
            logging.warning('Failed to write the latest json file for '+station)
            #print("Failed to write latest json file for "+station)
        # now to write the data for the HighCharts
        try:
            csv_for_highcharts(station,cfg,data,path,timeInfo)
        except:
            logging.warning('Failed to write csv data for HighCharts, check '+station+' data files')
            #print("Failed to write csv data for HighCharts, check file")
        #try:
        #push_to_webserver(station,path)
        #except:
        #    print("Failed to push files to skyrocket")
