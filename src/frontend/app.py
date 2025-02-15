import streamlit as st
import pandas as pd

def show_dashboard(df: pd.DataFrame):
    # Convert the 'ultimo' column to datetime
    df['ultimo_datetime'] = pd.to_datetime(df['ultimo'], dayfirst=True, errors='coerce')

    # Check for NaT values (conversion errors)
    print(df['ultimo_datetime'].isna().sum())
    
    # Sort by date
    df = df.sort_values('ultimo_datetime')

    # KPI calculations

    # Average errors per test
    df['fallos'] = df['fallos'].astype(int)  # Ensure 'fallos' is int
    avg_errores = df['fallos'].mean()

    # Percentage of tests passed
    # Assume a test is passed if it has less than 3 errors
    tests_aprobados = len(df[df['fallos'] <= 3])
    total_tests = len(df)
    porcentaje_aprobados = (tests_aprobados / total_tests) * 100

    # Dashboard title
    st.markdown('<h1 style="color: #87CEEB;">TODOTEST x PAU</h1>', unsafe_allow_html=True)

    # 1. KPIs (Key Performance Indicators)
    # HTML styles for the KPIs
    kpi_style = """
    <div style="display: flex; justify-content: space-between; gap: 20px;">
        <div style="background-color: #001f3f; padding: 20px; border-radius: 8px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
        <h4 style="color: #ffffff;">Total tests done 🏎️</h4>
        <p style="font-size: 24px; color: #2196F3;">{}</p>
        </div>
        <div style="background-color: #001f3f; padding: 20px; border-radius: 8px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
            <h4 style="color: #ffffff;">Average Errors/Test ❌</h4>
            <p style="font-size: 24px; color: #4CAF50;">{:.2f}</p>
        </div>
        <div style="background-color: #001f3f; padding: 20px; border-radius: 8px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
            <h4 style="color: #ffffff;">% Tests Passed 🤓</h4>
            <p style="font-size: 24px; color: #4CAF50;">{:.2f}%</p>
        </div>
    </div>
    """.format(total_tests, avg_errores, porcentaje_aprobados)

    # Display the KPIs
    st.markdown(kpi_style, unsafe_allow_html=True)

    # 2. Chart of number of tests per day
    st.subheader('Number of Tests per Day')

    # Group by date and count the tests per day
    tests_por_dia = df.groupby(df['ultimo_datetime'].dt.date).size().reset_index(name='Number of Tests')

    # Display the chart of number of tests per day
    st.bar_chart(tests_por_dia.set_index('ultimo_datetime')['Number of Tests'])

    # Other possible filters or interactions in the sidebar
    st.sidebar.write('You can interact with this dashboard to see the results and statistics.')