import pandas as pd
import matplotlib.pyplot as plt

# Dane wejściowe dla silników spalinowych z różnymi paliwami
data = {
    'Silnik': ['Silnik 1', 'Silnik 2', 'Silnik 3'],
    'Moc (kW)': [100, 150, 200],
    'Zużycie biogazu (m3/h)': [10, 15, 20],
    'Zużycie benzyny (l/h)': [8, 12, 16],
    'Zużycie diesla (l/h)': [7, 10, 14],
    'Wartość opałowa biogazu (MJ/m3)': [22.67, 21.05, 23.71],
    'Wartość opałowa benzyny (MJ/l)': [34.2, 34.2, 34.2],
    'Wartość opałowa diesla (MJ/l)': [35.8, 35.8, 35.8],
    'Koszt biogazu (USD/m3)': [0.5, 0.5, 0.5],
    'Koszt benzyny (USD/l)': [1.2, 1.2, 1.2],
    'Koszt diesla (USD/l)': [1.0, 1.0, 1.0]
}

# Tworzenie DataFrame z danymi
df = pd.DataFrame(data)

# Obliczanie dostarczonej energii z paliwa (MJ/h)
df['Dostarczona energia biogazu (MJ/h)'] = df['Zużycie biogazu (m3/h)'] * df['Wartość opałowa biogazu (MJ/m3)']
df['Dostarczona energia benzyny (MJ/h)'] = df['Zużycie benzyny (l/h)'] * df['Wartość opałowa benzyny (MJ/l)']
df['Dostarczona energia diesla (MJ/h)'] = df['Zużycie diesla (l/h)'] * df['Wartość opałowa diesla (MJ/l)']

# Obliczanie kosztu energii (USD/MJ)
df['Koszt energii biogazu (USD/MJ)'] = df['Koszt biogazu (USD/m3)'] / df['Wartość opałowa biogazu (MJ/m3)']
df['Koszt energii benzyny (USD/MJ)'] = df['Koszt benzyny (USD/l)'] / df['Wartość opałowa benzyny (MJ/l)']
df['Koszt energii diesla (USD/MJ)'] = df['Koszt diesla (USD/l)'] / df['Wartość opałowa diesla (MJ/l)']

# Wyświetlanie wyników
print(df)

# Tworzenie wykresu kosztów energii
plt.figure(figsize=(12, 8))

# Koszt energii
bar_width = 0.25
r1 = range(len(df['Silnik']))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

plt.bar(r1, df['Koszt energii biogazu (USD/MJ)'], color='blue', width=bar_width, edgecolor='grey', label='Biogaz')
plt.bar(r2, df['Koszt energii benzyny (USD/MJ)'], color='green', width=bar_width, edgecolor='grey', label='Benzyna')
plt.bar(r3, df['Koszt energii diesla (USD/MJ)'], color='red', width=bar_width, edgecolor='grey', label='Diesel')

plt.xlabel('Silnik', fontweight='bold')
plt.xticks([r + bar_width for r in range(len(df['Silnik']))], df['Silnik'])
plt.ylabel('Koszt energii (USD/MJ)')
plt.title('Porównanie kosztu energii dla różnych paliw')
plt.legend()

# Wyświetlanie wykresu
plt.tight_layout()
plt.show()

