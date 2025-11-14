import numpy as np

def money():
    print("Enter your travel expenses for the past 12 months:")
    money=np.array([250, 230, 240, 220, 210, 200, 
                        190, 195, 205, 220, 250, 260])
    month=['January','February','March', 'April','May', 'June',
'July','August','September','October','November','December']
    print('expenses by month')

    for i in range(len(month)):
        print(f'month:{month[i]} - {money[i]} byn')

    winter_index=np.array([11,0,1])
    summer_index=np.array([5,6,7])
    winter_cost=money[winter_index]
    summer_cost=money[summer_index]
    all_win_cost=np.sum(winter_cost)
    all_sum_cost=np.sum(summer_cost)

    print('comparison')
    print(f'All winter expenses: {all_win_cost} ')
    print(f'All summer expenses: {all_sum_cost} ')

    if all_win_cost > all_sum_cost:
        print("more money is spent on transportation during the winter season")
    elif all_sum_cost> all_win_cost:
        print("more money is spent on transportation during the summer season")
    else:
        print("expenses in winter and summer are the same")

    max_expense= np.max(money)
    max_index=np.where(money==max_expense)[0]

    print(f'max expense: {max_expense}')
    print(f' name of month: {[month[i] for i in max_index]}')
    print(f' namber of month: {max_index+1}')

money()