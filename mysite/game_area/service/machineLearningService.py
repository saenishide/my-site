from tkinter import Image
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn import metrics
import cv2
import numpy as np
from sklearn.datasets import fetch_openml

from mysite import settings

class MachineLearningService:
    clf = svm.SVC(gamma=0.001)

    def check_number(self, number_img):
        X = []
        # ここに数字認識の処理を書く
        path = settings.STATICFILES_DIRS[1] + '/img/' + 'test.jpg'
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
        image = cv2.resize(image,(28,28))
        # 白黒に変換
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('testest', image)
        # cv2.waitKey(0)
        data = np.asarray(image)
        X.append(data)
        X = np.array(X[0])
        print()
        data = np.array(X)
        result = []
        tmp_result = []
        for i in range(28):
            for j in range(28):
                if data[i][j] > 128:
                    tmp_result.append(0)
                else:
                    tmp_result.append(1)
        result.append(tmp_result)
        result = self.clf.predict(result)
        return result[0][0]
    
    def act_image_machine_learning(self):
        # 手書き文字の画像認識の機械学習を行う
        # 取り入れるのを変えようか、やり方探す
        x_train, y_train = fetch_openml('mnist_784', return_X_y=True)
        x_train_src = x_train
        y_train = y_train

        x_train_src = x_train_src.values
        x_train = []
        
        for x_t in x_train_src:
            tmp_result = []
            for x in x_t:
                if x > 50:
                    tmp_result.append(1)
                else:
                    tmp_result.append(0)
            x_train.append(tmp_result)

        self.clf.fit(x_train, y_train)
        print('機械学習完了')
        # predicted = self.clf.predict(x_test)
        # print(metrics.classification_report(y_test, predicted))  # 正解率など
        # print(metrics.confusion_matrix(y_test, predicted))  # 行:正解、列:予測
        