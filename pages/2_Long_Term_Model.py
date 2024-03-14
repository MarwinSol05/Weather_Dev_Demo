import streamlit as st

st.set_page_config(page_title = "Long-Term Forecast", )
st.sidebar.header("Long-Term Forecasting Model")

cols = st.columns(3)

metrics_ls = ['MAPE', 'MAE', 'RMSE']
country_ls = ['UK', 'IT', 'FR', 'DEU']
ts_ls = ['100m Wind', '2m Air Temp', 'Precipitation', 'Solar Radiation']

country = cols[0].selectbox(
    "Select Country",
    options = country_ls,
    index = 0,
    label_visibility = "visible",
    key = "country_select",
)

ts = cols[1].selectbox(
    "Select Element",
    options = ts_ls,
    index = 0,
    label_visibility = "visible",
    key = "ts_select",
)

metrics = cols[2].selectbox(
    "Select Metrics",
    options = metrics_ls,
    index = 0,
    label_visibility = "visible",
    key = "metrics_select",
)