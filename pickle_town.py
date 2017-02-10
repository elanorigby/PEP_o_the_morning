import pickle


def pickle_it(file, to_write):
    """
    replaces old data in pickle file with new data
    :param file:
    :param to_write:
    :return:
    """
    with open(file, 'wb') as f:
        pickle.dump(to_write, f)


def add_to_pickle(file, to_write):
    """
    adds new data to old data in file
    :param file:
    :param to_write:
    :return:
    """
    with open(file, 'ab') as f:
        pickle.dump(to_write, f)


def read_pickle(file):
    """
    gets useable python collection out of pickle file
    :param file:
    :return:
    """
    with open(file, 'rb') as f:
        return pickle.load(f)


def used_hard_reset():
    pickle_it('used.p', [])
    print("success")

used_hard_reset()