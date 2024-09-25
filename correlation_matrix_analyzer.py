import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title("Correlation Matrix Analyzer")

    # Upload dataset
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Read the dataset
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(df.head())

        # Select features for the correlation matrix
        features = st.multiselect("Select features for correlation matrix:", df.columns.tolist(), default=df.columns.tolist())
        
        if len(features) > 1:
            # Compute the correlation matrix
            corr = df[features].corr()

            # Select color palette
            palette = st.selectbox("Choose a color palette:", ["coolwarm", "viridis", "plasma", "cividis", "crest"])

            # Generate the heatmap
            plt.figure(figsize=(10, 8))
            sns.heatmap(corr, annot=True, fmt=".2f", cmap=palette, square=True, cbar_kws={"shrink": .8})
            plt.title("Correlation Matrix Heatmap")
            st.pyplot(plt)
        else:
            st.warning("Please select at least two features to generate the correlation matrix.")

if __name__ == "__main__":
    main()
