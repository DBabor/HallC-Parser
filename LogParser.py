"""
Contributors:
Dillon Babor - CCI Intern Mentored by Alexandre Camsonne

Created:
July 6th, 2023

Last Updated:
July 7th, 2023

Purpose:
This program is supposed to pull specific log data from JLab and upload it to the RCDB script
"""
import regex as re

def main():
    
    # dn was the data we decided to use
    dn = ["ecSHMS_Angle", "ecpSHMS_SHMS", "HALLA:p", "HALLC:p"]
    # just sets selecteddata to a list
    sd = []
    
    # set the open log.txt as opf (open file) and sets f to readlines 
    with open('log.txt', 'r') as opf:
        f = opf.readlines()
            
    # for each line in f, and phrase in dn (data needed) with the phrase in line, append the line to sd (selected data)
    # basically search for the dn (data needed) phrases and put them in the sd (selected data) list
    for line in f:
        for phrase in dn:
            if phrase in line:
                sd.append(line)

    # split line using regex by 2 spaces
    re.split(r"\s2", line)
    # I'm sure thats a really dirty way of doing it, but it works
    # Choose the data you want    
    # # The number is dependant on which part of the list it appears in. For this example, it would be 0=HALLA:p 1=HALLC:p 2=ecSHMS_Angle, 3=Error because ecpSHMS_SHMS is null
    choice = int(input("0=HALLA:p 1=HALLC:p 2=ecSHMS_Angle: "))
    sd = sd[choice].split()
    # 0=Config 1=Beam(?) 2=Comments
    # This section will be where we set it to upload the data, currently have the three columns in their seperate sections
    print(sd[0])
    print(sd[1])
    print(sd[2])
    
main()