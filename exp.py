#実際の品種と予測結果の品種を出力するためのプログラム
import pickle
import numpy as np
import pandas as pd
from numpy.random import *

def read_iris_data(file_name):
    uci_iris_data = []
    uci_iris_name = []
    uci_iris_target =[]
    uci_name_target_dict ={}

    for line in open(file_name):
        iris_data = line.strip().split(',')
        if iris_data == ['']:
            continue

        #data部分のパース
        data = np.array([float(i) for i in iris_data[:-1]])
        #target_names部分のパース
        name = iris_data[-1]

        #targetの計算
        if name not in uci_name_target_dict:
            uci_name_target_dict[name] = len(uci_name_target_dict)
        target = uci_name_target_dict[name]



        #各リストに追加
        uci_iris_data.append(data)
        uci_iris_name.append(name)
        uci_iris_target.append(target)


     #それぞれnumpyの配列へ変換
    uci_iris_data = np.array(uci_iris_data).reshape(len(uci_iris_data),4)
    uci_iris_name = np.array([i for i in uci_name_target_dict.keys()]).reshape(len(uci_name_target_dict),)
    uci_iris_target = np.array(uci_iris_target).reshape(len(uci_iris_target),)

     #outputをdict化
    iris = {
     'data':uci_iris_data,
     'target':uci_iris_target,
     'target_names':uci_iris_name
    }

    return iris

def main():
    #学習させたモデルのロード
    filename = open('model.sav','rb')
    model = pickle.load(filename)

    #入力データの作成
    a=randint(150)
    A_test = iris_data[a].reshape(-1,4)

    #予測
    features = model.predict(A_test)

    if features == 0:
        print("モデルが予測した品種は、Iris-setosaです。")

    elif features == 1:
        print("モデルが予測した品種は、Iris-versicolorです。")

    elif features == 2:
        print("モデルが予測した品種は、Iris-virginicaです。")


    print("テストに使われた品種は"+df.at[a,'label']+"です。")

#iris.dataの成形
iris = read_iris_data('iris.data')
iris_data = iris["data"]
iris_target = iris["target"]
iris_target_names = iris["target_names"]

#データ構造
df = pd.DataFrame(data=iris_data,columns=["sepal length","sepal width","petal length","petal width"])
df["label"]=[iris_target_names[i] for i in iris_target]

if __name__ == '__main__':
    main()
