#
# read a configuration file.
# from the configuration file it assumes the number of variables
# it also assumes order.
#
#import pdb
import logging
def configread(station):
    ''' This code reads a parameters configuration file.
    It will compute the number of variables to read from the parameters listed.
    It also will assume the order is the order listed in the file.
    Want this file to be dumb but reliable.
    Returns the an empty list if failure
    '''
    pathtocfgfile='c:/shore_data/'+station+'_parameters.txt'
    try:
        f=open(pathtocfgfile,'r')
        s=f.readlines()
        parameters=[]
        name=[]
        units=[]
        name2=[]
        outflag=[]
        # remove header line from file
        s.pop(0)
        nvalues=len(s)
        for line in s:
            line=line.rstrip('\n')
            line=line.split(',\t')
            parameters.append(line[0])
            name.append(line[1])
            units.append(line[2])
            name2.append(line[3])
            outflag.append(line[4])
        cfg=[nvalues, parameters, name, units, name2,outflag]
        f.close()
    except:
        # try to close config file if open
        try:
            f.close()
        except:
            pass
        logging.warning('An error occurred trying to read the conf file for '+station)
        #print("An Error occurred reading the config file for "+station)
        cfg=[]
    return cfg
