import numpy as np
import pandas as pd


def data_construction():
    train = pd.read_json("./Data/train.json")
    test = pd.read_json("./Data/test.json")


    X_band_1=np.array([np.array(band).astype(np.float32).reshape(75, 75) for band in train["band_1"]])
    X_band_2=np.array([np.array(band).astype(np.float32).reshape(75, 75) for band in train["band_2"]])
    X_train = np.concatenate([X_band_1[:, :, :, np.newaxis], X_band_2[:, :, :, np.newaxis],((X_band_1+X_band_2)/2)[:, :, :, np.newaxis]], axis=-1)


    X_band_test_1=np.array([np.array(band).astype(np.float32).reshape(75, 75) for band in test["band_1"]])
    X_band_test_2=np.array([np.array(band).astype(np.float32).reshape(75, 75) for band in test["band_2"]])
    X_test = np.concatenate([X_band_test_1[:, :, :, np.newaxis]
                            , X_band_test_2[:, :, :, np.newaxis]
                            , ((X_band_test_1+X_band_test_2)/2)[:, :, :, np.newaxis]], axis=-1)

    return train,test,X_train,X_test