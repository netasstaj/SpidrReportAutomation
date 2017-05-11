import json
import os
import sys
import time
from subprocess import call
from operator import itemgetter, attrgetter
import datetime

################################################################################
################################################################################

#This function works to fill languages

def fillLanguage(arrOfJson,decoded):

    count = 0;

    for item in decoded:
            arrOfJson[count][0] = item
            count = count + 1;
    return

################################################################################
################################################################################

#This function works to fill languages
#Returns what is number of different language in the json

def findNumberOfLanguage(decoded):

    count = 0;

    for item in decoded:
        if item!="header":
            count = count + 1;
    return count

################################################################################
################################################################################

#This function works to found language where it is return index

def findIndex(arrOfJson,item,numberOfLanguage):

    count=0;

    for num in range(0,numberOfLanguage):
        if arrOfJson[num][count] == item:
            return num
        else:   
            num = num + 1

################################################################################
################################################################################

#This function works to print all arrOfJson on terminal

def displayAllarrOfJson(arrOfJson,numberOfLanguage):

    for i in range(numberOfLanguage):
        for j in range(1):
            print arrOfJson[i]
    
################################################################################
################################################################################

#This function works to delete garbage and old files

def removeBeforFiles(fileName):
    os.remove(fileName)
 
################################################################################
################################################################################

#This function works to write edited json to true package file report

def writeEditedJson(arrFileNames,arrJson):

    for i in range(len(arrFileNames)):
        file = open(arrFileNames[i], 'w+')
        file.write(arrJson[i])
    
################################################################################
################################################################################

#This function works to write edited json to true package file report
#Return formed txt names's list

def createMakeFile(dir1,dir2):

    arrDir1Paths=[]
    arrDir2Paths=[]
    reportTxtName=[]
    reportTxtName2=[]

    
    newPath=dir1+"/wae --exclude-dir=mtaf --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)'";
    arrDir1Paths.append(newPath)
    reportTxtName.append("total.txt")
    newPath=dir1+"/wae --exclude-dir=media,platform,mtaf --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)'";
    arrDir1Paths.append(newPath)
    reportTxtName.append("womediaandplatform.txt")
    newPath=dir1+"/wae/platform --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)'";
    arrDir1Paths.append(newPath)
    reportTxtName.append("platform.txt")
    newPath=dir1+"/wae/media --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)' ";
    arrDir1Paths.append(newPath)
    reportTxtName.append("media.txt")
    newPath=dir1+"/wae/media/webrtcAdapt --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)'";
    arrDir1Paths.append(newPath)
    reportTxtName.append("broker.txt")
    newPath=dir1+"/wae/media --exclude-dir=webrtcAdapt --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)' ";
    arrDir1Paths.append(newPath)
    reportTxtName.append("mediawobroker.txt")


    newPath=dir2+"/wae --exclude-dir=mtaf --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)'";
    arrDir2Paths.append(newPath)
    reportTxtName2.append("totaldest.txt")
    newPath=dir2+"/wae --exclude-dir=media,platform,mtaf --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)'";
    arrDir2Paths.append(newPath)
    reportTxtName2.append("womediaandplatformdest.txt")
    newPath=dir2+"/wae/platform --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)'";
    arrDir2Paths.append(newPath)
    reportTxtName2.append("platformdest.txt")
    newPath=dir2+"/wae/media --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)' ";
    arrDir2Paths.append(newPath)
    reportTxtName2.append("mediadest.txt")
    newPath=dir2+"/wae/media/webrtcAdapt --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)'";
    arrDir2Paths.append(newPath)
    reportTxtName2.append("brokerdest.txt")
    newPath=dir2+"/wae/media --exclude-dir=webrtcAdapt --skip-archive='(war|ear|jar|zip|tar(.(gz|Z|bz2|xz|7z))?)' ";
    arrDir2Paths.append(newPath)
    reportTxtName2.append("mediawobrokerdest.txt")

    makeFile = open("makefile","wb")

    makeFile.write("all:\n")

    for i in range(len(arrDir1Paths)):
         makeFile.write("\t./cloc-1.72.pl %s --out=%s --json\n" %(arrDir1Paths[i],reportTxtName[i]))

    for i in range(len(arrDir2Paths)):
         makeFile.write("\t./cloc-1.72.pl %s --out=%s --json\n" %(arrDir2Paths[i],reportTxtName2[i]))

    makeFile.close();


    for i in reportTxtName2:
        reportTxtName.append(i)

    return reportTxtName

################################################################################
################################################################################

#This function works to write all arrOfJson to file jsonFormat
#tek dil olma sorunu var

def writeToFileInformation(arrOfJson,numberOfLanguage,fileName):

    theFile = open(fileName, "wb")
    dQ=chr(34)

    arrOfJson.sort(key=lambda x: x[5])

    theFile.write("{%sheader%s:{%sreport_file%s:%s%s%s}," %(dQ,dQ,dQ,dQ,dQ,arrOfJson[0][0],dQ))

    for i in range(numberOfLanguage):
        if i==0:
            theFile.write("%s%s%s:{%snFiles%s:%s%d%s,%sblank%s:%s%d%s,%scomment%s:%s%d%s,%scode%s:%s%d%s}," %(dQ,arrOfJson[i][1],dQ,dQ,dQ,dQ,arrOfJson[i][2],dQ,dQ,dQ,dQ,arrOfJson[i][3],dQ,dQ,dQ,dQ,arrOfJson[i][4],dQ,dQ,dQ,dQ,arrOfJson[i][5],dQ))
        elif i==numberOfLanguage-1:
            theFile.write("%s%s%s:{%snFiles%s:%s%d%s,%sblank%s:%s%d%s,%scomment%s:%s%d%s,%scode%s:%s%d%s}}" %(dQ,arrOfJson[i][1],dQ,dQ,dQ,dQ,arrOfJson[i][2],dQ,dQ,dQ,dQ,arrOfJson[i][3],dQ,dQ,dQ,dQ,arrOfJson[i][4],dQ,dQ,dQ,dQ,arrOfJson[i][5],dQ))
        else:
            theFile.write("%s%s%s:{%snFiles%s:%s%d%s,%sblank%s:%s%d%s,%scomment%s:%s%d%s,%scode%s:%s%d%s}," %(dQ,arrOfJson[i][1],dQ,dQ,dQ,dQ,arrOfJson[i][2],dQ,dQ,dQ,dQ,arrOfJson[i][3],dQ,dQ,dQ,dQ,arrOfJson[i][4],dQ,dQ,dQ,dQ,arrOfJson[i][5],dQ))

    theFile.close();

################################################################################
################################################################################

#This function works to clean up created json files from cloc program   

def bubble(badList,numberOfLanguage):
    
    length = numberOfLanguage - 1
    unsorted = True

    while unsorted:
        for element in range(0,length):
            unsorted = False
            if badList[element] > badList[element + 1]:
                hold = badList[element + 1]
                badList[element + 1] = badList[element]
                badList[element] = hold
                print badList
            else:
                unsorted = True

    print bubble(mylist)

def clearInFile(iterPackageName):
     
    arrJson=[]
    arrFileNames=[]

    count=0
    json=""
    a=""

    #print iterPackageName

    file = open(iterPackageName,"r") 
    allLines=file.readlines() 

    for i in allLines:

        count=count+1

        if (count>1 and count<9):
            count=count
        else:
            arr = i.replace(" ","")
            json = json + arr.rstrip('\n')

    file.close()  
    file = open(iterPackageName,"w")  
    file.write(json)
    file.close()   


################################################################################
################################################################################

def forDiffChart (arrDiff,arrDest,count):
    flag=0

    arrCurrent=[[0 for x in range(len(arrDiff[0]))] for y in range(count)] 
    
    for x in range(0,count):
        for z in range(0,len(arrDiff)):
            if str(arrDest[x][1])==(arrDiff[z][1]):
                if str(arrDiff[z][0])==str(arrDiff[0][0]):
                    for y in range(2,len(arrDiff[0])):
                        arrCurrent[x][y]=int(arrDest[x][y])-int(arrDiff[z][y])

                    flag=1

        if flag==0:
            for y in range(2,len(arrDiff[0])):
                arrCurrent[x][y]=int(arrDest[x][y])

        flag=0

    for x in range(0,count):
        for y in range(1,2):  
            arrCurrent[x][y]=arrDest[x][y] 
    
    newName=arrDiff[0][0]
 
    for x in range(0,count):
        for y in range(0,1): 
            arrCurrent[x][y]=newName   


    #for i in arrCurrent:
       # print i

    #print''
    #print''

    writeToFileInformation(arrCurrent,count,arrCurrent[0][0])


################################################################################    
################################################################################

def writeToTotalInfirmation(arrOfJson,numberOfLanguage,fileName):

    theFile = open(fileName, "wb")
    dQ=chr(34)

    #print numberOfLanguage

    theFile.write("{%sheader%s:{%sreport_file%s:%s%s%s}," %(dQ,dQ,dQ,dQ,dQ,fileName,dQ))

    for i in range(numberOfLanguage):

        newName=arrOfJson[i][0]
        newName=newName[:-8]

        if i==0:
            theFile.write("%s%s%s:{%snFiles%s:%s%d%s,%sblank%s:%s%d%s,%scomment%s:%s%d%s,%scode%s:%s%d%s}," %(dQ,newName,dQ,dQ,dQ,dQ,arrOfJson[i][2],dQ,dQ,dQ,dQ,arrOfJson[i][3],dQ,dQ,dQ,dQ,arrOfJson[i][4],dQ,dQ,dQ,dQ,arrOfJson[i][5],dQ))
        elif i==numberOfLanguage-1:
            theFile.write("%s%s%s:{%snFiles%s:%s%d%s,%sblank%s:%s%d%s,%scomment%s:%s%d%s,%scode%s:%s%d%s}}" %(dQ,newName,dQ,dQ,dQ,dQ,arrOfJson[i][2],dQ,dQ,dQ,dQ,arrOfJson[i][3],dQ,dQ,dQ,dQ,arrOfJson[i][4],dQ,dQ,dQ,dQ,arrOfJson[i][5],dQ))
        else:
            theFile.write("%s%s%s:{%snFiles%s:%s%d%s,%sblank%s:%s%d%s,%scomment%s:%s%d%s,%scode%s:%s%d%s}," %(dQ,newName,dQ,dQ,dQ,dQ,arrOfJson[i][2],dQ,dQ,dQ,dQ,arrOfJson[i][3],dQ,dQ,dQ,dQ,arrOfJson[i][4],dQ,dQ,dQ,dQ,arrOfJson[i][5],dQ))

    theFile.close();

################################################################################    
################################################################################

# All Process

try:

    reportTxtNames=createMakeFile(sys.argv[1],sys.argv[2])
    call(["make"])

    numberOfLanguage=0
    lastArrForJson=[[]]
    inPackInfoNumber=[]
    jsonWriteArray=[]
    jsonBound=[]

    for iterPackageName in reportTxtNames:
        
        clearInFile(iterPackageName)
        file = open(iterPackageName,"r")
        decoded = json.loads(file.read())

        #print decoded #print '' #print ''

        numberOfLanguage=numberOfLanguage+findNumberOfLanguage(decoded)

        #print numberOfLanguage

        jsonBound.append(numberOfLanguage)

        weight = 6
        height = numberOfLanguage
        index=0
        allCount=0
        destStart=0
        status2=1
        elmentCount=-1

        arrOfJson = [[0 for x in range(weight)] for y in range(height)] 

    for iterPackageName in reportTxtNames:

        clearInFile(iterPackageName)
        file = open(iterPackageName,"r")
        decoded = json.loads(file.read())           
        count=-1

        status=iterPackageName.find("dest")
        if status!=-1 and status2==1:
            status2=0

        for item in decoded:
            count=count+1
            
            if item!="header":
               arrOfJson[index][1]=item
               arrOfJson[index][0]=iterPackageName
               index=index+1    
               if status2!=0:
                   allCount=allCount+1  

            for item2 in decoded[item]:
                index=index-1
                if item2 == "nFiles":
                    arrOfJson[index][2]=decoded[item][item2]
                elif item2 == "blank":
                    arrOfJson[index][3]=decoded[item][item2]
                elif item2 == "comment":
                    arrOfJson[index][4]=decoded[item][item2]
                elif item2 == "code":
                    arrOfJson[index][5]=decoded[item][item2]
                index=index+1
            elmentCount=elmentCount+1    

        status=iterPackageName.find("dest")

        jsonBound.append(elmentCount)

        if status!=-1 :
            inPackInfoNumber.append(count)        
        #print count 

#########################################################################

    arrSum=[]
    count=0     
    size=0
    listOfListJson=[]
    listJson=[]  
    countSum=0

    bound=int(jsonBound[size])

    for i in arrOfJson:

        #print i

        listJson.append(i)
        count=count+1

        if(count==bound):
            size=size+1
            bound=int(jsonBound[size])
            #print ''
            #print ''

            listOfListJson.append(listJson)
            listJson=[]

############################################################################

    halfIndex=len(listOfListJson)/2
    listOfPre=[]
    preCount=0

    for listOfLast in listOfListJson[halfIndex:]:
        listOfPre=listOfListJson[preCount]
        preCount=preCount+1

        sizeLast=len(listOfLast)
        forDiffChart(listOfPre,listOfLast,sizeLast)

        writeToFileInformation(listOfLast,sizeLast,listOfLast[0][0])

        firstRead=open(listOfLast[0][0],"r")
        allLiness=firstRead.read()

        secondRead=open(listOfPre[0][0],"r")
        allLiness2=secondRead.read()

        JsonRow="myObj = " + allLiness
        JsonRow2="myObj = " + allLiness2

        jsonWriteArray.append(JsonRow)
        jsonWriteArray.append(JsonRow2)

        os.remove(listOfPre[0][0])
        os.remove(listOfLast[0][0])

        for i in listOfLast:
            if i[1]=="SUM":
                arrSum.append(i)
                countSum=countSum+1

        firstRead.close()
        secondRead.close()

############################################################################

    sampleRead=open("Reports/Patterns/index.html","r") 
    allLines=sampleRead.readlines()
    sampleRead.close()

    count=0

    an = datetime.datetime.today()
    dateStringName=""
    dateStringName= "Reports/" + str(an.day) + "." + str(an.month) + "." + str(an.year) + "-Report" + ".html"

    f=open(dateStringName,"w")

    for k in allLines:
        count=count+1
        if count==226:   
            f.write(jsonWriteArray[0])
        elif count==343:
            f.write(jsonWriteArray[1])
        elif count==457:
            f.write(jsonWriteArray[2])
        elif count==570:
            f.write(jsonWriteArray[3])
        elif count==683:    
            f.write(jsonWriteArray[4])
        elif count==796:
            f.write(jsonWriteArray[5])
        elif count==910:
            f.write(jsonWriteArray[6])
        elif count==1023:
            f.write(jsonWriteArray[7])
        elif count==1137:
            f.write(jsonWriteArray[8])
        elif count==1249:    
            f.write(jsonWriteArray[9])
        elif count==1361:
            f.write(jsonWriteArray[10])
        elif count==1474:    
            f.write(jsonWriteArray[11])    
        else:
            f.write(k)

    f.close()

################################################################################
################################################################################

except (ValueError):
    print "JSON format error"

################################################################################
################################################################################
