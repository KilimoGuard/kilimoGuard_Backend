from threading import Thread

from kilimo_guard.prediction_model import PredictionModel


class Multithreading:
    def start_model_training(self):
        th = Thread(target=PredictionModel.train_model, args=[])
        th.start()
        return th
