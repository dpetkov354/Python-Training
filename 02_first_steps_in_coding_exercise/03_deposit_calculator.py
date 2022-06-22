# 3 Deposit Calculator
deposited_value = float(input())
number_monthly_payments = float(input())
interest_rate = float(input())
interest_sum = deposited_value * (interest_rate / 100)
monthly_interest = interest_sum / 12
total_sum = deposited_value + (number_monthly_payments * monthly_interest)
print(f'Сума в края на срока: {total_sum} лв.')
