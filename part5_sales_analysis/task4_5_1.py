import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')

df = pd.read_excel('lab_4_part_5.xlsx', sheet_name='Sheet1')

df['Дата'] = pd.to_datetime(df['Дата'])
df['Количество'] = df['Количество'].astype(int)
df['Продажи'] = df['Продажи'].astype(float)
df['Себестоимость'] = df['Себестоимость'].astype(float)

df['Прибыль'] = df['Продажи'] - df['Себестоимость']
df['Рентабельность'] = df['Прибыль'] / df['Продажи'] * 100
df['Средняя_цена'] = df['Продажи'] / df['Количество']

monthly_sales = df.groupby(['Год', 'Год-мес']).agg({
    'Количество':'sum',
    'Продажи':'sum',
    'Себестоимость':'sum',
    'Прибыль':'sum'
}).reset_index()
monthly_sales['Средняя_цена'] = monthly_sales['Продажи']/monthly_sales['Количество']
monthly_sales['Рентабельность'] = monthly_sales['Прибыль']/monthly_sales['Продажи']*100
monthly_sales['Год_Мес'] = monthly_sales['Год'].astype(str) + '-' + monthly_sales['Год-мес'].astype(str).str.zfill(2)

product_monthly = df.groupby(['товар','Год-мес']).agg({
    'Количество':'sum',
    'Продажи':'sum',
    'Себестоимость':'sum',
    'Прибыль':'sum'
}).reset_index()
product_monthly['Средняя_цена'] = product_monthly['Продажи']/product_monthly['Количество']
product_monthly['Рентабельность'] = product_monthly['Прибыль']/product_monthly['Продажи']*100

point_monthly = df.groupby(['точка','Год-мес']).agg({
    'Количество':'sum',
    'Продажи':'sum',
    'Себестоимость':'sum',
    'Прибыль':'sum'
}).reset_index()
point_monthly['Средняя_цена'] = point_monthly['Продажи']/point_monthly['Количество']
point_monthly['Рентабельность'] = point_monthly['Прибыль']/point_monthly['Продажи']*100

plt.figure(figsize=(22,16))

plt.subplot(2,2,1)
for product in df['товар'].unique():
    data = product_monthly[product_monthly['товар']==product]
    plt.plot(data['Год-мес'], data['Продажи'], label=product)
plt.title('Динамика продаж по товарам')
plt.xlabel('Месяц')
plt.ylabel('Продажи')
plt.legend(fontsize=8)

plt.subplot(2,2,2)
for point in df['точка'].unique():
    data = point_monthly[point_monthly['точка']==point]
    plt.plot(data['Год-мес'], data['Продажи'], marker='o', label=point)
plt.title('Динамика продаж по точкам')
plt.xlabel('Месяц')
plt.ylabel('Продажи')
plt.legend()

plt.subplot(2,2,3)
avg_sales_point = point_monthly.groupby('точка')['Продажи'].mean().sort_values()
plt.barh(avg_sales_point.index, avg_sales_point.values)
plt.title('Средние продажи на точку в месяц')
plt.xlabel('Средние продажи')

plt.subplot(2,2,4)
plt.barh(df['товар'].value_counts().index, df.groupby('товар')['Продажи'].sum())
plt.title('Общий объем продаж по товарам')
plt.xlabel('Продажи')

plt.tight_layout()
plt.show()

last_months = monthly_sales.tail(6)
growth_rate = last_months['Продажи'].pct_change().mean()
forecast_total = last_months['Продажи'].iloc[-1]*(1+growth_rate) if growth_rate>0 else last_months['Продажи'].mean()

forecasts = {}
for product in df['товар'].unique():
    prod = product_monthly[product_monthly['товар']==product].tail(6)
    gr = prod['Продажи'].pct_change().mean()
    forecasts[product] = prod['Продажи'].iloc[-1]*(1+gr) if gr>0 else prod['Продажи'].mean()

summary_stats = {
    'Общий объем продаж': df['Продажи'].sum(),
    'Общее количество продаж': df['Количество'].sum(),
    'Средняя цена': df['Средняя_цена'].mean(),
    'Общая прибыль': df['Прибыль'].sum(),
    'Средняя рентабельность': df['Рентабельность'].mean(),
    'Количество уникальных товаров': df['товар'].nunique(),
    'Количество точек реализации': df['точка'].nunique()
}

print("Сводка ключевых показателей:")
for k,v in summary_stats.items():
    print(f"{k}: {v:,.0f}" if isinstance(v,(int,float)) else f"{k}: {v}")

print("\nПрогноз общего объема продаж на следующий месяц:", f"{forecast_total:,.0f}")
print("\nПрогноз продаж по каждому товару на следующий месяц:")
for k,v in forecasts.items():
    print(f"{k}: {v:,.0f}")
