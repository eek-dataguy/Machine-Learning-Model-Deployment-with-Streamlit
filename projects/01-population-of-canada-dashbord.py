import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

URL = "/workspaces/Machine-Learning-Model-Deployment-with-Streamlit/data/quarterly_canada_population.csv"

df = pd.read_csv(URL, dtype={'Quarter': str, 
                            'Canada': np.int32,
                            'Newfoundland and Labrador': np.int32,
                            'Prince Edward Island': np.int32,
                            'Nova Scotia': np.int32,
                            'New Brunswick': np.int32,
                            'Quebec': np.int32,
                            'Ontario': np.int32,
                            'Manitoba': np.int32,
                            'Saskatchewan': np.int32,
                            'Alberta': np.int32,
                            'British Columbia': np.int32,
                            'Yukon': np.int32,
                            'Northwest Territories': np.int32,
                            'Nunavut': np.int32})


st.title('Population of Canada')
st.markdown("Source can be found [here](https://raw.githubusercontent.com/eek-dataguy/Machine-Learning-Model-Deployment-with-Streamlit/refs/heads/main/data/quarterly_canada_population.csv)")

with st.expander("See full data table"):
    st.write(df)
    

with st.form("population_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Choose a starting date")
        start_quarter = st.selectbox("Quarter", options=['Q1', 'Q2', 'Q3', 'Q4'], index=2, key='startQ')

        min_year = int(df['Quarter'].str.split(" ").str[1].min())
        max_year = int(df['Quarter'].str.split(" ").str[1].max())
        start_year = st.slider("Year", min_value=min_year, max_value=max_year, value=min_year, step=1, key='startYear')

    with col2:
        st.write("Choose a ending date")
        ending_quarter = st.selectbox("Quarter", options=['Q1', 'Q2', 'Q3', 'Q4'], index=0, key='endQ')

        min_year = int(df['Quarter'].str.split(" ").str[1].min())
        max_year = int(df['Quarter'].str.split(" ").str[1].max())
        end_year = st.slider("Year", min_value=min_year, max_value=max_year, value=max_year, step=1, key='endYear')

    with col3:
        st.write('Choose a location')
        target = st.selectbox("Choose a location", options=df.columns[1:])

    submit_btn = st.form_submit_button("Analyst")


start_date = f"{start_quarter} {start_year}"
end_date = f"{ending_quarter} {end_year}"


def display_dashbord(start_date, end_date, target):
    tab1, tab2 = st.tabs(['Population Change', 'Compare'])

    with tab1:
        st.subheader(f"Population change from {start_date} to {end_date}")
        col1, col2 = st.columns(2)

        with col1:
            initial = df.loc[df['Quarter'] == start_date, target].item()
            final = df.loc[df['Quarter'] == end_date, target].item()

            percentage_diff = round((final - initial)/ initial * 100, 2)
            delta = f"{percentage_diff}%"

            st.metric(start_date, value= f"{initial:,}")
            st.metric(end_date, value= f"{final:,}", delta= delta)

        with col2:
            start_idx = df.loc[df['Quarter'] == start_date].index.item()
            end_idx = df.loc[df['Quarter'] == end_date].index.item()

            filtered_df = df.iloc[start_idx:end_idx+1]

            fig, ax = plt.subplots()
            ax.plot(filtered_df['Quarter'], filtered_df[target])
            ax.set_xlabel('Time')
            ax.set_ylabel('Population')
            ax.set_xticks([filtered_df['Quarter'].iloc[0], filtered_df['Quarter'].iloc[-1]])
            # ax.set_yticks([28000000, 30000000, 32000000, 34000000, 36000000, 38000000, 40000000],['28M', '30M', '32M', '34M', '36M', '38M', '40M'])
            fig.autofmt_xdate()

            st.pyplot(fig)

    with tab2:
        st.subheader("Compare with other locations")
        all_targets = st.multiselect('Choose other locations', options=df.columns[1:], default=target)

        fig, ax = plt.subplots()
        for each in all_targets:
            ax.plot(filtered_df['Quarter'], filtered_df[each])

        ax.set_xlabel('Time')
        ax.set_ylabel('Population')
        ax.set_xticks([filtered_df['Quarter'].iloc[0], filtered_df['Quarter'].iloc[-1]])
        # ax.set_yticks([0, 28000000, 30000000, 32000000, 34000000, 36000000, 38000000, 40000000],[0, '28M', '30M', '32M', '34M', '36M', '38M', '40M'])
        fig.autofmt_xdate()
        st.pyplot(fig)


if start_date not in df['Quarter'].to_list() or end_date not in df['Quarter'].to_list():
    st.error("No data Available, check your quarter and year selection!")
else:
    display_dashbord(start_date=start_date, end_date=end_date, target=target)