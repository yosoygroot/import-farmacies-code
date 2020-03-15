import csv
from opencage.geocoder import OpenCageGeocode

key = '...'
geocoder = OpenCageGeocode(key)

with open('/home3/jaume/Farmacies5.csv') as csvfile:
    with open('/home3/jaume/FarmaciesGC.csv', 'w') as csvout:
        equipaments = csv.reader(csvfile, delimiter=',')
        out = csv.writer(csvout, delimiter=',')
        i = 0
        for row in equipaments:
            if row[3].startswith('Salut|Farm') or i == 0:
                query = row[1] + ' ' + row[3] + ', ' + row[5] + ' ' + row[4] + ', Catalunya, Spain'
                query = query.replace("''", '**')
                query = query.replace("'", '')
                query = query.replace("**", "'")
                print(query)
                results = geocoder.geocode(query)
                row[9] = results[0]['geometry']['lat']
                row[8] = results[0]['geometry']['lng']
            out.writerow(row)
