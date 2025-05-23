# ML model training/prediction
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

def train_model(df: pd.DataFrame) -> RandomForestClassifier:
    df = df.dropna()
    X = df[['hour', 'weekday', 'month', 'Latitude', 'Longitude']]
    y = df['Primary Type']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    return model