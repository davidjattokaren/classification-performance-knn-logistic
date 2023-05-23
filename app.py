
import pickle
import streamlit as st

pickle_in = open('classifier', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()

# Define the function which will make the prediction using data
# inputs from users
def prediction(employee_experience, training_level):
    
    #For employee experience, the mean from the training dataset (calculated earlier) is 7.13, while the standard deviation is 2.23
    #Since we have normalized the variables while training the model, we need to normalize the new test data that comes in as well
    #This only affects the numeric variable, in this case that is employee_experience
    
    employee_experience = (employee_experience - 7.13)/(2.23)
    
    #For a better user experience, we allow the user to choose training level values (4, 6, 8) using one menu only, and then convert it
    #into the dummy variable format in the backend, which will be used on the model
    
    training_level4 = 0
    training_level6 = 0
    training_level8 = 0
    
    if training_level == 4:
        training_level4 = 1
    elif training_level == 6:
        training_level6 = 1
    else:
        training_level8 = 1
    # Make predictions
    prediction = classifier.predict(
        [[employee_experience, training_level4, training_level6, training_level8]])
    
    if prediction == 1:
        pred = 'Employee will most likely COMPLETE their task'
    else:
        pred = 'Employee will most likely NOT COMPLETE their task'
    return pred

# This is the main function in which we define our webpage
def main():
    
    st.title("Employee Task Completion Predictor")
    st.write("Please enter the Employee profile values below:")
    # col1, col2 = st.columns(2)
    # Create input fields
    st.subheader("Employee Parameters")
    employee_experience = st.number_input("Employee Years of Experience?",
                                  min_value=0.0,
                                  max_value=14.0,
                                  value=0.0,
                                  step=0.2,
                                 )
    training_level = st.number_input("Employee Training Level?",
                              min_value=4,
                              max_value=8,
                              value=4,
                              step=2
                             )

    result = ""
    
    # When 'Predict' is clicked, make the prediction and store it
    if st.button("ㅤㅤㅤPredictㅤㅤㅤ"):
        result = prediction(employee_experience, training_level)
        if result == "Employee will most likely COMPLETE their task":
            st.success(result)
        else:
            st.error(result)
        
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/f3/W._P._Carey_School_of_Business_logo.png", width = 150)
    st.write("Built by David Joseph Attokaren")
    st.write("Version 1.0.0")
    
if __name__=='__main__':
    main()
    
