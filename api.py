import pandas as pd

# sklearn
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from flask import Flask, request

from enum import Enum

app = Flask(__name__)


class Model(Enum):
    """
    Model choice
    """

    REGRESSION = "lr"
    RANDOM_FOREST = "rf"


def get_model(model: Model, test_size: int = 0.2):

    df_mes = pd.read_csv("transcoding_mesurment.tsv", sep="\t")
    # remove useless codec
    del df_mes["id"]
    del df_mes["codec"]
    del df_mes["o_codec"]

    # split train and test datasets
    Y = df_mes[["utime"]]

    x_train, x_test, y_train, y_test = train_test_split(df_mes, Y, test_size=test_size)

    if Model(model) is Model.REGRESSION:
        # Train
        lr = LinearRegression()
        lr.fit(x_train, y_train)

        return lr
    elif Model(model) is Model.RANDOM_FOREST:
        # Using the best estimators chooses with cross validation
        regressor = RandomForestRegressor(n_estimators=5, random_state=0, max_depth=9)
        regressor.fit(x_train, y_train)
        return regressor

    else:
        raise ValueError(
            f"You have to choose a model beetween {','.join(model for model in Model.__members__)}"
        )


@app.route("/predict", methods=["POST"])
def pred_linear_regression():
    regressor = get_model(request.json.get("model_type"))
    pred = regressor.predict([request.json.get("value")]).item(0)
    return {"value": pred}


if __name__ == "__main__":
    app.run(debug=True)
