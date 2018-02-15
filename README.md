# TOTVS-Data-Challenge
Data Challenge for job opportunity

I used Tableau to import the dataset, and from there I could visualize the pattern for the sales per weekday.
To generate a forecast for the time series, I built a LSTM Network, and generated 1 forecast for the next weekday. I updated the model considering this forecast as the actual value, so I could make another prediction. I repeated this process so I could have 7 forecasted values, which are the sales forecasts for the next week.
