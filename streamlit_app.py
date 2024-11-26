import datetime
import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler
import io

buffer = io.BytesIO()

def data_preprocessing(data_input, single_data, n):
    df = pd.read_csv('student_data_filtered.csv')
    df = df.drop(columns=['Status'], axis=1)
    df = pd.concat([data_input, df])

    df = StandardScaler().fit_transform(df)

    if single_data:
        return df[[n]]
    else:
        return df[0 : n]

def model_predict(df):
    model = joblib.load('model_rf.joblib')
    return model.predict(df)

def color_mapping(value):
    color = 'green' if value == 'Graduate' else 'red'
    return f'color: {color}'

def main():
    st.title('Jaya Jaya Institute Student Prediction')

    gender_mapping = {
        'Male': 1,
        'Female': 0
    }

    marital_status_mapping = {
        'Single': 1,
        'Married': 2,
        'Widower': 3,
        'Divorced': 4,
        'Facto Union': 5,
        'Legally Seperated': 6
    }

    application_mapping = {
        '1st Phase - General Contingent': 1,
        '1st Phase - Special Contingent (Azores Island)': 5,
        '1st Phase - Special Contingent (Madeira Island)': 16,
        '2nd Phase - General Contingent': 17,
        '3rd Phase - General Contingent': 18,
        'Ordinance No. 612/93': 2,
        'Ordinance No. 854-B/99': 10,
        'Ordinance No. 533-A/99, Item B2 (Different Plan)': 26,
        'Ordinance No. 533-A/99, Item B3 (Other Institution)': 27,
        'International Student (Bachelor)': 15,
        'Over 23 Years Old': 39,
        'Transfer': 42,
        'Change of Course': 43,
        'Holders of Other Higher Courses': 7,
        'Short Cycle Diploma Holders': 53,
        'Technological Specialization Diploma Holders': 44,
        'Change of Institution/Course': 51,
        'Change of Institution/Course (International)': 57,
    }

    # Seperate predictions for single data and multiple data
    tab_single, tab_multiple = st.tabs(['Single Data', 'Multiple Data'])

    # Prediction container for single data using input field
    with tab_single:
        with st.container():
            col_gender, col_age, col_marital = st.columns([2, 2, 3])
            with col_gender:
                gender = st.radio('Gender', options=['Male', 'Female'],
                    help='The gender of the student')
            with col_age:
                age = st.number_input('Age at Enrollment', min_value=17, max_value=70,
                    help='The age of the student at the time of enrollment')
            with col_marital:
                marital_status = st.selectbox('Marital Status', ('Single', 'Married',
                    'Widower', 'Divorced', 'Facto Union', 'Legally Seperated'),
                    help='The marital status of the student')

        st.write('')
        st.write('')

        with st.container():
            col_application, col_prev_grade, col_admission_grade = st.columns([3, 1.65, 1.1])
            with col_application:
                application_mode = st.selectbox('Application Mode', (
                    '1st Phase - General Contingent',
                    '1st Phase - Special Contingent (Azores Island)',
                    '1st Phase - Special Contingent (Madeira Island)',
                    '2nd Phase - General Contingent', '3rd Phase - General Contingent',
                    'Ordinance No. 612/93', 'Ordinance No. 854-B/99',
                    'Ordinance No. 533-A/99, Item B2 (Different Plan)',
                    'Ordinance No. 533-A/99, Item B3 (Other Institution)',
                    'International Student (Bachelor)', 'Over 23 Years Old',
                    'Transfer', 'Change of Course', 'Holders of Other Higher Courses',
                    'Short Cycle Diploma Holders',
                    'Technological Specialization Diploma Holders',
                    'Change of Institution/Course',
                    'Change of Institution/Course (International)'),
                    help='The method of application used by the student')
            with col_prev_grade:
                prev_qualification_grade = st.number_input('Previous Qualification Grade',
                    help='Grade of previous qualification (0-200)', min_value=0, max_value=200)
            with col_admission_grade:
                admission_grade = st.number_input('Admission Grade',
                    help="Student's admission grade (0-200)", min_value=0, max_value=200)

        with st.container():
            col_scholarship, col_tuition, col_displaced, col_debtor = st.columns([1.7, 2.1, 1.55, 1])
            with col_scholarship:
                scholarship_holder = 1 if st.checkbox(
                    'Scholarship', help='Whether the student is a scholarship holder') else 0
            with col_tuition:
                tuition_fees = 1 if st.checkbox(
                    'Tuition up to date', help="Whether the student's tuition fees are up to date") else 0
            with col_displaced:
                displaced = 1 if st.checkbox(
                    'Displaced', help='Whether the student is a displaced person') else 0
            with col_debtor:
                debtor = 1 if st.checkbox(
                    'Debtor', help='Whether the student is a debtor') else 0

        st.write('')
        st.write('')

        with st.container():
            col_1_enroll, col_2_enroll, col_2_eval = st.columns([1, 1, 1.2])
            with col_1_enroll:
                curricular_units_1st_sem_enrolled = st.number_input(
                    'Units 1st Semester Enrolled', min_value=0, max_value=26,
                    help='The number of curricular units enrolled by the student in the first semester')
            with col_2_enroll:
                curricular_units_2nd_sem_enrolled = st.number_input(
                    'Units 2nd Semester Enrolled', min_value=0, max_value=23,
                    help='The number of curricular units enrolled by the student in the second semester')
            with col_2_eval:
                curricular_units_2nd_sem_evaluations = st.number_input(
                    'Units 2nd Semester Evaluations', min_value=0, max_value=33,
                    help='The number of curricular units evaluations by the student in the second semester')

        with st.container():
            col_1_approved, col_2_approved, col_2_noeval = st.columns([1, 1, 1.2])
            with col_1_approved:
                curricular_units_1st_sem_approved = st.number_input(
                    'Units 1st Semester Approved', min_value=0, max_value=26,
                    help='The number of curricular units approved by the student in the first semester')
            with col_2_approved:
                curricular_units_2nd_sem_approved = st.number_input(
                    'Units 2nd Semester Approved', min_value=0, max_value=20,
                    help='The number of curricular units approved by the student in the second semester')
            with col_2_noeval:
                curricular_units_2nd_sem_without_evaluations = st.number_input(
                    'Units 2nd Semester No Evaluations', min_value=0, max_value=12,
                    help='The number of curricular units without evaluations by the student in the second semester')

        with st.container():
            col_1_grade, col_2_grade, col_2_empty = st.columns([1, 1, 1.2])
            with col_1_grade:
                curricular_units_1st_sem_grade = st.number_input(
                    'Units 1st Semester Grade', min_value=0, max_value=20,
                    help='The number of curricular units grade by the student in the first semester')
            with col_2_grade:
                curricular_units_2nd_sem_grade = st.number_input(
                    'Units 2nd Semester Grade', min_value=0, max_value=20,
                    help='The number of curricular units grade by the student in the second semester')

        # Mapping the categorical data
        gender = gender_mapping.get(gender)
        marital_status = marital_status_mapping.get(marital_status)
        application_mode = application_mapping.get(application_mode)

        data = [[marital_status, application_mode, prev_qualification_grade,
            admission_grade, displaced, debtor, tuition_fees,
            gender, scholarship_holder, age,
            curricular_units_1st_sem_enrolled,
            curricular_units_1st_sem_approved, curricular_units_1st_sem_grade,
            curricular_units_2nd_sem_enrolled,
            curricular_units_2nd_sem_evaluations,
            curricular_units_2nd_sem_approved, curricular_units_2nd_sem_grade,
            curricular_units_2nd_sem_without_evaluations]]

        df = pd.DataFrame(data, columns=[
            'Marital_status', 'Application_mode', 'Previous_qualification_grade',
            'Admission_grade', 'Displaced', 'Debtor', 'Tuition_fees_up_to_date',
            'Gender', 'Scholarship_holder', 'Age_at_enrollment',
            'Curricular_units_1st_sem_enrolled',
            'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
            'Curricular_units_2nd_sem_enrolled',
            'Curricular_units_2nd_sem_evaluations',
            'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
            'Curricular_units_2nd_sem_without_evaluations'])

        # Prediction result
        @st.dialog('Result')
        def prediction(output):
            if output == 1:
                st.success('Student Status Prediction: **Graduate**')
            else:
                st.error('Student Status Prediction: **Dropout**')

        # Single data predict button
        if st.button('✨ Predict'):
            data_input = data_preprocessing(df, True, 0)
            output = model_predict(data_input)
            prediction(output)

    # Prediction container for multiple data using file upload
    with tab_multiple:
        with st.expander('**User Guide**'):
            st.write("""
                1. First download the student data Excel template.
                2. Complete all student data columns in the Excel file.
                3. Upload the student data Excel file.
                4. Click the (**✨ Predict Data**) button.
                5. The prediction results will appear in table below
                6. The prediction results table can be downloaded in Excel format.
            """)

            # File template download button 
            with open('student_data_template.xlsx', 'rb') as file:
                st.download_button(
                    label='Download Template',
                    data=file,
                    file_name='Student Data Template.xlsx',
                    mime='application/vnd.ms-excel',
                    help='Download student data excel template')

        # File upload button
        uploaded_file = st.file_uploader(
            label='Upload Student Data',
            type=['xlsx', 'xls'],
            help='Upload student data with the template format')

        if uploaded_file is not None:
            up = pd.read_excel(uploaded_file)
            up['ID'] = up['ID'].astype(str)

            st.write('')
            st.write('')

            # Preview uploaded data
            preview = st.slider('**Preview Rows**', 1, len(up), 2)
            st.dataframe(up.head(preview))

            # Move column order based on raw data
            df_up = pd.DataFrame(up, columns=['ID', 'Name', 'Marital Status',
                'Application Mode', 'Previous Qualification Grade', 'Admission Grade',
                'Displaced', 'Debtor', 'Tuition up to date', 'Gender', 'Scholarship',
                'Age at Enrollment', 'Units 1st Semester Enrolled',
                'Units 1st Semester Approved', 'Units 1st Semester Grade',
                'Units 2nd Semester Enrolled', 'Units 2nd Semester Approved',
                'Units 2nd Semester Grade', 'Units 2nd Semester Evaluations',
                'Units 2nd Semester No Evaluations'])

            # Rename column based on the raw data
            df_up.rename(columns={
                'Marital Status': 'Marital_status',
                'Application Mode': 'Application_mode',
                'Previous Qualification Grade': 'Previous_qualification_grade',
                'Admission Grade': 'Admission_grade',
                'Tuition up to date': 'Tuition_fees_up_to_date',
                'Scholarship': 'Scholarship_holder',
                'Age at Enrollment': 'Age_at_enrollment',
                'Units 1st Semester Enrolled': 'Curricular_units_1st_sem_enrolled',
                'Units 1st Semester Approved': 'Curricular_units_1st_sem_approved',
                'Units 1st Semester Grade': 'Curricular_units_1st_sem_grade',
                'Units 2nd Semester Enrolled': 'Curricular_units_2nd_sem_enrolled',
                'Units 2nd Semester Approved': 'Curricular_units_2nd_sem_approved',
                'Units 2nd Semester Grade': 'Curricular_units_2nd_sem_grade',
                'Units 2nd Semester Evaluations': 'Curricular_units_2nd_sem_evaluations',
                'Units 2nd Semester No Evaluations': 'Curricular_units_2nd_sem_without_evaluations'
            }, inplace=True)

            # Seperate the ID and Name columns
            student_ids = df_up['ID']
            student_names = df_up['Name']
            df_up = df_up.drop(columns=['ID', 'Name'])

            # Categorical data columns data mapping
            df_up['Gender'] = df_up['Gender'].map(gender_mapping)
            df_up['Marital_status'] = df_up['Marital_status'].map(marital_status_mapping)
            df_up['Application_mode'] = df_up['Application_mode'].map(application_mapping)

            # Multiple data predict button
            if st.button('✨ Predict Data'):
                df_input = data_preprocessing(df_up, False, len(up))
                output = model_predict(df_input)

                prediction = ['Graduate' if pred == 1 else 'Dropout' for pred in output]
                result = pd.DataFrame({
                    'ID': student_ids,
                    'Name': student_names,
                    'Status': prediction
                })

                st.write('')
                st.write('')
                st.write('**Results**')
                st.dataframe(result.style.applymap(color_mapping, subset=['Status']))

                # Prepare the dataframe conversion to Excel file
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    result.to_excel(writer, sheet_name='Prediction', index=False)

                # Prediction file download button
                st.download_button(
                    label='Download Prediction',
                    data=buffer.getvalue(),
                    file_name='Student Data Prediction.xlsx',
                    mime='application/vnd.ms-excel',
                    help='Download student data prediction Excel file')

    st.write('')
    st.write('')

    year_now = datetime.date.today().year
    year = year_now if year_now == 2024 else f'2024 - {year_now}'
    name = "[Andrew Benedictus Jamesie](http://linkedin.com/in/andrewbjamesie 'Andrew Benedictus Jamesie | LinkedIn')"
    copyright = 'Copyright © ' + str(year) + ' ' + name
    st.caption(copyright)

if __name__ == '__main__':
    main()
