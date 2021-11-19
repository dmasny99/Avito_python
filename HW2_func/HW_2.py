import csv


def get_hierarchy(path: str = 'Corp Summary.csv') -> dict:
    """Gets the hierarchy of a department"""
    hierarchy_dict = {}
    with open(path, 'r', encoding='utf-8') as f:
        file = csv.reader(f, delimiter=';')
        next(file,)  # skip the header
        for row in file:
            if row[1] not in hierarchy_dict:  # row[1] is a department
                # row=[2] is a command inside the department
                hierarchy_dict[row[1]] = [row[2]]
            elif row[1] in hierarchy_dict and row[2] not in hierarchy_dict[row[1]]:
                hierarchy_dict[row[1]].append(row[2])
    return hierarchy_dict


def print_in_cool_way(bullet_point: str = '---', prefixes: list = [], **parametrs):
    """Prints values from a dict with custom bullet points"""
    for key in parametrs:
        print(key)
        if len(prefixes) != 0:
            for index, param in enumerate(parametrs[key]):
                print(bullet_point, prefixes[index], param)
        else:
            for param in parametrs[key]:
                print(bullet_point, param)


def get_report(path: str = 'Corp Summary.csv') -> dict:
    """Creates a report dict {'department':[number of workwers, min salary, max salary, avg salary]}"""
    report = {}
    with open(path, 'r', encoding='utf-8') as f:
        file = csv.reader(f, delimiter=';')
        next(file,)  # skip the header
        for row in file:
            if row[1] not in report:  # row[1] is a department
                report[row[1]] = [1, int(row[5]), int(row[5]), int(row[5])]
            elif row[1] in report:
                report[row[1]][0] = report[row[1]][0] + 1
                if int(row[5]) <= report[row[1]][1]:
                    report[row[1]][1] = int(row[5])
                else:
                    report[row[1]][1] = int(row[5])
                report[row[1]][3] = report[row[1]][3] + int(row[5])
    for key in report:
        report[key][3] = report[key][3]//report[key][0]
    return report


def write_report(report: dict):
    """Writes report to CSV"""
    with open("Report.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=";", lineterminator="\n")
        file_writer.writerow(
            ['Department', 'Number of workwers', 'Min salary', 'Max salary', 'Avg salary'])
        for key in report:
            file_writer.writerow([key]+report[key])


def greet_user():
    """Shows available commands and performs it"""
    print('''Hello!
             1 - Get the hierarchy of a department
             2 - Get the summary report from departments
             3 - Save the report
             Insert the number:''')
    valid_numbers = ['1', '2', '3']
    while True:
        command = input()
        if command not in valid_numbers:
            print('I dont understand you')
        if command == '1':
            print_in_cool_way(**get_hierarchy())
        elif command == '2':
            print_in_cool_way(prefixes=[
                'Number of workwers:', 'Min salary:', 'Max salary', 'Avg salary:'], **get_report())
        else:
            write_report(get_report())

if __nmae__ == '__main__':
    greet_user()
