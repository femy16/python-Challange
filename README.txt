Swrve Test: 

I have done this program in Python 3.

Installed sh module for the extracting of file by giving $ sudo pip3 install sh in terminal.

Installed dateutil to work with date formats in csv file by $ sudo pip3 install python-dateutil in terminal.

We can run the program by $ python3 swrve_test.py "https://s3.amazonaws.com/swrve-public/full_stack_programming_test/test_data.csv.gz".

In download_file(url, filename) function: The Program will download test_data.csv.gz file, also it will unzip the test_data.csv file from it, only if the file does not exist.

In readfile(csvfilename) function: The program will open and read the csv file downloaded.

In processfile(file_lines) function: The program will process the csv file to get the outputs.

In display_output(results) function: The program prints the outputs
 the outputs:
            Total count of all users : 100
            number of users with a device resolution of 640x960 (width x height) : 28
            total spend of all users in dollars: 51621
            user_id of the first user who joined : a888a1c57cf6af2ffee687bfdd7dc4c5
            
The program checks sys arguments, if there is no input url, it gives an error message :Please give a valid url.
Program also checks the filename at the end of url if its not gzipped CSV file, it gives an error message : Only gzipped CSV file accepted,Please give a valid url.

program also have unit testing with assert, which tests the output of processfile(file_lines) function.



