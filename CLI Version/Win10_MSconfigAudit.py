import subprocess
import re
import win32com.shell.shell as shell
import time

class MsConfig():
    def simplify_G(self,a,list_no=0,value_no=0,no=0,rm_ls_no=0,rm_ls_keys=[],rm_ls2_no=0,rm_ls2_keys=[]):
        ls1=a.split(' \n\n')
        ls1.remove('\n')
        #except:
         #   pass
        ls2=list()
        ls2.append(re.findall('\S+',ls1[0]))
        ls2.append(re.findall('\S+',ls1[1]))
        #print(ls2)
        if list_no !=0:
            if list_no==2:
                counter=0
                while counter<no:
                    ls2[0].insert(value_no,' '*(counter+1))
                    counter+=1
            if list_no==1:
                counter=0
                while counter<no:
                    ls2[1].insert(value_no,' '*(counter+1))
                    counter+=1
        if rm_ls_no != 0:
            for k in rm_ls_keys:
                ls2[0].remove(k)
        if rm_ls2_no != 0:
            for k in rm_ls2_keys:
                ls2[1].remove(k)
        ls1=list(zip(ls2[0],ls2[1]))
        #print(ls1)
        ls1=dict(ls1)
        print('\n')
        for a in ls1.keys():
            print('{0:30} {1}'.format(a,ls1[a]))
    
    def service_info(self):
        di={1:'Brief',2:'Config',3:'Status',4:'Control',5:'Default'}
        print('Following Options are available: ',di)
        try:
            opt=int(input("Please select an option: "))
        except: 
            print("Enter Correct Value")
        command='wmic service list '+di[opt]
        if opt==2:
            command='wmic service get DesktopInteract,ErrorControl,Name,ServiceType,StartMode'
        if opt==5:
            command=' wmic service get name, processid, startmode, state, status, exitcode,servicetype /format: table'
        try:    
            a=eval("subprocess.getoutput(command)")
            print(a)    
        except:
            print("Error \n Cannot proceed")
        #a=(eval("subprocess.getoutput(' wmic service get name, processid, startmode, state, status, exitcode,servicetype /format: table')"))
    
    def startup_info(self):
        di={1:'Brief',2:'Default'}
        print('Following Options are available: ',di)
        try:
            opt=int(input("Please select an option: "))
        except: 
            print("Enter Correct Value")
        command='wmic startup list '+di[opt]
        if opt==1:
            command=' wmic startup get caption,user/format: table'
        if opt==2:
            command=' wmic startup get description,user,caption/format: table'
        try:    
            a=eval("subprocess.getoutput(command)")
            print(a)    
        except:
            print("Error \n Cannot proceed")
        #print(eval("subprocess.getoutput('wmic startup get description,user,command/format: table')"))
    
    def bios_info(self):
        a=eval("subprocess.getoutput('wmic BIOS get SMBIOSBIOSVersion, Manufacturer, Name, SerialNumber, Version, Status, SMBIOSPresent /format: table')")
        self.simplify_G(a)
    
    def useraccount_info(self):
        di={1:'Brief',2:'Writeable',3:'Status'}
        print('Following Options are available: ',di)
        try:
            opt=int(input("Please select an option: "))
        except: print("Enter Correct Value")
        command='wmic useraccount list '+di[opt]
        if opt==1:
            command='wmic useraccount get AccountType,Caption,Domain,Name,SID'
        if opt==2:
            command='wmic useraccount get Disabled,Caption,Lockout,PasswordChangeable,PasswordExpires,PasswordRequired'
        try:    
            a=eval("subprocess.getoutput(command)")
            print(a)    
        except:
            print("Error \n Cannot proceed")
    
    def cpu_info(self):
        di={1:'Brief',2:'Config',3:'Status',4:'Instance'}
        print('Following Options are available: ',di)
        try:
            opt=int(input("Please select an option: "))
        except: print("Enter Correct Value")
        command='wmic cpu list '+di[opt]
        if opt==1:
                command='wmic cpu get Caption,DeviceID,Manufacturer,MaxClockSpeed,Name'
        try: 
            a=eval("subprocess.getoutput(command)")
            if opt==2:
                self.simplify_G(a,rm_ls_no=1,rm_ls_keys=['L2CacheSpeed','Version','VoltageCaps'],rm_ls2_no=2,rm_ls2_keys=['CPU','Socket','-'])
            elif opt==3:
                self.simplify_G(a,rm_ls_no=1,rm_ls_keys=['ErrorCleared','ErrorDescription','LastErrorCode','LoadPercentage'])
            else:
                print('\n',a)
        except:
            print("Error \n Cannot proceed")
    
    def group_info(self):
        di={1:'Brief',2:'Full',3:'Status',4:'Instance'}
        print('Following Options are available: ',di)
        try:
            opt=int(input("Please select an option: "))
        except: print("Enter Correct Value")
        command='wmic group list '+di[opt]
        if opt==2:
            command='wmic group get description,name /format:list'
        if opt==4:
            command='wmic group get name,domain'
        try: 
            a=eval("subprocess.getoutput(command)")
            if opt==2:
                #print(a)
                a=a.split('\n\n\n\n')
                a=[s.replace('\n','') for s in a]
                a=[s.split('Name=') for s in a]
                del a[0],a[-1]
                a={s[1]:s[0].replace('Description=','') for s in a}
                for s in a.keys():
                    print('\n{:30}\n{}'.format(s,a[s]),'\n')
            print('\n',a)
        except:
            print("Error \n Cannot proceed")
    
    def os_info(self):
        di={1:'Brief',2:'Free',3:'Status'}
        print('Following Options are available: ',di)
        try:
            opt=int(input("Please select an option: "))
        except: print("Enter Correct Value")
        command='wmic os list '+di[opt]
        try: 
            a=eval("subprocess.getoutput(command)")
            if opt==1:
                self.simplify_G(a,rm_ls_no=1,rm_ls_keys=['Organization'])
            if opt==2:
                self.simplify_G(a,list_no=2,value_no=4,no=3)
            else:
                print('\n',a)
        except:
            print("Error \n Cannot proceed")
    
    def sysaccount_info(self):
        di={1:'Brief',2:'Full',3:'Status',4:'instance'}
        print('Following Options are available: ',di)
        try:
            opt=int(input("Please select an option: "))
        except: print("Enter Correct Value")
        command='wmic sysaccount list '+di[opt]
        if opt==2:
            command='wmic sysaccount get Description,Domain,LocalAccount,Name,SID,SIDType,Status '
        try:    
            a=eval("subprocess.getoutput(command)")
            print(a)    
        except:
            print("Error \n Cannot proceed")
    
    def process_info(self):
        di={1:'Brief',2:'Io',3:'Memory',4:'Status'}
        print('Following Options are available: ',di)
        try:
            opt=int(input("Please select an option: "))
        except: print("Enter Correct Value")
        command='wmic process list '+di[opt]
        try:    
            a=eval("subprocess.getoutput(command)")
            print(a)    
        except:
            print("Error \n Cannot proceed")
            
    def computersystem_info(self):
        di={1:'Brief',2:'Power',3:'Status',4:'writeable'}
        print('Following Options are available: ',di)
        try:
            opt=int(input("Please select an option: "))
        except:print("Enter Correct Value")
        command='wmic computersystem list '+di[opt]
        if di[opt]=='writeable':
            command='wmic computersystem get AutomaticResetBootOption,CurrentTimeZone,EnableDaylightSavingsTime,Roles,Workgroup'
        try: 
            a=eval("subprocess.getoutput(command)")
            if opt==3:    
                self.simplify_G(a,list_no=2,value_no=2,no=1)
            elif opt==4:
                self.simplify_G(a,list_no=2,value_no=4,no=2)
            else:
                self.simplify_G(a)
        except:
            print("Error \n Cannot proceed")
        if opt != 1:
            print("\nNote:\n*Status = 2 represents 'not Implemented'\n*Status = 1 represents 'Enabled'\n*Status = 0 represents 'Disabled'")
    
    def net_info(self):
        di={1:'ACCOUNTS' , 2:'COMPUTER' ,3:'CONFIG' ,4:'CONTINUE' ,5:'FILE' ,6:'GROUP' ,7:'HELP',8:'LOCALGROUP' ,9:'PAUSE' ,10:'SESSION' ,11:'SHARE' ,12:'START' ,13:'STATISTICS' ,14: 'STOP' , 15:'TIME' , 16:'USE' , 17:'USER' , 18:'VIEW'}
        #di={1:'Brief',2:'Io',3:'Memory',4:'Status'}
        print('Following Options are available: ')#,di)
        for c in di.keys():
            print('{:<3}: {:20}'.format(c,di[c]))
        try:
            opt=int(input("Please select an option: "))
        except: print("Enter Correct Value")
        #command='net  '+di[opt] 
       # if opt==2 or 5 or 4:
        command='net '+di[opt]+' /help'    
        try:                
            a=eval("subprocess.getoutput(command)")
            print('\n',a)    
        except:
            print("Error \n Cannot proceed")
    
obj=MsConfig()
    
a=['service_info', 'startup_info', 'bios_info', 'computersystem_info', 'useraccount_info', 'cpu_info' \
   , 'group_info', 'os_info', 'sysaccount_info', 'process_info', 'net_info']

while True:
    print('\n\n')
    print('|{0:=^3} | {2:=<5} | {1:=^30} | {3:<5}'.format('','','',''))
    print('|{0:^3} | {2:<5} | {1:^30} | {3:<5}'.format('Sno','Attribute','',''))
    print('|{0:=^3} | {2:=<5} | {1:=^30} | {3:<5}'.format('','','',''))
    for i in range(len(a)):
        print('|{0:3} | {2:=<5} | {1:^30} | {3:<5}'.format(i+1,a[i],'',''))
    print('|{0:=^3} | {2:=<5} | {1:=^30} | {3:<5}'.format('','','',''))
    
    ch = input("Enter your Choice(1-11)\nPress Enter To exit\n")
        
    if ch == '1':
        obj.service_info()
    elif ch == '2':
        obj.startup_info()
    elif ch == '3':
        obj.bios_info()
    elif ch == '4':
        obj.computersystem_info()
    elif ch == '5':
        obj.useraccount_info()
    elif ch == '6':
        obj.cpu_info()
    elif ch == '7':
        obj.group_info()
    elif ch == '8':
        obj.os_info()
    elif ch == '9':
        obj.sysaccount_info()
    elif ch == '10':
        obj.process_info()
    elif ch == '11':
        obj.net_info()
    elif ch=='':
        break
    else: 
        print("Invalid Value\n\nProgram will close in next 3 seconds")
        time.sleep(3)
        break
        