login_status=False
usid=[]
pa=[]
uid_pwd={}
user_name=""
marks=0

# Attempt Quiz
def attemp_quiz():
    if login_status==True:
        global marks
        n=False
        while n!=True:
            print("\nEnter your Choice for quiz\n 1.DBMS\n 2.DSA\n 3.Python\n 0.Exit")
            ch=int(input("Enter your choice for quiz:"))
            
            if ch==1:
                with open("dbms.txt",'r') as a1:
                   data=a1.readlines()
            elif ch==2:
                with open("dsa.txt",'r') as a1:
                   data=a1.readlines()
            elif ch==3:
               with open("python.txt",'r') as a1:
                   data=a1.readlines()
            elif ch==0:
                print("\nMarks=",marks)
                break
            else:
                n=False
    
            
            q=[]
            q1=[]
            q2=[]
            ans={}
            for i in range(len(data)):
                q.append(data[i].replace("\n",""))
            for i in range(len(q)):
                q1=q[i].split(",")
                q2.append(q1)
                q1=[]
                ans[q2[i][0]]=q2[i][-1]
            for i in range(0,len(q2)):
                for j in range(len(q2[i])-1):
                    if j==0:
                        print(f"Que{i+1}:{q2[i][j]}")
                    else:
                        print(f"{j}:{q2[i][j]}")
                answer=int(input("Enter the option number:"))
    
                if ans[q2[i][0]]==q2[i][answer]:
               
                    marks=marks+1
                    print("\n")
           
            with open("marks.txt",'a') as a1:
                   a1.write(f"{user_name},{marks}\n")

            print("Want to do next quiz then choose option show above")

    else:
        print("\nFirst Login or Register\n")
        

# Register
def register():
    print("\n")
    print("-------Registration-------")

    name=input("Enter your name:")
    uid=input("Create a user_id:").lower()
    if uid in usid:
        print("\nGoto login section this id already exist or give a new user name")
    else:
        pwd=input("Create your password:").lower()
        enroll=input("enter your enrollment numbetr:").lower()
        with open("registration.txt","a") as reg:
            reg.write(f"{name},{enroll},{uid},{pwd}\n")
        
        with open("id-pass.txt",'a') as idpas:
            idpas.write(f"{uid},{pwd}\n")
    

# Login
def login():
     global login_status
     global user_name
     p=False
     with open("id-pass.txt",'r') as idpas:
        d1=idpas.readlines()
     
     
     
     while p!=True:
       
        useid=input("Enter valid user id: ").lower()
        if not d1:
            print("\nUser not exist go to registration")
            p=True
        
        else:
            for i in d1:
                u,p=i.split(",")
                p=p.replace("\n","")
                usid.append(u)
                pa.append(p)
                uid_pwd[u]=p
            
            k=False
            if useid in usid:
                 user_name=useid
                 while k!=True:
               
                    pw=input("Enter Correct password:").lower()
                    if uid_pwd[useid]==pw:
                      p=True
                      k=True
                   
                    else :
                         pw=input("Enter Correct password:").lower()
                         k=False
                         if uid_pwd[useid]==pw:
                            p=True
                            k=True
                        
    
            else:
                p=False
            login_status=True
        # else:
        #     print("\nUser not exist go to registration")
        #     p=True


        
do=[]
new=[]
def profile():
    global marks
   
    with open("marks.txt",'a') as a1:
       a1.write(f"divya,{marks}\n") 
    if login_status==True:
        print("\nThe user information are:")
        with open("registration.txt","r") as reg:
            data=reg.readlines()
        for i in data:
           do.append(i.replace("\n",""))
        for i in do:
            di=i.split(",")
            new.append(di)
       
        for i in new:
            if user_name in i:
               n=i[0]
               en=i[1]
               ud=i[2]
               p=""
       
        print("Name=",n)
        print("Enrollment Number=",en)
        print("User ID=",ud)
        print("Marks:",marks)
        print("Password=",p)
        with open("marks.txt",'r') as a1:
                data=a1.readlines()
        f1=[]
        f3=[]
        for i in data:
            f1.append(i.replace("\n",""))
       
        for i in f1:
            f2=i.split(",")
            f3.append(f2)
        
        for j in f3:
            if user_name in j:
                print("Marks=",j[1])
    else:
        print("\nFirst Login or Register\n")
      
       
# Exit
def exit():
    print("logging out..")

# Main
def main():
    print("---------Welcome to Python Programing Quiz Application---------")
   
    l=False
    while l!=True:
        print("\n---Welcome---")
        print("1.Register")
        print("2.Login")
        print("3.Profile")
        print("4.Attempt Quiz")
        print("5.Exit")
        choice=int(input("Enter your choice: "))

        if choice==1:
            register()
        elif choice==2:
            login()
        elif choice==3:
            profile()
        elif choice==4:
            attemp_quiz()


        elif choice==5:
            exit()
            l=True
        else:
            print("Invalid choice")
            l=False
        

            
main()