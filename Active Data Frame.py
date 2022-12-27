import arcpy.mapping as c
myMxd=c.MapDocument(r'C:\Data\UUEE.mxd')
maps=c.ListDataFrames(myMxd)
for item in maps:
    myMxd.activeView=item.name
    myMxd.title=item.name
    myMxd.saveACopy(r'C:\Data\Results'+item.name+'.mxd')
del myMxd
print "Done"

#For naming all visible layers

import arcpy.mapping as c
myMxd=c.MapDocument(r'C:\Data\Results\UUEE_2.mxd')
layers=c.ListLayers(myMxd)
for item in layers:
    if item.visible:
        print item.name
print "Done"

#To change visibility of layers

import arcpy.mapping as c
myMxd=c.MapDocument(r'C:\Data\Results\UUEE_2.mxd')
layers=c.ListLayers(myMxd)
for item in layers:
    if item.visible:
        item.visible=False
    else:
        item.visible=True
        print item.name
myMxd.save()
print "Done"
