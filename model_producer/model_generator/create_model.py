import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle


def main():
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    dataframe = pandas.read_csv(url, names=names)
    array = dataframe.values
    X = array[:, 0:8]
    Y = array[:, 8]
    test_size = 0.33
    seed = 7
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))


if __name__ == '__main__':
    main()