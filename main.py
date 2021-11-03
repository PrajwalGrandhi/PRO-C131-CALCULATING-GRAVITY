import csv

data=[]
file=open("final.csv")
csvreader=csv.reader(file)

for row in csvreader:
    data.append(row)

headers=data[0]
star_data=data[1:]

star_masses=[]
star_radiuses=[]

for data in star_data:
    mass=float(data[4])*1.989e+30
    radius=float(data[5])*6.957e+8
    star_masses.append(mass)
    star_radiuses.append(radius)
    

star_gravity=[]
for ind,data in enumerate(star_masses):
    gravity=(float(star_masses[ind])*5.972e+24)/(float(star_radiuses[ind])*float(star_radiuses[ind])*6371000*6371000)*6.674e-11
    star_gravity.append(gravity)

headers.append("star_gravity")
#final_data=star_data+star_gravity
print(star_gravity)
final_data=[]
for ind,data_row in enumerate(star_data):
    final_data.append(star_data[ind]+star_gravity[ind])

with open("real-final.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(final_data)