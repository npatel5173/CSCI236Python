#display total monthly cost 
def total_monthly_cost(loan_payment, insurance, gas, oil, tires, maintenance):
  monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance 
  print('Your total monthly cost is', format(monthly_cost, ',.2f'))
  
#display total annual cost  
def total_annual_cost(loan_payment, insurance, gas, oil, tires, maintenance):
  annual_cost = (loan_payment + insurance + gas + oil + tires + maintenance) * 12
  print('Your total annual cost is', format(annual_cost, ',.2f'))

#user input monthly cost for automobile 
print('Enter your monthly expenses incurred from your automobile.')
#loan payment expenses 
loan_payment = float(input('Loan payment: '))
#insurance expenses 
insurance = float(input('Car insurance: '))
#gas expenses
gas = float(input('Gas: '))  
#oil expenses
oil = float(input('Oil: '))
#tires expenses
tires = float(input('Tires: '))
#maintenance expenses
maintenance = float(input('Maintenance: ')) 

#call monthly and annual costs
total_monthly_cost(loan_payment, insurance, gas, oil, tires, maintenance)
total_annual_cost(loan_payment, insurance, gas, oil, tires, maintenance)
