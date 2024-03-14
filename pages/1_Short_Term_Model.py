import streamlit as st
from st_ant_tree import st_ant_tree
from read_data import get_wind_data
from model_input import get_region_country

st.set_page_config(page_title = 'Short-Term Forecast', )
st.sidebar.header('Short-Term Forecasting Model')

reg_cty_tree, start_cols = get_region_country()
metrics_ls = ['MAPE', 'MAE', 'RMSE']
ts_ls = ['100m Wind', '2m Air Temp', 'Precipitation', 'Solar Radiation']

cols = st.columns(2)

st.subheader("Select the country")
reg_cty_ls = st_ant_tree(treeData = reg_cty_tree,  key = 'reg_cty_select', allowClear = True, showSearch = True, disabled = False, defaultValue = start_cols)

ts = cols[0].selectbox(
    'Select Element',
    options = ts_ls,
    index = 0,
    label_visibility = 'visible',
    key = 'ts_select',
)

metrics = cols[1].selectbox(
    'Select Verification Metric',
    options = metrics_ls,
    index = 0,
    label_visibility = 'visible',
    key = 'metrics_select',
)

wind_data = get_wind_data()
wind_data