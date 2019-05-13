#データの成形
import numpy as np

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

     #それぞれnumpyの配列へ変換(無理やり)
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
    iris = read_iris_data('iris.data')

if __name__ == '__main__':
    main()
