from sklearn.preprocessing import StandardScaler

# Standardize the data to have zero mean and unit variance
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['age', 'income']])

# Encode categorical variables as dummy variables
encoded_data = pd.get_dummies(df, columns=['gender'])

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(encoded_data.drop(['sales'], axis=1), encoded_data['sales'], test_size=0.2, random_state=42)
