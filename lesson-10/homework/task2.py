import csv

def read_grades(file_name):
    grades = []
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Grade'] = int(row['Grade'])
            grades.append(row)
    return grades

def calculate_average(grades):
    subject_totals = {}
    subject_counts = {}
    
    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']
        
        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0
        
        subject_totals[subject] += grade
        subject_counts[subject] += 1
    
    averages = {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}
    return averages

def write_averages(file_name, averages):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, avg])

if __name__ == "__main__":
    grades = read_grades("grades.csv")
    averages = calculate_average(grades)
    write_averages("average_grades.csv", averages)
    print("Average grades written to average_grades.csv")
