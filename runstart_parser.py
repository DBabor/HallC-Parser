"""
Contributors:
Dillon Babor - CCI Intern Mentored by Alexandre Camsonne

Created:
July 6th, 2023

Last Updated:
July 24th, 2023

Purpose:
This program is supposed to pull specific start of run log data from JLab and upload it to the RCDB script
"""
import regex as re

def main():
    
    # Mainly placeholder data, really easy to add more to pull
    dn = ["hac_bcm_average", "haD2_P_Fill_Target_R", "HALLA:p"]
    # just sets selecteddata to a list
    sd = []
    
    # set the open log.txt as opf (open file) and sets f to readlines 
    with open('runstart_data.txt', 'r') as opf:
        f = opf.readlines()
    
    # for each line in f, and phrase in dn (data needed) with the phrase in line, append the line to sd (selected data)
    # basically search for the dn (data needed) phrases and put them in the sd (selected data) list
    for line in f:
        for phrase in dn:
            if phrase in line:
                sd.append(line)
                
    # split line using regex by 2 spaces
    re.split(r"\s2", line)
    
    nf = open("testStart.txt", "a")
    
    # Seperates the strings, so you have run number and current together
    for x in range(len(sd)):
        thing = sd[x].split()
        
        # More can be added more if needed, these are the run configuration, data, and then comments.
        # Prints out the first item in the list
        nf.write(f"{thing[0]}   ")
        # Prints out the second item in the list
        nf.write(f"{thing[1]}   ")
        # gives the option to input a comment
        comment = input(f"If you want to enter a comment for ({thing[0]})\nYou can do so here. If nothing to add, press enter: ")
        nf.write(f"{comment}\n")
    
    nf.close()

main()