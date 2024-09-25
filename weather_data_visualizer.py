import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title("Weather Data Visualizer")

    # Upload dataset
    uploaded_file = st.file_uploader("Choose a CSV file with weather data", type="csv")

    if uploaded_file is not None:
        # Read the dataset
        df = pd.read_csv(uploaded_file)
        df['date'] = pd.to_datetime(df['date'])  # Ensure date is in datetime format
        st.write("Data Preview:")
        st.dataframe(df.head())

        # Select plot type
        plot_type = st.selectbox("Select plot type:", ["Temperature Trends", "Precipitation Over Time", "Comparison Between Locations"])

        if plot_type == "Temperature Trends":
            location = st.selectbox("Select location:", df['location'].unique())
            location_data = df[df['location'] == location]

            plt.figure(figsize=(12, 6))
            sns.lineplot(x='date', y='temperature', data=location_data, marker='o')
            plt.title(f"Temperature Trends in {location}")
            plt.xlabel("Date")
            plt.ylabel("Temperature (°C)")
            plt.xticks(rotation=45)
            st.pyplot(plt)

        elif plot_type == "Precipitation Over Time":
            location = st.selectbox("Select location:", df['location'].unique())
            location_data = df[df['location'] == location]

            plt.figure(figsize=(12, 6))
            sns.barplot(x='date', y='precipitation', data=location_data, color='blue')
            plt.title(f"Precipitation Over Time in {location}")
            plt.xlabel("Date")
            plt.ylabel("Precipitation (mm)")
            plt.xticks(rotation=45)
            st.pyplot(plt)

        elif plot_type == "Comparison Between Locations":
            selected_locations = st.multiselect("Select locations to compare:", df['location'].unique())

            if len(selected_locations) > 0:
                comparison_data = df[df['location'].isin(selected_locations)]

                plt.figure(figsize=(12, 6))
                sns.lineplot(x='date', y='temperature', hue='location', data=comparison_data, marker='o')
                plt.title("Temperature Comparison Between Locations")
                plt.xlabel("Date")
                plt.ylabel("Temperature (°C)")
                plt.xticks(rotation=45)
                st.pyplot(plt)

if __name__ == "__main__":
    main()
