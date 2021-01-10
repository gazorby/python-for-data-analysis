## README

Analysis of YouTube videos dataset

### API

The api has one endpoint :

### `/predict` [POST]

JSON params:

-   `value` : The video characteristics in a list (without `id`, `codec` and `o_codec`). Example : `[130.35667,176,144,54590,12,27,1537,0,1564,64483,825054,0,889537,56000,12,176,144,22508,0.612]`

-   `model_type` (required) Determine the model to choose for the prediction
(can be either `lr` for linear regression or `rf` for random forest)

returns:

-   The predicted values


### Results

MSE with linear regression : 3.3225e-27

MSE with random forest, using `max_depth=9` and `n_estimators=5` : 0.0269
