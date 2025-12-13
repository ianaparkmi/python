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
counts, bins, patches = plt.hist(df['REVENUE_AMOUNT'], bins=50, alpha=0.7)
for count, patch in zip(counts, patches):
    if count > 0:
        plt.text(
            patch.get_x() + patch.get_width() / 2,
            count,
            int(count),
            ha='center',
            va='bottom',
            fontsize=7
        )

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
for i, v in enumerate(top_airports.values):
    plt.text(i, v, v, ha='center', va='bottom')
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
for x, y in zip(monthly_data.index, monthly_data.values):
    plt.text(x, y, y, ha='center', va='bottom')
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

print("\n5. АНАЛИЗ СПОСОБОВ ОПЛАТЫ")
fop_stats = df['FOP_TYPE_CODE'].value_counts().head(5)
print("Топ-5 способов оплаты:")
print(fop_stats)

payment_by_sale = pd.crosstab(df['FOP_TYPE_CODE'], df['SALE_TYPE']).head(15)
print("\nСпособы оплаты по типам продаж:")
print(payment_by_sale)
plt.figure(figsize=(12, 4))

ax1 = plt.subplot(1, 2, 1)
fop_stats.head(5).plot(kind='bar', ax=ax1)
for p in ax1.patches:
    ax1.annotate(
        int(p.get_height()),
        (p.get_x() + p.get_width() / 2, p.get_height()),
        ha='center',
        va='bottom'
    )
ax1.set_title('Топ-5 способов оплаты')
ax1.set_ylabel('Количество')
ax2 = plt.subplot(1, 2, 2)
payment_by_sale.plot(kind='bar', ax=ax2)
for p in ax2.patches:
    if p.get_height() > 0:
        ax2.annotate(
            int(p.get_height()),
            (p.get_x() + p.get_width() / 2, p.get_height()),
            ha='center',
            va='bottom',
            fontsize=8
        )
ax2.set_title('Способы оплаты по типам продаж')
ax2.set_ylabel('Количество')
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
for x, y in zip(monthly_trend.index, monthly_trend['REVENUE_AMOUNT']):
    plt.text(x, y, f'{int(y)}', ha='center', va='bottom')
plt.plot(monthly_trend.index, monthly_trend['COUNT']*10, label='Количество (x10)', marker='s')  
for x, y in zip(monthly_trend.index, monthly_trend['COUNT'] * 10):
    plt.text(x, y, f'{int(y/10)}', ha='center', va='bottom')
plt.title('Тренд выручки и количества перелетов по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Выручка / Количество')
plt.legend()
plt.grid(True)
plt.show()
