grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# упорядочим множество
students_1 = list(students)
students_sort = sorted(students_1)

# вычислим средний бал
a = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]),
     sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]

# составляем словарь
dictionary = {students_sort: a for students_sort, a in zip(students_sort, a)}
print(dictionary)
