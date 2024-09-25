import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def main():
    st.title("Customer Segmentation Tool")

    # Upload dataset
    uploaded_file = st.file_uploader("Choose a CSV file with customer data", type="csv")

    if uploaded_file is not None:
        # Read the dataset
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.dataframe(df.head())

        # Select features for clustering
        features = st.multiselect("Select features for clustering:", df.columns.tolist()[1:], default=[df.columns[1], df.columns[2]])

        if len(features) >= 2:
            # Perform KMeans clustering
            k = st.slider("Select number of clusters (k):", 1, 10, 3)
            kmeans = KMeans(n_clusters=k, random_state=42)
            df['Cluster'] = kmeans.fit_predict(df[features])

            # Scatter plot
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=df[features[0]], y=df[features[1]], hue=df['Cluster'], palette='viridis', data=df, s=100)
            plt.title("Customer Segmentation Scatter Plot")
            plt.xlabel(features[0])
            plt.ylabel(features[1])
            st.pyplot(plt)

            # Violin plot
            plt.figure(figsize=(10, 6))
            sns.violinplot(x='Cluster', y=features[1], data=df, inner="quartile", palette='muted')
            plt.title("Violin Plot of Customer Segments")
            plt.xlabel("Cluster")
            plt.ylabel(features[1])
            st.pyplot(plt)

            # Show cluster centers
            cluster_centers = pd.DataFrame(kmeans.cluster_centers_, columns=features)
            st.write("Cluster Centers:")
            st.dataframe(cluster_centers)

if __name__ == "__main__":
    main()
