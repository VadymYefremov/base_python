import pickle


def rd_pickle():
    with open('faces_dump.pickle', 'rb') as fl:
        data = pickle.load(fl)
        print(data)
