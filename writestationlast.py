#
# write station last csv
#
from csv import writer
import logging
def writestationlast(station,cfg,data,path,timeInfo):
    ''' This is code to write out a csv file of the latest data.
    writestationlast(station,cfg,data,path,timeInfo)
    station is the station name (e.g. Trinidad)
    cfg is from configread
    data is new data from get_station
    path is output path to write data to (upper level)
    timeInfo is local tine information
    The code returns 0 for succes or -1 for failure
    '''
    name=cfg[2]
    fileout=path+'last'+station+'.csv'
    try:
        f=open(fileout,'wt')
        tmpcsv=writer(f)
        str1='Parameter'
        str2='Last value'
        str3='Local Time'
        tmpcsv.writerow((str1,str2,str3))
        # NOTE: If run on a PC it appears that there are extra lines.
        # On a Linux machine it looks fine (^M is at the end of the lines)
        for i in range(len(name)):
            tmpcsv.writerow((name[i],data[-1][i],timeInfo[0][-1]))
        f.close()
        return 0
    except:
        try:
            f.close()
        except:
            pass
        logging.warning('Could not write latest csv file for station '+station)
        #print("Could not write latest csv file for station "+station)
        return -1
