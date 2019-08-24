
import time
import re    
import win32com.shell.shell as shell
di={
 'MinimumPasswordAge'          : 'between 1 and 998',
 'MaximumPasswordAge'          : 'between 1 and 999, or 0 to specify that passwords never expire',
 'MinimumPasswordLength'       : 'between 1 and 20 characters, or 0 to specify no password.',
 'PasswordComplexity'          : 'Enable (for better security)',#disabled
 'PasswordHistorySize'         : 'between 0 and 24 passwords',
 'LockoutBadCount'             : 'between 0 and 999 or 0 to specify that account will never be locked out',
 'RequireLogonToChangePassword': 'Option No Longer Exists in new version',
 'ForceLogoffWhenHourExpire'   : 'non zero (enable for better security)',
 'NewAdministratorName'        : '"No Default Value"',
 'NewGuestName'                : '"No Default Value"',
 'ClearTextPassword'           : 'Non Zero (Provides Encryption)',
 'LSAAnonymousNameLookup'      : '0 (Restricts Anonymous LSA)',
 'EnableAdminAccount'          : '0 (preferred disable)',
 'EnableGuestAccount'          : '0 (preferred disable)'
}
#time.sleep(5)   # Delays for 5 seconds. You can also use a float value.
def find_encoding(path):
    import chardet
    encoding=chardet.detect(open(path,'rb').read())['encoding']
def password_policy_logs():
    name=input('Please Enter filename: ')
    ls=[]
    #st=str()
    counter=int(0)
    startpos=84               #Bytes to seek before reading password policy
    lno=13                    #lines to be read under password policy
    path='C:\\All1\\'+name+'.txt'
    
    commands=r'SecEdit.exe /export /cfg '+path
    #print(commands)
    try:
        command1='mkdir C:\\All1'
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+command1)
    except:
        pass
    try:
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
    except:
        print('Not able to get administrative privalages\nProgram is closing in next three seconds ')
        for a in range(3):
            time.sleep(1)
            print('.',end=' ')
    
    print('\nGenerating report. Wait for 5 seconds')
    time.sleep(6) 
    
    with open(path,'a+',encoding='utf-16-le') as file:
        file.seek(startpos,0)
        while counter<=lno:
            line=file.readline().strip()
            if line!='':
                ls.append(line.split(' = '))
                counter+=1
                
    ls=dict(ls)
    ###############################################################################
    print('\n|{:_^30}|{:_^16}|{:_^72}|'.format('Keys','UserValues','RecommendedValues'))
    for a in di.keys():
        print('|{:^30}|{:^16}|{:<72}|'.format(a,ls[a],di[a]))
    file=open('C:\All1\Explain.txt',encoding='utf-8')
    pos=int()
    ls=[]
    line=file.readline()
    #print(line)
    str_a='\n'
    for a in range(14):
        while True:
            line=file.readline()
            line=line.strip()
            #print(line)
            if line=='&&':
                ls.append(str_a)
                str_a=''
                break
            else :
                str_a=str_a+'\n'+line
    ls=dict(zip(range(14),ls))
    print('|{:_^30}|{:_^16}|{:_^72}|'.format('','',''))
    print('\n\n') 
    
    while True:
        sno=1
        print('|{0:=^5} | {0:=^5} | {0:=^30} | {0:^5}'.format(''))
        print('|{0: ^5} | {2: ^5} | {1: ^30} | {2:^5}'.format('s.no','Attributes',''))
        print('|{0:=^5} | {0:=^5} | {0:=^30} | {0:^5}'.format(''))

        for a in di.keys():
            print('|{0:^5} | {2:=^5} | {1:^30} | {2:^5}'.format(sno,a,''))
            sno+=1
        try: 
            opt=int(input('\nEnter an option for its "Explanation\n (press enter to continue) :  \n'))
            print(ls[opt-1])
        except: pass

        choice=input("Continue (Y/N)?\n (press enter to exit) :  \n")
        if choice=='':
            break
    #############################################################################
    
    #choice=input("Enter Choice ")   
password_policy_logs()
#password_policy_logs(name)   
