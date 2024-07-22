data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(len(data_structure))

def calculate_structure_sum(*data_structure):
  summator = ()
  for i in data_structure[0::1]:
    if isinstance(i, str):
      summator += len(i) # тут добавляем длину элемента если он является типом str
    elif isinstance(i, (float, int)):
      summator += int(i)
      summator += float(i) # добавляем значения int и float
    elif isinstance(i, (set, list, tuple)):
      summator += sum(i[0::1]) # добавляем сумму значений если тип set , list, tuple
    elif isinstance(i, dict):
      for key, value in i.items():
        summator += len(calculate_structure_sum(key)) # добавляем длину элемента ключ
        summator += calculate_structure_sum(value) # добавляем значение ключа
    return summator

result = calculate_structure_sum(*data_structure)
print(result)