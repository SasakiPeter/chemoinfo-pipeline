def select_satisfy_lipinski(X_train, y, X_test, id_test):
    X_train = X_train[X_train['Lipinski'] == 1].reset_index(drop=True)
    y = y.iloc[X_train.index.values].reset_index(drop=True)
    X_test = X_test[X_test['Lipinski'] == 1].reset_index(drop=True)
    id_test = id_test.iloc[X_test.index.values].reset_index(drop=True)
    return X_train, y, X_test, id_test


def select_not_satisfy_lipinski(X_train, y, X_test, id_test):
    X_train = X_train[X_train['Lipinski'] == 0].reset_index(drop=True)
    y = y.iloc[X_train.index.values].reset_index(drop=True)
    X_test = X_test[X_test['Lipinski'] == 0].reset_index(drop=True)
    id_test = id_test.iloc[X_test.index.values].reset_index(drop=True)
    return X_train, y, X_test, id_test


def select_core_feature(X_train, y, X_test, id_test):
    X_train = X_train[['Basicity', 'MW']]
    X_test = X_test[['Basicity', 'MW']]
    return X_train, y, X_test, id_test
