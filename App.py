import time 
from bin import userfunc
from bin import crypto


class TODO():
    def __init__(self):
        self.filepath = "./src/db.json"
        self.dbjson = {"data":[]}

    def Menu(self):

        content = userfunc.UserFunc.GetData(self)
        MenuList = []
        for x in content:
            MenuList.append(x)
        print(f"""                                   [TODO List]
                            |{time.ctime()}|
========================================================================================""")
    
        for i in MenuList:
            print("|"+"ID:"+str(i["Id"])+"| \t |"+"Task:"+crypto.DecryptoTask(i["Todo"])+"| \t |"+"Completed:"+str(i["Completed"])+"| \t |"+"Date:"+crypto.DecryptoTask(i["CreatedTime"])+"|")
            print("="*88)
        

    def MenuQuestion(self):
        print("|0) Get Task List |1) Add New data | 2) Remove data | 3) Exit|\n")
        try:
            menuNum = int(input("Please Enter(0/1/2/3) ? \t:"))
        except ValueError:
            print("Just menu numbers !!!")
            exit(1)
        except UnboundLocalError:
            print("check your value !!!")
        if menuNum == 1:
            try:
                task = str(input("Task :"))
                boolInput = int(input("Complated (True = 1/False = 0) :"))
                if boolInput == 1:
                    boolTask = True
                elif boolInput == 0:
                    boolTask = False
                else:
                    print("Check your values !!!")
                    exit(1)
            except ValueError:
                print("Check your values!")
                exit(1)
            userfunc.UserFunc.AddData(self,task,boolTask)
        elif menuNum == 2:
            try:
                menu2num = int(input("Please enter id of the data :"))
                if menu2num > userfunc.UserFunc.GetId(self):
                    print("Check data id that you want to remove !!!")
                elif menu2num == 0:
                    print("Check data id that you want to remove !!!")
                else:
                    userfunc.UserFunc.RemoveData(self,menu2num)
            except ValueError:
                print("Id must be integer.")
                exit(1)
        elif menuNum == 0:
            TODO.Menu(self)
        elif menuNum == 3:
            print("G00dBye !")
            exit(1)
        else:
            exit(1)

if __name__ == '__main__':
    while True:
    
        Start= TODO()
        Start.MenuQuestion()
            
        
            