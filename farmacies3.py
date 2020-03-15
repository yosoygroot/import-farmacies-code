import csv
import glob
import os

in_files = glob.glob('/home3/jaume/farmacies/*.csv')
for in_file in in_files:
    name = os.path.basename(in_file).split('.')[0]
    in_fd = open(in_file)
    in_csv = csv.reader(in_fd, delimiter=',')
    out_fd = open('/home3/jaume/farmacies-josm/' + name + '.osm', 'w')
    out_fd.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    out_fd.writelines("<osm version='0.6' generator='Farmacies CODIV-19'>\n")
    i = -1
    for farmacia in in_csv:
        out_fd.writelines("\t<node id='" + str(i) + "' visible='true' lat='" + farmacia[17] + "' lon='" + farmacia[16] + "'>\n")
        out_fd.writelines("\t\t<tag k='amenity' v='pharmacy' />\n")
        if farmacia[0].strip() != '':
            out_fd.writelines("\t\t<tag k='ref' v='" + farmacia[0] + "' />\n")
        if farmacia[2].strip() != '':
            out_fd.writelines("\t\t<tag k='name' v=\"" + farmacia[2] + "\" />\n")
        txt = farmacia[5].strip().split(',')
        error = False
        if len(txt) > 0:
            if txt[0].split(' ')[0] == 'CR':
                via = 'carrer '
                via = via + txt[0].lower()[3:].title()
            elif txt[0].split(' ')[0] == 'CT':
                via = 'carretera '
                via = via + txt[0].lower()[3:].title()
            elif txt[0].split(' ')[0] == 'AV':
                via = 'avinguda '
                via = via + txt[0].lower()[3:].title()
            elif txt[0].split(' ')[0] == 'RB':
                via = 'rambla '
                via = via + txt[0].lower()[3:].title()
            elif txt[0].split(' ')[0] == 'RD':
                via = 'ronda '
                via = via + txt[0].lower()[3:].title()
            elif txt[0].split(' ')[0] == 'PG':
                via = 'passeig '
                via = via + txt[0].lower()[3:].title()
            elif txt[0].split(' ')[0] == 'PS':
                via = 'passatge '
                via = via + txt[0].lower()[3:].title()
            elif txt[0].split(' ')[0] == 'PL':
                via = 'plaça  '
                via = via + txt[0].lower()[3:].title()
            elif txt[0].split(' ')[0] == 'RV':
                via = 'raval '
                via = via + txt[0].lower()[3:].title()
            elif txt[0].split(' ')[0] == 'RI':
                via = 'riera '
                via = via + txt[0].lower()[3:].title()
            else:
                error = True
        if len(txt) > 1:
            try:
                num = str(int(txt[1]))
            except ValueError:
                num = txt[1]
        mes = ''
        if len(txt) > 2:
            mes = ', ' + txt[2].lower()
        if error:
            via = farmacia[5].lower()
        else:
            via = via + ', ' + num + mes
        if via.strip() != '':
            out_fd.writelines("\t\t<tag k='addr:full' v=\"" + via + "\" />\n")
            out_fd.writelines("\t\t<tag k='addr:street' v=\"" + via.split(',')[0] + "\" />\n")
            out_fd.writelines("\t\t<tag k='addr:housenumber' v=\"" + num + "\" />\n")
        if farmacia[8].strip() != '':
            out_fd.writelines("\t\t<tag k='addr:postcode' v='" + farmacia[8] + "' />\n")
        if farmacia[9].strip() != '':
            out_fd.writelines("\t\t<tag k='addr:city' v=\"" + farmacia[9] + "\" />\n")
        if farmacia[11].strip() != '':
            out_fd.writelines("\t\t<tag k='contact:phone' v='+34" + farmacia[11] + "' />\n")
        if farmacia[13].strip() != '':
            out_fd.writelines("\t\t<tag k='contact:fax' v='+34" + farmacia[13] + "' />\n")
        if farmacia[18].strip() != '':
            out_fd.writelines("\t\t<tag k='contact:email' v='" + farmacia[18] + "' />\n")
        if farmacia[19].strip() != '':
            out_fd.writelines("\t\t<tag k='contact:web' v='" + farmacia[19] + "' />\n")
        if farmacia[20].strip() != '':
            out_fd.writelines("\t\t<tag k='source:date' v='" + farmacia[20] + "' />\n")
        out_fd.writelines("\t\t<tag k='dispensing' v='yes' />\n")
        out_fd.writelines("\t\t<tag k='source' v='Generalitat de Catalunya' />\n")
        out_fd.writelines("\t</node>\n")
        i -= 1
    out_fd.writelines("</osm>\n")
