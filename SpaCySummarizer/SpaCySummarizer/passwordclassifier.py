import streamlit
import joblib
import random
import string
def generate_password(length):
    characters = string.digit + string.ascii_letters + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return password
def load_model(model_file):
    model = joblib.load(os.path.join(model_file),"rb")
    return model
def classify_password(password,model):
    vect_password = pswd_cv.transform([password]).toarray()
    predictor = load_model(model)
    prediction = predictor.predict(vect_password)
    return prediction
    streamlit.title("Password Strength Classifier")
    choice = streamlit.sidebar.selectbox("Select an Option",["Classify Password","Generate Password"])
    if choice == "Classify Password":
        password = streamlit.text_input("Enter a password")
        streamlit.write("LR Classification: " + classify_password(password,"models/logit_pswd_model.pkl"))
        streamlit.write("Naives Baye Classification: " + classify_password(password,"models/nv_pswd_model.pkl"))
        
    elif choice == "Generate Password":
        num = streamlit.number_input("Enter a length between 8 and 25",8,25)
        password = generate_password(num)
        streamlit.write(password)

if __name__ == "__main__":
    main()
