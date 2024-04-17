import pandas as pd
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity

# Sample data: User-song matrix with additional features (song metadata, user demographics, and user listening history)
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4, 4, 5],
    'song_id': [101, 102, 103, 101, 104, 102, 103, 104, 105, 101],
    'rating': [5, 4, 3, 5, 4, 3, 2, 5, 4, 3],
    'genre': ['Pop', 'Pop', 'Rock', 'Pop', 'Hip-Hop', 'Rock', 'Rock', 'Hip-Hop', 'Hip-Hop', 'Pop'],
    'age': [25, 25, 25, 30, 30, 35, 35, 40, 40, 45],
    'gender': ['M', 'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M']
}

df = pd.DataFrame(data)

# Convert categorical features to numerical using one-hot encoding
df = pd.get_dummies(df, columns=['genre', 'gender'])

# Create user-song matrix (rows represent users, columns represent songs)
user_song_matrix = df.pivot(index='user_id', columns='song_id', values='rating').fillna(0).values

# Apply Non-negative Matrix Factorization (NMF) for matrix factorization
model = NMF(n_components=2, init='random', random_state=0)
W = model.fit_transform(user_song_matrix)
H = model.components_

# Calculate cosine similarity between songs based on factorized matrices
song_similarity = cosine_similarity(H)

def recommend_songs(user_id, song_similarity, k=2):
    # Find top k most similar songs to the songs the user has listened to
    listened_songs = user_song_matrix[user_id].nonzero()[0]
    similar_songs = np.argsort(song_similarity[listened_songs].mean(axis=0))[::-1][:k]
    
    # Initialize a dictionary to store song recommendations and their scores
    song_recommendations = {}
    
    # Iterate over similar songs and recommend songs that the given user has not listened to
    for similar_song in similar_songs:
        for i in range(len(user_song_matrix[user_id])):
            if user_song_matrix[user_id][i] == 0 and user_song_matrix[:, similar_song].max() > 0:
                if i not in song_recommendations:
                    song_recommendations[i] = song_similarity[similar_song].mean()
                else:
                    song_recommendations[i] += song_similarity[similar_song].mean()
    
    # Sort song recommendations by score in descending order
    sorted_recommendations = sorted(song_recommendations.items(), key=lambda x: x[1], reverse=True)
    
    # Return top recommended songs
    return sorted_recommendations

# Example: Recommend songs for user with ID 1
user_id = 1
recommendations = recommend_songs(user_id, song_similarity)
print("Recommended songs for user {}: {}".format(user_id, [song for song, score in recommendations]))
