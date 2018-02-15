# TOTVS-Data-Challenge
Data Challenge for job opportunity

## 1st step - Parse and Extract the data
The given file 'sample.txt' was opened in Tableau (before opening this dataset, I renamed it to 'sample 2.json' to ease the Tableau Connect process). The Tableau file is 'TOTVS.twb' on this repository.
Since the purpose of this challenge is identify pattern on how much a customer spend on the restaurant and also calculate a sales forecast for the following week, I cleaned the data so that I remain only with the main data below:

![main_data](https://user-images.githubusercontent.com/4992938/36237106-122afd20-11e1-11e8-9b45-e0a1019eade0.png)

As you can see above, I also created a calculated field named 'Ticked Medio', which is the average spend per customer, and is calculated dividing the 'total sales amount' per 'quantity of tables' at a given day.

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

## 3rd step - Calculate a sales forecast for the next week
For this step, I exported only the sales per day, and also the corresponding weekdays. Because we already found out that there is a strong correlation between sales and weekday, both data need to be used on our forecast model.
So I generated a clean dataset from Tableau, to be used on Python, with only those 2 columns. This is the file 'real_sales.csv' on this repository.
The idea is to make a Recurrent Neural Network composed with Long short-term memory (LSTM) units, mostly known as LSTM Network, since this is usually well suited to predict time series.
So, I splited the 'real_sales.csv' dataset in Train and Test datasets, in aproximately 75% / 25% of data respectively. The splited datasets are found as 'real_sales_train.csv' and 'real_sales_test.csv' on this repository.
Now we have the Train and Test datasets for our LSTM Network.

