import arcpy.mapping as c
myMxd=c.MapDocument(r'C:\Data\UUEE.mxd')
maps=c.ListDataFrames(myMxd)
for item in maps:
    myMxd.activeView=item.name
    myMxd.title=item.name
    myMxd.saveACopy(r'C:\Data\Results'+item.name+'.mxd')
del myMxd
print "Done"
