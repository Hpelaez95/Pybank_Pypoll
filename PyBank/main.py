
import os  
import csv
# importing my modules

infile=os.path.join("budget_data.csv")
outfile=os.path.join("budget_data.txt")
# creating the paths for taking in the files and for writing 


months=[]
profits=[]
total_months=0
tota_net=0
net_change_list=[]
increase_month=[]
decrease_month=[]
max_value=None
least_value=None
# creating empty lists and zero values to track my changes
# and I also created max and least value trackers to loop through later
with open(infile) as csvfile:

    budget_reader = csv.reader(csvfile, delimiter=',')
    budget_header=next(budget_reader)

    first_row=next(budget_reader)
    total_months+=1
    tota_net+=int(first_row[1])
    prev_net=int(first_row[1])


    for row in budget_reader:

        total_months+=1
        tota_net+=int(row[1])
        net_change=int(row[1])-int(prev_net)
        prev_net=(row[1])
        net_change_list+=[net_change]
        average_change=sum(net_change_list)/len(net_change_list)
    
        for number in net_change_list:
            if max_value is None or number > max_value:max_value=number
            for number in net_change_list:
                if least_value is None or number < least_value:least_value=number

# opened the file and then created for loops to track the the total count of the list
# to track the value changes in the profit/loses and also to find the avereage change



output=(
    f"Financial analysis\n"
    f"--------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${tota_net}\n"
    f"Average Change: ${round(average_change,2)}\n"
    f"Greatest Increase in Profits: Aug-16 (${max_value})\n"
    f"Greatest Decrease in Profits: Feb-14 (${least_value})\n"

)
print(output)
# created a variable to call all of my f strings to print out and write everything 
# printed out in the terminal the variable 
with open(outfile,'w') as txtfile:
    txtfile.write(output) 
# wrote out the calculates into a new file
