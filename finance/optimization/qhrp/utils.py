import os 
import json
from typing import Any

def readJsonFile(file_path: str) -> Any:

    with open(file_path) as json_file:
        data = json.load(json_file)
        
    return data

def writeJsonFile(file_path:str,new_data:Any) -> None:
    if not checkFileExistance(file_path):        
        f = open(file_path, "x")
    
    filesize = os.path.getsize(file_path)

    if (filesize!=0):
        data=readJsonFile(file_path)
        data.append(new_data)
    else:
        data=[]
        data.append(new_data)
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile,indent=2)

def checkFileExistance(filePath: str) -> bool:
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def getenvcached(name):
    from getpass import getpass
    user1 = os.getenv(name)
    if user1 is None:
        try:
            user1 = readJsonFile("env.json")[-1][name]
            return user1
        except:
            pass
    if user1 is None:
        try:
            user1 = readJsonFile(".env.json")[-1][name]
            return user1
        except:
            pass
    if user1 is None:
        user1 = getpass(name)
    try:
        j = readJsonFile(".env.json")[-1]
        j[name] = user1
        #print("write env file/0", j)
        writeJsonFile(".env.json", j)
    except:
        #print("write env file")
        writeJsonFile(".env.json", {name:user1})
    return user1