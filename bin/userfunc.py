#libaries 
import json
import datetime
from . import crypto

class UserFunc():
    def __init__(self):
        self.filepath = "./src/db.json"
        self.dbjson = {"data":[]}
    
    
    
    
    def GetLength(self) -> int:
        """It returns last index number DB.json of "data" list ."""
        ArrayJson = []
        fileJson = open(self.filepath)
        ArrayJson = json.load(fileJson)
        return len(ArrayJson["data"])
    
    
    
    def GetData(self) -> list:
        """ It returns all data as list in db.json ."""
        ArrayJson = []
        fileJson = open(self.filepath)
        ArrayJson = json.load(fileJson)
        return (ArrayJson["data"])

    
    
    
    def GetId(self) -> int:
        """It returns the id of last data."""
        ArrayJson = []
        fileJson = open(self.filepath)
        ArrayJson = json.load(fileJson)
        try:
           return ArrayJson["data"][-1]["Id"]
        except IndexError:
            return 0
        except KeyError:
            return 0
    
    
    
    def AddData(self,Todo:str,Comp:bool):
        
        
        """It append new data to db.json file.\n Auto from last Index """
        Array = []
        JsonDataFormat = {"Id": UserFunc.GetId(self)+1,"Todo":crypto.CryptoTask(Todo),"Completed":Comp,"CreatedTime":crypto.CryptoTask(str(datetime.date.today()) +"\t"+datetime.datetime.now().strftime("%H:%M:%S"))}
        fileJson = open(self.filepath,"r+")
        ArrayJson = json.load(fileJson)
        for i in ArrayJson["data"]:
            Array.append(i)
        Array.append(JsonDataFormat)
        ArrayJson["data"] = Array
        with open(self.filepath,mode="r+") as file:
            self.dbjson["data"]=Array
            json.dump(self.dbjson,file)
    
    
    
    
    def RemoveData(self,ID:int or None = None):
        """It removes the data "ID" number is ID  from db.json. 
        The default ID is last item.
        If you type to wrong ID number , it will remove last data. """
        if ID is None :
            ID=0
        Array = []
        fileJson = open(self.filepath,"r+")
        ArrayJson = json.load(fileJson)
        for i in ArrayJson["data"]:
            Array.append(i)
        try:
            Array.pop(ID-1)
        except IndexError:
            ID=0
            try:
                Array.pop(ID)
            except IndexError:
                print("The Json file is empty.")
        with open(self.filepath,mode="w") as file:
            self.dbjson["data"]=Array
            json.dump(self.dbjson,file)
    


