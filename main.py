

def print_list_col(arr):
    for i, num in enumerate(arr):
        print(f"i-{i}, num-{num}")


def print_list_row_i_val(arr):
    row = ""
    for i, num in enumerate(arr):
        row += f"[{i}/{num}], "
    print(row)


arr = [1,5,10,14,20,6,8,10]

print_list_row_i_val(arr)

students_grades = [8,9,10,10,4,8,10,3,8,5,8]

print_list_row_i_val(students_grades)

print_list_col(students_grades)

print_list_col(students_grades)









