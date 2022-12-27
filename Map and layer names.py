#Rename map and layers by numerical list
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

#Rename map or layers and quantify their numbers

import arcpy.mapping as c
myMxd=c.MapDocument(r'C:\Data\Results\UUEE_2.mxd')
maps=c.ListDataFrames(myMxd)
countMap=0
for item in maps:
    layers=c.ListLayers(myMxd, "", item)
    countMap+=1
    for lyr in layers:
        tot=len(layers)
print "The map ", countMap, "has ", len(layers), "maps."
name=raw_input("What do you like to rename, map or layer? ")
if name=="map":
    number=int(input("Which map do you want to rename? "))
    newName=raw_input("Enter the new name: ")
    if number<=len(maps):
        item=maps[number-1]
        item.name=newName
    else:
        print "Insert a number between 1 and ", len(maps)
if name=="layer":
    number=int(input("Which layer do you want to rename? "))
    newName=raw_input("Enter the new name: ")
    layers=c.ListLayers(myMxd)
    for lyr in layers:
        if number<=len(layers):
            lyr=layers[number-1]
            lyr.name=newName
        else:
            print "Insert a number between 1 and ", len(layers)
    
myMxd.save()
del myMxd   
print "Done"

#Capitalize layer names

import arcpy.mapping as c
myMxd=c.MapDocument(r'C:\Data\Results\UUEE_2.mxd')
map=myMxd.activeDataFrame

layers=c.ListLayers(myMxd,"",map)
for lyr in layers:
    lyr.name=lyr.name.upper() #or .lower for lower case
myMxd.save()
del myMxd
print "Done"
