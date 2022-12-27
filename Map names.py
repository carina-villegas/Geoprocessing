import arcpy.mapping as c
myMxd=c.MapDocument(r'C:\Data\UUEE.mxd')
maps=c.ListDataFrames(myMxd)
count=1
for item in maps:
    item.name=str(count)+"."+item.name
    n=1
    layers=c.ListLayers(myMxd, "", item)
    for lyr in layers:
        lyr.name=str(count)+"."+str(n)+"_"+lyr.name
        n=n+1
    count=count+1
  
myMxd.saveACopy(r'C:\Data\UUEE_2.mxd')
print "DONE"

