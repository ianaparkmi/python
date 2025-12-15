import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random

fake = Faker('ru_RU')
random.seed(0)
np.random.seed(0)
YEARS = [2021, 2022, 2023, 2024, 2025]
SPECIALTIES = [
    'Computer Science',
    'Economics', 
    'Law',
    'Medicine',
    'Civil Engineering',
    'Psychology',
    'Philology'
]
SUBJECTS = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Russian Language', 'Foreign Language']
EDUCATION_FORMS = ['Budget', 'Paid', 'Targeted']

def generate_student(num_students=50):
    students=[]
    for _ in range(num_students):
        year=random.choice(YEARS)
        specialty=random.choice(SPECIALTIES)
        ct_scores = {}
        for subject in SUBJECTS:
            for _ in range(100):
                if subject in ['Mathematics', 'Physics']:
                    ct_scores[subject] = random.randint(75, 100)
                elif subject in ['Medicine', 'Chemistry']:
                    ct_scores[subject] = random.randint(70, 95)
                else:
                    ct_scores[subject] = random.randint(65, 90)
        certificate_score = random.uniform(7.5, 10.0)
        sorted_scores = sorted(ct_scores.values(), reverse=True)
        top_3_scores = sorted_scores[:3]
        ct_total = sum(top_3_scores)
        cert_scaled = certificate_score * 10
        total_score = ct_total + cert_scaled
        student = {
            'Full Name': fake.name(),
            'Admission Year': year,
            'Education Form': random.choice(EDUCATION_FORMS),
            'Test Scores': ct_scores,
            'Certificate Average': certificate_score,
            'Total Score': round(total_score, 2),
            'Specialty': specialty,
            'Registration Address': fake.city(),
            'Phone Number': fake.phone_number()
        }
        students.append(student)
    return students

def graph():
    plt.figure(figsize=(15,15))
    # средний балла ЦТ по предметам
    plt.subplot(2, 3, 1)
    ct_data = []
    for year in YEARS:
        year_data = df[df['Admission Year'] == year]
        for subject in SUBJECTS:
            avg_score = year_data['Test Scores'].apply(lambda x: x[subject]).mean()
            ct_data.append({'Year': year, 'Subject': subject, 'Average Score': avg_score})
    
    test_df = pd.DataFrame(ct_data)
    
    for subject in SUBJECTS:
        subject_data = test_df[test_df['Subject'] == subject]
        plt.plot(subject_data['Year'], subject_data['Average Score'], marker='o', label=subject)
    
    plt.title('Average Test Scores by Subject (2021-2023)')
    plt.xlabel('Year')
    plt.ylabel('Average Score')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(YEARS)
    plt.grid(True)
 #  средний балл аттестата
    plt.subplot(2, 3, 2)
    certificate_trend = df.groupby('Admission Year')['Certificate Average'].mean()
    plt.plot(certificate_trend.index, certificate_trend.values, marker='o', color='red', linewidth=2)
    plt.title('Certificate Average Score Trend')
    plt.xlabel('Year')
    plt.ylabel('Certificate Average Score')
    plt.xticks(YEARS)
    plt.grid(True)
# 3. Динамика проходного балла по специальностям
    plt.subplot(2, 3, 3)
    passing_scores = df.groupby(['Admission Year', 'Specialty'])['Total Score'].min().unstack()
    passing_scores.plot(ax=plt.gca(), marker='o', linewidth=2)
    plt.title('Dynamics of Passing Scores by Specialty', fontsize=14, fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Passing Score')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(YEARS)
    plt.grid(True, alpha=0.3)

# 4. Количество поступивших по специальностям
    plt.subplot(2, 3, 4)
    specialty_counts = df.groupby(['Admission Year', 'Specialty']).size().unstack()
    specialty_counts.plot(kind='bar', ax=plt.gca(), width=0.8)
    plt.title('Number of students by specialty', fontsize=14, fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Number of students')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)

 # 5. Статистика по формам обучения
    plt.subplot(2, 3, 5)
    form_counts = df.groupby(['Admission Year', 'Education Form']).size().unstack()
    form_counts.plot(kind='bar', ax=plt.gca(), width=0.8)
    plt.title('Distribution by education Form', fontsize=14, fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Number of students')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)

# 6. Распределение общего балла по годам
    plt.subplot(2, 3, 6)
    for year in YEARS:
        year_data = df[df['Admission Year'] == year]['Total Score']
        plt.hist(year_data, alpha=0.6, label=str(year), bins=20)
    plt.title('Distribution of total scores by year', fontsize=14, fontweight='bold')
    plt.xlabel('Total score')
    plt.ylabel('Number of students')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

students_data = generate_student(500)
df = pd.DataFrame(students_data)
graph()