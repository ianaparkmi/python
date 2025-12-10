#создать новую ветку и создать новое виртуальное окружение питон 3.10 сгенерироывать следующие данные виды украшений (серги кольцо подвески и тд)
# страна производитель, метал(белое золото красное золото и тд) с драгаценными камнчми или без драгоценных камней, цена за один грамм метала 
# считаем в отдельном столбце стоимость ювелирного изделия (если есть драгоценный камень то умножаем на 2) 
#визуализация по: распределение по виду украшений, распределение тех кто имеет драгоценные камни, по стране производства, график по количеству товаров и их общая стоимость (по всем видам)import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from faker import Faker

fake = Faker('ru_RU')
np.random.seed(42)

n = 50
types = ['серьги', 'кольца', 'подвески', 'браслеты', 'цепочки', 'кулоны']

данные = []
for i in range(n):
    вид = fake.random_element(types)
    страна = fake.country()
    камень = fake.random_element(['с камнем', 'без камня'])
    вес = fake.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=1, max_value=50)
    цена_грамм = fake.random_element([2500, 1500, 3000, 2800])
    
    стоимость = вес * цена_грамм
    if камень == 'с камнем':
        стоимость *= 2
    
    название_украшения = fake.word().capitalize()
    if вид == 'серьги':
        название = f"Серьги '{название_украшения}'"
    elif вид == 'кольца':
        название = f"Кольцо '{название_украшения}'"
    elif вид == 'подвески':
        название = f"Подвеска '{название_украшения}'"
    else:
        название = f"{вид.capitalize()} '{название_украшения}'"
    
    данные.append({
        'ID': i + 1,
        'Название': название,
        'Вид': вид,
        'Страна': страна,
        'Камень': камень,
        'Вес_г': вес,
        'Цена_за_грамм': цена_грамм,
        'Стоимость': round(стоимость, 2),
        'Металл': fake.random_element(['золото', 'серебро', 'белое золото', 'красное золото']),
    })

df = pd.DataFrame(данные)
print(df)
распределение_виды = df['Вид'].value_counts()
типы = распределение_виды.index
количество = распределение_виды.values

с_камнем = []
без_камня = []
for t in типы:
    mask = df['Вид'] == t
    с_камнем.append(df.loc[mask & (df['Камень'] == 'с камнем'), 'Стоимость'].count())
    без_камня.append(df.loc[mask & (df['Камень'] == 'без камня'), 'Стоимость'].count())

количество_по_видам = []
стоимость_по_видам = []
for t in типы:
    mask = df['Вид'] == t
    количество_по_видам.append(mask.sum())
    стоимость_по_видам.append(df.loc[mask, 'Стоимость'].sum() / 1000)

fig = plt.figure(figsize=(16, 12))

ax1 = plt.subplot(2, 2, 1)
bars1 = ax1.bar(типы, количество, color='pink')
ax1.set_title('Количество украшений по видам')
ax1.set_xlabel('Вид украшения')
ax1.set_ylabel('Количество, шт')

for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', color='black')

ax2 = plt.subplot(2, 2, 2)

x = np.arange(len(типы))
width = 0.4
bars2_with = ax2.bar(x - width/2, с_камнем, width, label='С камнем', color='gold')
bars2_without = ax2.bar(x + width/2, без_камня, width, label='Без камня', color='silver')
ax2.set_title('Наличие камней по видам украшений')
ax2.set_xlabel('Вид украшения')
ax2.set_ylabel('Количество, шт')
ax2.set_xticks(x)
ax2.set_xticklabels(типы, rotation=45, ha='right')
ax2.legend()

for bars in [bars2_with, bars2_without]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                     f'{int(height)}', ha='center', va='bottom', color='black')

ax3 = plt.subplot(2, 2, 3)
top_страны = df['Страна'].value_counts().head(6)
ax3.pie(top_страны.values, labels=top_страны.index, autopct='%1.0f%%', 
        colors=['lightblue', 'lightgreen', 'pink', 'yellow', 'orange', 'gray'])
ax3.set_title('Топ-6 стран производства')

ax4 = plt.subplot(2, 2, 4)

bars4 = ax4.bar(типы, количество_по_видам, width=0.6, color='lightblue', label='Количество (шт)')
ax4.set_xlabel('Вид украшения')
ax4.set_ylabel('Количество, шт')
ax4.tick_params(axis='y')

for bar in bars4:
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', color='black')

ax4_secondary = ax4.twinx()
line = ax4_secondary.plot(типы, стоимость_по_видам, color='red', marker='o', 
                          linewidth=2, markersize=8, label='Стоимость (тыс. руб)')
ax4_secondary.set_ylabel('Стоимость, тыс. руб')
ax4_secondary.tick_params(axis='y')

for i, (t, val) in enumerate(zip(типы, стоимость_по_видам)):
    ax4_secondary.text(i, val + (max(стоимость_по_видам)*0.02),
                       f'{val:.0f}', ha='center', va='bottom', color='black')

ax4.set_title('Количество и стоимость проданного по видам')
plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45, ha='right')

lines_labels = [bars4, line[0]]
labels = ['Количество (шт)', 'Стоимость (тыс. руб)']
ax4.legend(lines_labels, labels, loc='upper left')

plt.tight_layout()
plt.show()