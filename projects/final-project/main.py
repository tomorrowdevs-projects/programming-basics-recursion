#--DICTIONARIES INITIALIZATION--#
roomIdDict={}   #{roomId:roomName}
objIdDict={}    #{objId:{name:objName,place:objPlace,container:True/False}}

def printIdDict(idDict,idList=None):
    #--OBTAINING PADDING VALUES--#
    maxIdLen=0
    maxNameLen=0
    if idList==None:
        idList=list(idDict.keys())
    else:
        idList.sort()

    if len(idList)>0:
        for key in idList:
            if len(key)>maxIdLen:
                maxIdLen=len(key)
            
            if 'R' in key:
                value=idDict[key]
                if len(value)>maxNameLen:
                    maxNameLen=len(value)
            else:
                value=idDict[key]['name']
                if len(value)>maxNameLen:
                    maxNameLen=len(value)
            
        #--BUILDING STRING TO BE PRINTED--#
        strToPrint=''
        for id in idList:
            if 'R' in id:
                name=idDict[id]
                strToPrint='ID: {:>'+str(maxIdLen)+'} - NAME: {:>'+str(maxNameLen)+'}\n'
                print(strToPrint.format(id,name))
            else:
                name=idDict[id]['name']
                if objIdDict[id]['container']:
                    container='yes'
                else:
                    container='no'
                strToPrint='ID: {:>'+str(maxIdLen)+'} - NAME: {:>'+str(maxNameLen)+'} - CONTAINER: {:>3}\n'
                print(strToPrint.format(id,name,container))
    else:
        if len(idDict)==0:
            print('No object has been defined yet!')
        else:
            print('The room or the object is empty!')
        
def dictContent(id,subObjResearch=False,keyList=None,contentList=None,containerList=None,passedIdList=None):
    if contentList==None:
        contentList=[]
        keyList=list(objIdDict.keys())
        containerList=[]

    if passedIdList==None:
        passedIdList=[]

    if len(keyList)>0:
        currentKey=keyList.pop(0)
        keyList.append(currentKey)
        if not currentKey in passedIdList:
            passedIdList.append(currentKey)
            if objIdDict[currentKey]['place']==id:
                contentList.append(currentKey)
                if subObjResearch and objIdDict[currentKey]['container']:
                    containerList.append(currentKey)     
            return dictContent(id,subObjResearch,keyList,contentList,containerList,passedIdList)
        else:
            if len(containerList)>0:
                currentContainer=containerList.pop(0)
                return dictContent(currentContainer,subObjResearch,keyList,contentList,containerList,passedIdList=None)
            else:
                return contentList
    else:
        return contentList

def explore(placeId=None):
    if placeId==None:
        print("""Here's the list of the rooms ids:""")
        printIdDict(roomIdDict)
        print("""Here's the list of the objects ids:""")
        printIdDict(objIdDict)
        placeId=input("""Enter the id of the object or the room that you want to explore: """)
        while not (placeId in roomIdDict or placeId in objIdDict):
            placeId=input("""Wrong input, retry: """)

    if (not 'R' in placeId and objIdDict[placeId]['container']) or 'R' in placeId:
        contentList=dictContent(placeId)
        if len(contentList)>0:
            print("""Here's the content of the selected room/object: """)
            printIdDict(objIdDict,contentList)
            if 'R' in placeId:
                operation=input('What do you want to do?\n- choose another room or object [1]\n- go to main menu [2]\n- choose one of these objects [3]')
                while not operation in ['1','2','3']:
                    operation=input('Wrong input, retry: ')
            else:
                operation=input('What do you want to do?\n- choose another room or object [1]\n- go to main menu [2]\n- choose one of these objects [3]\n- go to the upper level [4]')
                while not operation in ['1','2','3','4']:
                    operation=input('Wrong input, retry: ')
            
            if operation=='1':
                explore()
            elif operation=='2':
                pass
            elif operation=='3':
                placeId=input('Choose one of the previous ids: ')
                while not placeId in contentList:
                    placeId=input('Wrong input, retry: ')
                explore(placeId)
            else:
                placeId=objIdDict[placeId]['place']
                explore(placeId)
        else:
            print("""The room or the object is empty!""")
            if 'R' in placeId:
                operation=input('What do you want to do?\n- choose another room or object [1]\n- go to main menu [2]')
                while not operation in ['1','2']:
                    operation=input('Wrong input, retry: ')
            else:
                operation=input('What do you want to do?\n- choose another room or object [1]\n- go to main menu [2]\n- go to the upper level [3]')
                while not operation in ['1','2','3']:
                    operation=input('Wrong input, retry: ')
            
            if operation=='1':
                explore()
            elif operation=='2':
                pass
            else:
                placeId=objIdDict[placeId]['place']
                explore(placeId)
    else:
        print("""The object can contain nothing!""")
        operation=input('What do you want to do?\n- choose another room or object [1]\n- go to main menu [2]\n- go to the upper level [3]')
        while not operation in ['1','2','3']:
            operation=input('Wrong input, retry: ')
        
        if operation=='1':
            explore()
        elif operation=='2':
            pass
        else:
            placeId=objIdDict[placeId]['place']
            explore(placeId)

def addRoom():
    roomName=input('Please, enter the name of the room to be added: ')
    while roomName in list(roomIdDict.values()):
        roomName=input('Name already used, retry: ')

    #SAVING ROOM INFO TO THE HOUSE DIC                
    if len(roomIdDict)==0:
        roomIdDict['R1']=roomName
    else:
        roomId=int(list(roomIdDict.keys())[-1].replace('R',''))+1
        roomId='R'+str(roomId)
        roomIdDict[roomId]=roomName
    printIdDict(roomIdDict)

def deleteRoom():
    #ASKING FOR ROOM ID TO DELETE
    printIdDict(roomIdDict)
    roomId=input('Enter the ID relevant to the room to be deleted: ')
    while not roomId in list(roomIdDict.keys()):
        roomId=input('Wrong input! Retry: ')
    
    roomContent=dictContent(roomId)
    if len(roomContent)>0:
        print('Warning! Room is not empty! Do you really want to delete it? You will lost every item in it!')
        operation=input('You can:\n- abort the deletion [1]\n- perform the deletion [2]\n- transfer the items to another room and perform the deletion [3]\nEnter the number of operation you want to perform: ')
        while not operation in ['1','2','3']:
            operation=input('Wrong input! Retry: ')
    else:
        operation=input('You can:\n- abort the deletion [1]\n- perform the deletion [2]\nEnter the number of operation you want to perform: ')
        while not operation in ['1','2']:
            operation=input('Wrong input! Retry: ')

    if operation=='1':
        print('Deletion aborted!')
        pass
    elif operation=='2':
        roomContent=dictContent(roomId,subObjResearch=True)
        for objId in roomContent:
            del(objIdDict[objId])
        del(roomIdDict[roomId])
    else:
        newRoomId=input('Enter the id of the destination room: ')
        while newRoomId==roomId or not newRoomId in roomIdDict:
            newRoomId=input('Wrong input, retry: ')

        for objId in roomContent:   
            objIdDict[objId]['place']=newRoomId

def modifyRoom():
    #ASKING FOR ROOM ID TO MODIFY
    printIdDict(roomIdDict)
    roomId=input('Enter the ID relevant to the room to be modified: ')
    while not roomId in list(roomIdDict.keys()):
        roomId=input('Wrong input! Retry: ')
    
    newRoomName=input('Please, enter the new name of the room: ')
    while newRoomName in list(roomIdDict.values()):
        newRoomName=input('Name already used, retry: ')
    roomIdDict[roomId]=newRoomName  

def setHouseRooms():
    if len(roomIdDict)==0:
        #--ASK FOR THE INSERTION MODE--#
        stdHouseRooms=['Entrance','Stay','Kitchen','Bathroom','Bedroom','Studio']
        print("""Here's a standard house room list: {}""".format(' - '.join(stdHouseRooms)))
        print('If the previous list fits your home, then enter 1. If you want to enter manually your rooms, then enter 2.')
        setHouseMode=input('Please, enter the number of operation you want to perform: ')
        while not setHouseMode in ['1','2']:
            setHouseMode=input('Wrong, input! Retry: ')
    else:
        setHouseMode='2'
      
    #--PERFORMING INSERTION--#
    if setHouseMode=='1':
        for room,Id in zip(stdHouseRooms,range(1,len(stdHouseRooms)+1)):
            roomIdDict['R'+str(Id)]=room
        printIdDict(roomIdDict)
    else:
        operation=''
        while operation!='0':
            if len(roomIdDict)==0:
                operation=input('You can:\n- Add a room [1]\n- Exit [0]\nEnter the number of the operation you want to perform: ')
                while not operation in ['0','1']:
                    operation=input('Wrong input! Retry: ')
            else:
                printIdDict(roomIdDict)
                operation=input('You can:\n- Add a room [1]\n- Delete a room [2]\n- Modify a room [3]\n- Exit [0]\nEnter the number of the operation you want to perform: ')
                while not operation in ['0','1','2','3']:
                    operation=input('Wrong input! Retry: ')

            if operation=='1':
                addRoom()
            elif operation=='2':
                deleteRoom()
            elif operation=='3':
                modifyRoom()
        printIdDict(roomIdDict)

def addObject():
    objName=input('Please, enter the name of the object to be added: ')          
    if len(objIdDict)==0:
        objId='O1'
        objIdDict[objId]={'name':objName}
    else:
        objId=list(objIdDict.keys())[-1].replace('O','')
        objId='O'+str(int(objId)+1)
        objIdDict[objId]={'name':objName}
    operation=input('If the object can contain other object input 1, otherwise input 2: ')
    while not operation in ['1','2']:
        operation=input('Sorry, wrong input! Retry: ')
    
    if operation=='1':
        objIdDict[objId]['container']=True
    else:
        objIdDict[objId]['container']=False
    
    print("""Here's the list of the rooms ids:""")
    printIdDict(roomIdDict)
    print("""Here's the list of the objects ids:""")
    printIdDict(objIdDict)
    placeId=input('Please, enter the id of the room or the object where you want to put the object: ')
    while not placeId in roomIdDict and not placeId in objIdDict:
        placeId=input('Wrong input, retry: ')

    if not 'R' in placeId:
        while not objIdDict[placeId]['container']:
            print("""The object selected can contain nothing""")
            operation=input('What you want to do:\n- select another place [1]\n- main menu [2]')
            while not operation in ['1','2']:
                operation=input('Wrong input, retry: ')
            if operation=='1':
                placeId=input('Please, enter the id of the room or the object where you want to put the object: ')
                while not placeId in roomIdDict and not placeId in objIdDict:
                    placeId=input('Wrong input, retry: ')
            else:
                del(objIdDict[objId])
                return
    objIdDict[objId]['place']=placeId
              
def modifyObject():
    printIdDict(objIdDict)
    objId=input('Please, enter the id of the object to be modified: ')
    print("What you want to modify?\n- name [1]\n- place [2]\n- holding capability [3]")
    operation=input('Enter the number of the operation to perform: ')
    while not operation in ['1','2','3']:
        operation=input('Sorry! Wrong input, retry: ')
    
    if operation=='1':
        name=input('Enter the new name of the object: ')
        objIdDict[objId]['name']=name
    elif operation=='2':
        print("""Here's the list of the rooms ids:""")
        printIdDict(roomIdDict)
        print("""Here's the list of the objects ids:""")
        printIdDict(objIdDict)
        placeId=input('Please, enter the id of the room or the object where you want to put the object: ')
        while not placeId in roomIdDict and not placeId in objIdDict:
            placeId=input('Wrong input, retry: ')

        if not 'R' in placeId:
            while not objIdDict[placeId]['container']:
                print("""The object selected can contain nothing""")
                operation=input('What you want to do:\n- select another place [1]\n- main menu [2]')
                while not operation in ['1','2']:
                    operation=input('Wrong input, retry: ')
                if operation=='1':
                    placeId=input('Please, enter the id of the room or the object where you want to put the object: ')
                    while not placeId in roomIdDict or not placeId in objIdDict:
                        placeId=input('Wrong input, retry: ')
                else:
                    return
        objIdDict[objId]['place']=placeId
    else:
        if objIdDict[objId]['container']:
            contentList=dictContent(objId)
            if len(contentList)>0:
                operation=input('The object contains other objects! Do you want to move all the objects (1) or you want to abort (2)?')
                while not operation in ['1','2']:
                    print('Wrong input, retry!')
                    operation=input('The object contains other objects! Do you want to move all the objects (1) or you want to abort (2)?')
                    
                if operation=='1':
                    printIdDict(roomIdDict)
                    printIdDict(objIdDict)
                    destId=input('Enter the id of the destination place: ')
                    if 'R' in destId:
                        for id in contentList:
                            objIdDict[id]['place']=destId
                    else:
                        while not objIdDict[destId]['container']:
                            print('You choosed a non container object, please retry!')
                            destId=input('Enter the id of the destination place: ')
                        for id in contentList:
                            objIdDict[id]['place']=destId
                else:
                    print('Modification aborted!')
                    pass
            objIdDict[objId]['container']=False
        else:
            objIdDict[objId]['container']=True

def deleteObject():
    objId=input('Enter the id of the object to be deleted: ')
    contentList=dictContent(objId,subObjResearch=True)
    if len(contentList)>0:
        operation=input('The object is not empty! You can:\n- move all objects to another place [1]\n- delete the object and its content [2]\n- abort the deletion [3]\nEnter ther number of the operation you want to perform: ')
        while not operation in ['1','2','3']:
            print('Wrong input, retry!')
            operation=input('The object is not empty! You can:\n- move all objects to another place [1]\n- delete the object and its content [2]\n- abort the deletion [3]\nEnter ther number of the operation you want to perform: ')
        
        if operation=='1':
            printIdDict(roomIdDict)
            printIdDict(objIdDict)
            placeId=input('Please, enter the id of the room or the object where you want to put the object: ')
            while not placeId in roomIdDict and not placeId in objIdDict:
                placeId=input('Wrong input, retry: ')

            if not 'R' in placeId:
                while not objIdDict[placeId]['container']:
                    print("""The object selected can contain nothing""")
                    operation=input('What you want to do:\n- select another place [1]\n- main menu [2]')
                    while not operation in ['1','2']:
                        operation=input('Wrong input, retry: ')
                    if operation=='1':
                        placeId=input('Please, enter the id of the room or the object where you want to put the object: ')
                        while not placeId in roomIdDict or not placeId in objIdDict:
                            placeId=input('Wrong input, retry: ')
                        for id in contentList:
                            objIdDict[id]['place']=placeId
                    else:
                        return
            else:
                for id in contentList:
                    objIdDict[id]['place']=placeId
            del(objIdDict[objId])
        elif operation=='2':
            for id in contentList:
                del(objIdDict[id])
            del(objIdDict[objId])
        else:
            print('Deletion aborted!')
            pass
    else:
        del(objIdDict[objId])

def main():
    print('HOUSEHOLD CATALOG MANAGER')
    setHouseRooms()
    operation=''
    operation=input('You can:\n- Explore house [1]\n- Modify rooms [2]\n- Add an object [3]\n- Modify an object [4]\n- Delete an object [5]\n\nChoose the operation you want to perform or enter 0 to exit: ')
    while not operation=='0':
        if operation=='1':
            explore()
        elif operation=='2':
            setHouseRooms()
        elif operation=='3':
            addObject()
        elif operation=='4':
            modifyObject()
        else:
            deleteObject()
        operation=input('You can:\n- Explore house [1]\n- Modify rooms [2]\n- Add an object [3]\n- Modify an object [4]\n- Delete an object [5]\n\nChoose the operation you want to perform or enter 0 to exit: ')
if __name__=='__main__':
    main()