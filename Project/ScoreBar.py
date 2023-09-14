import matplotlib.pyplot as Plt
import numpy as Np

# Score Bar

Scores = Np.random.randint(0, 20, 100)
print('Scores:\n', Scores)

Scores_Bool = Scores >= 10
Passed = Scores[Scores_Bool]
Failed = Scores[~Scores_Bool]
print('Passed Scores:\n', Passed)
print('Failed Scores:\n', Failed)

Data = {'0 - 9': list(filter(lambda X: X < 10, Failed)),
        '10 - 12': list(filter(lambda X: X <= 12, Passed)),
        '12 - 14': list(filter(lambda X: 12 < X <= 14, Passed)),
        '14 - 16': list(filter(lambda X: 14 < X <= 16, Passed)),
        '16 - 18': list(filter(lambda X: 16 < X <= 18, Passed)),
        '18 - 20': list(filter(lambda X: 18 < X <= 20, Passed)),
        }
print('Sorted Scores:\n', Data)

Key_Name = list(Data.keys())
Value_Len = []
for i in list(Data.values()):
    Value_Len.append(len(i))
Total_Points = 0
for i in list(Data.values()):
    for j in i:
        Total_Points += j
Value_AVG = Total_Points / 100
Key_Name.append('AVG')
Value_Len.append(Value_AVG)

Plt.bar(Key_Name, Value_Len)
Plt.show()
