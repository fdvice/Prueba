import numpy as np 
import pandas as pd
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from matplotlib import rcParams
step=6
rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False
X, y = make_classification(
    n_samples=1000, 
    n_features=2, 
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=42,
    weights=[0.50]
)

df = pd.concat([pd.DataFrame(X), pd.Series(y)], axis=1)
df.columns = ['x1', 'x2', 'y']
# 5 random rows
if(step==1):
    print(df.sample(10))

def plot(df: pd.DataFrame, x1: str, x2: str, y: str, title: str = '', save: bool = False, figname='figure.png'):
    plt.figure(figsize=(14, 7))
    plt.scatter(x=df[df[y] == 0][x1], y=df[df[y] == 0][x2], label='y = 0')
    plt.scatter(x=df[df[y] == 1][x1], y=df[df[y] == 1][x2], label='y = 1')
    plt.title(title, fontsize=20)
    plt.legend()
    if save:
        plt.savefig(figname, dpi=300, bbox_inches='tight', pad_inches=0)
    plt.show()
if(step==2):
    plot(df=df, x1='x1', x2='x2', y='y', title='Dataset with 2 classes')

X, y = make_classification(
    n_samples=1000, 
    n_features=2, 
    n_redundant=0,
    n_clusters_per_class=1,
    flip_y=0.25,
    random_state=42
)

df = pd.concat([pd.DataFrame(X), pd.Series(y)], axis=1)
df.columns = ['x1', 'x2', 'y']

if(step==3):
    plot(df=df, x1='x1', x2='x2', y='y', title='Dataset with 2 classes - Added noise')
X, y = make_classification(
    n_samples=1000, 
    n_features=2, 
    n_redundant=0,
    n_clusters_per_class=1,
    weights=[0.95],
    random_state=42
)

df = pd.concat([pd.DataFrame(X), pd.Series(y)], axis=1)
df.columns = ['x1', 'x2', 'y']

if(step==4):
    plot(df=df, x1='x1', x2='x2', y='y', title='Dataset with 2 classes - Class imbalance (weights=0.95)')
X, y = make_classification(
    n_samples=1000, 
    n_features=2, 
    n_redundant=0,
    n_clusters_per_class=1,
    weights=[0.05],
    random_state=42
)

df = pd.concat([pd.DataFrame(X), pd.Series(y)], axis=1)
df.columns = ['x1', 'x2', 'y']

if(step==5):
    plot(df=df, x1='x1', x2='x2', y='y', title='Dataset with 2 classes - Class imbalance (weights=0.05)')
X, y = make_classification(
    n_samples=1000, 
    n_features=2, 
    n_redundant=0,
    n_clusters_per_class=1,
    class_sep=5,
    random_state=42
)

df = pd.concat([pd.DataFrame(X), pd.Series(y)], axis=1)
df.columns = ['x1', 'x2', 'y']

if(step==6):
    plot(df=df, x1='x1', x2='x2', y='y', title='Dataset with 2 classes - Make classification easier')

