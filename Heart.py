import streamlit as st 
import pandas as pd 
st.title("HEART DISEASE Prediction")
st.sidebar.title("Enter Your Health Report")
df=pd.read_csv("D:/data/heart.csv")
df.drop(['FastingBS','Oldpeak','ExerciseAngina'],axis=1,inplace=True)
df.Sex.replace({"M":0,"F":1},inplace=True)
df.ChestPainType.replace({'ATA':0,'NAP':1,'ASY':2,'TA':3},inplace=True)
df.RestingECG.replace({'Normal':0,'ST':1,'LVH':2},inplace=True)
df.ST_Slope.replace({'Up':0,'Flat':1,'Down':2},inplace=True)

#st.write(df.head(20))

x=df.drop('HeartDisease',axis=1)
y=df.HeartDisease
#st.write(x)
#st.write(y)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x,y)
age=st.sidebar.number_input("Enter Your Age")
gender=st.sidebar.selectbox("Gender",("Male","Female"))
if gender=="Female":
    gender=1
elif gender=="Male":
    gender=0
chest=st.sidebar.selectbox("Enter Your Chest Pain Type",("ATA","NAP","ASY","TA"))
if chest=="ASY":
    chest=2
elif chest=="NAP":
    chest=1
elif chest=="ATA":
    chest=0
elif chest=="TA":
    chest=3
ecg=st.sidebar.selectbox("select ECG",("Normal","ST","LVH="))
if ecg=="LVH":
    ecg=2
elif ecg=="ST":
    ecg=1
elif ecg=="Normal":
    ecg=0

slope=st.sidebar.selectbox("ST_Slope",("Up","Flat","Down"))
if slope=="Up":
    slope=0
elif slope=="Flat":
    slope=1
elif slope=="Down":
    slope=2

bp=st.sidebar.number_input("Enter Blood Pressure")
coles=st.sidebar.number_input("Enter your Cholestrol")
hr=st.sidebar.number_input("Enter Heart Rate")
b=st.sidebar.button("VIEW")
if b:
    pred=model.predict([[age,gender,chest,bp,coles,ecg,hr,slope]])
    if pred==0:
        st.subheader("YOU Have No Heart Disease Your Heart is FINE ")
        st.success("Heart Disease Negative")
        st.balloons()
    else:
        if pred==1:
            st.subheader("Your Heart  is Not Well PLease Start Treatment")
            st.error("Heart Disease Positive")
