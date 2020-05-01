''' To Use This Hotel Management Program
    First Create Database named hotel
    Second Create Tables namely
    1. Customer_data
    2. Room_rent
    3. restaurentbill
    4. laundrybill
    5. gamebill
    6. grandbill
'''

# For error free Runnig of Program

import datetime

import mysql.connector as sql

import random

t_date = datetime.date.today()      # Will import today's date
year = t_date.year                  # Will import year 

mydb = sql.connect(host = 'localhost', user = 'root', passwd = 'admin')
if mydb.is_connected == False:
    print("Error in connecting Mysql")
else:
    print("Connected to Sql database")
cursor = mydb.cursor()



l = []
cursor.execute("Show databases")
print("\n\t\t****** Databases  ******")
for xy in cursor:
    l.append(*xy)
name_d = "hotel2"
for a in range(len(l)):
    if (l[a] == name_d):
        print(f"Database {name_d} Selected")
        
if name_d not in l:
    print("\nDatabase doesn't exist ")
    print("Press Enter to Create Database")
    Cd = input()
    while Cd =="":
        cursor.execute("Create database hotel2")
        print("Database hotel2 Created")
        break
    cursor.execute("Use hotel2")

    cursor.execute("Create table customer_data(NAME varchar(15), ADDRESS char(25), CHECKINDATE varchar(10),CHECKOUTDATE varchar(10), ROOMNO int Primary key, Year int)")
    print("Table customer_data Created")

    cursor.execute("Create table gamebill(GameMenu varchar(20),Price int, HoursPlayed int, Cost int, Roomno int, foreign key(Roomno) references Customer_data(Roomno))")
    print("Table gamebill Created")

    cursor.execute("Create table grandbill(Name varchar(20), Address varchar(25), Checkindate varchar(12), Checkoutdate varchar(12), Roomrent int, Restaurentbill int, Laundrybill int, Gamebill int, Subtotal int, Grandtotalbill int, Roomno int, foreign key(Roomno) references Customer_data(Roomno))")
    print("Table grandbill Created")

    cursor.execute("Create table laundrybill(Item varchar(20), Price int, Quantity int, Rate int, Roomno int, foreign key(Roomno) references Customer_data(Roomno))")
    print("Table laundrybill Created")

    cursor.execute("Create table restaurentbill(Item varchar(15), Price int, Quantity int, Rate int, Roomno int, foreign key(Roomno) references Customer_data(Roomno))")
    print("Table restaurentbill Created")

    cursor.execute("Create table room_rent(RoomType char(2), Roomrent int, Roomno int, foreign key(Roomno) references Customer_data(Roomno))")
    print("Table room_rent Created")


cursor.execute("Use hotel2")
print ("\n\n*****WELCOME TO HEWING HOTEL*****\n")

a = []
roomno = []
rt = ""
gt = ''
r = 0
s = 0
p = 0
t = 0
name = ''
address = ''
cindate = ''
coutdate = ''

a = 1800

rno = 0
rint = []

def inputdata():
    global address
    
    global name
    global cindate
    global coutdate
    
    
    name = input("\nEnter your name:")
    
    address = input("\nEnter your address:")
    
    cindate = input("\nEnter your check in date and month:")
    
    coutdate = input("\nEnter your checkout date and month:")
    
    print("\n\t\t\tNAME : ",name.upper(),"\n\t\t\tADDRESS : ",address,"\n\t\t\tCHECK IN DATE : ",cindate,"\n\t\t\tCHECK OUT DATE : ",coutdate)
    
    global rno
    rno = random.randint(0,200)
    roomno.append(rno)
    print("\n\t\t\tYour Room No.:",rno,"\n")
    cursor.execute("Select Roomno from customer_data")
    for z in cursor:
        rint.append(*z)
    for q in rint:
        if q == rno:
            print("Room no already Occupied")
            w = q
            break
       
        if w != rno:               
            data = "Insert into customer_data values('{}', '{}', '{}', '{}', {}, {})".format(name, address, cindate, coutdate, rno, year)
            cursor.execute(data)
            mydb.commit()
            print("\n\t\t\tCustomer_Data Added")
    rno = roomno.pop(0)
    
    
    
  
    
def roomrent():
    global s
    global rno
    global roomno

    print ("We have the following rooms for you:-")

    print ("1.  type A---->rs 6000 PN\-")

    print ("2.  type B---->rs 5000 PN\-")
 
    print ("3.  type C---->rs 4000 PN\-")

    print ("4.  type D---->rs 3000 PN\-")

    
    x = int(input("Enter Your Choice Please->"))

    n = int(input("\t\t\tFor How Many Nights Did You Stay:"))

    
        
    if(x==1):

        print ("\t\t\tyou have opted room type A")
        x = "A"
        s = 6000*n
        print("\t\t\t",s,"Room type : ",x)

    elif (x==2):

        print ("\t\t\tyou have opted room type B")
        x = "B"
        s = 5000*n
        print("\t\t\t",s,"Room type : ",x)

    elif (x==3):

        print ("\t\t\tyou have opted room type C")
        x = "C"
        s = 4000*n
        print("\t\t\t",s,"Room type : ",x)

    elif (x==4):
        print ("\t\t\tyou have opted room type D")
        x = "D"
        s = 3000*n
        print("\t\t\t",s,"Room type : ",x)
        

    else:

        print ("please choose a room")


    print ("\t\t\tyour room rent is =",s,"\n")
    rent = "Insert into room_rent values('{}', {}, {})".format(x, s, rno)
    cursor.execute(rent)
    mydb.commit()
    print("\t\tRoom rent Updated ")




def restaurentbill():
    global r
    global rno
    global roomno
    print("\t\t\t*****RESTAURANT MENU*****")

    print("\n1.water----->Rs20","\n2.tea----->Rs10","\n3.breakfast combo--->Rs90","\n4.lunch---->Rs110","\n5.dinner--->Rs150","\n6.Exit")


    while (1):
        
        c = int(input("Enter your choice:"))


        if (c==1):
            d = int(input("Enter the quantity:"))
            r = r+20*d
            item = "Water"
            price = 20
            foodbill = "Insert into restaurentbill values('{}', {}, {}, {}, {})".format(item, price, d, r, rno)
            cursor.execute(foodbill)
            mydb.commit()

        elif (c==2):
            d = int(input("Enter the quantity:"))
            r = r+10*d
            item = "Tea"
            price = 10
            foodbill = "Insert into restaurentbill values('{}', {}, {}, {}, {})".format(item, price, d, r, rno)
            cursor.execute(foodbill)
            mydb.commit()

        elif (c==3):
            d = int(input("Enter the quantity:"))
            r = r+90*d
            item = "Breakfast Combo"
            price = 90
            foodbill = "Insert into restaurentbill values('{}', {}, {}, {}, {})".format(item, price, d, r, rno)
            cursor.execute(foodbill)
            mydb.commit()

        elif (c==4):
            d = int(input("Enter the quantity:"))
            r = r+110*d
            item = "Lunch"
            price = 110
            foodbill = "Insert into restaurentbill values('{}', {}, {}, {}, {})".format(item, price, d, r, rno)
            cursor.execute(foodbill)
            mydb.commit()


        elif (c==5):
            d = int(input("Enter the quantity:"))
            r = r+150*d
            item = "Dinner"
            price = 150
            foodbill = "Insert into restaurentbill values('{}', {}, {}, {}, {})".format(item, price, d, r, rno)
            cursor.execute(foodbill)
            mydb.commit()

        elif (c==6):
            break

        else:
            print("Invalid option")
        
        
    
    
    print ("\t\tTotal food Cost=Rs",r,"\n")
    print("\t\tRestaurent bill Updated ")


def laundrybill():
    global t
    global rno
    global roomno
    print ("\t\t\t******LAUNDRY MENU*******")

    print ("\n1.Shorts----->Rs3","\n2.Trousers----->Rs4","\n3.Shirt--->Rs5","\n4.Jeans---->Rs6","\n5.Girlsuit--->Rs8","\n6.Exit")

    while (1):

        e = int(input("Enter your choice:"))

        if (e==1):
            f = int(input("Enter the quantity:"))
            t = t+3*f
            item = "Shorts" 
            price = 3
            clothebill = "Insert into laundrybill values('{}', {}, {}, {}, {})".format(item, price, f, t,rno)
            cursor.execute(clothebill)
            mydb.commit()

        elif (e==2):
            f = int(input("Enter the quantity:"))
            t = t+4*f
            item = "Trousers"
            price = 4
            clothebill = "Insert into laundrybill values('{}', {}, {}, {}, {})".format(item, price, f, t,rno)
            cursor.execute(clothebill)
            mydb.commit()

        elif (e==3):
            f = int(input("Enter the quantity:"))
            t = t+5*f
            item = "Shirt"
            price = 5
            clothebill = "Insert into laundrybill values('{}', {}, {}, {}, {})".format(item, price, f, t,rno)
            cursor.execute(clothebill)
            mydb.commit()

        elif (e==4):
            f = int(input("Enter the quantity:"))
            t = t+6*f
            item = "Jeans"
            price = 6
            clothebill = "Insert into laundrybill values('{}', {}, {}, {}, {})".format(item, price, f, t,rno)
            cursor.execute(clothebill)
            mydb.commit()

        elif (e==5):
            f = int(input("Enter the quantity:"))
            t = t+8*f
            item = "Girlsuit"
            price = 8
            clothebill = "Insert into laundrybill values('{}', {}, {}, {}, {})".format(item, price, f, t,rno)
            cursor.execute(clothebill)
            mydb.commit()

        elif (e==6):
            break
        else:

            print ("Invalid option")


    print ("\t\tTotal Laundary Cost=Rs",t,"\n")
    print("\t\tLaundry Bill Updated ")

def gamebill():
    global p
    global rno
    global roomno
    print ("\t\t\t******GAME MENU*******")

    print ("\n1.Table tennis----->Rs60","\n2.Bowling----->Rs80","\n3.Snooker--->Rs70","\n4.Video games---->Rs90","\n5.Pool--->Rs50","\n6.Exit")



    while (1):

            
        g = int(input("Enter your choice:"))


        if (g==1):
            h = int(input("No. of hours:"))
            p = p+60*h
            item = "Table tennis"
            price = 60
            gbill = "Insert into gamebill values('{}', {}, {}, {}, {})".format(item, price, h, p ,rno)
            cursor.execute(gbill)
            mydb.commit()

        elif (g==2):
            h = int(input("No. of hours:"))
            p = p+80*h
            item = "Bowling"
            price = 80
            gbill = "Insert into gamebill values('{}', {}, {}, {}, {})".format(item, price, h, p ,rno)
            cursor.execute(gbill)
            mydb.commit()


        elif (g==3):
            h = int(input("No. of hours:"))
            p = p+70*h
            item = "Snooker"
            price = 70
            gbill = "Insert into gamebill values('{}', {}, {}, {}, {})".format(item, price, h, p ,rno)
            cursor.execute(gbill)
            mydb.commit()


        elif (g==4):
            h = int(input("No. of hours:"))
            p = p+90*h
            item = "Video games"
            price = 90
            gbill = "Insert into gamebill values('{}', {}, {}, {}, {})".format(item, price, h, p ,rno)
            cursor.execute(gbill)
            mydb.commit()


        elif (g==5):
            h = int(input("No. of hours:"))
            p = p+50*h
            item = "Pool"
            price = 50
            gbill = "Insert into gamebill values('{}', {}, {}, {}, {})".format(item, price, h, p ,rno)
            cursor.execute(gbill)
            mydb.commit()


        elif (g==6):
            break

        else:

            print ("Invalid option")



    print ("\t\tTotal Game Bill=Rs",p,"\n")
    print("\t\tGame bill Updated ")

def display():
    global rno
    global roomno
    
    print ("\t\t\t******HOTEL BILL******")

    print ("\t\t\tCustomer details:")

    print ("\nCustomer name:",name)

    print ("\nCustomer address:",address)

    print ("\nCheck in date:",cindate)

    print ("\nCheck out date",coutdate)

    print ("\nRoom no.",rno)

    print ("\nYour Room rent is:",s)

    print ("\nYour Food bill is:",r)

    print ("\nYour laundary bill is:",t)
    print ("\nYour Game bill is:",p)

    rt=s+t+p+r

    print ("Your sub total bill is:",rt)
    print ("Additional Service Charges is",a)
    gt = rt + a

    print ("Your grandtotal bill is:",gt,"\n")
    
    grndbill = "Insert into grandbill values('{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {})".format(name, address, cindate, coutdate, s, r, t, p, rt, gt, rno)
    cursor.execute(grndbill)
    mydb.commit()

            

        

        

def main():
    
    
    
    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate rommrent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Calculate gamebill")

        print("6.Show total cost")

        print("7.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            inputdata()

        elif (b==2):

            roomrent()

        elif (b==3):

            restaurentbill()

        elif (b==4):

            laundrybill()

        elif (b==5):

            gamebill()

        elif (b==6):

            display()

        elif (b==7):

            quit()
        else:
            print("Wrong input ")

main()







