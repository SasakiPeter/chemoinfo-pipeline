from pipeline.preprocess.decompose import decompose_binary
from pipeline.preprocess.encode import label_encoding
from pipeline.preprocess.generate import create_basicity
from pipeline.preprocess.interpolate import nan_to_zero
from pipeline.preprocess.load_data import load_train, load_test
from pipeline.preprocess.reduce import remove_const, remove_nan
from pipeline.preprocess.scale import standardize
from pipeline.preprocess.select import (
    select_satisfy_lipinski,
    select_not_satisfy_lipinski,
    select_core_feature
)


def preprocess():
    X_train, y_train = load_train()
    X_test, id_test = load_test()
    print('X_train shape: ', X_train.shape,
          'y_train shape: ', y_train.shape)
    print('X_test shape: ', X_test.shape,
          'id_test shape: ', id_test.shape)

    # ここにテストを書きたい
