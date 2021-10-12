# Author: MOG 10/12/21

invest_amnt = input("What is your investment amount? ")
interest_rate = input("What is the annual interest rate (as a decimal)? ")
time = input("How many years is the money in the account? ")

future_value = float(invest_amnt) * ((1 + float(interest_rate) / 12) ** 12 * float(time))

print("The future favue of your investment after " + time + " years, is $" + str(future_value) + ".")