import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

df=pd.read_excel('s7_data_sample_rev4_50k.xlsx', sheet_name='DATA')
print("1. ОБЩИЕ ОПИСАТЕЛЬНЫЕ СТАТИСТИКИ")
print(f"Всего записей: {len(df)}")
print(f"Средняя выручка: {df['REVENUE_AMOUNT'].mean():.2f}")
print(f"Минимальная выручка: {df['REVENUE_AMOUNT'].min()}")
print(f"Максимальная выручка: {df['REVENUE_AMOUNT'].max()}")
#гистогр
plt.figure(figsize=(10,4))
plt.hist(df['REVENUE_AMOUNT'],bins=50, alpha=0.7)
plt.title("распределение выручки")
plt.xlabel('выручка')
plt.ylabel('Количество')
plt.show()

print("\n2. АНАЛИЗ АЭРОПОРТОВ")
top_airports=df['ORIG_CITY_CODE'].value_counts().head(10)
print("Топ-10 аэропортов отправления:")
print(top_airports)
#cтолбчатая дгр
plt.figure(figsize=(12,6))
top_airports.plot(kind='bar')
plt.title("'Топ-10 аэропортов отправления'")
plt.ylabel('Количество рейсов')
plt.show()

print("3. АНАЛИЗ СЕЗОННОСТИ")
df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
df['FLIGHT_DATE_LOC'] = pd.to_datetime(df['FLIGHT_DATE_LOC'])
df['MONTH']=df['FLIGHT_DATE_LOC'].dt.month
monthly_data = df.groupby('MONTH').size()
print("Количество перелетов по месяцам:")
print(monthly_data)

plt.figure(figsize=(10,4))
monthly_data.plot(kind='line', marker='o')
plt.title('Сезонность перелетов по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Количество перелетов')
plt.grid(True)
plt.show()

print("\n4. АНАЛИЗ ТИПОВ ПАССАЖИРОВ")
pax_stats=df['PAX_TYPE'].value_counts()
print("Распределение типов пассажиров:")
print(pax_stats)
pax_revenue = df.groupby('PAX_TYPE')['REVENUE_AMOUNT'].mean()
print("Средняя выручка по типам пассажиров:")
print(pax_revenue)
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
pax_stats.plot(kind='pie', autopct='%1.1f%%')
plt.title('Типы пассажиров')
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
pax_stats.plot(kind='pie', autopct='%1.1f%%')
plt.title('Типы пассажиров')

print("\n5. АНАЛИЗ СПОСОБОВ ОПЛАТЫ")
fop_stats = df['FOP_TYPE_CODE'].value_counts().head(5)
print("Топ-5 способов оплаты:")
print(fop_stats)

payment_by_sale = pd.crosstab(df['FOP_TYPE_CODE'], df['SALE_TYPE']).head(5)
print("\nСпособы оплаты по типам продаж:")
print(payment_by_sale)
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
fop_stats.head(5).plot(kind='bar')
plt.title('Топ-5 способов оплаты')
plt.ylabel('Количество')
plt.subplot(1, 2, 2)
payment_by_sale.plot(kind='bar')
plt.title('Способы оплаты по типам продаж')
plt.ylabel('Количество')
plt.legend(title='Тип продажи')
plt.tight_layout()
plt.show()

print("6. ПРОГНОЗИРОВАНИЕ")
print("Простой прогноз на основе средних значений:")
print(f"Среднее количество перелетов в месяц: {len(df) // 12}")
print(f"Средняя месячная выручка: {df['REVENUE_AMOUNT'].sum() // 12:.0f}")
monthly_trend = df.groupby('MONTH').agg({
    'REVENUE_AMOUNT': 'sum',
    'PAX_TYPE': 'count'
}).rename(columns={'PAX_TYPE': 'COUNT'})
print("\nТренд по месяцам (выручка и количество):")
print(monthly_trend)
plt.figure(figsize=(10, 4))
plt.plot(monthly_trend.index, monthly_trend['REVENUE_AMOUNT'], label='Выручка', marker='o')
plt.plot(monthly_trend.index, monthly_trend['COUNT']*10, label='Количество (x10)', marker='s')  
plt.title('Тренд выручки и количества перелетов по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Выручка / Количество')
plt.legend()
plt.grid(True)
plt.show()
