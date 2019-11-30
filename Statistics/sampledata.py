from random import random





def sampledata(data, sample_size):

    random_sample = random.sample(data, k=sample_size)

    return random_sample