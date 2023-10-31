from matplotlib import pyplot as plt

# Постройте как можно больше графиков, приведенных в этом разде­
# ле, - напишите собственные программы, не подглядывая в приведен­
# ный код.

# 1 Example of a line graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.show()

# 2 Example of a bar chart

categories = ['Oranges', 'Bananas', 'Lemons', 'Apples', 'Tomatoes']
values = [10, 15, 7, 12, 9]
plt.bar(categories, values, color='skyblue')
plt.show()

# 3 Example histogram
data = [3, 2, 4, 1, 5, 6, 2, 7, 3, 4]
plt.hist(data, bins=5, edgecolor='black')
plt.show()
