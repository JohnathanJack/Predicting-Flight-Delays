## Project Goals
Become familiar with the process of creating prediction models and use various methods to evaluate them.

## Process
View the included tables and create news from them, including more relevant information for feature creation.
Perform EDA through questions and gain insights to valuable features.
Create MVP and preliminary predictive model.
Refine features and compare models.
Create Visuals on insights and continue testing models.
Clean up files and prepare presentation on findings.

## Results
Decided on using random forest and XGBoost.
Random forest:
Parameters: crs_elapsed_time, distance, month, departing hour, arrival hour, origin, destination and op_unique_carrier 
R2 Score: 0.005
Mean Squared Error: 2478.71
Root Mean Squared Error: 49.79

XGBoost:
Parameters: crs_elapsed_time, distance, month, departing hour, arrival hour, origin, destination and op_unique_carrier 
R2 Score: 0.013
Mean Squared Error: 2272.64
Root Mean Squared Error: 47.67

## Challenges
Understanding the hyperparameters of different machine learning models, and how to optimize them.
Forging new features that are important and increases model accuracy.
Limitations for weather and location API. Not feasable to create a table of more than 500 weather forecasts.


## Future Goals
Continue experimenting with features until the results from the models resemble usable information.
Complete classification problem deciding on flight cancellation.
Try more regression models, and experiment with binary classification.