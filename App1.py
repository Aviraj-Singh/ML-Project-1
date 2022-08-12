import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("FineTech_app_ML_model.pickle","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_outcome(X):
   
    prediction=classifier.predict(X)
    print(prediction)
    return prediction

def main():
    st.title("Hello Fam!")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">FineTech App ML Model </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    lst=[]
    dayofweek = st.number_input("dayofweek")
    lst.append(dayofweek)
    hour = st.number_input("hour")
    lst.append(hour)
    age = st.number_input("age")
    lst.append(age)
    numscreens = st.number_input("numscreens")
    lst.append(numscreens)
    minigame = st.number_input("minigame")
    lst.append(minigame)
    used_premium_feature = st.number_input("used_premium_feature")
    lst.append(used_premium_feature)
    liked = st.number_input("liked")
    lst.append(liked)
    location = st.number_input("location")
    lst.append(location)
    Institutions = st.number_input("Institutions")
    lst.append(Institutions)
    VerifyPhone = st.number_input("VerifyPhone")
    lst.append(VerifyPhone)
    BankVerification = st.number_input("BankVerification")
    lst.append(BankVerification)
    VerifyDateOfBirth = st.number_input("VerifyDateOfBirth")
    lst.append(VerifyDateOfBirth)
    ProfilePage = st.number_input("ProfilePage")
    lst.append(ProfilePage)
    VerifyCountry = st.number_input("VerifyCountry")
    lst.append(VerifyCountry)
    Cycle = st.number_input("Cycle")
    lst.append(Cycle)
    idscreen = st.number_input("idscreen")
    lst.append(idscreen)
    Splash = st.number_input("Splash")
    lst.append(Splash)
    RewardsContainer = st.number_input("RewardsContainer")
    lst.append(RewardsContainer)
    EditProfile = st.number_input("EditProfile")
    lst.append(EditProfile)
    Finances = st.number_input("Finances")
    lst.append(Finances)
    Alerts = st.number_input("Alerts")
    lst.append(Alerts)
    Leaderboard = st.number_input("Leaderboard")
    lst.append(Leaderboard)
    VerifyMobile = st.number_input("VerifyMobile")
    lst.append(VerifyMobile)
    VerifyHousing = st.number_input("VerifyHousing")
    lst.append(VerifyHousing)
    RewardDetail = st.number_input("RewardDetail")
    lst.append(RewardDetail)
    VerifyHousingAmount = st.number_input("VerifyHousingAmount")
    lst.append(VerifyHousingAmount)
    ProfileMaritalStatus = st.number_input("ProfileMaritalStatus")
    lst.append(ProfileMaritalStatus)
    ProfileChildren = st.number_input("ProfileChildren")
    lst.append(ProfileChildren)
    ProfileEducation = st.number_input("ProfileEducation")
    lst.append(ProfileEducation)
    ProfileEducationMajor = st.number_input("ProfileEducationMajor")
    lst.append(ProfileEducationMajor)
    Rewards = st.number_input("Rewards")
    lst.append(Rewards)
    AccountView = st.number_input("AccountView")
    lst.append(AccountView)
    VerifyAnnualIncome = st.number_input("VerifyAnnualIncome")
    lst.append(VerifyAnnualIncome)
    VerifyIncomeType = st.number_input("VerifyIncomeType")
    lst.append(VerifyIncomeType)
    ProfileJobTitle = st.number_input("ProfileJobTitle")
    lst.append(ProfileJobTitle)
    Login = st.number_input("Login")
    lst.append(Login)
    ProfileEmploymentLength = st.number_input("ProfileEmploymentLength")
    lst.append(ProfileEmploymentLength)
    WebView = st.number_input("WebView")
    lst.append(WebView)
    SecurityModal = st.number_input("SecurityModal")
    lst.append(SecurityModal)
    ResendToken = st.number_input("ResendToken")
    lst.append(ResendToken)
    TransactionList = st.number_input("TransactionList")
    lst.append(TransactionList)
    NetworkFailure = st.number_input("NetworkFailure")
    lst.append(NetworkFailure)
    ListPicker = st.number_input("ListPicker")
    lst.append(ListPicker)
    remain_screen_list = st.number_input("remain_screen_list")
    lst.append(remain_screen_list)
    saving_screens_count = st.number_input("saving_screens_count")
    lst.append(saving_screens_count)
    credit_screens_count = st.number_input("credit_screens_count")
    lst.append(credit_screens_count)
    cc_screens_count = st.number_input("cc_screens_count")
    lst.append(cc_screens_count)
    loan_screens_count = st.number_input("loan_screens_count")
    lst.append(loan_screens_count)
    
    x = np.array(lst)
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    x = x.reshape(1,-1)
    X_train_sc = sc.fit_transform(x)
    

    result=""
    if st.button("Predict"):
        result=predict_outcome(X_train_sc)
    if result==[0]:
        st.success('No need to send discount code for this user')
    elif result==[1]:
        st.success('Send the discount coupon to this user')
    #st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("This is my first model")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    