from qgis.core import QgsGeometry
from qgis.core import QgsFeature
from qgis.core import QgsPointXY
from qgis.core import QgsSpatialIndex
from qgis.core import QgsFeatureRequest

import csv
from qgis.utils import iface

layer = iface.activeLayer()
iter = layer.getFeatures()
grid = [f for f in iter]
groups = dict()
file = open('/home3/jaume/farmacies-2020-03-14.csv')
farmacies = csv.reader(file, delimiter=',')
i = 0

index = QgsSpatialIndex()
for feat in grid:
    index.addFeature(feat)
    groups[feat.id()] = list()

for farmacia in farmacies:
    if i > 0:
        punt = QgsGeometry.fromPointXY(QgsPointXY(float(farmacia[16]), float(farmacia[17])))
        intersects = index.intersects(punt.boundingBox())
        if len(intersects) > 0:
            request = QgsFeatureRequest()
            request.setFilterFids(intersects)
            feats = [f for f in layer.getFeatures(request)]
            found = False
            for feat in feats:
                if punt.intersects(feat.geometry()):
                    groups[feat.id()].append(farmacia)
                    found = True
            if not found:
                print('Error')
        else:
            print('Error')
        
    if i % 100 == 0:
        print(i)
    i += 1
    
for k, v in groups.items():
    if len(v) > 0:
        file = open('/home3/jaume/farmacies/' + str(k) + '.csv', 'w')
        out = csv.writer(file, delimiter=',')
        for f in v:
            out.writerow(f)
