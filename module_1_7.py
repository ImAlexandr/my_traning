grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Sr_bal=dict()
students=sorted(students)
n = 0
while n < len(grades):
    bal=sum(grades[n])/len(grades[n])
    Sr_bal.update({students[n]:bal})
    n += 1
print(Sr_bal)