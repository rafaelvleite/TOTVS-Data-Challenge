# TOTVS-Data-Challenge
Data Challenge for job opportunity

## 1st step - Parse and Extract the data
The given file 'sample.txt' was opened in Tableau (before opening, I renamed this file to 'sample 2.json' to ease this process).
Since the purpose of this challenge is identify pattern on how much a customer spend on the restaurant and also calculate a sales forecast for the following week, I cleaned the data so that I remain only with the main data below:

![main_data](https://user-images.githubusercontent.com/4992938/36237106-122afd20-11e1-11e8-9b45-e0a1019eade0.png)

## 2nd step - Identify a pattern on any set of fields that can help predict how much a customer will spend
As per the cleaned data above, we can see that the average spend per table is highly related on the weekday. More on that can be seen on the Tableau visualization analysis below:

![weekday_distribution_average_spend](https://user-images.githubusercontent.com/4992938/36237811-74b8e89a-11e5-11e8-8acc-be6c87a62248.png)

From this analysis, we can predict how a customer will spend according to the weekday:

Monday: ~ 63
Tuesday: ~ 64
Wednesday: ~86
Thursday: ~53
Friday: ~45
Saturday: ~70








I used Tableau to import the dataset, and from there I could visualize the pattern for the sales per weekday.
To generate a forecast for the time series, I built a LSTM Network, and generated 1 forecast for the next weekday. I updated the model considering this forecast as the actual value, so I could make another prediction. I repeated this process so I could have 7 forecasted values, which are the sales forecasts for the next week.
