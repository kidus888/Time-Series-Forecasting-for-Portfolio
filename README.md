# Time-Series-Forecasting-for-Portfolio

## Financial Forecasting and Portfolio Optimization ##

This project uses time series forecasting and machine learning techniques to optimize a three-asset portfolio comprising Tesla stock (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY). Through this analysis, we aim to create a data-driven investment strategy that maximizes returns while minimizing risk, utilizing historical data and predictive models.

## Project Overview ##

1. Forecast Stock Prices: Using historical stock price data from Yahoo Finance, we implement and compare machine learning models—specifically ARIMA and LSTM—to forecast future daily prices for TSLA, BND, and SPY.

2. Analyze Trends and Volatility: Based on the forecasts, we analyze future price trends, volatility, and potential market risks for each asset.

3. Portfolio Optimization: Using the forecasted data, we optimize asset weights in the portfolio to maximize the Sharpe Ratio, achieving a balance between returns and volatility.

4. Risk Management: Calculations such as Value at Risk (VaR) allow us to quantify potential losses, especially for high-volatility assets like Tesla.

## Project Structure ##

data/: Folder for raw and processed datasets, including historical price data and forecasted price data for each asset.

notebooks/: Jupyter notebooks for each task:

       Task_1_Data_Preprocessing.ipynb: Data loading, preprocessing, and exploration.
       Task_2_Model_Development.ipynb: Time series forecasting model implementation (ARIMA and LSTM).
       Task_3_Forecast_Analysis.ipynb: Analysis of forecasted trends, volatility, and risk.
       Task_4_Portfolio_Optimization.ipynb: Portfolio optimization based on forecasted data, Sharpe Ratio maximization, and VaR calculation.
scripts/: Python scripts for functions used across notebooks (data processing, forecasting, and optimization functions).

README.md: Project description, setup instructions, and usage.

requirements.txt: List of dependencies for reproducing the environment.

## Getting Started ##

1. Clone the Repository
git clone https://github.com/yourusername/Financial-Forecasting-Portfolio-Optimization.git

cd Financial-Forecasting-Portfolio-Optimization

3. Set Up the Environment
We recommend setting up a virtual environment:

python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt

Dependencies include:

pandas, numpy, matplotlib, seaborn for data processing and visualization
yfinance for fetching stock data
pmdarima for ARIMA model tuning
tensorflow for LSTM model development
scipy, sklearn for statistical calculations and optimization


# Project Workflow #

## Data Preprocessing ##

  Load historical data for TSLA, BND, and SPY using yfinance.
  
  Clean and preprocess data to handle missing values and prepare for time series modeling.
  
## Time Series Forecasting Model Development ##
  Implement ARIMA and LSTM models to forecast future prices for each asset.
  
  Evaluate model performance using metrics such as MAE, RMSE, and MAPE.
  
  Save forecasted data for use in portfolio optimization.
  
 ## Forecast Analysis ##
 
  Analyze forecasted trends, volatility, and confidence intervals.
  
  Identify potential market opportunities and risks based on predicted trends.
  
## Portfolio Optimization ##

   Combine forecasted data for TSLA, BND, and SPY.
   
   Calculate expected returns, portfolio variance, and Sharpe Ratio.
   
   Use optimization techniques to maximize the Sharpe Ratio, balancing returns and risks.
   
   Analyze the optimized portfolio, including Value at Risk (VaR) and other risk measures.
   
## Results ##

1. Forecasting Accuracy: The LSTM model generally performed better for high-volatility assets like TSLA, while ARIMA was effective for more stable assets like BND and SPY.

2. Portfolio Insights: The optimized portfolio increased allocations in SPY and BND to mitigate the risk from TSLA’s volatility while still capitalizing on potential growth.
   
3. Sharpe Ratio Improvement: The optimized weights achieved a favorable risk-return balance, as indicated by a higher Sharpe Ratio.
   
## Key Learnings ##

Forecasting for Volatile Assets: LSTM models are well-suited for handling volatile stocks, capturing long-term dependencies better than ARIMA.

Importance of Risk Management: Balancing growth assets with stable assets like bond ETFs can significantly improve portfolio stability.

Data-Driven Decision Making: Forecasting and optimization offer quantitative support for portfolio adjustments, aiding in data-driven investment strategies.


## Contributing ##

Contributions are welcome! Please feel free to submit pull requests for improvements, additional features, or bug fixes. For major changes, please open an issue first to discuss your ideas.

Happy forecasting and investing! 🚀
