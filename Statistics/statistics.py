from Calculator.calculator import Calculator
from Statistics.mean import mean
from Statistics.median import median
from Statistics.mode import mod
from Statistics.popstand import popstand
from Statistics.vpop import vpop
from Statistics.popuvar import popuvar
from Statistics.samplestand import samplestand
from Statistics.zscore import zscore
from CsvReader.CsvReader import CsvReader

class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = mean(d)
        return self.result

    def median(self):
        d = []
        for row in self.data.data:
           d.append(row['v'])
        self.result = median(d)
        return self.result

    def mod(self):
        d = []
        for row in self.data.data:
             d.append(row['v'])
        self.result = mod(d)
        return self.result

    def popstand(self):
         d = []
         for row in self.data.data:
             d.append(row['v'])
         self.result = popstand(d)
         return self.result

    def vpop(self):
         d = []
         for row in self.data.data:
            d.append(row['v'])
         self.result = vpop(d)
         return self.result

    def confidence(self):
         d = []
         for row in self.data.data:
             d.append(row['v'])
         self.result = popstand(d)
         return self.result

    def popuvar(self):
         d = []
         for row in self.data.data:
             d.append(row['v'])
         self.result = popuvar(d)
         return self.result

    def samplestand(self):
         d = []
         for row in self.data.data:
             d.append(row['v'])
         self.result = samplestand(d)
         return self.result

    def zscore(self):
        d = []
        for row in self.data.data:
            d.append(row['v'])
        self.result = zscore(d)
        return self.result