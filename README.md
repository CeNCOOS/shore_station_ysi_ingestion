# shore_station_ysi_getdata_code
 python code to append ysi storm central code

This code is set up to run on my personal PC.  Paths are hardwired and will need to be changed to read from 
the appropriate locations.

The code is meant to be simple.  Configuration data are in the station_parameters.txt files.  The last
column of which is wether to output the data or not as a csv file (1=yes, 0=no).

The csv_for_Highcharts file will need to have a time cut off for data to keep.  The way it is currently
written it should just keep appending to the file ad nauseum.
