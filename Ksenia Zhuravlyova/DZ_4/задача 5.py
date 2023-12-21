file = open('numbers.txt')
text = file.read()
suma = len(str(text).split()) #14
positiv = len([int(n) for n in map(int, text.split()) if n>=0])
mini = min(map(int, text.split())) #-5
maxi = max(map(int, text.split())) #20

sum_s = sum(map(int, text.split())) #60
arif = sum_s / suma #4.29

print(suma)
print(positiv)
print(mini)
print(maxi)
print(sum_s)
print(float('{:.2f}'.format(arif)))







#%%
