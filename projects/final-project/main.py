#--DICTIONARIES INITIALIZATION--#
HouseDic={} #main dictionary {RoomName:{Obj:[Obj]|None}} (None if the object can contain nothing)
RoomIdDic={} #dictionary used to map RoomName to RoomId (this app can be used only from command line, so enter a number it's better than enter a name)
ObjIdDic={}

def PrintIdDic(IdDic):
    #--OBTAINING PADDING VALUES--#
    MaxIdLen=0
    MaxNameLen=0
    for Id in list(IdDic.keys()):
        if len(Id)>MaxIdLen:
            MaxIdLen=len(str(Id))
        
        Name=IdDic[Id]['Name']
        if len(Name)>MaxNameLen:
            MaxNameLen=len(Name)

    #--BUILDING STRING TO BE PRINTED--#
    StrToPrint=''
    for Id in IdDic:
        Name=IdDic[Id]['Name']
        Str='ID: {:>'+str(MaxIdLen)+'} - NAME: {:>'+str(MaxNameLen)+'}\n'
        StrToPrint=StrToPrint+Str.format(Id,Name)
    print(StrToPrint)

def PrintMainDic(MainDic,IdDic):
    #--OBTAINING PADDING VALUES--#
    MaxIdLen=0
    MaxNameLen=0
    for Id in list(MainDic.keys()):
        if len(Id)>MaxIdLen:
            MaxIdLen=len(str(Id))
    
        Name=IdDic[Id]['Name']
        if len(Name)>MaxNameLen:
            MaxNameLen=len(Name)

    #--BUILDING STRING TO BE PRINTED--#
    StrToPrint=''
    for Id in MainDic:
        if Id in IdDic:
            Name=IdDic[Id]['Name']
            Str='ID: {:>'+str(MaxIdLen)+'} - NAME: {:>'+str(MaxNameLen)+'}\n'
            StrToPrint=StrToPrint+Str.format(Id,Name)
    print(StrToPrint)

def Explore(MainDic,RootDic={None:HouseDic},Id=None):
    if Id!=None:
        RootDic[Id]=MainDic

    if len(MainDic)>0:
        if 'R' in list(MainDic.keys())[0]:
            IdDic=RoomIdDic
        else:
            IdDic=ObjIdDic

    if len(MainDic)>0:
        print("""Here's the content of the room\object:""")
        PrintMainDic(MainDic,IdDic)
        
        if len(RootDic)>1:
            print('You can:\n- go on with exploring [1]\n- main menu [2]\n- go back to the upper level [3]')
            Operation=input('Enter the number of the operation to perform: ')
            while not Operation in ['1','2','3']:
                Operation=input('Sorry! Wrong input, retry: ')
        else:
            print('You can:\n- go on with exploring [1]\n- main menu [2]')
            Operation=input('Enter the number of the operation to perform: ')
            while not Operation in ['1','2']:
                Operation=input('Sorry! Wrong input, retry: ')
        
        if Operation=='1':
            Id=input('Please, enter the ID of the object or room you want to explore: ')
            while not Id in MainDic:
                Id=input('Wrong input! Please, retry: ')
            Content=MainDic[Id]
            if type(Content)==dict:
                RootDic[Id]=Content
                return Explore(Content,RootDic)
            else:
                print("""This object can contain nothing""")
                if len(RootDic)>1:
                    print('You can:\n- go back to the upper level [1]\n- main menu [2]\n- explore other objects in the current place [3]')
                    Operation=input('Enter the number of the operation to perform: ')
                    while not Operation in ['1','2','3']:
                        Operation=input('Sorry! Wrong input, retry: ')

                    if Operation=='1':
                        RootDic.pop(list(RootDic.keys())[-1])
                        Id=list(RootDic.keys())[-1]
                        return Explore(RootDic[Id],RootDic)
                    elif Operation=='2':
                        return None, None
                    else:
                        return Explore(MainDic,RootDic)
                else:
                    print('You can:\n- go back to the room list [1]\n- main menu [2]\n- explore other objects in the current place [3]')
                    Operation=input('Enter the number of the operation to perform: ')
                    while not Operation in ['1','2','3']:
                        Operation=input('Sorry! Wrong input, retry: ')
                    
                    if Operation=='1':
                        Id=list(RootDic.keys())[-1]
                        Place=RootDic[Id]
                        return Explore(Place,RootDic)
                    elif Operation=='2':
                        return None, None
                    else:
                        return Explore(MainDic,RootDic)
        elif Operation=='2':
            Id=list(RootDic.keys())[-1]
            Place=RootDic[Id]
            return Place,Id
        else:
            RootDic.pop(list(RootDic.keys())[-1])
            Id=list(RootDic.keys())[-1]
            return Explore(RootDic[Id],RootDic)
    else:
        print('The room or the object is empty')
        if len(RootDic)>1:
            print('You can:\n- go back to the upper level [1]\n- main menu [2]\n')
            Operation=input('Enter the number of the operation to perform: ')
            while not Operation in ['1','2']:
                Operation=input('Sorry! Wrong input, retry: ')

            if Operation=='1':
                RootDic.pop(list(RootDic.keys())[-1])
                Id=list(RootDic.keys())[-1]
                Place=RootDic[Id]
                return Explore(Place,RootDic)
            else:
                Id=list(RootDic.keys())[-1]
                Place=RootDic[Id]
                return Place,Id
        else:
            print('You can:\n- go back to the room list [1]\n- main menu [2]\n')
            Operation=input('Enter the number of the operation to perform: ')
            while not Operation in ['1','2']:
                Operation=input('Sorry! Wrong input, retry: ')

            if Operation=='1':
                Id=list(RootDic.keys())[-1]
                Place=RootDic[Id]
                return Explore(Place,RootDic)
            else:
                Id=list(RootDic.keys())[-1]
                Place=RootDic[Id]
                return Place,Id

def AddRoom():
    RoomName=input('Please, enter the name of the room to be added: ')
    if len(HouseDic)>0:
        for Id in RoomIdDic:
            if RoomName==RoomIdDic[Id]['Name']:
                print('Warning: room already inserted! Retry!')

    #SAVING ROOM INFO TO THE HOUSE DIC                
    if len(RoomIdDic)==0:
        RoomIdDic['R1']={'Name':RoomName}
    else:
        RoomId=int(list(RoomIdDic.keys())[-1].replace('R',''))+1
        RoomId='R'+str(RoomId)
        RoomIdDic[RoomId]={'Name':RoomName}
    HouseDic[RoomId]={}
    print(HouseDic)

def DicContent(MainDic):
    Content=[]
    for Id in MainDic:
        if type(MainDic[Id])==dict:
            Content.append(Id)
            Content+DicContent(MainDic[Id])
        else:
            Content.append(Id)
    return Content  

def DeleteRoom():
    #ASKING FOR ROOM ID TO DELETE
    PrintIdDic(RoomIdDic)
    RoomId=input('Enter the ID relevant to the room to be deleted: ')
    while not RoomId in list(RoomIdDic.keys()):
        RoomId=input('Wrong input! Retry: ')
    
    if len(HouseDic[RoomId])>0:
        print('Warning! Room is not empty! Do you really want to delete it? You will lost every item in it!')
        Operation=input('You can:\n- abort the deletion [1]\n- perform the deletion [2]\n- transfer the item to another room and perform the deletion [3]\nEnter the number of operation you want to perform: ')
        while not Operation in ['1','2','3']:
            Operation=input('Wrong input! Retry: ')
    else:
        Operation=input('You can:\n- abort the deletion [1]\n- perform the deletion [2]\nEnter the number of operation you want to perform: ')
        while not Operation in ['1','2']:
            Operation=input('Wrong input! Retry: ')

    if Operation=='1':
        print('Deletion aborted!')
        pass
    elif Operation=='2':
        Content=DicContent(HouseDic[RoomId])
        for ObjId in Content:
            ObjIdDic.pop(ObjId)
        RoomIdDic.pop(RoomId)
        HouseDic.pop(RoomId)
    else:
        PrintIdDic(RoomIdDic)
        DestRoomId=input('Enter the ID relevant to the room where you want to transfer the items: ')
        while not DestRoomId in RoomIdDic or DestRoomId==RoomId:
            DestRoomId=input('Wrong input! Retry: ')
        HouseDic[DestRoomId].update(HouseDic[RoomId])
        Content=DicContent(HouseDic[RoomId])
        for ObjId in Content:
            ObjIdDic[ObjId]['Place']=DestRoomId
        RoomIdDic.pop(RoomId)
        HouseDic.pop(RoomId)

def ModifyRoom():
    #ASKING FOR ROOM ID TO MODIFY
    PrintIdDic(RoomIdDic)
    RoomId=input('Enter the ID relevant to the room to be modified: ')
    while not RoomId in list(RoomIdDic.keys()):
        RoomId=input('Wrong input! Retry: ')
    NewRoomName=input('Please, enter the new name of the room: ')
    for Id in RoomIdDic:
            if NewRoomName==RoomIdDic[Id]['Name']:
                print('Warning: room already inserted! Retry!')
    RoomIdDic[RoomId]['Name']=NewRoomName  

def SetHouseRooms():
    if len(HouseDic)==0:
        #--ASK FOR THE INSERTION MODE--#
        StdHouseRooms=['Entrance','Stay','Kitchen','Bathroom','Bedroom','Studio']
        print("""Here's a standard house room list: {}""".format(' - '.join(StdHouseRooms)))
        print('If the previous list fits your home, then enter 1. If you want to enter manually your rooms, then enter 2.')
        SetHouseMode=input('Please, enter the number of operation you want to perform: ')
        while not SetHouseMode in ['1','2']:
            SetHouseMode=input('Wrong, input! Retry: ')
    else:
        SetHouseMode='2'
      
    #--PERFORMING INSERTION--#
    if SetHouseMode=='1':
        for Room,Id in zip(StdHouseRooms,range(1,len(StdHouseRooms)+1)):
            HouseDic['R'+str(Id)]={}
            RoomIdDic['R'+str(Id)]={'Name':Room}
        PrintIdDic(RoomIdDic)
        return HouseDic,RoomIdDic
    else:
        Operation=''
        while Operation!='0':
            if len(HouseDic)==0:
                Operation=input('You can:\n- Add a room [1]\n- Exit [0]\nEnter the number of the operation you want to perform: ')
                while not Operation in ['0','1']:
                    Operation=input('Wrong input! Retry: ')
            else:
                PrintIdDic(RoomIdDic)
                Operation=input('You can:\n- Add a room [1]\n- Delete a room [2]\n- Modify a room [3]\n- Exit [0]\nEnter the number of the operation you want to perform: ')
                while not Operation in ['0','1','2','3']:
                    Operation=input('Wrong input! Retry: ')

            
            if Operation=='1':
                AddRoom()
            elif Operation=='2':
                DeleteRoom()
            elif Operation=='3':
                ModifyRoom()
        PrintIdDic(RoomIdDic)

def RootFinder(ObjId):
    RootList=[]
    ContainerId=ObjIdDic[ObjId]['Place']
    RootList.append(ContainerId)
    if 'R' in ContainerId:
        return RootList
    else:
        return RootList+RootFinder(ContainerId)

def GoToRoot(RootList):
    Container=HouseDic
    for Id in RootList:
        Container=Container[Id]
    return Container

def AddObject():
    ObjName=input('Please, enter the name of the object to be added: ')
    #SAVING OBJECT INFO TO THE HOUSE DIC                
    if len(ObjIdDic)==0:
        ObjId='O1'
        ObjIdDic[ObjId]={'Name':ObjName}
    else:
        ObjId=list(ObjIdDic.keys())[-1].replace('O','')
        ObjId='O'+str(int(ObjId)+1)
        ObjIdDic[ObjId]={'Name':ObjName}
    Operation=input('If the object can contain other object input 1, otherwise input 2: ')
    while not Operation in ['1','2']:
        Operation=input('Sorry, wrong input! Retry: ')
    
    if Operation=='1':
        IsObjContainer=True
    else:
        IsObjContainer=False
    PrintIdDic(RoomIdDic)
    RoomId=input('Please, enter the id of the room where you want to put the object: ')
    if len(HouseDic[RoomId])>0:
        print('Do you want to put the object in the room [1] or into an object inside the room [2]?')
        Operation=input('Enter the number of the operation you want to perform: ')
        while not Operation in ['1','2']:
            Operation=input('Sorry, wrong input! Retry: ')
        
        if Operation=='1':
            if IsObjContainer:
                HouseDic[RoomId][ObjId]={}
                ObjIdDic[ObjId]['Container']=True
            else:
                HouseDic[RoomId][ObjId]=None
                ObjIdDic[ObjId]['Container']=False
            ObjIdDic[ObjId]['Place']=RoomId
        else:
            Container,ContainerId=Explore(HouseDic[RoomId],Id=RoomId)
            while Container==None or ContainerId==None:
                print("You can't place the object here. Please, retry.")
                Container,ContainerId=Explore(HouseDic[RoomId],Id=RoomId)
            
            if IsObjContainer:
                Container[ObjId]={}
            else:
                Container[ObjId]=None
            ObjIdDic[ObjId]['Place']=ContainerId
    else:
        if IsObjContainer:
            HouseDic[RoomId][ObjName]={}
            ObjIdDic[ObjId]['Container']=True
        else:
            HouseDic[RoomId][ObjName]=None
            ObjIdDic[ObjId]['Container']=False
        ObjIdDic[ObjId]['Place']=RoomId

def ModifyObject():
    PrintIdDic(ObjIdDic)
    ObjId=input('Please, enter the id of the object to be modified: ')
    print("What you want to modify?\n- name [1]\n- place [2]\n- holding capability [3]")
    Operation=input('Enter the number of the operation to perform: ')
    while not Operation in ['1','2','3']:
        Operation=input('Sorry! Wrong input, retry: ')
    
    if Operation=='1':
        Name=input('Enter the new name of the object: ')
        ObjIdDic[ObjId]['Name']=Name
    elif Operation=='2':
        PrintIdDic(RoomIdDic)
        DestRoomId=input('Enter the destination room id: ')
        if len(HouseDic[DestRoomId])>0:
            print('Do you want to put the object in the room [1] or into an object inside the room [2]?')
            Operation=input('Enter the number of the operation you want to perform: ')
            while not Operation in ['1','2']:
                Operation=input('Sorry, wrong input! Retry: ')
            
            if Operation=='1':
                if ObjIdDic[ObjId]['Container']:
                    HouseDic[DestRoomId][ObjId]={}
                else:
                    HouseDic[DestRoomId][ObjId]=None
                ObjIdDic[ObjId]['Place']=DestRoomId
            else:
                Container,ContainerId=Explore(HouseDic[DestRoomId],Id=ObjIdDic)
                while Container==None or ContainerId==None:
                    print("You can't place the object here. Please, retry.")
                    Container,ContainerId=Explore(HouseDic[DestRoomId],Id=ObjIdDic)
                
                if ObjIdDic[ObjId]['Container']:
                    Container[ObjId]={}
                else:
                    Container[ObjId]=None
                ObjIdDic[ObjId]['Place']=ContainerId
        else:
            if ObjIdDic[ObjId]['Container']:
                HouseDic[DestRoomId][ObjId]={}
            else:
                HouseDic[DestRoomId][ObjId]=None
            ObjIdDic[ObjId]['Place']=DestRoomId
    else:
        if ObjIdDic[ObjId]['Container']:
            RootList=RootFinder(ObjId)
            RootList.reverse()
            Container=GoToRoot(RootList)
            if len(Container)>0:
                Operation=input('The object contains other objects! Do you want to move all the objects (1) or you want to abort (2)?')
                while not Operation in ['1','2']:
                    print('Wrong input, retry!')
                    Operation=input('The object contains other objects! Do you want to move all the objects (1) or you want to abort (2)?')
                
                if Operation=='1':
                    PrintIdDic(RoomIdDic)
                    PrintIdDic(ObjIdDic)
                    DestId=input('Enter the id of the destination place: ')
                    if 'R' in DestId:
                        NewPlace=HouseDic[DestId]
                    else:
                        NewRootList=RootFinder(DestId)
                        NewPlace=GoToRoot(NewRootList)[DestId]
                        while type(NewPlace)!=dict:
                            print('You choosed a non container object, please retry!')
                            DestId=input('Enter the id of the destination place: ')
                            NewRootList=RootFinder(DestId)
                            NewPlace=GoToRoot(NewRootList)[DestId]
                    for Id in Container[ObjId]:
                        ObjIdDic[Id]['Place']=DestId
                    NewPlace.update(Container[ObjId])
                    Container[ObjId]=None
                else:
                    print('Modification aborted!')
                    pass
        else:
            ObjIdDic[ObjId]['Cotainer']=False

def main():
    print('HOUSEHOLD CATALOG MANAGER')
    SetHouseRooms()
    Operation=''
    Operation=input('You can:\n- Explore house [1]\n- Modify rooms [2]\n- Add an object [3]\n- Modify an object [4]\n- Delete an object [5]\n\nChoose the operation you want to perform or enter 0 to exit: ')
    while not Operation=='0':
        if Operation=='1':
            Explore(HouseDic)
        elif Operation=='2':
            SetHouseRooms()
        elif Operation=='3':
            AddObject()
        elif Operation=='4':
            ModifyObject()
        else:
            pass

    #---    DEBUG   ---#
    # SetHouseRooms()
    # HouseDic['R2']['O1']={}
    # ObjIdDic['O1']={'Name':'FirstObj','Place':'R2','Container':True}
    # HouseDic['R3']['O2']=None
    # ObjIdDic['O2']={'Name':'SecondObj','Place':'R3','Container':False}
    # HouseDic['R2']['O1']['O3']={}
    # ObjIdDic['O3']={'Name':'ThirdObj','Place':'O1','Container':True}
    # HouseDic['R2']['O1']['O3']['O4']=None
    # ObjIdDic['O4']={'Name':'FourthObj','Place':'O3','Container':False}
    # print(HouseDic)
    # ModifyObject()
    # print(HouseDic)
    # print(ObjIdDic)

if __name__=='__main__':
    main()