# Copyright 2018 Utkarsh Bhatt
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from bs4 import BeautifulSoup
import requests
from clint.textui import progress

def checkPresence(path , size):
    if os.path.isfile(path):
        if size > os.path.getsize(path):
            print("Lecture downloaded earlier is of smaller size ({}KB vs {}KB)".format(os.path.getsize(path)/(8*1024), size/1024))
            return True;
        else:
            print("Lecture already downloaded")
            return  False;
    else:
        return True


choice = int()
def save_file(url, name):
    if(choice is 1):
        path = name+".mp4"
    elif(choice is 2):
        path = name+".3gp"
    elif(choice is 3):
        path = name+".flv"
    r = requests.get(url, stream=True)
    total_length = int(r.headers.get('content-length'))
    if checkPresence(path, total_length):
        with open(path, 'wb') as f:
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                if chunk:
                    f.write(chunk)
                    f.flush()

nptel_url = raw_input("Enter the NPTEL video download URL: ")
file = requests.get(nptel_url).content
soup = BeautifulSoup(file, 'html.parser')
choice = int(input("Enter the format to save the file in \n1 for MP4 \n2 for 3GP and \n3 for FLV \nIf you're confused enter 1\nInput : "))

if(choice in (1,2,3)):
    links = list()
    if(choice is 1):
        print("Checking for availability of MP4 videos.")
        for instance in soup.find_all('a'):
            if("MP4 Download" in str(BeautifulSoup(str(instance), 'html.parser').find_all('b'))):
                url = "https://nptel.ac.in"+instance.get('href')
                links.extend(tuple((url, url.split('subjectName=')[1])))
        for index in range(0, len(links)+1, 2):
            print("Downloading Lecture number :"+str(int((index/2)+1)))
            save_file(links[index], str(links[index+1]).replace(' ', '_'))
            
    elif(choice is 2):
        print("Checking for availability of 3GP videos.")
        for instance in soup.find_all('a'):
            if("3GP Download" in str(BeautifulSoup(str(instance), 'html.parser').find_all('b'))):
                url = "https://nptel.ac.in"+instance.get('href')
                links.extend(tuple((url, url.split('subjectName=')[1])))
        for index in range(0, len(links)+1, 2):
            print("Downloading Lecture number :"+str(int((index/2)+1)))
            save_file(links[index], str(links[index+1]).replace(' ', '_'))
    elif(choice is 3):
        print("Checking for availability of FLV videos.")
        for instance in soup.find_all('a'):
            if("FLV Download" in str(BeautifulSoup(str(instance), 'html.parser').find_all('b'))):
                url = "https://nptel.ac.in"+instance.get('href')
                links.extend(tuple((url, url.split('subjectName=')[1])))
        for index in range(0, len(links)+1, 2):
            print("Downloading Lecture number :"+str(int((index/2)+1)))
            save_file(links[index], str(links[index+1]).replace(' ', '_'))
        

        
            
