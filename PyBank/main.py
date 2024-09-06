import os
import csv
csv_path = os.path.join('..', 'PyBank', 'Resources', "budget_data.csv")
csv_path1 = os.path.join('..', 'PyBank', "Analysis", "budgetanalysis.txt")

date_count = 0
total_profit_losses = 0
difference = 0
profits = []
greatest_increase = 0
greatest_decrease = 999999999999
greatest_increase_date = ""
greatest_decrease_date = ""


with open (csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    first_row = next(csvreader)
    date_count = 1
    total_profit_losses = int(first_row[1])
    previous = int(first_row[1])


    for row in csvreader:
        date = row[0]
# The total number of months included in the dataset
        date_count += 1

# The net total amount of "Profit/Losses" over the entire period
        total_profit_losses += int(row[1])

# Changes in profit/losses
        difference = int(row[1]) - previous
        previous = int(row[1])
        profits.append(difference)
       
# The greatest increase in profits (date and amount) over the entire period
        if difference > greatest_increase:
            greatest_increase = difference
            greatest_increase_date = date
# The greatest decrease in profits (date and amount) over the entire period
        if difference < greatest_decrease:
            greatest_decrease = difference
            greatest_decrease_date = date

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
avg_profit_loss = sum(profits)/len(profits)

         
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {date_count}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${avg_profit_loss:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase}) \n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")


print(output)
         
with open(csv_path1, "w") as textfile:
    textfile.write(output)
         



        
