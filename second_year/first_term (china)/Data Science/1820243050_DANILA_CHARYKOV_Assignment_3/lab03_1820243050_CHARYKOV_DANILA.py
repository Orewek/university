import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.impute import SimpleImputer


def main() -> None:
    data = pd.read_csv('C:/Dev/china/Assignment3-Breast-Cancer-Diagnose.csv')
    imputer = SimpleImputer(strategy='mean')
    X = data.drop(columns=['id', 'diagnosis'])
    X = imputer.fit_transform(X)
    y = data['diagnosis']

    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.25, random_state=42)

    name = input('Please, choose classifer: SVM, Logistic Regression, Random Forest')

    if name == 'Logistic Regression':
        classifier = LogisticRegression()
        param_grid = {
            'classifier__C': [0.1, 1, 10, 100]
        }
    elif name == 'SVM':
        classifier = SVC()
        param_grid = {
            'classifier__C': [0.1, 1, 10, 100],
            'classifier__kernel': ['linear', 'rbf']
        }
    elif name == 'Random Forest':
        classifier = RandomForestClassifier()
        param_grid = {
            'classifier__n_estimators': [100, 200, 300],
            'classifier__max_depth': [None, 5, 10, 20]
        }

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', classifier)
    ])

    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    print(f"Best parameters for {name}: {grid_search.best_params_}")


    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', classifier)
    ])
    pipeline.set_params(**grid_search.best_params_)

    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, pos_label='M')
    recall = recall_score(y_test, y_pred, pos_label='M')
    f1 = f1_score(y_test, y_pred, pos_label='M')

    print(f"""
           Performance metrics for {name}\n'
           Accuracy: {accuracy}\n'
           Precision: {precision}\n'
           Recall: {recall}\n'
           F1 Score: {f1}
           """)


if __name__ == '__main__':
    main()
