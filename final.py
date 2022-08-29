import streamlit as st
import numpy as np
import pickle

loaded_model=pickle.load(open('trained_model.pkl', 'rb'))

st.set_page_config(page_title="Heart disease prediction App",layout="centered",initial_sidebar_state="expanded")


# front end elements of the web page
html_temp = """ 
    <div style ="background-color:gray;padding:10px"> 
    <h1 style ="color:black;text-align:center;">Heart Disease Prediction App</h1> 
    </div> 
    """

# display the front end aspect
st.markdown(html_temp, unsafe_allow_html=True)

# following lines create boxes in which user can enter data required to make prediction
Age = st.slider("Age", 1,100)
#for sex
Sex_display = ('Male','Female')
Sex_options = list(range(len(Sex_display)))
Sex=st.selectbox("Gender",Sex_options,format_func=lambda x:Sex_display[x])

ChestPainType_display = ('Atypical angina','Non-anginal pain','Asymptomatic','Typical angina')
ChestPainType_options = list(range(len(ChestPainType_display)))
ChestPainType=st.selectbox("ChestPainType",ChestPainType_options,format_func=lambda x:ChestPainType_display[x])

RestingECG_display = ('Normal','ST-T Wave abnormality','Possible or definite left ventricular hypertrophy')
RestingECG_options = list(range(len(RestingECG_display)))
RestingECG=st.selectbox("RestingECG",RestingECG_options,format_func=lambda x:RestingECG_display[x])

ExerciseAngina_display = ('Yes','No')
ExerciseAngina_options = list(range(len(ExerciseAngina_display)))
ExerciseAngina=st.selectbox("ExerciseAngina",ExerciseAngina_options,format_func=lambda x:ExerciseAngina_display[x])

ST_Slope_display = ('Upsloping: better heart rate with excercise(uncommon)','Flatsloping: minimal change(typical healthy heart)',
                    'Downsloping: signs of unhealthy heart')
ST_Slope_options = list(range(len(ST_Slope_display)))
ST_Slope=st.selectbox("ST_Slope",ST_Slope_options,format_func=lambda x:ST_Slope_display[x])


RestingBP= st.selectbox('Resting Blood Pressure', range(1, 500, 1))
Cholesterol = st.selectbox('Cholestoral in mg/dl', range(1, 1000, 1))
FastingBS = st.selectbox("Fasting Blood Sugar ", range(0,2))
MaxHR = st.number_input('Maximum Heart Rate Achieved')
Oldpeak = st.number_input('Oldpeak')


if st.button("Predict"):
    result=loaded_model.predict(np.array([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS,RestingECG,MaxHR, ExerciseAngina, Oldpeak, ST_Slope]]))[0]
    if result == 0:
        st.write('You have no heart disease!')
    else:
        st.write('Warning! You have heart disease!')

st.sidebar.subheader("About")

st.sidebar.info("This web app is helps you to find out whether you have a heart disease or not.")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether you have a heart disease.")
