
import pandas as pd

data = []

truth_table = [
    [0,0,0,0,0],
    [0,0,1,1,0],
    [0,1,0,1,0],
    [0,1,1,0,1],
    [1,0,0,1,0],
    [1,0,1,0,1],
    [1,1,0,0,1],
    [1,1,1,1,1]
]

for row in truth_table:

    A,B,Cin,Sum,Cout = row

    # No Fault
    data.append([A,B,Cin,Sum,Cout,"No Fault"])

    # Sum stuck at 0
    if Sum != 0:
        data.append([A,B,Cin,0,Cout,"Sum Stuck-at-0"])

    # Sum stuck at 1
    if Sum != 1:
        data.append([A,B,Cin,1,Cout,"Sum Stuck-at-1"])

    # Cout stuck at 0
    if Cout != 0:
        data.append([A,B,Cin,Sum,0,"Cout Stuck-at-0"])

    # Cout stuck at 1
    if Cout != 1:
        data.append([A,B,Cin,Sum,1,"Cout Stuck-at-1"])

df = pd.DataFrame(data, columns=[
    "A","B","Cin","Sum","Cout","Fault"
])

df.to_csv("dataset.csv", index=False)

print(df)
print("Dataset created successfully!")
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("dataset.csv")

# Features and labels
X = df[["A","B","Cin","Sum","Cout"]]
y = df["Fault"]

# Train model on full dataset
model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

# Predict on same data
y_pred = model.predict(X)

# Accuracy
accuracy = accuracy_score(y, y_pred)

print("Accuracy:", accuracy)

import joblib
import pandas as pd

# Load trained model
model = joblib.load("fault_model.pkl")

# User input
A = int(input("Enter A: "))
B = int(input("Enter B: "))
Cin = int(input("Enter Cin: "))
Sum = int(input("Enter observed Sum: "))
Cout = int(input("Enter observed Cout: "))

# Create dataframe with feature names
input_data = pd.DataFrame(
    [[A,B,Cin,Sum,Cout]],
    columns=["A","B","Cin","Sum","Cout"]
)

# Prediction
prediction = model.predict(input_data)

print("Detected Fault:", prediction[0])