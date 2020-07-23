# Day_13_03_colormap.py
import numpy as np
import matplotlib.pyplot as plt;
from matplotlib import cm
import seaborn as sns
import pandas as pd


x = np.random.rand(100)
y = np.random.rand(100)
t = np.arange(100)

print(x)

# plt.plot(x, y)
# plt.plot(x, y, 'ro')
plt.scatter(x, y, c=t)
plt.show()


# 문제
# scatter 함수를 이용해서 대각선을 2개 그려보세요.
def colormap_2():
    x = np.arange(100)

    plt.scatter(x, x, c=x)
    # plt.scatter(x, x[::-1], c=x)
    plt.scatter(x[::-1], x, c=x, cmap='viridis')
    plt.show()


def colormap_3():
    print(plt.colormaps())
    print(len(plt.colormaps()))

    x = np.arange(100)

    plt.subplot(1, 2, 1)
    plt.scatter(x, x, c=x, cmap='gist_rainbow')

    plt.subplot(1, 2, 2)
    plt.scatter(x, x, c=x, cmap='gist_rainbow')

    plt.colorbar()
    plt.show()


def colormap_4():
    jet = cm.get_cmap('jet')

    print(jet(-5))
    print(jet(0))
    print(jet(128))
    print(jet(255))
    print(jet(256))
    print()

    print(jet(0.1))
    print(jet(0.5))
    print(jet(128/255))
    print(jet(0.9))
    print()

    print(jet([0, 255]))
    print(jet(range(0, 256, 64)))
    print(jet(np.linspace(0.2, 0.5, 7)))

    # print(np.arange(0, 1, 0.1))
    # print(np.linspace(0, 1, 11))


def colormap_5():
    n = np.random.rand(10, 10)
    print(n)

    # plt.imshow(n)
    plt.imshow(n, cmap='winter')
    plt.show()


def colormap_6():
    flights = sns.load_dataset('flights')
    print(flights)

    df = flights.pivot('month', 'year', 'passengers')
    print(df)

    # plt.pcolor(df)
    # plt.xticks(np.arange(12), df.columns)
    # plt.yticks(np.arange(0, 12, 2), df.columns[::2])
    # plt.yticks(0.5 + np.arrane(12), df.index)

    # plt.title('flights heatmap')
    # plt.colorbar()
    # sns.heatmap(df)
    # sns.heatmap(df, annot=True, fmt='d')
    sns.heatmap(df, annot=True, fmt='d', cmap='viridis')

    plt.show()


# colormap_1()
# colormap_2()
# colormap_3()
# colormap_4()
# colormap_5()
colormap_6()