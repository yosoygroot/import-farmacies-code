import csv

with open('/home3/jaume/Equipaments_de_Catalunya.csv') as csvfile:
    with open('/home3/jaume/farmacies-2020-03-14.csv', 'w') as csvout:
        equipaments = csv.reader(csvfile, delimiter=',')
        out = csv.writer(csvout, delimiter=',')
        i = 0
        for row in equipaments:
            if row[3].startswith('Salut|Farm') or i == 0:
                out.writerow(row)
            i += 1
