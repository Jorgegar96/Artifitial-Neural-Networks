import numpy as np
import pandas as pd
from ArtificialNeuralNetwork import ArtificialNeuralNetwork


data = pd.read_csv('./Datasets/part3_data_train.csv')
dimensions = np.array([len(data.columns)-1, 10, 5])
X = data.loc[:, data.columns != "clase"].to_numpy().T
labels = pd.get_dummies(data["clase"]).to_numpy().T
nn = ArtificialNeuralNetwork(dimensions, name="Shamu")
nn.printNetwork()
nn.saveAsJSON()

nn.trainNetwork(X, labels, alpha=0.01, max_epochs=100)
nn.printNetwork()
nn.saveAsExcel()

val = pd.read_csv('./Datasets/part3_data_val.csv')
val_x = val.loc[:, val.columns != 'clase'].to_numpy()
val_y = pd.get_dummies(val["clase"]).to_numpy()
nn.test(val_x.T, val_y.T)

nn.test(X.T, labels.T)

nn = ArtificialNeuralNetwork(jsonPath='./Datasets/part1_red_prueba.json')
nn.printNetwork()
