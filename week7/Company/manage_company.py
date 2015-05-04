import sqlite3

connection = sqlite3.connect('company.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

options=[
    'list_employees',
    'monthly_spending',
    'yearly_spending',
    'add_employee',
    'delete_employee',
    'update_employee'
]

print('You have the following options:')
for opt in options:
    print(opt)

list_employees = """
SELECT id, name, position FROM users ORDER BY id;
"""

monthly_spending = """
SELECT sum(monthly_salary) as monthly_sum FROM users;
"""

yearly_spending = """
SELECT sum(monthly_salary * 12) as yearly_sum FROM users;
"""


while True:
    choice = input('command>')
    if str(choice) not in options:
        print('Bad command. Please input some of the options.')
        continue
    break

if choice == 'list_employees':
    result = cursor.execute(list_employees).fetchall()

    for row in result:
        print('{}. {} - {}'.format(row[0], row[1], row[2]))

if choice == 'monthly_spending':
    result = cursor.execute(monthly_spending)
    row = result.fetchone()
    print("The company is spending ${} every month!".format(row['monthly_sum']))

if choice == 'yearly_spending':
    result = cursor.execute(yearly_spending)
    row = result.fetchone()
    print("The company is spending ${} every year!".format(row['yearly_sum']))

if choice == 'add_employee':
    new_name = str(input('name>'))
    new_monthly_salary = int(input('monthly_salary>'))
    new_yearly_bonus = int(input('yearly_bonus>'))
    new_position = str(input('position>'))
    cursor.execute("""INSERT INTO users(name, monthly_salary, yearly_bonus, position) \
        values(?, ?, ?, ?);""", (new_name, new_monthly_salary, new_yearly_bonus, new_position))

if choice == 'delete_employee':
    employee_id = int(input('id>'))
    name_emp = cursor.execute(""" SELECT name FROM users WHERE id = '%d' """ % employee_id)
    result = name_emp.fetchone()
    cursor.execute("""
        DELETE FROM users WHERE id = '%d'
        """  % employee_id)
    print("{} wasa deleted".format(result['name']))

if choice == 'update_employee':
    upd_id = int(input('id>'))
    upd_name = str(input('name>'))
    upd_monthly_salary = int(input('monthly_salary>'))
    upd_yearly_bonus = int(input('yearly_bonus>'))
    upd_position = str(input('position>'))
    cursor.execute("""
        UPDATE users SET name = '%s', monthly_salary = '%d',
        yearly_bonus = '%d', position = '%s' WHERE id='%d'""" % (upd_name, upd_monthly_salary,
        upd_yearly_bonus, upd_position, upd_id))


connection.commit()
