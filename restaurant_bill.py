print("Hello,mate")
Total_bill=float(input("What is your Total bill ? \n"))

Tip=input("What percent of tip you want to give ? \n")

No_of_people=input("Among How many you want to split the bill ? \n")

#assinging lo kuda diff data types ni accept cheyadu

Tip_percentage=(float(Tip)/100)

Total_bill_after_tip=(float(Tip_percentage)+1)*float(Total_bill)

Each_person_pay=round(float(Total_bill_after_tip)/float(No_of_people),2)

print(f"Each person should contribute of : {Each_person_pay}")

print("Thank you and Have a nice day")


      