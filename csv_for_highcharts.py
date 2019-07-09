#
# Need to write data for HighCharts
#
import numpy as np
from csv import writer, reader
import os
#import pdb
import platform
import logging
def csv_for_highcharts(station,cfg,data,path,timeInfo):
    '''
    This code writes the sensor CSV files that HighCharts uses to plot.
    This could probably be done using other python code to create the plots that could be embedded.
    csv_for_highcharts(station,cfg,data,path,timeInfo)
    '''
    name=cfg[2]
    units=cfg[3]
    outflag=cfg[5]
    # figure out which variables to output
    a1=[z for z,e in enumerate(outflag) if int(e) !=0]
    la=len(a1)
    for i in range(la):
        j=a1[i]
        # step 1 generate filenames for data to be read from and written to
        parameter_filename=path+'/'+station+'_'+name[j]+'.csv'
        tmp_filename=path+'/'+station+'_'+name[j]+'.tmp'
        # step 2 try and open parameter file if it exists
        try:
            #f=open(parameter_filename,'rU+') # U= universal new lines and is depreciated
            f=open(parameter_filename,newline='')
        except:
            mylen=len(data)
            ik=np.arange(0,mylen)
            f=open(parameter_filename,'wt') # write text
            fw=writer(f,delimiter='%')
            fw.writerow(["javascriptTime_Local, "+name[j]])
            for k in ik:
                fw.writerow([str(timeInfo[6][k])+","+data[k][j]])
            #print("Could not open file so writing current data for "+station+" "+name[j])
            logging.warning('Could not open file so writing current data for '+station+' '+name[j])
            #f.close()
        else:
            # if we do open the file look for rows with new time stap
            fr=reader(f,delimiter=',')
            found=0
            findtime=0
            rc=0
            new_time=str(timeInfo[6][-1])
            time=[]
            myval=[]
            newval=[]
            for row in fr:
                try: row[0]
                except: pass
                else:
                    findtime=row[0].find(new_time)
                    try:
                        time.append(int(row[0]))
                        myval.append(float(row[1]))
                    except:
                        header=row[:]
                        pass
                    if findtime !=-1:
                        pass
                    rc=rc+1
                    if findtime >= 1:
                        logging.info('Data already in csv file')
                        #print('data already in csv file')
                        found=1
                        break
            ki=np.arange(0,len(timeInfo[6][:]))
            for k in ki:
                time.append(int(timeInfo[6][k]))
                try:
                    myval.append(float(data[k][j]))
                except:
                    myval.append(data[k][j])
            rc=rc+1
            newtime,index=np.unique(time,return_index=True)
            ji=np.arange(0,len(index))
            for jj in ji:
                try:
                    newval.append(myval[index[jj]])
                except:
                    pass
            perm_f=open(parameter_filename,newline='')
            try:
                tmp_f=open(tmp_filename,'wt')
            except:
                mkdir_p(path)
                tmp_f=open(tmp_filename,'wt')
            lasttime=newtime[-1]
            tmp_fw=writer(tmp_f,delimiter='%')
            tmp_fw.writerow(header)
            lp=np.arange(0,len(newtime))
            js_diffNow1970=timeInfo[7]
            for ip in lp:
                timediff=js_diffNow1970-newtime[ip]
                # if time difference is less than about 6.66 days (not sure why this number)
                if timediff < 575600000:
                    try:
                        tmp_fw.writerow([str(newtime[ip])+","+str(newval[ip])])
                    except:
                        pass
            tmp_f.close()
            perm_f.close()
        finally:
            f.close()
    # the following renames the temporary files to the csv files.
    for pcsvf in os.listdir(path):
        if pcsvf.endswith(".tmp"):
            oldname=path+pcsvf
            newname=path+pcsvf[0:-4]+'.csv'
            print(oldname)
            print(newname)
            try:
                bits,system=platform.architecture()
                if 'Windows' in system:
                    os.remove(newname)
                os.rename(oldname,newname) # on Windows you can't do this
            except:
                logging.warning("This file doesn't exit: "+oldname )
                #print("This file doesn't exit: "+oldname)
    # end of code
