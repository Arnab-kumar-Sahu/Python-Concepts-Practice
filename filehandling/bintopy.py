import pickle

with open('binary.pkl', 'rb') as file:
    po=pickle.load(file)
    print(po)