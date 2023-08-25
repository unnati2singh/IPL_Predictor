import csv


def load_data():
    data = []
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data


def suggest_career_options(data, skills):
    suggested_careers = []
    for career in data:
        required_skills = career['Skills Required'].split(', ')
        if all(skill.lower() in skills for skill in required_skills):
            suggested_careers.append(career['Career Option'])
    return suggested_careers


# Replace 'career_data.csv' with the path to your CSV file
file_path = 'career_data.csv'
career_data = load_data(file_path)

user_skills = input(
    "Enter your skills (comma-separated): ").lower().split(', ')

suggested_options = suggest_career_options(career_data, user_skills)

if suggested_options:
    print("Suggested career options:")
    for option in suggested_options:
        print(option)
else:
    print("No matching career options found.")
