#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

people = 0
poiCount = 0
salaryCount = 0
emailAddressCount = 0
totalPaymentsCount = 0
poiTotalPaymentsCount = 0

for person in enron_data:
    people = people + 1
    if enron_data[person]['poi'] == 1:
        poiCount += 1
        if enron_data[person]['total_payments'] != 'NaN':
            poiTotalPaymentsCount += 1
    if enron_data[person]['salary'] != 'NaN':
        salaryCount += 1
    if enron_data[person]['email_address'] != 'NaN':
        emailAddressCount += 1
    if enron_data[person]['total_payments'] != 'NaN':
        totalPaymentsCount += 1

print "Enron data poi count:",poiCount

poiFile = open("../final_project/poi_names.txt")
poiCount2 = 0
lines = poiFile.readlines() 
for line in lines:
    if line[0] == '(':
        poiCount2 += 1
print "Total POIs:",poiCount2

print "people:", people
print "salaries:", salaryCount
print "email addresses:", emailAddressCount
print "total payments count:", totalPaymentsCount
print "POI total payments count:", poiTotalPaymentsCount

print "percent people without total payments:", float(people - totalPaymentsCount)/float(people)
print "percent POIs without total payments:", float(poiCount - poiTotalPaymentsCount)/float(poiCount)