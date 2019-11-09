import csv
import gzip
from datetime import datetime
import datetime 
import dateutil.parser
from sh import gunzip
import os
import requests
import sys
from test_swrve_test import assert_equal




def download_file(url, filename):
   
   csvfilename=os.path.splitext(os.path.basename(filename))[0]
   if not os.path.isfile(csvfilename):
       print('Downloading File')
       response = requests.get(url)
       
       if response.status_code == 200:
          
            with open(filename, 'wb') as file:
               
               for chunk in response:
                   file.write(chunk)
            gunzip(filename) 
            return(csvfilename)
     
   else:
       print('File exists')
       return(csvfilename)
       

def readfile(csvfilename):
    file_lines = csv.DictReader(open(csvfilename))
    return(file_lines)
    
def processfile(file_lines):
    
    def str_to_date(s):
        return dateutil.parser.parse(s)
        
    total_spend = 0
    total_users=0
    now = datetime.datetime.now()
    most_recent_date=dateutil.parser.parse(str(now)[:19]+"+00:00")
    most_recent_id = 0
    no_using_640x960=0
    
    for row in file_lines:
        total_spend += int(row["spend"])
        total_users+=1
        
        date_joined = str_to_date(row['date_joined'])
        if date_joined < most_recent_date:
            most_recent_date = date_joined
            most_recent_id = row["user_id"]
        if row['device_height']=='960' and row['device_width']=='640':
            no_using_640x960+=1
            
    return([total_users,no_using_640x960,total_spend,most_recent_id])
            
def display_output(results):
    print("Total count of all users : "+str(results[0]))
    print("number of users with a device resolution of 640x960 (width x height) : "+str(results[1]))
    print("total spend of all users in dollars: "+str(results[2]))
    print("user_id of the first user who joined : "+results[3])
    
def tests():
    assert_equal(processfile(file_lines),[0,0,0,0])
    assert_equal(len(results),4)
    assert_equal(type(results),list)

    print("all tests pass")    
    
   
if (len(sys.argv)==2):
    
    url = sys.argv[1] 
    filename=url.split("/")[-1]
    gz_tag=filename.split(".")[-1]
    
    if(gz_tag=='gz'):
        csvfilename=download_file(url,filename)
        file_lines=readfile(csvfilename)
        results=processfile(file_lines)
        display_output(results)
        tests()
    else:
        print("Only gzipped CSV file accepted,Please give a valid url")
else:
    print("Please give a valid url")
    
    


