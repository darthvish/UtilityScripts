from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup
import csv
import logging

logging.basicConfig(filename="logging.log",filemode="w",level=logging.DEBUG)

def main():
    BASE_URL = "http://www.alexa.com/topsites/countries;%d/IN"
    fh = open("AlexaIndiaTop.csv","w")
    csv_writer = csv.writer(fh)
    csv_writer.writerow(["rank","name","desc"])
    # first get the page for current page
    # put all those data in csv file
    # do it again till there is no page
    for x in range(0, 20):
        print ".. downloading.. %d"x
        con = requests.get(BASE_URL%x)
        soup = BeautifulSoup(con.text)
        con.close()

        # create a list to hold our data for each site
        site_data_row = []
        for each_obj in soup.find_all(attrs={"class":"site-listing"}):
            # logging statements
            logging.debug(each_obj.div.text)
            logging.debug(each_obj.a.text)
            logging.debug(each_obj.find(attrs={"class":"description"}).text)
            site_data_row.append(each_obj.div.text)
            site_data_row.append(each_obj.a.text)
            site_data_row.append(each_obj.find(attrs={"class":"description"}).text.encode("utf-8"))
            csv_writer.writerow(site_data_row)
            site_data_row=[]

    fh.close()
    print "all information downloaded"






if __name__ == "__main__":
    main()