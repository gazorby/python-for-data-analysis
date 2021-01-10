## README

Analysis of YouTube videos dataset

### API

The api has one endpoint :

### `/predict` [POST]

JSON params:

-   `value` : The video characteristics in a list (without `id`, `codec` and `o_codec`)

-   `model_type` (required) Determine the model to choose for the prediction
(can be either `lr` for linear regression or `rf` for random forest)

returns:

-   The predicted values


### Results

MSE with linear regression : 3.3225e-27

MSE with random forest, using `max_depth=9` and `n_estimators=5` : 0.0269
