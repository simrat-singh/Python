# The function removes the spaces around the Strings on each record
def remove_white_spaces(record):
    clean_list = list()
    for item in record:
        clean_list.append(str(item).strip())
    return clean_list

# This function creates one record i.e one row to be written
# Logic applied:
# STEP 1: Creates an empty dictionary and assign values of ID and Name to it
# STEP 2: It checks exitence for each test, if it exists the the test name (Test_1,
#       Test_2, Test_4 and Test_4) is passed as key and its value is passed a value. And if
#       the test doesnt exist in the line record, 0 is passed as value in the dictionary
# STEP 3: Average for scores is calulated and passed to dictionary with
# key "Avg."


def create_record(temp_record):

    grades_dict = dict()
    grades_dict['ID'] = temp_record[0]
    grades_dict['Name'] = temp_record[1]  # STEP 1

    # STEP 2 beigns
    if 'Test_1' not in temp_record:
        grades_dict["Test_1"] = 0
    else:
        grades_dict["Test_1"] = int(
            temp_record[temp_record.index('Test_1') + 1])

    if 'Test_2' not in temp_record:
        grades_dict["Test_2"] = 0
    else:
        grades_dict["Test_2"] = int(
            temp_record[temp_record.index('Test_2') + 1])

    if 'Test_3' not in temp_record:
        grades_dict["Test_3"] = 0
    else:
        grades_dict["Test_3"] = int(
            temp_record[temp_record.index('Test_3') + 1])

    if 'Test_4' not in temp_record:
        grades_dict["Test_4"] = 0
    else:
        grades_dict["Test_4"] = int(
            temp_record[temp_record.index('Test_4') + 1])
    # STEP 2 ends

    average = (grades_dict["Test_1"] + grades_dict["Test_2"] +
               grades_dict["Test_3"] + grades_dict["Test_4"]) / 4
    grades_dict["Avg."] = average  # STEP 3
    return grades_dict

# Writes record created by function 'create_record'


def write_record(temp_record):
    print(
        "{0:^10s}|{1:^10s}|{2:^10d}|{3:^10d}|{4:^10d}|{5:^10d}|{6:^10.2f}" .format(
            temp_record['ID'],
            temp_record['Name'],
            temp_record['Test_1'],
            temp_record['Test_2'],
            temp_record['Test_3'],
            temp_record['Test_4'],
            temp_record['Avg.']))

# First method to be called
# LOGIC APPLIED:
# STEP 1: The function reads the file grades.txt
# STEP 2: Writes the top heading
# STEP 3: Splits the line read to create a list of items read
# STEP 4: Calls method 'remove_white_spaces' to remove empty spaces around each value in the list
# STEP 5: Calls method 'write_record' to write the output. 'write_record'
# internally calls 'create_record' to create each line to be written on console


def print_grades(input_file):
    grades_file = open(input_file, 'r')
    flag = True
    print("{0:<10s}|{1:^10s}|{2:^10s}|{3:^10s}|{4:^10s}|{5:^10s}|{6:^10s}" .format(
        'ID', 'Name', 'Test_1', 'Test_2', 'Test_3', 'Test_4', 'Avg'))  # STEP 2
    while flag:
        temp_record = grades_file.readline()
        if temp_record != "":
            temp_record = temp_record.split(",")  # STEP 3
            temp_record = remove_white_spaces(temp_record)  # STEP 4
            write_record(create_record(temp_record))
        else:
            flag = False


print_grades('grades.txt')
