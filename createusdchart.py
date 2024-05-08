import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime

# Specify the symbol of the asset to be fetched
ticker = "ALARK.IS"

# Get the current date
end_date = datetime.now().strftime("%Y-%m-%d")

# Fetch the data using yFinance, you can change the start date and end date
data = yf.download(ticker, start="2020-01-01", end=end_date)

# Symbol for USD/TRY exchange rate from the interval
usd_try_ticker = "USDTRY=X"
usd_try_data = yf.download(usd_try_ticker, start="2020-01-01", end=end_date)

# Get the USD/TRY exchange rate data
usd_try_prices = usd_try_data['Close']

# Divide closing prices in TL to USD by USD/TRY exchange rate to convert to USD
data['Close'] /= usd_try_prices

# Format the data to two decimal places
data['Close'] = data['Close'].round(2)

# Plot the closing prices as a graph
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Closing Price',
                         hovertemplate='<b>Date</b>: %{x|%d-%m-%Y}<br><b>Price</b>: $%{y:.2f}<extra></extra>',
                         fill='tozeroy',  # Fill area below the line to x-axis
                         fillcolor='rgba(147, 112, 219, 0.2)',  # Light purple color
                         line=dict(color='#9370DB'),  # Line color
                         ))

fig.update_layout(
    title={
        'text': "ALARK.IS Stock Price (USD)",
        'y':0.98,  # Title position from top
        'x':0.03,  # Title position from left
        'xanchor': 'left',
        'yanchor': 'top'
    },
    xaxis_title="Date",
    yaxis_title="Stock Price (USD)",
    hovermode="x",
    template="plotly_white",
    plot_bgcolor="white",
    margin={"t": 80, "l": 50, "r": 50, "b": 50},  # Adjust margins
    height=900,  # Height of the plot
    width=1900,   # Width of the plot
)

fig.update_xaxes(
    showgrid=True,  # Show vertical grid lines
    gridcolor="rgba(0, 0, 0, 0.1)",  # Grid line color (light gray)
    linecolor="gray",  # Color of the x-axis line (black)
    linewidth=2,  # Thickness of the x-axis line
    tickformat="%b %Y",  # Date format on the x-axis (Month and Year)
    rangeslider_visible=False,  # Disable range slider on the x-axis
)

fig.update_yaxes(
    showgrid=True,  # Show horizontal grid lines
    gridcolor="rgba(0, 0, 0, 0.1)",  # Grid line color (light gray)
    linecolor="gray",  # Color of the y-axis line (black)
    linewidth=2,  # Thickness of the y-axis line
)

# Show the plot
fig.show()
