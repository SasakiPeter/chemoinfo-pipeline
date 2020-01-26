from sklearn.preprocessing import StandardScaler


def standardize(X_train, y, X_test, id_test):
    scaler = StandardScaler()
    X_train.iloc[:, :] = scaler.fit_transform(X_train)
    X_test.iloc[:, :] = scaler.transform(X_test)
    return X_train, y, X_test, id_test


# def standardization(X):
#     return (X - X.mean()) / X.std(ddof=1)


# def standardize(X_train, X_valid, y_train, y_valid, X_test):
#     scaler = StandardScaler()
#     X_train = scaler.fit_transform(X_train)
#     X_valid = scaler.fit_transform(X_valid)
#     X_test = scaler.transform(X_test)
#     return X_train, X_valid, y_train, y_valid, X_test

    # idx = X_train.shape[0]
    # X = pd.concat([X_train, X_test])
    # X = standardization(X)
    # X_train = X.iloc[:idx, :]
    # X_test = X.iloc[idx:, :]
    # return X_train, y, X_test, id_test
