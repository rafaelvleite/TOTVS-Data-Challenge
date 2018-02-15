# TOTVS-Data-Challenge
Data Challenge for job opportunity

## 1st step - Parse and Extract the data
The given file **'sample.txt'** was opened in Tableau (before opening this dataset, I renamed it to **'sample 2.json'** to ease the Tableau Connect process). The Tableau file is **'TOTVS.twb'** on this repository.

Since the purpose of this challenge is identify pattern on how much a customer spend on the restaurant and also calculate a sales forecast for the following week, I cleaned the data so that I remain only with the main data below:

![main_data](https://user-images.githubusercontent.com/4992938/36237106-122afd20-11e1-11e8-9b45-e0a1019eade0.png)

As you can see above, I also created a calculated field named 'Ticked Medio', which is the average spend per customer, and is calculated dividing the 'total sales amount' per 'quantity of tables' at a given day.

## 2nd step - Identify a pattern on any set of fields that can help predict how much a customer will spend
As per the cleaned data above, we can see that the average spend per table is highly related on the weekday. More on that can be seen on the Tableau visualization analysis below:

![weekday_distribution_average_spend](https://user-images.githubusercontent.com/4992938/36237811-74b8e89a-11e5-11e8-8acc-be6c87a62248.png)

From this analysis, we can predict how a customer will spend according to the weekday:

- Monday: ~ 63
- Tuesday: ~ 64
- Wednesday: ~86
- Thursday: ~53
- Friday: ~45
- Saturday: ~70

## 3rd step - Calculate a sales forecast for the next week
For this step, I exported only the sales per day, and also the corresponding weekdays. Because we already found out that there is a strong correlation between sales and weekday, both data need to be used on our forecast model.

So I generated a clean dataset from Tableau, to be used on Python, with only those 2 columns. This is the file **'real_sales.csv'** on this repository.

The idea is to make a Recurrent Neural Network composed with Long short-term memory (LSTM) units, mostly known as LSTM Network, since this is usually well suited to predict time series.

So, I splited the **'real_sales.csv'** dataset into Train and Test datasets, in aproximately 75% / 25% amount of data respectively. The splited datasets are found as **'real_sales_train.csv'** and **'real_sales_test.csv'** on this repository.

Now we have the Train and Test datasets for our LSTM Network and we can move forward to our forecast model.

In the model flie **'tovs-challenge.py'** on this repository, I make this model. Basically, these are the steps I took:

- Imported the Training Set
- Applied a Feature Scaling to standardize the features of data. 
- Created a data structure with input of 7 timesteps (X_train) and output t+1 (y_train), so we could be "walking" with our model day by day. 
- Reshaped the X_train in order to fit the Recurrent Neural Network
- I builted the RNN, and optimized it with 300 units of LSTM in the input layer, compiled with 'RMSprop' optimizer, which is very suitable for RNN's, and used the loss function 'mean_squared_error', which showed the best results.
- To fit the RNN to the Training Set, I used 'batch' of 1, because we want to predict values based on a Time Series, and 50 epochs that showed to be optimum to avoid Underfitting and OverFitting.
- After the model was trained, I made the predictions and plotted the results to validate our model. You can see the result below, which is the prediction for the last 4 days of the sales data:

![model_validation](https://user-images.githubusercontent.com/4992938/36238659-274eb80e-11eb-11e8-92c4-107c08d1ed5e.png)

- As you can see, the model fits very well considering the low amount of data we have.
- Now the the model was validated, I moved forward to the next step, which is the sales forecasts for the next week (6 days, monday through saturday)
- I run the model and I got the plotted results below:

![sales_forecats](https://user-images.githubusercontent.com/4992938/36238749-b90e8788-11eb-11e8-8d42-6480ba8bef73.jpg)

###How amazing is that?###









