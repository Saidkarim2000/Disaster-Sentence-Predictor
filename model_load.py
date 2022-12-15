import pickle

model = pickle.load(open('sgd_model.pkl', 'rb'))

def predict_label(f_path:list):
    sentence = [f_path]
    print(sentence)
    result = model.predict(sentence)
    print(result)
    if result[0]:
        print(result)
        return ("This comment indicates a disaster")
    else:
        print(result)
        return ("This comment doesn't indicate a disaster")

    