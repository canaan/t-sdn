#!/usr/bin/env python

import sys
import json
import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

def scraping(url):
#def scraping(url, output_name):
    # Selenium settings
    driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
    # get a HTML response
    driver.get(url)
    html = driver.page_source.encode('utf-8')  # more sophisticated methods may be available
    # parse the response
    soup = BeautifulSoup(html, "lxml")
    # extract
    ## title
    header = soup.find("head")
    title = header.find("title").text
    ## description
    description = header.find("meta", attrs={"name": "description"})
    description_content = description.attrs['content'].text
    # output
    output = {"title": title, "description": description_content}

    dictdumper (output)


def dictdumper (dic) :
        print json.dumps (dic, sort_keys = True, indent = 4)


if __name__ == '__main__':
    # arguments
    argvs = sys.argv
    print argvs[1]
#    print argvs[2]
    ## check
    if len(argvs) == 0:
        print "Usage: python scraping.py [url] [output]"
        exit()
    url = argvs[1]
#    output_name = argvs[2]

    scraping(url)
    #scraping(url, output_name)
