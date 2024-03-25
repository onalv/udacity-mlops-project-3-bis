# Model Card

For additional information, see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

We utilized a Random Forest classifier for prediction purposes. The default configuration settings were employed during the training phase.

## Intended Use

This model is designed to predict the salary category of an individual based on their financial attributes. It aims to assist in financial analysis and planning.

## Training Data

The data source is the UCI Machine Learning Repository's Census Income dataset (https://archive.ics.uci.edu/ml/datasets/census+income); 80% of the data was used for training, employing stratified KFold for the process.

## Evaluation Data

The source of the data is https://archive.ics.uci.edu/ml/datasets/census+income; 20% of the data was used to validate the model's performance.

## Metrics

The model's performance was evaluated using Accuracy score, F1 beta score, Precision, and Recall. The values obtained were:
| Metric | Value |
|--------|-------|
| Accuracy | 0.82 |
| Precision | 0.68 |
| Recall | 0.57 |
| Fbeta | 0.62 |

## Ethical Considerations

For Ethical Considerations, the metrics were also calculated on data slices. This approach is intended to drive towards a model that may potentially discriminate against people; further investigation before using it should be done.

## Caveats and Recommendations

The data is biased based on gender. There is a data imbalance that needs to be investigated further.
