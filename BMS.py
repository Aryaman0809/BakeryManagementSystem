#MENU FUNCTION
def menu():
    print("\n\t\t\t\t\t\t\t\t\t\tBAKER'S STREET")
    print("\n\n\n")
    print("\t\t---------------------------------------------------------------------------------------")
    print("\t\t|Sr.no.\t\t Item\t\t\t\t\t\t Qty\t\t\t\t\tCost\t\t          |")
    print("\t\t---------------------------------------------------------------------------------------")
    for i in range(len(sr)):
        if(sr[i-2]!=0 and scp[i-2]=='y'):
            if(cost2[i]<1000):
                 print("\t\t|",sr[i],"\t\t",item[i],"\t\t",qty1[i],"/",qty2[i],"/",qty3[i],"\t\tRs.",cost1[i],"/",cost2[i],"/",cost3[i]," |")
                 print("\t\t---------------------------------------------------------------------------------------")
            else:
                print("\t\t|",sr[i],"\t\t",item[i],"\t\t",qty1[i],"/",qty2[i],"/",qty3[i],"\t\tRs.",cost1[i],"/",cost2[i],"/",cost3[i],"|")
                print("\t\t---------------------------------------------------------------------------------------")
               
           
               
           
#ADD FUNCTION 
def add():
    global p
    p=2
    flag=False
    for i in range(len(sr)):
        if(sr[i]==0):
            flag=True
            break
    if (flag==False):
        s=input("")
        k=i+2
        sr.append(k)
        print("Your next item's ID is",k)
        c=input("Enter the item: ")
        item.append(c)
        qty1.append(0.5)
        qty2.append(1.0)
        qty3.append(2.0)
        d=int(input("Enter the cost for half kg:"))
        cost1.append(d)
        cost2.append(d*2)
        cost3.append(d*4)
        loading()
        p=p+1
        print("Item has been added")

        print("\n\t\t\t\t\t\t\t\t\t\tBAKER'S STREET")
        print("\n\n\n")
        print("\t\t---------------------------------------------------------------------------------------")
        print("\t\t|Sr.no.\t\t Item\t\t\t\t\t\t Qty\t\t\t\t\tCost\t\t          |")
        print("\t\t---------------------------------------------------------------------------------------")
        for i in range(len(sr)):
            if (sr[i-p]!=0 and scp[i-p]=='y'):
                if (cost2[i]<1000):
                    print("\t\t|",sr[i],"\t\t",item[i],"\t\t", qty1[i],"/",qty2[i],"/",qty3[i],"\t\tRs.",
                          cost1[i],"/",cost2[i],"/",cost3[i]," |")
                    print("\t\t---------------------------------------------------------------------------------------")
                else:
                    print("\t\t|",sr[i],"\t\t",item[i],"\t\t",qty1[i],"/",qty2[i],"/",qty3[i],"\t\tRs.",
                          cost1[i],"/",cost2[i],"/",cost3[i],"|")
                    print("\t\t---------------------------------------------------------------------------------------")
   
        
       
       
#REMOVE FUNCTION
def remove():
    again=1
    while(again==1):
        psr=int(input("Enter item no.:"))
        flag=False
        for i in range(len(sr)):
            if(sr[i]==psr):
                flag=True
                scp[i-2]='n'
                loading()
                print("item has been removed")
                break
        if(flag==False):
            print("Invalid item no.!!!")
        again=int(input("Press 1 if you want to remain in remove"))
    print("\n\t\t\t\t\t\t\t\t\t\tBAKER'S STREET")
    print("\n\n\n")
    print("\t\t---------------------------------------------------------------------------------------")
    print("\t\t|Sr.no.\t\t Item\t\t\t\t\t\t Qty\t\t\t\t\tCost\t\t          |")
    print("\t\t---------------------------------------------------------------------------------------")
    for i in range(len(sr)):
        if (sr[i-2]!=0 and scp[i-2]=='y'):
            if (cost2[i]<1000):
                print("\t\t|",sr[i],"\t\t",item[i],"\t\t",qty1[i],"/",qty2[i],"/",qty3[i],"\t\tRs.",
                         cost1[i],"/",cost2[i],"/",cost3[i]," |")
                print("\t\t---------------------------------------------------------------------------------------")
            else:
                print("\t\t|",sr[i],"\t\t",item[i],"\t\t",qty1[i],"/",qty2[i],"/",qty3[i],"\t\tRs.",
                         cost1[i],"/",cost2[i], "/",cost3[i],"|")
                print("\t\t---------------------------------------------------------------------------------------")
       
#LOADING FUNCTION
def loading():
    print("LOADING")
    m=1
    for i in range(1,10000001):                               #DELAY LOOP
        if(m==10000000):
            m=1
            print(".......")
        m+=1
    print("")

#MODIFY FUNCTION
def modify():
    print("")
    pid=int(input("Enter the item ID:"))
    flag=False
    for i in range(len(sr)):
        if(pid==sr[i-2] and scp[i-2]=='y'):
            flag=True
            print("The current cost is:",cost1[i-2],"/",cost2[i-2],"/",cost3[i-2])
            print("")
            a=int(input("Enter the cost to be modified for half kg:"))
            cost1[i-2]=a
            b=int(input("Enter the cost to be modified for 1 kg:"))
            cost2[i-2]=b
            c=int(input("Enter the cost to be modified for 2 kg:"))
            cost3[i-2]=c
            print("")
            loading()
            print("The new cost has been modified.")
            break
    if(flag==False):
        print("Wrong item ID")
        
    print("\n\t\t\t\t\t\t\t\t\t\tBAKER'S STREET")
    print("\n\n\n")
    print("\t\t---------------------------------------------------------------------------------------")
    print("\t\t|Sr.no.\t\t Item\t\t\t\t\t\t Qty\t\t\t\t\tCost\t\t          |")
    print("\t\t---------------------------------------------------------------------------------------")
    for i in range(len(sr)):
        if (sr[i-2]!=0 and scp[i-2]=='y'):
            if (cost2[i]<1000):
                print("\t\t|",sr[i],"\t\t",item[i],"\t\t",qty1[i],"/",qty2[i],"/",qty3[i],"\t\tRs.",
                          cost1[i],"/",cost2[i],"/",cost3[i]," |")
                print("\t\t---------------------------------------------------------------------------------------")
            else:
                print("\t\t|",sr[i],"\t\t",item[i],"\t\t",qty1[i],"/",qty2[i],"/",qty3[i],"\t\tRs.",
                          cost1[i],"/",cost2[i],"/",cost3[i],"|")
                print("\t\t---------------------------------------------------------------------------------------")
#BILL FUNCTION        
def bill():
    x=1
    m=1
    k=1
    q=[]
    t=[]
    c=[]
    menu()
    abc=""
    print("")
    n=input("ENTER THE CUSTOMER'S NAME: ")
    print("")
    print("1. Circular")
    print("2. Heart shape")
    shape=int(input("Enter the shape of the cake that customer wants: "))
    if(shape==1):
        print("The customer wants a cake of circular shape.")
    elif(shape==2):
        print("The customer wants a cake of heart shape.")
    else:
        print("Invalid shape entered! Taking Circular as Default")
    bill=0
    while(m==1):
        k+=1
        choice=int(input("Enter the serial number of the cake that the customer wants:"))
        for i in range(len(sr)):
            if(choice==sr[i]):
                quantity=float(input("Enter the quantity of cake that the customer wants(0.5/1.0/2.0)(in kg):"))
                nq=int(input("Enter the number of cakes that the customer wants:"))
                if(quantity==0.5):
                    bill=bill+cost1[i]*nq
                    q.append(quantity)
                    t.append(item[i])
                    c.append(cost1[i])
                elif(quantity==1):
                    bill=bill+cost2[i]*nq
                    q.append(quantity)
                    t.append(item[i])
                    c.append(cost2[i])
                else:
                    bill=bill+cost3[i]*nq
                    q.append(quantity)
                    t.append(item[i])
                    c.append(cost3[i])
        m=int(input("Press 1 if the customer wants to add something to his/her order:"))
    fbill=bill+(0.025*bill)+(0.025*bill)
    tde.append(fbill)
    print("\t\t\t\t\t\t\t\t\t~~~~~TOTAL BILL~~~~\t\t\t\n")
    print("\t\t|Sr.no.\t\t Qty\t\t\t Item\t\t\t\t\t\t\t Cost|\n")
    print("\t\t-------------------------------------------------------------------------------")
    for i in range(1,k):
      print("\t\t|",i,"\t\t",q[i-1],"\t\t\t",t[i-1],"\t\t\t",c[i-1]*nq,"|")
      print("\t\t--------------------------------------------------------------------------------")
    print("\n\n")
    print("\t\t\t---BAKER'S STREET---")
    print("\t\tName:",n)
    print("\t\tTOTAl          : ",bill)
    print("\t\tCGST           : ",(0.025*bill))
    print("\t\tSGST           : ",(0.025*bill))
    print("\t\tFINAL BILL     : ",fbill)
    print("\t\tTHANK YOU!! HOPE YOU VISIT AGAIN!!")
 
#MAIN FUNCTION
def main():
    out=0
    again=1
    while(again==1):
        print("\f") #\f for clear screen
        print("\n\n\n")
        print("\t\t\t\t---BAKER'S STREET---")
        print("\t\t\t\t 1.MENU CARD\n")
        print("\t\t\t\t 2.ADD\n")
        print("\t\t\t\t 3.MODIFY\n")
        print("\t\t\t\t 4.REMOVE\n")
        print("\t\t\t\t 5.BILL")
        ch=int(input("\t\t\t\t ENTER YOUR CHOICE:"))
        if(ch==1):
            menu()
        elif(ch==2):
            add()
        elif(ch==3):
            modify()
        elif(ch==4):
            remove()
        elif(ch==5):
            start()
        else:
            print("Invalid Choice")
        if(out==0):
            again=int(input("Enter 1 to remain in the main menu: "))

#START FUNCTION
def start():
    i=1
    global id
    id=0
    while(i==1):
        z=int(input("ENTER 1 TO KEEP SHOP OPEN AND 0 TO CLOSE IT:"))
        print("")
        if(z==1):
            id=id+1
            bill()
        else:
            earnings()
            i=0

#EARNINGS FUNCTION
def earnings():
    global fe
    fe=0
    for i in range (len(tde)):
        fe=fe+tde[i]
    print("Total earnings of your day are: ",fe,"\n")
    print("Total customers in a are: ",id)
            
sr=[1,2,3,4,5,6,7,8,9,10]
item=["Blackforest cake   ","Rainbow cake       ","Red Velvet cake     ","Cheesecake         ","Pineapple cake     ","Chocolate Cake     "
,"Strawberry Cake    ","Ferrero Rocher Cake","Swiss chocolate    ","Walnut cake        "]
qty1=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
qty2=[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
qty3=[2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0,2.0]
cost1=[400,620,650,710,400,450,400,550,600,500]
cost2=[800,1240,1300,1420,800,900,800,1100,1200,1000]
cost3=[1600,2480,2600,2840,1600,1800,1600,2200,2400,2000]
scp=['y','y','y','y','y','y','y','y','y','y'] #scrapList
tde=[] #TotalDayEarning
main()
