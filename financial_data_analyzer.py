import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("Financial Data Analyzer")

    # Upload dataset
    uploaded_file = st.file_uploader("Choose a CSV file with financial data", type="csv")

    if uploaded_file is not None:
        # Read the dataset
        df = pd.read_csv(uploaded_file)
        df['date'] = pd.to_datetime(df['date'])  # Ensure date is in datetime format
        st.write("Data Preview:")
        st.dataframe(df.head())

        # Calculate returns and volatility
        df['returns'] = df['stock_price'].pct_change()
        df['volatility'] = df['returns'].rolling(window=21).std()  # 21-day rolling volatility
        df.dropna(inplace=True)  # Drop NaN values created by pct_change()

        # Line plot for stock prices
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='date', y='stock_price', data=df, marker='o')
        plt.title("Stock Prices Over Time")
        plt.xlabel("Date")
        plt.ylabel("Stock Price")
        plt.xticks(rotation=45)
        st.pyplot(plt)

        # Line plot for returns
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='date', y='returns', data=df, marker='o', color='orange')
        plt.title("Returns Over Time")
        plt.xlabel("Date")
        plt.ylabel("Returns")
        plt.xticks(rotation=45)
        st.pyplot(plt)

        # Distribution plot for returns
        plt.figure(figsize=(12, 6))
        sns.histplot(df['returns'], bins=30, kde=True)
        plt.title("Distribution of Returns")
        plt.xlabel("Returns")
        plt.ylabel("Frequency")
        st.pyplot(plt)

        # Volatility plot
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='date', y='volatility', data=df, color='red', marker='o')
        plt.title("Volatility Over Time")
        plt.xlabel("Date")
        plt.ylabel("Volatility")
        plt.xticks(rotation=45)
        st.pyplot(plt)

        # Regression line on returns
        plt.figure(figsize=(12, 6))
        sns.regplot(x='stock_price', y='returns', data=df, marker='o')
        plt.title("Regression Line of Returns vs Stock Price")
        plt.xlabel("Stock Price")
        plt.ylabel("Returns")
        st.pyplot(plt)

if __name__ == "__main__":
    main()
