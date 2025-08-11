name = input()
age = int(input())
salary = int(input())
bonus_percent = float(input())
print('Employee Name:', name)
print('Age:', age)
print('Monthly Salary: $' + str(salary))
annual_salary_without_bonus = salary * 12
annual_bonus_amount = 12 * salary * bonus_percent
annual_salary_with_bonus = annual_salary_without_bonus + annual_bonus_amount
print('Annual Salary (without bonus):', annual_salary_without_bonus)
print('Annual Bonus Amount:', annual_bonus_amount)
print('Total Annual Salary (with bonus): $' + str(annual_salary_with_bonus))
