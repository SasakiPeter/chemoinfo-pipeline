def create_basicity(X_train, y, X_test, id_test):
    X_train.loc[:, 'Basicity'] = X_train.loc[:, 'nBase'].values - \
        X_train.loc[:, 'nAcid'].values
    X_test.loc[:, 'Basicity'] = X_test.loc[:, 'nBase'].values - \
        X_test.loc[:, 'nAcid'].values
    return X_train, y, X_test, id_test
