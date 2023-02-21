import csv
with open('department.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("ID Department Name")
 print("---------------------------------")
 for column in data:
   print(column['department_id'], column['department_name'])
