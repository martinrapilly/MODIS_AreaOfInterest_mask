# -*- coding: windows-1258 -*-
##MODIS_AreaOfInterest_Mask script
##Author: Martin Rapilly
##Applies a mask of the area of Interest (polygon) on a list of MODIS images

import time
try:
##keeping track of start time
    import datetime  
    inicio = datetime.datetime.now()  
    print 'start time: ' + str(inicio) +'\n'
    time1 = time.clock()
    time.sleep(1)

##loading libraries arcpy and spatial analyst extension
    print "loading libraries"
    import sys, unicodedata 
    import arcpy, os
    import arcpy.mapping as mapping
    from arcpy.sa import *
    arcpy.CheckOutExtension("Spatial")
    print "Libraries loaded\n"
 
   
#Folder path to MODIS images
    RutaEntrada="F:/.../MODIS IMAGES FOLDER"
#defines workspace
    arcpy.env.workspace = RutaEntrada

    
#creates raster list to apply mask on
    Rasters = arcpy.ListRasters("*", "TIF")
    print "raster list done"
    print Rasters
    
#Snap to first raster to use exact same grid on all outputs
    tile = Rasters[0]
    arcpy.env.snapRaster = tile

#for loop to check if output raster already exists; if not, apply Extract by mask function on one image   
    for r in Rasters:
        if os.path.exists ("F:/.../"+ r + ".tif"):
            print "file already exists: "+"Mask_"+ r + ".tif"
        else:
            outExtractByMask = ExtractByMask(r,"F:/.../SHP_POLYGON.shp")
            outExtractByMask.save("F:/.../OUTPUTFOLDER/"+"Mask_"+ r + ".tif")
            print "mask with polygon done on image: "+r
     
##print end time   
    time2 = time.clock()
    final=datetime.datetime.now()
    print "Processing done at " + str(final)+ ' in '+ str((time2-time1)/3600) + " hours" 
  
except Exception,e: print str(e)
