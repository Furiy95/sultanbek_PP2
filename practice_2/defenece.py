a = {'Sultanbek': 'M', 'Diana': 'F', 'Cristinao': 'M'}
girl =[]
boy = []
for i in a: 
    if a[i] == 'M':
        boy.append(i)
    else:
        girl.append(i)
print(girl)
print(boy)