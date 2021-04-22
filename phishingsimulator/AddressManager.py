import pandas as pd
import random


class AdressManager:

    def __init__(self, path):
        self.adresses = pd.read_excel(path)["Adresses"].tolist()
        shuffled_adresses = self.adresses.copy()
        random.shuffle(shuffled_adresses)
        self.split_A = shuffled_adresses[0:int((len(shuffled_adresses) / 2))]
        self.split_B = shuffled_adresses[int((len(shuffled_adresses) / 2)): len(shuffled_adresses)]
        self.path = path
        self.links = pd.read_excel(self.path)["link"].tolist()

    def get_adresses(self):
        return self.adresses

    def get_split_A(self):
        return self.split_A

    def get_split_B(self):
        return self.split_B

    def get_links(self):
        return self.links
