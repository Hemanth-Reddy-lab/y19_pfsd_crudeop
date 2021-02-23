import crude
mydb=crude.dbutil()
mydb.init()
while(True):
    print("select")
    print("1.insert\n2.delete\n3.read\n4.update")
    ch=int(input())
    if(ch==1):
        lst=[]
        lst.append(int(input("ENter id:\n")))
        lst.append(input("Enter Name:\n"))
        lst.append(input("Enter email:\n"))
        mydb.insert(tuple(lst))
    elif(ch==2):
        print("Enter id you want to delete:\n")
        key=int(input())
        mydb.delete(key)
    elif(ch==3):
        mydb.read()
    elif(ch==4):
        print("Enter id you want to update:\n")
        id=int(input())
        print("Enter column you want to update:\n1.id\n2.name\n3.column")
        col=int(input())
        if(col==1):
            column='id'
        elif(col==2):
            column='name'
        else:
            column='email'
        print("Enter the new value in"+col+"column:\n")
        new=input()
        mydb.update(id,col,new)
    else:
        break