import pickle

def pickle_it(file, to_write):
    with open(file, 'wb') as f:
        pickle.dump(to_write, f)


def read_pickle(file):
    with open(file, 'rb') as f:
        return pickle.load(f)
