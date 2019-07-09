#
# push to skyrocket
#
from datetime import datetime, timedelta
import os
import paramiko
import shutil
import pdb
#station="Monterey"
#path="c:/shore_data/"
def push_to_webserver(station,path):
    epoch=datetime(1970,1,1)
    seconds_in_a_day=60*60*24
    four_minutes=timedelta(minutes=4)
    pyfour_minutes_ago=datetime.utcnow()-four_minutes
    rightnow=datetime.utcnow()
    since_epocha=pyfour_minutes_ago-epoch
    since_epochb=rightnow-epoch

    a=since_epocha.days*seconds_in_a_day+since_epocha.seconds
    b=since_epochb.days*seconds_in_a_day+since_epochb.seconds
    # Need a test place to push files...
    #webdir='/var/www/html/sections/data/shore/'+station+'/'
    skyrocketdir='/home/flbahr/'+station+'/'
    #    skyrocketdir='/var/www/html/sites/all/libraries/shorestations/data/'+station+'/'
    # set up ftp connection
    host="skyrocket.mbari.org"
    port=22
    transport=paramiko.Transport((host,port))
    # is there a way to store these encripted so they can't be seen?
    # This code will be run from a non web accessible folder.
    username=
    password=
    #
    transport.connect(username=username,password=password)
    sftp=paramiko.SFTPClient.from_transport(transport)
    print('\n* Copying '+station+' files to the web Server. ftp open')
    #
    try:
        sftp.chdir(skyrocketdir)
    except IOError:
        sftp.mkdir(skyrocketdir)
        sftp.chdir(skyrocketdir)
    for dirname,dirnames,filenames in os.walk(path):
        copied=0
        for filename in filenames:
            if '~' in filename: pass
            elif 'conductivity' in filename: pass
            elif 'latitude' in filename: pass
            elif 'longitude' in filename: pass
            elif 'NetCDF' in filename: pass
            elif 'tmp' in filename: pass
            elif 'battery' in filename: pass
            elif 'resist' in filename: pass
            elif 'uncal' in filename: pass
            elif 'stationid' in filename: pass
            elif 'phmv' in filename: pass
            elif 'save' in filename: pass
            elif 'r.txt' in filename: pass
            elif 'winch' in filename: pass
            elif 'ctrl' in filename: pass
            elif 'g2depth' in filename: pass
            elif 'MossLanding_pressure' in filename: pass
            elif 'orp' in filename: pass
            elif 'charge' in filename: pass
            elif '.py' in filename: pass
            elif '.txt' in filename: pass
            elif '.m' in filename: pass
            elif '.nc' in filename: pass
            else:
                # code copies all files in directory regardless of station name
                # need to fix this?
                thisFile=os.path.join(dirname,filename)
                if os.stat(thisFile).st_mtime > a:
                    webfile=os.path.join(webdir,filename)
                    lowerfile=filename.lower()
                    skyrocketfile=os.path.join(skyrocketdir,lowerfile)
                    try: shutil.copyfile(thisfile,webfile)
                    except:
                        print('copyfile of '+thisFile+' failed, make Directory and try Again')
                        mkdir_p(webdir)
                        try: shutil.copyfile(thisfile,webfile)
                        except: print('Failed again')
                        else: pass
                    else: copied=1
                    try:
                        sftp.put(thisFile,skyrocketfile)
                    except:
                        pass
    if copied==1: print('- Files Copied')
    sftp.close()
    transport.close()
    print('FTP Closed')
#
def mkdir_p(path):
    try: os.makedirs(path)
    except OSError as exec:
        if exec.errno==errno.EEXIST and os.path.isdir(path): pass
        else: raise
    
    
