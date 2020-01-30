import pickle
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'finalized_model.sav')


class ModelPredictor:

    def __init__(self):
        self.loaded_model = pickle.load(open(my_file, 'rb'))

    def predict(self, x, y):
        return self.loaded_model.score(x, y)
