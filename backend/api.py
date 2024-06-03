import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier

from flask import Flask, jsonify, request
import json

app = Flask(__name__)


def purify(df):
    if "Timestamp" in df:
        df.drop(["Timestamp"], axis=1, inplace=True)

    if "DAILY_STRESS" in df:
        df["DAILY_STRESS"] = pd.to_numeric(df["DAILY_STRESS"], errors="coerce")

        average_stress = round(df["DAILY_STRESS"].mean())
        df["DAILY_STRESS"] = df["DAILY_STRESS"].fillna(value=average_stress)

        df["DAILY_STRESS"] = df["DAILY_STRESS"].astype(int)

    label_encoder = LabelEncoder()
    df["GENDER"] = label_encoder.fit_transform(df["GENDER"])  # 0: Female, 1: Male
    df["AGE"] = label_encoder.fit_transform(
        df["AGE"]
    )  # 1: 36-50, 2: > 50, 0: 21-35 3: < 20

    return df


def get_model() -> MLPClassifier:
    file_url = "https://raw.githubusercontent.com/daryll-ko/stress/18a2bd7178aa1cfe48c027b1e2e03f9dbfeed161/Wellbeing_and_lifestyle_data_Kaggle.csv"
    df = pd.read_csv(file_url)

    df = purify(df)

    df_copy = df.copy()  # just making a copy for later

    X = df_copy.drop(["DAILY_STRESS"], axis=1)
    y = df_copy["DAILY_STRESS"]

    # Scaling the features
    scaler = MinMaxScaler(feature_range=(-1, 1))

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=180
    )

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    mlp = MLPClassifier(
        hidden_layer_sizes=(5),
        max_iter=10000,
        learning_rate_init=0.001,
        activation="tanh",
    )
    mlp.fit(X_train, y_train)

    return mlp


mlp = get_model()


@app.route("/")
def hello():
    return "Hello world"


@app.route("/api/point", methods=["POST"])
def run_model():
    data = json.loads(request.get_json())

    my_df = pd.DataFrame(columns=[*map(lambda o: o["col"], data)])
    my_df.loc[0] = [*map(lambda o: o["value"], data)]
    my_df = purify(my_df)

    print(my_df)

    res = mlp.predict(my_df.values)
    verdict = res[0] // 3

    print(f"verdict = {verdict}")

    return jsonify({"verdict": str(verdict)})


if __name__ == "__main__":
    app.run()
