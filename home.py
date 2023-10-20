import streamlit as st
import pickle
import pandas as pd

def app():
    st.markdown("<h4 style='font-weight: bold; font-style: italic; font-family: Optima; color: #8BE8E5'>The Shield 🛡</h4>", unsafe_allow_html=True)  # This title should be inside the app function

    # Load the model and perform other data processing

    model = pickle.load(open('online_fraud_detection.pkl', 'rb'))
    # df = pd.read_csv('column explanation.txt')

    
 #background image
    import base64 
    def add_bg_from_local(image_file):
            with open(image_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                    background-size: cover
                }}
                </style>
                """,
                unsafe_allow_html=True
                )
    add_bg_from_local('the2.jpeg') 

    custom_css = """
        <style>
            .st-af {
                color: black !important;
            }
        </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    with st.form('my_form', clear_on_submit=True):
        st.subheader("Fraud Detection")
        # with st.expander("Variable Definitions"):
        #     st.table(df)
        Type_of_Transaction = st.selectbox('Type of Transaction', ['', 'CASH_OUT', 'PAYMENT', 'CASH_IN', 'TRANSFER', 'DEBIT'])
        Amount = float(st.number_input('Amount'))
        Balance_Before_Transaction = float(st.number_input('Balance Before Transaction'))
        Balance_After_Transaction = float(st.number_input('Balance After Transaction'))
        Recipients_Old_Balance = float(st.number_input("Recipient Old Balance"))
        Recipients_New_Balance = float(st.number_input("Recipient New Balance"))
        
        submitted = st.form_submit_button("SUBMIT")   
        if (Type_of_Transaction and Amount and Balance_Before_Transaction and Balance_After_Transaction and Recipients_Old_Balance and Recipients_New_Balance):
            if submitted:
                with st.spinner(text='Loading..'):
                    st.write("Your Inputted Data:")           

                    input_var = pd.DataFrame([{'type': Type_of_Transaction, 'amount': Amount, 'oldbalanceOrg': Balance_Before_Transaction, 'newbalanceOrig': Balance_After_Transaction, 'oldbalanceDest': Recipients_Old_Balance, 'newbalanceDest': Recipients_New_Balance}])
                    st.write(input_var) 
                        
                    from sklearn.preprocessing import LabelEncoder, StandardScaler
                    lb = LabelEncoder()
                    scaler = StandardScaler()
                    for i in input_var:
                        if input_var[i].dtypes == 'int' or input_var[i].dtypes == 'float':
                            input_var[[i]] = scaler.fit_transform(input_var[[i]])
                        else:
                            input_var[i] = lb.fit_transform(input_var[i])
                    
                    prediction = model.predict(input_var)
                    
                    if prediction == 0:
                        st.error('Transaction is not fraudulent')
                    else:
                        st.success('Transaction is fraudulent')
