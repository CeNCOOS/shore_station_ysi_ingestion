import logging
#import pdb
def writestationlastj(station,cfg,data,path,timeInfo,lat,lon,ageFlag):
    ''' This is code to write out a json file of the latest data.
    writestationlast(station,cfg,data,path,timeInfo)
    station is the station name (e.g. Trinidad)
    cfg is from configread
    data is new data from get_station
    path is output path to write data to (upper level)
    timeInfo is local tine information
    The code returns 0 for succes or -1 for failure
    The variables passed are explicitly written so it is easy to see
    what you need.
    '''
#station='Trinidad'
#path='c:/shore_data/'
    name=cfg[2] # name
    units=cfg[3] # units
    outflag=cfg[5] # output flags (0=no, 1=yes)
    fileout=path+'/last'+station+'.json'
    try:
        f=open(fileout,'wt')
        f.write('[{"name": "Latitude", "units": " ","value":"'+lat+'"},')
        f.write('{"name":"Longitude","units":" ","vlaue":"'+lon+'"},')
        # check if we shoud output
        a1=[z for z,e in enumerate(outflag) if int(e) !=0]
        #pdb.set_trace()
        # need code for if data is too old
        #if ageCheck is False:
        #    f.write('{"name":"Maintenance","units":" ","value":" "},')
        ln=len(a1)
        for i in range(ln):
            j=a1[i]
            if i < ln-1:
                if ageFlag==1:
                    f.write('{"name":"<span class="'+'\'old-data\''+'>'+name[j]+'</span>'+
                            '","units":"'+'<span class='+'\'old-data\''+'>'+units[j]+'</span>'+
                            '","value":"'+'<span class='+'\'old-data\''+'>'+data[-1][j]+'</span>'+
                            '","timestring":"'+'<span class='+'\'old-data\''+'>'+timeInfo[0][-1]+'</span>'+
                            '"},')
                elif ageFlag==7:
                    f.write('{"name":"<span class="'+'\'super-old-data\''+'>'+name[j]+'</span>'+
                            '","units":"'+'<span class='+'\'super-old-data\''+'>'+units[j]+'</span>'+
                            '","value":"'+'<span class='+'\'super-old-data\''+'>'+data[-1][j]+'</span>'+
                            '","timestring":"'+'<span class='+'\'super-old-data\''+'>'+timeInfo[0][-1]+'</span>'+
                            '"},')
                else:
                    f.write('{"name":"'+name[j]+
                            '","units":"'+units[j]+
                            '","value":"'+data[-1][j]+
                            '","timestring":"'+timeInfo[0][-1]+
                            '"},')
            else:
                if ageFlag==1:
                    f.write('{"name":"<span class="'+'\'old-data\''+'>'+name[j]+'</span>'+
                            '","units":"'+'<span class='+'\'old-data\''+'>'+units[j]+'</span>'+
                            '","value":"'+'<span class='+'\'old-data\''+'>'+data[-1][j]+'</span>'+
                            '","timestring":"'+'<span class='+'\'old-data\''+'>'+timeInfo[0][-1]+'</span>'+
                            '"}')
                elif ageFlag==7:
                    f.write('{"name":"<span class="'+'\'super-old-data\''+'>'+name[j]+'</span>'+
                            '","units":"'+'<span class='+'\'super-old-data\''+'>'+units[j]+'</span>'+
                            '","value":"'+'<span class='+'\'super-old-data\''+'>'+data[-1][j]+'</span>'+
                            '","timestring":"'+'<span class='+'\'super-old-data\''+'>'+timeInfo[0][-1]+'</span>'+
                            '"}')
                else:
                    f.write('{"name":"'+name[j]+
                            '","units":"'+units[j]+
                            '","value":"'+data[-1][j]+
                            '","timestring":"'+timeInfo[0][-1]+
                            '"}')
        f.write(']')
        f.close()
        return 0
    except:
        try:
            f.close()
        except:
            pass
        logging.warning('Could not write latest json file for station '+station)
        #print("Could not write latest json file for station "+station)
        return -1
