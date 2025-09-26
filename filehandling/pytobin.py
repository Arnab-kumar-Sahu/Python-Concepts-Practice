with open("binary.pkl","wb") as file:
    import pickle
    po={"dhan dei mate paisa kaudina dabu"}
    bo=pickle.dumps(po)
    file.write(bo)
