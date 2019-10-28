#name:Kathryn McCullough
#email: kathryn,mccullough1@marist.edu
#description: If the average temperature for a day is below 60, then the number of degrees below 60 is added
#to the heating degree days. If the temperature is above 80, the amount over 80 is added to the cooling degree days.
#Write a program that accepts a sequence of average daily temperatures and computes the running total of cooling and heating degree days.



def main():
    temp= input("Please input the average daily temperatures and separate with periods (.): ")
    temp=temp.split(".")
    cool=0
    #Cooling Degree Days
    heat=0
    #Heating Degree Days

    for i in temp:
        if int(i) < 60 or int(i) > 80:
            if int(i) > 80:
                cool= cool + (int(i)-80)
                #If the temperature is above 80, the amount over 80 is added to the cooling degree days
            else:
                heat = heat + (60-int(i))
                #If the average temperature for a day is below 60, then the number of degrees below 60 is added to the heating degree days
        
    print("There will be", cool, "cooling degree days.")
    print("There will be", heat, "heating degree days.")
main()
    
